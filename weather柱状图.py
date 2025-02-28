# _*_coding : utf-8 _*_
# @Time : 2024/12/3 17:11
# @Author : 刘佳琳
# @File : weather柱状图
# @Project : pythonProject2
import csv  # 写入csv文件m
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
df = pd.read_csv('weather.csv', encoding='gb18030')
df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
df['month'] = df['日期'].dt.month
df_agg = df.groupby(['month', '天气']).size().reset_index()
df_agg.columns = ['month', 'tianqi', 'count']
timeline = Timeline()
timeline.add_schema(play_interval=1000)  # 单位是:ms(毫秒)
for month in df_agg['month'].unique():#返回一个数组或 Series 中所有唯一（不重复）值的数组
    # 获取天气的值
    data = (
        df_agg[df_agg['month'] == month][['tianqi', 'count']]
        .sort_values(by='count', ascending=True)
        .values.tolist()
    )
    bar = Bar()
    bar.add_xaxis([x[0] for x in data])
    bar.add_yaxis('', [x[1] for x in data])
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position='right'))
    bar.set_global_opts(title_opts=opts.TitleOpts(title='2023年重庆每月天气变化 '))
    timeline.add(bar, f'{month}月')
timeline.render('weather.html')