import solara

# 這是一個「元件」，因為它戴了魔術帽
@solara.component
def Page():
    # Solara 會將這個 Markdown 物件翻譯成網頁 HTML
    solara.Markdown("這是一個 Solara 元件！")

# 這只是一個「普通函式」，Solara 會忽略它
def my_helper_function():
    return 2 + 2