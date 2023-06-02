import pandas as pd
import urllib
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib


matplotlib.style.use('seaborn-v0_8-whitegrid')
# matplotlib.rcParams['axes.unicode_minus'] = False
# matplotlib.rcParams['axes.spines.top'] = False
# matplotlib.rcParams['axes.spines.right'] = False
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.size'] = 9
# matplotlib.rcParams['xtick.direction'] = 'out'
# matplotlib.rcParams['ytick.direction'] = 'out'
matplotlib.rcParams['font.serif'] = ['STSong']
matplotlib.rcParams['font.style'] = 'normal'
matplotlib.rcParams['font.weight'] = 'normal'
matplotlib.rcParams['axes.xmargin'] = 0.05
matplotlib.rcParams['pdf.fonttype'] = 42


def plot_obs(df, title='', filename='myfig.png'):
    '''plot'''
    fig, ax = plt.subplots(figsize=(10, 3), nrows=1, ncols=1)
    if isinstance(df, pd.DataFrame):
        if 'residual' in df.columns:
            df['residual'].plot(ax=ax,
                                ls='solid',
                                # color='red',
                                linewidth=1.0,
                                label='去年变数据')
            df['trend'].plot(ax=ax,
                            ls='solid',
                            # color='gray',
                            linewidth=1.0,
                            label='趋势变化')
        if 'relative_range' in df.columns:
            df['relative_range'].plot(ax=ax,
                                    ls='solid',
                                    # color='red',
                                    linewidth=1.0,
                                    label='相对变化幅度')
            df['annual_1'].plot(ax=ax,
                                ls='solid',
                                # color='blue',
                                linewidth=1.0,
                                label='年变化幅度')
            df['annual_2'].plot(ax=ax,
                                ls='solid',
                                # color='blue',
                                linewidth=1.0,
                                label='年变化幅度')
            df['std_1'].plot(ax=ax,
                            ls='dashed',
                            # color='darkorange',
                            linewidth=1.0,
                            label='2.5倍“平均均方差”阈值线')
            df['std_2'].plot(ax=ax,
                            ls='dashed',
                            # color='darkorange',
                            linewidth=1.0,
                            label='2.5倍“平均均方差”阈值线')
    else:
            df.plot(ax=ax, linewidth=1.0, label='原始曲线')
    # if isinstance(df, pd.DataFrame):
    #     ax.legend(df.columns.tolist(), fancybox=False, loc='upper left', bbox_to_anchor=(1.0, 1.0))
    # else:
    #     ax.legend(['OBSVALUE'], fancybox=False, loc='upper left', bbox_to_anchor=(1.0, 1.0))
    plt.legend(fancybox=False, loc='upper left', bbox_to_anchor=(1.0, 1.0))
    ax.set_ylabel(r'$\Omega \cdot m$')
    ax.set_title(title)
    fig.savefig(f'../figures/{filename}', dpi=300, bbox_inches='tight')


startdate = (dt.datetime.today() + dt.timedelta(-1 * 365 * 5)).strftime('%Y%m%d')
enddate = dt.datetime.today().strftime('%Y%m%d')
stationname = '马陵山'

params = urllib.parse.urlencode({'database': 'BAIJIATUAN',
                                'stationname': stationname,
                                'startdate': startdate,
                                'enddate': enddate,
                                'methodname': '地电阻率',
                                'sampling': '小时值',
                                'basetype': '预处理库',
                                'itemname': '直流单装置地电阻率观测东西向',
                                'pointid': '',
                                'returntype': 'false'})
url = f'http://10.2.102.181:8888/resistivity_avam?{params}'
print(url)
df = pd.read_json(url, orient='split')
df.index.name = '日期'
df1 = df['OBSVALUE']
df2 = df[['residual', 'trend']]
df3 = df[['relative_range', 'annual_1', 'annual_2', 'std_1', 'std_2']]
plot_obs(df1, filename='马陵山地电阻率东西向.png')
plot_obs(df2, filename='马陵山地电阻率东西向残差.png')
plot_obs(df3, filename='马陵山地电阻率东西向相对变化幅度.png')

params = urllib.parse.urlencode({'database': 'BAIJIATUAN',
                                'stationname': stationname,
                                'startdate': startdate,
                                'enddate': enddate,
                                'methodname': '地电阻率',
                                'sampling': '小时值',
                                'basetype': '预处理库',
                                'itemname': '直流单装置地电阻率观测北南向',
                                'pointid': '',
                                'gaps': '20190504 20191029',
                                'returntype': 'false'})
url = f'http://10.2.102.181:8888/resistivity_avam?{params}'
df = pd.read_json(url, orient='split')
df.index.name = '日期'
df1 = df['OBSVALUE']
df2 = df[['residual', 'trend']]
df3 = df[['relative_range', 'annual_1', 'annual_2', 'std_1', 'std_2']]
plot_obs(df1, filename='马陵山地电阻率南北向.png')
plot_obs(df2, filename='马陵山地电阻率南北向残差.png')
plot_obs(df3, filename='马陵山地电阻率南北向相对变化幅度.png')
