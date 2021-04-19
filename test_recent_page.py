from .pages.recent_page import RecentPage
from .yadi_disk_api import API


class TestUserRecent:
    def test_upload_file(self, new_file, browser):
        link = "https://disk.yandex.ru/client/recent"
        page = RecentPage(browser, link)
        page.open()
        page.should_be_folder_or_file(new_file)

    def test_delete_file(self, new_file, browser):
        link = "https://disk.yandex.ru/client/recent"
        page = RecentPage(browser, link)
        page.open()
        disk = API()
        page.should_be_folder_or_file(new_file)
        disk.delete_file_or_folder(new_file)
        page.should_not_be_folder_or_file(new_file)
