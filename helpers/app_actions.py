from appium.webdriver.common.appiumby import AppiumBy
import time


class Base(object):
    def __init__(self, driver):
        self.driver = driver

        
class AppAction(Base):
    def click_button(self, label):
        nav = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{label}")
        assert nav.is_displayed()
        assert nav.is_enabled()
        nav.click()
        time.sleep(0.25)
        
    def click_button_by_id(self, id):
        nav = self.driver.find_element(AppiumBy.ID, f"{id}")
        assert nav.is_displayed()
        assert nav.is_enabled()
        nav.click()
        time.sleep(0.5)
        
    def confirm_element_text(self, expected_text, element):
        el = self.driver.find_element(AppiumBy.CLASS_NAME, f"{element}")
        assert f"{expected_text}" in el.text
        
    def confirm_element_is_visible(self, element):
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{element}")
        assert el.is_displayed()
  
    def confirm_element_by_XPATH_is_visible(self, element):
        el = self.driver.find_element(AppiumBy.XPATH, f"{element}")
        assert el.is_displayed()
        
    def confirm_element_by_ID_is_visible(self, element_id):
        el = self.driver.find_element(AppiumBy.ID, f"{element_id}")
        assert el.is_displayed()
        
    def alert_is_visible(self, alert):
        popup = self.driver.find_element(AppiumBy.XPATH, f"{alert}")
        assert popup.is_displayed()
        
    def confirm_alert_title(self, alert_title):
        text = self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name=f"{alert_title}"]')
        assert text.is_displayed()
        
    def alert_action(self, action):
        button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{action}")
        assert button.is_displayed()
        assert button.is_enabled()
        button.click()
        
    def dismiss_popover(self, action):
        button = self.driver.find_element(AppiumBy.XPATH, f"{action}")
        button.click()
        
    def sheet_action(self, action):
        button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"{action}")
        assert button.is_displayed()
        assert button.is_enabled()
        button.click()
        
    def enter_text(self, text_input, text_value):
        input = self.driver.find_element(AppiumBy.XPATH, f"{text_input}")
        assert input.is_displayed()
        input.click()
        input.send_keys(text_value)
       
    def scroll_to_element(self, element):
        self.driver.execute_script('mobile: scrollGesture', {'elementId': element, 'direction': 'down'})