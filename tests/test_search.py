import re
from playwright.sync_api import Page, expect
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(
        page: Page,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None: 

    
    phrase = 'panda'

    # Given the Duckduckgo home page is displayed
    search_page.load()

    # When the user seaches for a phrase 
    search_page.search(phrase)

    # Then the search result query is the phrase 
    expect(result_page.result_input).to_have_value(phrase)

    # And the search result links pertain to the phrase   
    assert result_page.result_link_titles_contain_phase(phrase)

    # And the search result title contains the phrase 
    expect(page).to_have_title("panda at DuckDuckGo")

