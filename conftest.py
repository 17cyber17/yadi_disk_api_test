import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .yadi_disk_api import API

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
    path_to_folder = "QA"
    disk.create_folder(path_to_folder)

    yield path_to_folder
    disk.delete_file_or_folder(path_to_folder)
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
