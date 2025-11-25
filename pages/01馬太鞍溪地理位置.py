import solara
import plotly.express as px
import leafmap.maplibregl as leafmap
import os

MAPTILER_KEY = os.environ.get("maptilerAPI", "") 

def create_3d_map():
    if not MAPTILER_KEY:
        m = leafmap.Map(
            center=[121.395, 23.515], 
            zoom=10, 
            style="OpenStreetMap",
        )
        m.layout.height = "700px"
        return m
    
    style_url = f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"
    
    m = leafmap.Map(
        style=style_url,
        center=[121.380, 23.632] ,
        zoom=12,
        pitch=65,
        bearing=15,
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
        流域面積：161.80平方公里
        ''')
            
        solara.Markdown("## 3D 地形展示 (MapLibre GL)")

        solara.display(map_object)