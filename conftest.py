import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def chrome_driver(request):
    chrome_driver = WebDriver(executable_path='F://selenium//chromedriver.exe')
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture()
def firefox_driver(request):
    firefox_driver = WebDriver(executable_path='C://Program Files (x86)//Mozilla Firefox//geckodriver.exe')
    firefox_driver.implicitly_wait(3)
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.close()


@pytest.fixture()
def opera_driver(request):
    opera_driver = WebDriver(executable_path='C://Users//HOME//AppData//'
                                             'Local//Programs//Opera//60.0.3255.27//operadriver.exe')
    opera_driver.implicitly_wait(3)
    opera_driver.maximize_window()
    yield opera_driver
    opera_driver.close()