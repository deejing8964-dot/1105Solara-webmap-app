# This file moved into the `pages/` package.
# Use the package-level `pages.Page` navigator as a safe redirect so
# accidental imports won't crash.
from pages import Page

__all__ = ["Page"]