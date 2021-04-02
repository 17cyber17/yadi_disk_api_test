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

    def test_create_folder(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        page.should_be_folder_or_file(new_folder)

    def test_delete_folder(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        page.should_be_folder_or_file(new_folder)
        disk.delete_file_or_folder(new_folder)
        page.should_not_be_folder_or_file(new_folder)

    def test_upload_url(self, new_file, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        page.should_be_folder_or_file(new_file)

    def test_copy_file(self, new_file, new_folder, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        page.should_be_folder_or_file(new_file)
        page.should_be_folder_or_file(new_folder)
        path_copied_resource = new_file
        path_created_resource = new_folder + "%2F" + new_file
        disk.create_copy_file_or_folder(path_copied_resource, path_created_resource)
        page.should_be_folder_or_file(path_created_resource)

    def test_move_file(self, new_file, new_folder, browser):
        link = "https://disk.yandex.ru/client/disk"
        page = DiskPage(browser, link)
        disk = API()
        page.should_be_folder_or_file(new_file)
        page.should_be_folder_or_file(new_folder)
        path_resource_move = new_file
        path_created_resource = new_folder + "%2F" + new_file
        disk.move_file_or_folder(path_resource_move, path_created_resource)
        page.should_be_folder_or_file(path_created_resource)

