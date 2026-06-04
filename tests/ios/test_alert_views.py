import pytest
# from conftest_ios import test_setup_ios
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.alertViewsScreen import AlertViewsScreen as onAlertViewsScreen


"""
IOS APP Alert Views
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestAlertViews:
    """ALERTS"""
    
    def test_simple_alert_view(self):
        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Simple')
        onAlertViewsScreen.confirm_simple_alert
        onAlertViewsScreen.click_on_alert_action(self, "OK")
        
    def test_ok_cancel_alert_view(self):
        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Okay / Cancel')
        onAlertViewsScreen.click_on_alert_action(self, "Cancel")       
        onAlertViewsScreen.select_alert_view(self, 'Okay / Cancel')
        onAlertViewsScreen.click_on_alert_action(self, 'OK')

    def test_other_alert_view(self):
        onHomeScreen.tap(self, 'Alert Views')
        
        # ALERT - CHOICE ONE
        onAlertViewsScreen.select_alert_view(self, 'Other')
        onAlertViewsScreen.click_on_alert_action(self, 'Choice One') 
        
        # ALERT - CHOICE TWO
        onAlertViewsScreen.select_alert_view(self, 'Other')
        onAlertViewsScreen.select_alert_view(self, 'Choice Two')
        
        # ALERT - CANCEL CHOICES
        onAlertViewsScreen.select_alert_view(self, 'Other')
        onAlertViewsScreen.select_alert_view(self, 'Cancel')
        
    def test_text_entry_alert_view(self):
        text_input = "//XCUIElementTypeTextField"
        text_value = "this is a test case"

        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Text Entry')
        onAlertViewsScreen.submit_text_in_alert_input(self, text_input, text_value)
        onAlertViewsScreen.click_on_alert_action(self, 'OK')
    
    def test_secure_text_entry_alert_view(self):
        text_input = "//XCUIElementTypeSecureTextField"
        text_value = "password"

        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Secure Text Entry')
        onAlertViewsScreen.submit_text_in_alert_input(self, text_input, text_value)
        onAlertViewsScreen.click_on_alert_action(self, 'OK')
    
    """ACTION SHEETS"""
    
    def test_confirm_cancel_alert_action(self):
        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Confirm / Cancel')
        onAlertViewsScreen.click_action_on_sheet(self, 'Confirm')
        
        onAlertViewsScreen.select_alert_view(self, 'Confirm / Cancel')
        onAlertViewsScreen.click_action_on_sheet(self, 'Cancel')
    
    def test_destructive_alert_action(self):
        onHomeScreen.tap(self, 'Alert Views')
        onAlertViewsScreen.select_alert_view(self, 'Destructive')
        onAlertViewsScreen.click_action_on_sheet(self, 'Destructive Choice')
        
        onAlertViewsScreen.select_alert_view(self, 'Destructive')
        onAlertViewsScreen.click_action_on_sheet(self, 'Safe Choice')