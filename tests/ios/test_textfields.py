import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSHomeScreen
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.textviewScreen import TextViewsScreen as onTextViewsScreen

"""
IOS APP TEXT FIELDS
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestTextViews:
    """TEXT INPUTS"""
    
    def test_default_text_field(self):
        onHomeScreen.select_option(self, 'Text Fields')
        onTextViewsScreen.enter_text_in_field(self, iOSHomeScreen.defaultInput, 'this is a default field test case')
        
    def test_tinted_text_field(self):
        onHomeScreen.select_option(self, 'Text Fields')
        onTextViewsScreen.enter_text_in_field(self, iOSHomeScreen.tintedInput, 'this is a tinted field test case')
        
    def test_secure_text_field(self):
        onHomeScreen.select_option(self, 'Text Fields')
        onTextViewsScreen.enter_text_in_field(self, iOSHomeScreen.secureInput, 'this is a secure field test case')
