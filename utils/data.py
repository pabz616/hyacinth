class Project:
    appium_server_url = 'http://127.0.0.1:4723'
    android_app = '/Users/pablovergara/Desktop/automation/hyacinth/apps/android/ApiDemos-debug.apk'
    ios_app = '/Users/pablovergara/Desktop/automation/hyacinth/apps/ios/UIKitCatalog-iphonesimulator.app'
    name = "Appium w. Pytest"
    
    
class AndroidHomeScreen:
    buttons = [
        "Access'ibility", 'Accessibility', 'Animation', 'App', 'Content', 'Graphics', 
        'Media', 'NFC', 'OS', 'Preference', 'Text', 'Views']
    
    
class iOSHomeScreen:
    buttons = [
        "Activity Indicators", "Alert Views", "Buttons", "Date Picker",
        "Image View", "Page Control", "Picker View", "Progress Views",
        "Search", "Segmented Controls", "Sliders", "Stack Views",
        "Steppers", "Switches", "Text Fields", "Toolbars", "Web View"]

    
class iOSTextViewsScreen:
    defaultInput = '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField[@value="Placeholder text"]'
    tintedInput = '//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField[@value="Placeholder text"]'
    secureInput = '//XCUIElementTypeSecureTextField[@value="Placeholder text"]'
    specificKeyboardInput = '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField[@value="Placeholder text"]'
    customInput = '//XCUIElementTypeImage[@name="text_field_background"]'
    
        
class Accessibility:
    accessibility_node_provider_copy = "Enable TalkBack and Explore-by-touch from accessibility settings. Then touch the colored squares."