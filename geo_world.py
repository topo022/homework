from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

math = (
    Geo()
    .add_schema(maptype="world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        toolbox_opts=opts.ToolboxOpts(),
        visualmap_opts=opts.VisualMapOpts(max_=30),
        title_opts=opts.TitleOpts(title="2023数院留学地图"),
    )

)
math.add_coordinate_json(json_file='./data/world_country.json')
math.add("概率统计",
         [
          ("United States",21),
          ("France",1),
          ("Singapore",1),
          ("北京",23),
      ],
         type_=ChartType.EFFECT_SCATTER,
         )
math.add(
    "概率统计",
    [
        ("北京","United States"),
        ("北京","France"),
        ("北京","Singapore"),
    ],
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,symbol_size=6,color="darkblue"
    ),
    linestyle_opts=opts.LineStyleOpts(curve=0.2),
)
math.add(
    "金融系",
    [
        ("United States",3),
        ("Singapore",1),
        ("北京",4),
    ],
    type_=ChartType.EFFECT_SCATTER,
)
math.add(
    "金融系",
    [
        ("北京","United States"),
        ("北京","Singapore"),
    ],
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,symbol_size=6,color="green"
    ),
    linestyle_opts=opts.LineStyleOpts(curve=0),
)
math.add(
    "大数据",
    [
        ("Netherlands",1),
        ("United States",1),
        ("Singapore",1),
        ("北京",3),
    ],
    type_=ChartType.EFFECT_SCATTER,
)
math.add(
    "大数据",
    [
        ("北京","United States"),
        ("北京","Netherlands"),
        ("北京","Singapore"),
    ],
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,symbol_size=6,color="yellow"
    ),
    linestyle_opts=opts.LineStyleOpts(curve=0.05),
)
math.add(
    "数学系",
    [
        ("United States",12),
        ("German",1),
        ("Singapore",2),
        ("France",2),
        ("Switzerland",2),
        ("Japan",1),
        ("北京",20),
    ],
    type_=ChartType.EFFECT_SCATTER,
)
math.add(
    "数学系",
    [
        ("北京","United States"),
        ("北京","France"),
        ("北京","Singapore"),
        ("北京","German"),
        ("北京","Switzerland"),
        ("北京","Japan"),
    ],
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,symbol_size=6,color="red"
    ),
    linestyle_opts=opts.LineStyleOpts(curve=0.15),
)
math.add(
    "信息与计算",
    [
        ("United States",9),
        ("Hong Kong",2),
        ("Switzerland",1),
        ("北京",12),
    ],
    type_=ChartType.EFFECT_SCATTER,
)
math.add(
    "信息与计算",
    [
        ("北京","United States"),
        ("北京","Switzerland"),
        ("北京","Hong Kong"),
    ],
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,symbol_size=6,color="blue"
    ),
    linestyle_opts=opts.LineStyleOpts(curve=0.1),
)
math.render('./output/geo_world.html')