from pathlib import Path
import importlib.util
import solara


# 掃描同目錄下的 .py 檔（排除 __init__.py），嘗試載入有 `Page` 元件的模組
_package_dir = Path(__file__).parent
_pages = []  # list of (title, component)
_errors = []

for i, _p in enumerate(sorted(_package_dir.glob("*.py"))):
    if _p.name == "__init__.py":
        continue
    try:
        spec = importlib.util.spec_from_file_location(f"pages._page_{i}", str(_p))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "Page"):
            title = getattr(module, "PAGE_TITLE", _p.stem)
            _pages.append((title, module.Page))
    except Exception as e:
        _errors.append(f"{_p.name}: {e}")


@solara.component
def Page():
    solara.Title("1105 Solara Webmap App")

    if _errors:
        solara.Markdown("**匯入模組時發生錯誤（不會中斷頁面）：**")
        for e in _errors:
            solara.Markdown(f"- `{e}`")

    if not _pages:
        solara.Markdown("目前沒有可用的子頁面（請檢查 pages 目錄下的 .py 檔）。")
        return

    sel = solara.reactive(0)

    def make_click(i):
        def _():
            sel.value = i

        return _

    solara.Markdown("### 選擇頁面：")
    for i, (title, _) in enumerate(_pages):
        solara.Button(title, on_click=make_click(i))

    _comp = _pages[sel.value][1]
    return _comp()


__all__ = ["Page"]
