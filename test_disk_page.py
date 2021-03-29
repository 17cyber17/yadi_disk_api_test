from .pages.login_page import LoginPage
from .pages.disk_page import DiskPage
from .yadi_disk_api import API
import pytest

class TestUserDisk():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://disk.yandex.ru/client/disk"
        login_page = LoginPage(browser, link)
        login_page.open()
        login = "cyber17.semyon@yandex.ru"
        password = "321654987asdfghjz"
        login_page.login_user(login, password)


    def test_create_folder(self, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        path_to_folder = "QA%2FQA1%2FQA2"
        disk.create_folder(path_to_folder)
        page.should_be_folder_or_file(path_to_folder)

    @pytest.mark.skip
    def test_upload_url(self, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        path_created_resource = "cat.jpg"
        url = "https://i.imgur.com/Ve9zZPX.jpg"
        disk.upload_url(path_created_resource, url)
        page.should_be_file_or_file(path_created_resource)

    @pytest.mark.skip
    def test_copy_file_or_folder(self, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        url = "https://i.imgur.com/Ve9zZPX.jpg"
        path_created_resource = "cat.jpg"
        disk.upload_url(path_created_resource, url)
        path_copied_resource = path_created_resource
        path_created_resource = "QA%2Fcat.jpg"
        disk.create_copy_file_or_folder(path_copied_resource, path_created_resource)
        page.should_be_folder_or_file(path_created_resource)

