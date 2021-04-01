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

    def test_upload_file(self, browser):
        link = "https://disk.yandex.ru/client/published"
        page = RecentPage(browser, link)
        disk = API()
        path_created_resource = "cat.jpg"
        url = "https://i.imgur.com/Ve9zZPX.jpg"
        disk.upload_url(path_created_resource, url)
        page.should_be_folder_or_file(path_created_resource)
        disk.delete_file_or_folder(path_created_resource)
        disk.empty_trash()

    def test_delete_file(self, browser):
        link = "https://disk.yandex.ru/client/published"
        page = RecentPage(browser, link)
        disk = API()
        path_created_resource = "cat.jpg"
        url = "https://i.imgur.com/Ve9zZPX.jpg"
        disk.upload_url(path_created_resource, url)
        page.should_be_folder_or_file(path_created_resource)
        disk.delete_file_or_folder(path_created_resource)
        page.should_not_be_folder_or_file(path_created_resource)
        disk.empty_trash()