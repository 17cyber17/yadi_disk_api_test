from selenium import webdriver
from .yadi_disk_api import API
from .pages.login_page import LoginPage
import urllib.parse
import pytest
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    link = "https://disk.yandex.ru/client"
    login_page = LoginPage(browser, link)
    login_page.open()
    login = "your login"
    password = "your password"
    login_page.login_user(login, password)
    time.sleep(1)
    # Пришлось добавить ожидание для того что бы можно было открыть другую страницу.
    # Без  него страница логина не успевает до конца загрузиться.


@pytest.fixture(scope="function", params=["QA%2FQA2"])
def new_folder(request):
    disk = API()
    end_name = 0
    beginning_name = 0
    path_to_folder = request.param
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
    beginning_name = 0

    for i in true_path:
        end_name += 1
        if i == "/":
            disk.delete_file_or_folder(path_to_folder[0:end_name-1])
            beginning_name = end_name
            break

    if beginning_name == 0 and end_name != 0:
        disk.delete_file_or_folder(path_to_folder)

    disk.empty_trash()


@pytest.fixture(scope="function", params=["catcat"])
def new_file(request):
    disk = API()
    url = "https://i.imgur.com/Ve9zZPX.jpg"
    path_created_resource = request.param
    disk.upload_url(path_created_resource, url)

    yield path_created_resource
    disk.delete_file_or_folder(path_created_resource)
    disk.empty_trash()
