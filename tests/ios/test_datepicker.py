import pytest
from conftest_ios import test_setup_ios
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.datepickerViewScreen import DatePickerViewsScreen as onDatePickerViewsScreen


"""
IOS APP DATE PICKER
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestDatePickerViews:
    def test_current_date_and_time(self):
        onHomeScreen.select_option(self, 'Date Picker')
        onDatePickerViewsScreen.confirm_date_and_time(self)
        
    def test_change_current_date(self):
        onHomeScreen.select_option(self, 'Date Picker')
        onDatePickerViewsScreen.set_new_date(self)
     
    @pytest.mark.skip(reason="time picker is not getting clicked")    
    def test_change_current_time(self):
        onHomeScreen.select_option(self, 'Date Picker')
        onDatePickerViewsScreen.set_new_time(self)