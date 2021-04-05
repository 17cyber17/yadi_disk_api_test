from .base_page import BasePage
from yadi_disk_api import API
import urllib.parse

class TrashPage(BasePage):
    def delete_full_folder(self, path_to_folder):
        end_name = 0
        beginning_name = 0
        disk = API()
        true_path = urllib.parse.unquote(path_to_folder)
        for i in true_path:
            end_name += 1
            if i == "/":
                disk.delete_file_or_folder(path_to_folder[0:end_name - 1])
                beginning_name = end_name
                break

        if beginning_name == 0 and end_name != 0:
            disk.delete_file_or_folder(path_to_folder)

    def should_not_be_folder_in_trash(self, path_to_folder):
        end_name = 0
        beginning_name = 0
        true_path = urllib.parse.unquote(path_to_folder)
        for i in true_path:
            end_name += 1
            if i == "/":
                self.should_not_be_folder_or_file(path_to_folder[0:end_name - 1])
                beginning_name = end_name
                break

        if beginning_name == 0 and end_name != 0:
            self.should_not_be_folder_or_file(path_to_folder)

    def should_be_folder_in_trash(self, path_to_folder):
        end_name = 0
        beginning_name = 0
        true_path = urllib.parse.unquote(path_to_folder)
        for i in true_path:
            end_name += 1
            if i == "/":
                self.should_be_folder_or_file(path_to_folder[0:end_name - 1])
                beginning_name = end_name
                break

        if beginning_name == 0 and end_name != 0:
            self.should_be_folder_or_file(path_to_folder)
