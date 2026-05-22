import pytest
from screens.android.homeScreen import HomeScreen as fromHomeScreen
from screens.android.viewsScreen import ViewsScreen as onViewsScreen
from screens.android.controlsLightScreen import LightThemeControlScreen as onLightThemeControlScreen


"""
TEST LIGHT-THEMED VIEW CONTROLS
"""


@pytest.mark.usefixtures('test_setup_android')
class TestViewControlScreen:
    def test_light_theme_control_screen(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.checkUI(self)

    def test_light_theme_save_action(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.click_save_button(self)
        
    def test_light_theme_control_text_input(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.enter_text(self, 'this is a cool android app test')
        
    def test_light_theme_click_all_checkbox_options(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.click_checkbox(self, 'Checkbox 1')
        onLightThemeControlScreen.click_checkbox(self, 'Checkbox 2')
        
    def test_light_theme_click_all_radiobutton_options(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.click_radio_button(self, 'RadioButton 1')
        onLightThemeControlScreen.click_radio_button(self, 'RadioButton 2')
        
    def test_light_theme_add_to_favorites(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.click_favorite(self)
        
    def test_light_theme_click_off_switch(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.click_off_switch1(self)
        onLightThemeControlScreen.click_off_switch2(self)
        
    def test_light_theme_select_from_list(self):
        fromHomeScreen.navigate_to_views_screen(self)
        onViewsScreen.navigate_to_light_theme_control_screen(self)
        onLightThemeControlScreen.select_from_list(self)
