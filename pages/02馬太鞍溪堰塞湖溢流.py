import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(import solara
import leafmap.leafmap as leafmap

def create_split_map():
    # 直接使用 split_map，傳入底圖名稱字串
    split_control = leafmap.split_map(
        left_layer="Esri.WorldImagery",  # 左邊：衛星圖 只能底圖圖層  不能是物件
        right_layer="OpenStreetMap",     # 右邊：街道圖 只能底圖圖層  不能是物件
        left_label="衛星影像",
        right_label="街道地圖",
        center=[23.632, 121.380], # 台北
        zoom=12,
        # ipyleaflet 的 split_map 本身就會回傳一個地圖物件，不需要額外設定 height
    )
    
    # (可選) 如果您想調整高度，可以在回傳的地圖物件上設定
    split_control.layout.height = "650px"

    return split_control

@solara.component
def Page():


    with solara.Column():
        solara.Markdown('''
        ## 「堰塞湖」危機
        
        ---

        由於2025年7月21日颱風薇帕外圍環流夾帶的雨勢引發山崩，並於馬太鞍溪上游萬榮鄉處形成堰塞湖，其後因受颱風樺加沙外圍環流暴雨影響而於2025年9月23日發生多次溢流。
        ---
        #### 溢流事件經過：

        2025年7月21日，馬太鞍溪上游於發生大規模山崩，引發了規模4.9的非構造地震[2]，崩塌量約2億立方公尺，形成壩高約200公尺之堰塞湖。[3]

        2025年8月10日，因應楊柳颱風靠近臺灣，中央政府開始擬定疏散避難計畫。

        2025年9月23日，颱風樺加沙的強大雨勢導致該堰塞湖溢流[4]。
        ''')
        solara.Markdown("## 2D 捲簾比對 (Split Map)")
    
    split_widget = solara.use_memo(create_split_map, dependencies=[])
    
    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)
        center=[-74.0095, 40.7046],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("Satellite", visible=False)
    m.add_overture_3d_buildings(template="simple")
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()