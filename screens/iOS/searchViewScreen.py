from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver

        
class SearchViewScreen(Base):        
    def tap(self, label):
        AppAction.click_button(self, label)
        
    def confirm_screen_header(self, text, label):
        AppAction.confirm_element_text(self, text, label)
        
    def confirm_element_is_visible(self, element):
        AppAction.confirm_element_is_visible(self, element)
        
    def confirm_input_is_visible(self, element):
        AppAction.confirm_element_by_XPATH_is_visible(self, element)
        
    def enter_search_query(self, input, term):
        AppAction.enter_text(self, input, term)