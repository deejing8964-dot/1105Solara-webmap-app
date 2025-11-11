import solara

count = solara.reactive(0)
@solara.component
def Page():
    with solara.Column(align="center"):
        solara.Title("首頁")
        markdown = "歡迎使用我的Solara app！"
        solara.Markdown(markdown)
        solara.Markdown(f"## 功德+{count.value}")
        def increment():
            count.value += 1 
        solara.Button("按我增加功德", on_click=increment)
        
