import solara
import plotly.express as px
import leafmap.maplibregl as leafmap
import os

@solara.component
def Page():

    with solara.Column(align="center"):
        

        solara.Markdown("## 馬太鞍溪簡介")
        solara.Markdown("---")
        solara.Markdown('''
                馬太鞍溪，原名瓦納納溪，是花蓮縣花蓮溪的支流之一。該溪發源自丹大山東北坡，流經花蓮縣萬榮鄉、鳳林鎮與光復鄉等鄉鎮，為鳳林鎮與光復鄉之界河，與光復溪匯流為花蓮溪。
                位於馬太鞍溪沖積扇上緣的馬太鞍部落以馬太鞍豐年舞祭而聞名；沖積扇上的馬太鞍溼地目前規劃成生態保留區。台灣鐵路臺東線光復隧道在馬太鞍溪河床底下，以隧道穿越的方式行經。
                ''')