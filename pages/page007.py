import solara
import geopandas as gpd
import time

def load_data():
    print("...正在從網路下載資料 (這很慢)...")
    time.sleep(3)
    tw_counties_url = "https://raw.githubusercontent.com/g0v/twgeojson/master/json/twCounty2010.geo.json"
    gdf = gpd.read_file(tw_counties_url)

    # ★ Solara 不支援 GeoDataFrame → 必須轉 Pandas DataFrame
    df = gdf.copy()
    df["geometry"] = df.geometry.astype(str)  # 轉文字來保存資料
    return df

@solara.component
def Page():
    df = solara.use_memo(load_data, dependencies=[])

    solara.Markdown(f"成功載入 {len(df)} 筆台灣縣市資料！")

    solara.DataFrame(df.head())
