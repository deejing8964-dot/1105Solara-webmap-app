import solara

count = solara.reactive(0)
@solara.component
def Page():
    with solara.Column(align="center"):
        solara.Title("首頁")
        markdown = "歡迎使用我的Solara app！"
        solara.Markdown(markdown)
        solara.Markdown(f"## 按鈕被點擊了 {count.value} 次！")
        def increment():
            count.value += 1 
        solara.Button("click me！", on_click=increment)
        
