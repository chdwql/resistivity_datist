import os
import pandas as pd
import urllib
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib


def configure_matplotlib():
    '''配置Matplotlib的样式和参数'''
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
    matplotlib.rcParams['legend.fancybox'] = False


def plot_figure(df, filename='myfig.png', figsize=(8, 8)):
    '''绘制图表'''
    fig, ax = plt.subplots(figsize=figsize, nrows=3, ncols=1)
    if isinstance(df, pd.DataFrame):
        if 'OBSVALUE' in df.columns:
            df['OBSVALUE'].plot(ax=ax[0], linewidth=1.0, label='原始曲线', legend=True)
            ax[0].set_ylabel(r'$\Omega \cdot m$')
        if 'residual' in df.columns:
            df['residual'].plot(ax=ax[1], ls='solid', color='red', linewidth=1.0,
                                label='去年变数据', legend=True)
            df['trend'].plot(ax=ax[1], ls='solid', color='gray', linewidth=1.0,
                             label='趋势变化', legend=True)
            ax[1].set_ylabel(r'$\Omega \cdot m$')
        if 'relative_range' in df.columns:
            df['relative_range'].plot(ax=ax[2], ls='solid', color='red', linewidth=1.0,
                                      label='相对变化幅度', legend=True)
            df['annual_1'].plot(ax=ax[2], ls='solid', color='blue', linewidth=1.0,
                                label='年变化幅度', legend=True)
            df['annual_2'].plot(ax=ax[2], ls='solid', color='blue', linewidth=1.0,
                                label='年变化幅度')
            df['std_1'].plot(ax=ax[2], ls='dashed', color='darkorange', linewidth=1.0,
                             label='2.5倍“平均均方差”阈值线', legend=True)
            df['std_2'].plot(ax=ax[2], ls='dashed', color='darkorange', linewidth=1.0,
                             label='2.5倍“平均均方差”阈值线')
            ax[2].set_ylabel(r'$\Omega \cdot m$')

    if not os.path.exists('figures'):
        os.makedirs('figures')

    fig.savefig(f'./figures/{filename}', dpi=300, bbox_inches='tight')


def fetch_resistivity_data(stationname, filename):
    startdate = (dt.datetime.today() + dt.timedelta(-1 * 365 * 5)).strftime('%Y%m%d')
    enddate = dt.datetime.today().strftime('%Y%m%d')

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

    df = pd.read_json(url, orient='split')
    df.index.name = '日期'

    plot_figure(df, filename)

def get_plot():
    "执行代码"
    configure_matplotlib()
    stationname = '马陵山'
    filename = '马陵山地电阻率东西向.png'
    fetch_resistivity_data(stationname, filename)

if __name__ == '__main__':
    get_plot()
