from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker


def bar_datazoom_slider(pl_list,pe_list,re_list) -> Bar:
    c = (
        Bar()
        .add_xaxis(pl_list)
        .add_yaxis("接待人次",
                   pe_list,
                   yaxis_index=0,
                   color='hsl(200,80%,80%)')
        .add_yaxis("旅游收入",
                   re_list,
                   yaxis_index=2,
                   color='hsl(250,80%,80%)')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2023中国各省旅游接待人次及旅游收入"),
            datazoom_opts=[opts.DataZoomOpts()],
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="接待人次",
                type_="value",
                min_=0,
                max_=15,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 亿人次"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="收入",
                min_=0,
                max_=150,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 百亿元"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
    )
    grid = Grid()  # grid可以拼合多个图，本例不用grid会显示不全
    grid.add(c,
             opts.GridOpts(pos_left="5%", pos_right="20%"),  # 参见“直角坐标系网格配置项”
             is_control_axis_index=True  # 是否由自己控制 Axis 索引
             )
    return grid




def pie_rosetype(pl_list,pe_list,re_list) -> Pie:
    peo=[]
    revenue=[]
    for i in range(0,len(pl_list)):
        peo.append((pl_list[i],pe_list[i]))
        revenue.append((pl_list[i],re_list[i]))
    v = pl_list
    c = (
        Pie()
        .add(
            "",
            peo,
            radius=["20%", "65%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
            selected_offset=10,
        )
        .add(
            "",
            revenue,
            radius=["20%", "65%"],
            center=["75%", "50%"],
            rosetype="area",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=""),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_left="0%", orient="vertical"))
    )
    return c








def table_base(pl_list,pe_list,re_list,co_list) -> Table:
    table = Table()

    headers = ["省市", "接待人次(亿)", "旅游收入(百亿元)", "平均消费(元)"]
    rows=[]
    for i in range(len(pl_list)):
        rows.append([pl_list[i],pe_list[i],re_list[i],co_list[i]])
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="表格")
    )
    return table


def page_simple_layout(pl_list,pe_list,re_list,co_list):
    page = Page(interval=30,layout=Page.SimplePageLayout)#Page内置了两种布局：simple，draggable
    page.add(
        bar_datazoom_slider(pl_list,pe_list,re_list),
        pie_rosetype(pl_list,pe_list,re_list),
        table_base(pl_list,pe_list,re_list,co_list),
    )
    page.render("./output/table.html")


if __name__ == "__main__":
    src_filename = './data/tour.csv'

    src_file = open(src_filename, 'r')
    line_list = src_file.readlines()  # 返回列表，文件中的一行是一个元素
    src_file.close()

    print(line_list)  # 检查读入数据的情况

    # 将读入的每行数据拆分成元组
    place_list = []  # 用于保存元组(人物姓名,出现次数)
    people_list=[]
    revenue_list=[]
    consume_list=[]

    for line in line_list:
        line = line.strip()  # 删除'\n'
        line_split = line.split(',')  # 以逗号作为标志，把字符串切分成词，存在列表中
        place_list.append(line_split[0])
        people_list.append(line_split[1])
        revenue_list.append(line_split[2])
        consume_list.append(line_split[3])

    del place_list[0]
    del people_list[0]
    del revenue_list[0]
    page_simple_layout(place_list,people_list,revenue_list,consume_list)

