import pytest

from playwright.sync_api import Page
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

@pytest.fixture
def result_page (page:Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)

@pytest.fixture
def search_page (page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)