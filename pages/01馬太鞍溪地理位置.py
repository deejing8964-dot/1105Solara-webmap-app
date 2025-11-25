import solara
import plotly.express as px
import leafmap.maplibregl as leafmap
import os

MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "") 

def create_3d_map():
    # 檢查 API Key 是否存在
    if not MAPTILER_KEY:
        # 如果沒有 Key，回傳一個基礎地圖，但不會有地形
        m = leafmap.Map(
            center=[121.395, 23.515], 
            zoom=10, 
            style="OpenStreetMap",
        )
        # 這是標準的 ipywidgets 語法，對 maplibregl.Map 物件有效
        m.layout.height = "700px"
        return m
    
    # MapTiler Outdoor-v2 Style 內建支援地形資料
    style_url = f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"
    
    m = leafmap.Map(
        style=style_url,
        center=[121.380, 23.632] ,
        zoom=12,
        pitch=65,  # 傾斜角度 (65度)
        bearing=15, # 旋轉角度 (15度)
        # 啟用地形：當使用 MapTiler Style 時，通常只需設定 style URL，
        # Leafmap 會自動處理 style.json 內定義的地形源。
        # 如果需要明確設定，通常是: terrain={"source": "mapbox-dem"}
        )
    m.layout.height = "700px"
    return m


@solara.component
def Page():
    map_object = solara.use_memo(create_3d_map, dependencies=[MAPTILER_KEY])

    with solara.Column():
        
        solara.Markdown("## 地理位置")
        solara.Markdown('''
        溪長約：38.58 公里
        流域面積：161.80平方公里（62.47平方英里）''')
            
        solara.Markdown("## 3D 地形展示 (MapLibre GL)")

        solara.display(map_object)