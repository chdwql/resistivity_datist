import pandas as pd
import urllib
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib


matplotlib.style.use('seaborn')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['axes.spines.top'] = False
matplotlib.rcParams['axes.spines.right'] = False
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.size'] = 9
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
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
            df['residual'].plot(ax=ax, ls='solid', color='red', linewidth=1.0)
            df['trend'].plot(ax=ax, ls='solid', color='gray', linewidth=1.0)
        if 'relative_range' in df.columns:
            df['relative_range'].plot(ax=ax, ls='solid', color='red', linewidth=1.0)
            df['annual_1'].plot(ax=ax, ls='solid', color='blue', linewidth=1.0)
            df['annual_2'].plot(ax=ax, ls='solid', color='blue', linewidth=1.0)
            df['std_1'].plot(ax=ax, ls='dashed', color='darkorange', linewidth=1.0)
            df['std_2'].plot(ax=ax, ls='dashed', color='darkorange', linewidth=1.0)
    else:
            df.plot(ax=ax, color='red', linewidth=1.0)
    if isinstance(df, pd.DataFrame):
        ax.legend(df.columns.tolist(), fancybox=False, loc='upper left', bbox_to_anchor=(1.0, 1.0))
    else:
        ax.legend(['OBSVALUE'], fancybox=False, loc='upper left', bbox_to_anchor=(1.0, 1.0))
    ax.set_ylabel(r'$\Omega \cdot m$')
    ax.set_title(title)
    fig.savefig(f'./figures/{filename}', dpi=300, bbox_inches='tight')


startdate = (dt.datetime.today() + dt.timedelta(-1 * 365 *5)).strftime('%Y%m%d')
startdate = '20180101'
enddate = dt.datetime.today().strftime('%Y%m%d')
stationname = '新沂'

# params = urllib.parse.urlencode({'database': 'BAIJIATUAN',
#                                 'stationname': stationname,
#                                 'startdate': startdate,
#                                 'enddate': enddate,
#                                 'methodname': '地电阻率',
#                                 'sampling': '小时值',
#                                 'basetype': '预处理库',
#                                 'itemname': '直流单装置地电阻率观测东西向',
#                                 'piontid': '3',
#                                 'returntype': 'false'})
# url = f'http://10.2.102.181:8888/resistivity_avam?{params}'
# df = pd.read_json(url, orient='split')
# df.index.name = '日期'
# df1 = df['OBSVALUE']
# df2 = df[['residual', 'trend']]
# df3 = df[['relative_range', 'annual_1', 'annual_2', 'std_1', 'std_2']]
# plot_obs(df1, filename='新沂地电阻率东西向—3.png')
# plot_obs(df2, filename='新沂地电阻率东西向残差—3.png')
# plot_obs(df3, filename='新沂地电阻率东西向相对变化幅度—3.png')

params = urllib.parse.urlencode({'database': 'BAIJIATUAN',
                                'stationname': stationname,
                                'startdate': startdate,
                                'enddate': enddate,
                                'methodname': '地电阻率',
                                'sampling': '小时值',
                                'basetype': '预处理库',
                                'itemname': '直流单装置地电阻率观测北南向',
                                'pointid': '9',
                                'returntype': 'false'})
url = f'http://10.2.102.181:8888/resistivity_avam?{params}'
# url = f'http://10.37.187.192:8888/resistivity_avam?{params}'
df = pd.read_json(url, orient='split')
df.index.name = '日期'
df1 = df['OBSVALUE']
df2 = df[['residual', 'trend']]
df3 = df[['relative_range', 'annual_1', 'annual_2', 'std_1', 'std_2']]
plot_obs(df1, filename='新沂地电阻率南北向—9.png')
plot_obs(df2, filename='新沂地电阻率南北向残差—9.png')
plot_obs(df3, filename='新沂地电阻率南北向相对变化幅度—9.png')

params = urllib.parse.urlencode({'database': 'BAIJIATUAN',
                                'stationname': stationname,
                                'startdate': startdate,
                                'enddate': enddate,
                                'methodname': '地电阻率',
                                'sampling': '小时值',
                                'basetype': '预处理库',
                                'itemname': '直流单装置地电阻率观测北南向',
                                'pointid': '3',
                                'returntype': 'false'})
url = f'http://10.2.102.181:8888/resistivity_avam?{params}'
df = pd.read_json(url, orient='split')
df.index.name = '日期'
df1 = df['OBSVALUE']
df2 = df[['residual', 'trend']]
df3 = df[['relative_range', 'annual_1', 'annual_2', 'std_1', 'std_2']]
plot_obs(df1, filename='新沂地电阻率南北向—3.png')
plot_obs(df2, filename='新沂地电阻率南北向残差—3.png')
plot_obs(df3, filename='新沂地电阻率南北向相对变化幅度—3.png')