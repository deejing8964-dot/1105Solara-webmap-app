
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
		# 使用 spec_from_file_location 載入任意檔名的模組（可以容許非標準識別字的檔名）
		spec = importlib.util.spec_from_file_location(f"pages._page_{i}", str(_p))
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		if hasattr(module, "Page"):
			# 以檔名（不含副檔名）當作標題，使用者可在各模組中覆寫 PAGE_TITLE
			title = getattr(module, "PAGE_TITLE", _p.stem)
			_pages.append((title, module.Page))
	except Exception as e:
		# 不讓整個套件匯入失敗，收集錯誤以便在 UI 顯示
		_errors.append(f"{_p.name}: {e}")


@solara.component
def Page():
	"""Package-level Page：顯示簡單目錄並在使用者點選後載入對應頁面。

	目的：當 Solara 在 Hugging Face 上啟動時不會顯示空白頁面。
	"""
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

	# 顯示目前選中的頁面元件
	_comp = _pages[sel.value][1]
	return _comp()


__all__ = ["Page"]
