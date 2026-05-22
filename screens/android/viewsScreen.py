from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        

class ViewsScreen(Base):
    def navigate_to_autocomplete_screen(self):
        AppAction.click_button(self, "Auto Complete")
        
    def navigate_to_light_theme_control_screen(self):
        AppAction.click_button(self, "Controls")
        AppAction.click_button(self, "1. Light Theme")