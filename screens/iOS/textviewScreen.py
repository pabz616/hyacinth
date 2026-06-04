from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class TextViewsScreen(Base):
    def tap(self, label):
        AppAction.click_button(self, label)
        
    def enter_text_in_field(self, field, text):
        AppAction.enter_text(self, field, text)