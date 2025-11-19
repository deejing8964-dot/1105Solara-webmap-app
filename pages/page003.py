import solara

@solara.component
def Page():
    # 設定瀏覽器標籤頁的標題
    solara.Title("我的 Solara WebGIS App")

    solara.Markdown("# 這是一個 H1 標題")
    solara.Markdown("這是一般的文字。 **粗體** *斜體*。")
    solara.Markdown('''

    ''')

    solara.Info("這是一條資訊提示。")
    solara.Warning("這是一條警告！")
    solara.Error("糟糕，發生了錯誤。")