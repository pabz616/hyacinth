from helpers.app_actions import AppAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        
        
class AutoCompleteScreen(Base):
    def checkUI(self):
        screen_top = '//android.widget.TextView[@content-desc="1. Screen Top"]'
        screen_bottom = '//android.widget.TextView[@content-desc="2. Screen Bottom"]'
        scrollable = '//android.widget.TextView[@content-desc="3. Scroll"]'
        contacts = '//android.widget.TextView[@content-desc="4. Contacts"]'
        contacts_with_hint = '//android.widget.TextView[@content-desc="5. Contacts with Hint"]'
        multiple_items = '//android.widget.TextView[@content-desc="6. Multiple items"]'
        
        AppAction.confirm_element_by_XPATH_is_visible(self, screen_top)
        AppAction.confirm_element_by_XPATH_is_visible(self, screen_bottom)
        AppAction.confirm_element_by_XPATH_is_visible(self, scrollable)
        AppAction.confirm_element_by_XPATH_is_visible(self, contacts)
        AppAction.confirm_element_by_XPATH_is_visible(self, contacts_with_hint)
        AppAction.confirm_element_by_XPATH_is_visible(self, multiple_items)
        
    def navigate_to_screen_top_and_enter_text(self, text_value):
        country_input = '//android.widget.AutoCompleteTextView[@resource-id="io.appium.android.apis:id/edit"]'
        # value = 'British Virgin Islands'
        
        AppAction.click_button(self, "1. Screen Top")
        AppAction.enter_text(self, country_input, "British Vi")
        # assert value in self.driver.page_source, f"Expected '{value}' to be in the page source but got '{self.driver.page_source}'"
   
    def navigate_to_screen_bottom_and_enter_text(self, text_value):
        country_input = '//android.widget.AutoCompleteTextView[@resource-id="io.appium.android.apis:id/edit"]'
        
        AppAction.click_button(self, "2. Screen Bottom")
        AppAction.enter_text(self, country_input, text_value)
        # AppAction.confirm_element_is_visible(self, content)
        
    def navigate_to_scrollView_and_scroll_down(self):
        input = 'io.appium.android.apis:id/edit'
        
        AppAction.click_button(self, "3. Scroll")
        AppAction.click_button(self, "Scroll")
        AppAction.scroll_to_element(self, input)
        AppAction.confirm_element_is_visible(self, input)
    
    def navigate_to_contacts(self):
        AppAction.click_button(self, "4. Contacts")
    
    def navigate_to_contacts_with_hint(self):
        AppAction.click_button(self, "5. Contacts with Hint")
    
    def navigate_to_multiple_items_and_enter_text(self, text_value):
        country_input = '//android.widget.MultiAutoCompleteTextView[@resource-id="io.appium.android.apis:id/edit"]'
        
        AppAction.click_button(self, "6. Multiple items")
        AppAction.enter_text(self, country_input, text_value)


