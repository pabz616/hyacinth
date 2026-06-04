from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver

        
class ImageViewsScreen(Base):
    def confirm_screen_header(self, text, label):
        AppAction.confirm_element_text(self, text, label)
        
    def confirm_images_on_screen(self, label):
        AppAction.confirm_element_is_visible(self, label)