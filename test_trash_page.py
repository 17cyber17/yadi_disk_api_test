from .pages.trash_page import TrashPage
from .yadi_disk_api import API


class TestUserTrash:
    def test_delete_folder(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        page.open()
        page.delete_full_folder(new_folder)
        # Проверяем только корень так как в корзине нельзя просматривать вложения
        page.should_be_root(new_folder)

    def test_empty_trash(self, new_folder, new_file, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        page.open()
        disk = API()
        page.delete_full_folder(new_folder)
        page.should_be_root(new_folder)
        disk.delete_file_or_folder(new_file)
        page.should_be_folder_or_file(new_file)
        disk.empty_trash()
        page.should_not_be_root(new_folder)
        page.should_not_be_folder_or_file(new_file)

    def test_restore_resource_from_trash(self, new_folder, new_file, browser):
        link = "https://disk.yandex.ru/client/trash"
        page = TrashPage(browser, link)
        page.open()
        disk = API()
        page.delete_full_folder(new_folder)
        page.should_be_root(new_folder)
        disk.delete_file_or_folder(new_file)
        page.should_be_folder_or_file(new_file)
        path = page.path_to_trash()
        disk.restore_resource_from_trash(path[0])
        page.should_not_be_root(new_folder)
        disk.restore_resource_from_trash(path[1])
        page.should_not_be_folder_or_file(new_file)
