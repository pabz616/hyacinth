import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSSearchViewScreen as searchViewElement
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.searchViewScreen import SearchViewScreen as onSearchViewScreen


"""
IOS APP CUSTOMSEARCH SCREEN
"""

@pytest.mark.usefixtures('test_setup_ios')
class TestCustomSearchView:
    """CUSTOM SEARCH"""
    
    def test_custom_search_view_screen(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Custom')
        onSearchViewScreen.confirm_screen_header(self, "Custom Search Bar", searchViewElement.search_header)
        onSearchViewScreen.confirm_input_is_visible(self, searchViewElement.searchInput)

    def test_custom_search(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Custom')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "Custom Search")
        onSearchViewScreen.tap(self, searchViewElement.submitButton)
        
    def test_cancel_custom_search(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Custom')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "Custom Search")
        onSearchViewScreen.tap(self, searchViewElement.cancelButton)