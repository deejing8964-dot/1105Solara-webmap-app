import solara
import duckdb
import pandas as pd
import plotly.express as px
import leafmap.maplibregl as leafmap

CITIES_CSV_URL = 'https://data.gishub.org/duckdb/cities.csv'

all_countries = solara.reactive([])
selected_country = solara.reactive("")
data_df = solara.reactive(pd.DataFrame())

def load_country_list():
    """初始化：載入國家清單"""
    try:
        con = duckdb.connect()
        con.install_extension("httpfs")
        con.load_extension("httpfs")
        result = con.sql(f"""
            SELECT DISTINCT country
            FROM '{CITIES_CSV_URL}'
            ORDER BY country
        """).fetchall()
        country_list = [row[0] for row in result]
        all_countries.set(country_list)
        if "USA" in country_list:
            selected_country.set("USA")
        elif country_list:
            selected_country.set(country_list[0])
        con.close()
    except Exception as e:
        print(f"Error loading countries: {e}")

def load_filtered_data():
    """根據選中國家載入城市資料"""
    country_name = selected_country.value
    if not country_name:
        return
    try:
        con = duckdb.connect()
        con.install_extension("httpfs")
        con.load_extension("httpfs")
        df_result = con.sql(f"""
            SELECT name, country, population, latitude, longitude
            FROM '{CITIES_CSV_URL}'
            WHERE country = '{country_name}'
            ORDER BY population DESC
            LIMIT 10
        """).df()
        data_df.set(df_result)
        con.close()
    except Exception as e:
        print(f"Error executing query: {e}")
        data_df.set(pd.DataFrame())

@solara.component
def CityMap(df: pd.DataFrame):
    """顯示城市地圖"""
    if df.empty:
        return solara.Info("沒有城市數據可顯示")
    center = [df['latitude'].iloc[0], df['longitude'].iloc[0]]
    m = leafmap.Map(
        center=center,
        zoom=4,
        add_sidebar=True,
        height="600px"
    )
    m.add_basemap("Esri.WorldImagery", before_id=m.first_symbol_layer_id)
    
    # 轉成 GeoJSON
    features = []
    for _, row in df.iterrows():
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [row["longitude"], row["latitude"]]},
            "properties": {
                "name": row["name"],
                "population": int(row["population"]) if row["population"] else None
            }
        })
    geojson = {"type": "FeatureCollection", "features": features}
    m.add_geojson(geojson)
    return m.to_solara()

@solara.component
def Page():
    solara.Title("城市地理人口分析 (DuckDB + Solara + Leafmap)")
    
    solara.use_effect(load_country_list, dependencies=[])
    solara.use_effect(load_filtered_data, dependencies=[selected_country.value])

    with solara.Card(title="城市篩選器"):
        solara.Select(
            label="選擇國家",
            value=selected_country,
            values=all_countries.value
        )

    if selected_country.value and not data_df.value.empty:
        df = data_df.value
        solara.Markdown(f"## {selected_country.value} 前 {len(df)} 大城市")
        CityMap(df)
        solara.Markdown(f"### 📋 數據表格")
        solara.DataFrame(df)
        
        solara.Markdown(f"### 📊 {selected_country.value} 人口分布 (Plotly)")
        fig_hist = px.bar(
            df,
            x="name",
            y="population",
            color="population",
            title=f"{selected_country.value} 城市人口分布",
            labels={"name":"城市名稱","population":"人口數"},
            height=400
        )
        fig_hist.update_layout(xaxis_tickangle=-45)
        solara.FigurePlotly(fig_hist)
        
        fig_pie = px.pie(
            df,
            names="name",
            values="population",
            title=f"{selected_country.value} 各城市人口比例",
            height=400
        )
        solara.FigurePlotly(fig_pie)

    else:
        solara.Info("正在載入資料...")

Page()
