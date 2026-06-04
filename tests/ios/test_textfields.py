import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSTextViewsScreen as textViews
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.textviewScreen import TextViewsScreen as onTextViewsScreen

"""
IOS APP TEXT FIELDS
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestTextViews:
    """TEXT INPUTS"""
    
    def test_multiple_text_field(self):
        onHomeScreen.select_option(self, 'Text Fields')
        onTextViewsScreen.enter_text_in_field(self, textViews.defaultInput, 'this is a default field test case')
        onTextViewsScreen.enter_text_in_field(self, textViews.tintedInput, 'this is a tinted field test case')
        onTextViewsScreen.enter_text_in_field(self, textViews.secureInput, 'this is a secure field test case')
        onTextViewsScreen.enter_text_in_field(self, textViews.specificKeyboardInput, 'this is a specific keyboard field test case')
        onTextViewsScreen.enter_text_in_field(self, textViews.customInput, 'this is a custom field test case')
