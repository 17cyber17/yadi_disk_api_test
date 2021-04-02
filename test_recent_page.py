from .pages.login_page import LoginPage
from .pages.recent_page import RecentPage
from .yadi_disk_api import API
import pytest

class TestUserShared():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://disk.yandex.ru/client/recent"
        login_page = LoginPage(browser, link)
        login_page.open()
        login = "cyber17.semyon@yandex.ru"
        password = "321654987asdfghjz"
        login_page.login_user(login, password)

    def test_upload_file(self, new_file, browser):
        link = "https://disk.yandex.ru/client/published"
        page = RecentPage(browser, link)
        page.should_be_folder_or_file(new_file)

    def test_delete_file(self, new_file, browser):
        link = "https://disk.yandex.ru/client/published"
        page = RecentPage(browser, link)
        disk = API()
        page.should_be_folder_or_file(new_file)
        disk.delete_file_or_folder(new_file)
        page.should_not_be_folder_or_file(new_file)
