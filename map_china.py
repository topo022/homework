from pyecharts import options as opts
from pyecharts.charts import Map
import csv



src_filename = './data/tour.csv'

src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

print(line_list)  # 检查读入数据的情况

# 将读入的每行数据拆分成元组
place_list = []  #用于保存元组(人物姓名,出现次数)
for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',') # 以逗号作为标志，把字符串切分成词，存在列表中
    place_list.append((line_split[0],line_split[1]))

del place_list[0]

tour_map=(
    Map()
    .add("各省市旅游人次(亿)",
         place_list,
         maptype='china',)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='各省市旅游情况'),
                     visualmap_opts=opts.VisualMapOpts(max_=12))
)

tour_map.render('./output/map_china.html')




