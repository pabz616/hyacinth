import pytest
from conftest_ios import test_setup_ios
from utils.data import iOSImageElement as imageElement
from screens.iOS.homeScreen import HomeScreen as onHomeScreen
from screens.iOS.imageViewScreen import ImageViewsScreen as onImageViewsScreen

"""
IOS APP IMAGE VIEWS TESTS
"""


@pytest.mark.usefixtures('test_setup_ios')
class TestImageViews:
    """IMAGE VIEWS"""
    def test_confirm_images_on_screen(self):
        onHomeScreen.tap(self, 'Image View')
        onImageViewsScreen.confirm_screen_header(self, 'Image View', imageElement.header)
        onImageViewsScreen.confirm_images_on_screen(self, imageElement.image1)