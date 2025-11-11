import solara

count = solara.reactive(0)
@solara.component
def Page():
    with solara.Column(align="center"):
        solara.Title("My Solara App")
        solara.Markdown(f"## 按鈕被點擊了 {count.value} 次！")
        def increment():
            count.value += 1 
        solara.Button("點我！", on_click=increment)
