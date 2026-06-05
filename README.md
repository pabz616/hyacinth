# hyacinth

Appium w. Python

As of June 2026, version is `3.2.4`

## Setup

### Documentation

* `https://appium.github.io/python-client-sphinx/`
* `https://appium.io/docs/en/2.5/quickstart/`
* `https://www.lambdatest.com/support/docs/appium-python-pytest/`

## Pre-flight Check

* Check current version of Appium - `appium -v` .. reconcile with release notes - `https://www.npmjs.com/package/appium?activeTab=versions` .. update accordingly if behind.
* Launch appium inspector and verify you can access the app via the inspector.
* Run appium-doctor and confirm setup. `appium-doctor --ios` or `appium-doctor --android`
* Install appium driver for android - `appium driver install uiautomator2`
* Verify your system is updated by reconciling the out from the list with current version - `appium driver list`
  * To update a driver - `appium driver update <driver-name>` (pro tip! grab some coffee .. this will be tedious!)

| Driver List |
| :------------ |
| xcuitest |
| espresso |
| gecko |
| safari |
| uiautomator2 |
| flutter |
| mac2 |
| chromium |

### Directions

1. Following the quickstart documentation, use appium-doctor to correct any misconfiguration issues
2. If you are using VSCode, add python and simcode extensions, otherwise you can use genymotion or real devices
3. Install the necessary drivers for ios and android
4. Use the following configurations (`conftest.py` / `conftest_ios.py`) and set your environment up accordingly
5. Launch appium server
6. Launch the device emulator(s)
7. For android, run the script: `../tests/android/pytest_setup_check.py`(be mindful of the imports from other directories)
8. For ios, run the script: `../tests/ios/pytest_ios_setup.py` (be mindful of the imports from other directories)


Demo Apps
1. For Android, `../apps/android/ApiDemos-debug.apk`
2. For iOS, `../apps/ios/UIKitCatalog-iphonesimulator.app`
