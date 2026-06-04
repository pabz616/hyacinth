import pytest
from conftest_ios import test_setup_ios
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from utils.data import iOSSearchViewScreen as searchViewElement
from screens.iOS.searchViewScreen import SearchViewScreen as onSearchViewScreen


"""
IOS APP SEARCH SCREEN
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestDefaultSearchView:
    """DEFAULT SEARCH"""

    def test_default_search_view_screen(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.confirm_screen_header(self, "Default Search Bar", searchViewElement.search_header)
        onSearchViewScreen.confirm_input_is_visible(self, searchViewElement.searchInput)
        onSearchViewScreen.confirm_element_is_visible(self, searchViewElement.scope1)
        onSearchViewScreen.confirm_element_is_visible(self, searchViewElement.scope2)
    
    def test_submit_search(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "Appium")
        # TODO - Normally there would be an assertion here for the search results, but the demo app doesn't have one
        onSearchViewScreen.tap(self, searchViewElement.submitButton)
        
    def test_submit_search_with_emoji(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "I'm so happy! 😀")
        onSearchViewScreen.tap(self, searchViewElement.submitButton)
        
    def test_submit_search_with_invalid_characters(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "I'm no hacker! <script>alert('Hacked!');</script>")
        # TODO - Normally there would be an error message or some sort of validation for invalid characters, but the demo app doesn't have one
        onSearchViewScreen.tap(self, searchViewElement.submitButton)
        
    def test_cancel_search(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.enter_search_query(self, searchViewElement.searchInput, "Another search term")
        onSearchViewScreen.tap(self, searchViewElement.cancelButton)

    def test_scope_buttons(self):
        onHomeScreen.tap(self, 'Search')
        onSearchViewScreen.tap(self, 'Default')
        onSearchViewScreen.tap(self, searchViewElement.scope2)
        onSearchViewScreen.tap(self, searchViewElement.scope1)