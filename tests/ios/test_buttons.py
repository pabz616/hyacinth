import pytest
from conftest_ios import test_setup_ios
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.buttonViewsScreen import ButtonViewsScreen as onButtonViewsScreen


"""
IOS APP BUTTON TYPES
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestButtonViews:
    def test_text_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'Button')
        
    def test_contact_add_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'add')
        
    def test_detail_disclosure_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'More Info')
        
    def test_image_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'X Button')
        
    def test_attributed_text_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'Button')
        
    def test_symbol_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'Person')
        
    def test_text_and_symbol_button(self):
        onHomeScreen.tap(self, 'Buttons')
        onButtonViewsScreen.click_on_button(self, 'Button')