import solara

# 1. 建立一個「響應式」變數，作為元件的「記憶」
#    注意：我們使用 .value 來存取它的值
name = solara.reactive("Guest")

@solara.component
def Page():
    # 2. Solara 會「監視」name.value
    solara.Markdown(f"## 你好, {name.value}!")

    # 3. 這個函式會改變 name.value
    def on_click():
        name.value = "Chingmu"

    # 4. 按鈕點擊時，name.value 改變，
    #    上面的 Markdown 元件會「自動」更新
    solara.Button("點我改名", on_click=on_click)