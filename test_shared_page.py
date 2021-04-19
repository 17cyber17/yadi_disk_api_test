from .pages.shared_page import SharedPage
from .yadi_disk_api import API


class TestUserShared:
    def test_create_publish_root(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/published"
        page = SharedPage(browser, link)
        disk = API()
        # Проверяем в этом тесте только корень так как при переходе в папку страница меняется на страницу диска.
        path = page.root_directory(new_folder)
        disk.publish_resource(path)
        # Если открыть страницу до публикации там будет неактуальная информация.
        page.open()
        page.should_be_folder_or_file(path)

    def test_create_unpublish_root(self, new_folder, browser):
        link = "https://disk.yandex.ru/client/published"
        page = SharedPage(browser, link)
        disk = API()
        path = page.root_directory(new_folder)
        disk.publish_resource(path)
        # Если открыть страницу до публикации там будет неактуальная информация.
        page.open()
        page.should_be_folder_or_file(path)
        disk.unpublish_resource(path)
        page.should_not_be_folder_or_file(path)
