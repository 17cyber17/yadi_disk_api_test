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

    def path_to_trash(self):
        disk = API()
        path = []
        end_path = 0
        beginning_path = 0
        len_path = 4
        resources_trash = disk.resources_trash()

        # нужно начинать с четвертого для того что бы не добавить лишний путь т.к четвертым символом обязательно будет _
        for i in resources_trash[4:]:
            len_path += 1
            if i == "/":
                beginning_path = len_path
            if i == '_':
                end_path = len_path + 40
                # путь в корзине отличается от оригинального лишь суфиксом и его длина составляет 40 символов
                path.append(resources_trash[beginning_path:end_path])

        return path





