from .pages.login_page import LoginPage
from .pages.trash_page import TrashPage
from .yadi_disk_api import API
import pytest
import time

class TestUserShared():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://disk.yandex.ru/client/trash"
        login_page = LoginPage(browser, link)
        login_page.open()
        login = "cyber17.semyon@yandex.ru"
        password = "321654987asdfghjz"
        login_page.login_user(login, password)

    def test_delete_folder(self, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        disk = API()
        path_to_folder = "QA"
        disk.create_folder(path_to_folder)
        disk.delete_file_or_folder(path_to_folder)
        page.should_be_folder_or_file(path_to_folder)
        disk.empty_trash()

    def test_empty_trash(self, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        disk = API()
        path_to_folder = "QA"
        disk.create_folder(path_to_folder)
        disk.delete_file_or_folder(path_to_folder)
        page.should_be_folder_or_file(path_to_folder)
        disk.empty_trash()
        time.sleep(1)
        page.should_not_be_folder_or_file(path_to_folder)

    @pytest.mark.skip
    def test_restore_resource_from_trash(self, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        disk = API()
        path_to_folder = "QA"
        disk.create_folder(path_to_folder)
        disk.delete_file_or_folder(path_to_folder)
        page.should_be_folder_or_file(path_to_folder)
        disk.restore_resource_from_trash(path_to_folder)
        time.sleep(1)
        page.should_not_be_folder_or_file(path_to_folder)
        disk.delete_file_or_folder(path_to_folder)
        disk.empty_trash()