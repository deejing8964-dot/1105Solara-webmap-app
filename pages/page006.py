import solara
import pandas as pd
import plotly.express as px

# 準備資料
df = pd.DataFrame(
    {"x": [1, 2, 3, 4], "y": [10, 11, 12, 13]}
)
fig = px.scatter(df, x="x", y="y", title="我的 Plotly 圖表")

@solara.component
def Page():
    solara.Markdown("## 顯示 DataFrame")
    solara.DataFrame(df)

    solara.Markdown("## 顯示 Plotly 圖表")
    solara.FigurePlotly(fig)