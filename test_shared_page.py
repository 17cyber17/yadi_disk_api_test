from .pages.login_page import LoginPage
from .pages.shared_page import SharedPage
from .yadi_disk_api import API
import pytest

class TestUserShared():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://disk.yandex.ru/client/published"
        login_page = LoginPage(browser, link)
        login_page.open()
        login = "cyber17.semyon@yandex.ru"
        password = "321654987asdfghjz"
        login_page.login_user(login, password)

    def test_create_publish(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/published"
        page = SharedPage(browser, link)
        disk = API()
        disk.publish_resource(new_folder)
        page.should_be_folder_or_file(new_folder)

    def test_create_unpublish(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/published"
        page = SharedPage(browser, link)
        disk = API()
        disk.publish_resource(new_folder)
        page.should_be_folder_or_file(new_folder)
        disk.unpublish_resource(new_folder)
        page.should_not_be_folder_or_file(new_folder)