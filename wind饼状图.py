# _*_coding : utf-8 _*_
# @Time : 2024/12/4 17:31
# @Author : 刘佳琳
# @File : wind饼状图
# @Project : pythonProject2
from pyecharts.charts import Timeline
from pyecharts.charts import Pie
from pyecharts import options as opts
import csv  # 写入csv文件
import pandas as pd
df = pd.read_csv('weather.csv', encoding='gb18030')
df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
df['month'] = df['日期'].dt.month
df_agg = df.groupby(['month', '风向']).size().reset_index()
df_agg.columns = ['month', 'fengxiang', 'count']
timeline = Timeline()
timeline.add_schema(play_interval=1000)  # 单位是:ms(毫秒)
for month in df_agg['month'].unique():
    # 获取天气的值
    data = (
        df_agg[df_agg['month'] == month][['fengxiang', 'count']]
        .sort_values(by='count', ascending=True)
        .values.tolist()
    )
    pie = Pie()# 创建一个饼图Pie对象
    pie.add(
        series_name='重庆2023年风向',
        data_pair=data,
        radius=["40%", "75%"],  # 设置内外圆的半径
    ) # 添加数据和配置项
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title='2023年重庆每月风向变化'),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="right"),
    ) # 设置全局配置项
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    timeline.add(pie, f'{month}月')
# 渲染图表到HTML文件
timeline.render('wind.html')
