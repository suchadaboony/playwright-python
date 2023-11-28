from playwright.sync_api import Page
from typing import List


class DuckDuckGoResultPage:

    def __init__(self, page:Page) -> None:
        self.page = page
        self.result_links = page.get_by_test_id("result")
        self.result_input = page.locator('id=search_form_input')
        
    def result_link_titles(self) -> List[str]:
        self.result_links.nth(4).wait_for()
        return self.result_links.all_text_contents()
    
    def result_link_titles_contain_phase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum