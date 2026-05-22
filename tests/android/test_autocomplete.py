import pytest
from screens.android.homeScreen import HomeScreen as onHomeScreen
from screens.android.viewsScreen import ViewsScreen as onViewsScreen
from screens.android.autocompleteScreen import AutoCompleteScreen as onAutoCompleteScreen


""" TEST AUTOCOMPLETE FEATURES """


@pytest.mark.usefixtures('test_setup_android')
class TestAutoCompleteScreen:
    def test_autocomplete_screen_UI(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.checkUI(self)

    def test_autocomplete_screen_top(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_screen_top_and_enter_text(self, "British Vi")
        # Expected to find "British Virgin Islands" in the content after entering "British Vi"
    
    def test_autocomplete_screen_bottom_and_enter_text(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_screen_bottom_and_enter_text(self, "British Vi")
        pass

    @pytest.mark.skip(reason="Need to fix scrolling to the element.") 
    def test_autocomplete_screen_scrollable(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_scrollView_and_scroll_down(self)
        pass
    
    def test_autocomplete_screen_contacts(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_contacts(self)
        pass    
    
    def test_autocomplete_screen_contacts_with_hint(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_contacts_with_hint(self)
        pass 
    
    def test_autocomplete_screen_multiple_items(self):
        onHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_autocomplete_screen(self)
        onAutoCompleteScreen.navigate_to_multiple_items_and_enter_text(self, "Flo")
        # Expected to find "Florida" in the content after entering "Flo"

