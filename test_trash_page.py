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

    def test_delete_folder(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        page.delete_full_folder(new_folder)
        page.should_be_folder_or_file(new_folder)

    def test_empty_trash(self, new_folder, new_file, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        disk = API()
        page.delete_full_folder(new_folder)
        page.should_be_folder_in_trash(new_folder)
        disk.delete_file_or_folder(new_file)
        page.should_be_folder_or_file(new_file)
        disk.empty_trash()
        page.should_not_be_folder_in_trash(new_folder)
        #Пришлось написать новую функцию для проверки папки в корзине так как в ней нельзя просматривать вложенния
        page.should_not_be_folder_or_file(new_file)

    @pytest.mark.xfail  #Нерабочий запрос в api
    def test_restore_resource_from_trash(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        disk = API()
        page.delete_folder(new_folder)
        page.should_be_folder_or_file(new_folder)
        disk.restore_resource_from_trash(new_folder)
        time.sleep(1)
        page.should_not_be_folder_or_file(new_folder)