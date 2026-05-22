import pytest
from os import environ
from appium import webdriver
from utils.data import Project
from appium.options.ios import XCUITestOptions

    
@pytest.fixture(scope='function')
def test_setup_ios(request):
    test_name = request.node.name
    build = environ.get('BUILD', "Pytest iOS Sample")
    caps = {}
    caps["deviceName"] = 'iPhone 17 Pro'
    caps["platformName"] = 'iOS'
    caps["platformVersion"] = '26.2'
    caps["app"] = f"{Project.ios_app}"
    caps["automationName"] = 'XCUITest'
    caps["isRealMobile"] = True
    caps['project'] = f"{Project.name}"
    caps['build'] = build
    caps['name'] = test_name
    driver = webdriver.Remote(f"{Project.appium_server_url}", options=XCUITestOptions().load_capabilities(caps))
    request.cls.driver = driver
    
    yield driver
    driver.quit()