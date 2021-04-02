import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .yadi_disk_api import API
import urllib.parse

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()

@pytest.fixture(scope="function")
def new_folder():
    disk = API()
    end_name = 0
    beginning_name = 0
    path_to_folder = "QA%2FQA2"
    true_path = urllib.parse.unquote(path_to_folder)

    for i in true_path:
        end_name += 1
        if i == "/":
            disk.create_folder(path_to_folder[0:end_name-1])
            end_name += 2
            beginning_name = end_name

    if beginning_name == 0 and end_name != 0:
        disk.create_folder(path_to_folder)
    else:
        if beginning_name != 0:
            disk.create_folder(path_to_folder[0:end_name])

    yield path_to_folder
    end_name = 0

    for i in true_path:
        end_name += 1
        if i == "/":
            disk.delete_file_or_folder(path_to_folder[0:end_name-1])
            break

    disk.empty_trash()

@pytest.fixture(scope="function")
def new_file():
    disk = API()
    url = "https://i.imgur.com/Ve9zZPX.jpg"
    path_created_resource = "catcat"
    disk.upload_url(path_created_resource, url)

    yield path_created_resource
    disk.delete_file_or_folder(path_created_resource)
    disk.empty_trash()
