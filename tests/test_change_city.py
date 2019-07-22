import allure
from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import AttachmentType


@allure.title('Проверка перехода по ссылке на сайте')
@allure.severity(Severity.CRITICAL)
def test_change_city_chrome(chrome_driver: WebDriver):

    with allure.step('ищем страницу сайта'):
        chrome_driver.get('https://google.ru')
        search_input = chrome_driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
        search_button = chrome_driver.find_element_by_xpath('//div[@class="FPdoLc VlcLAe"]//input[@type="submit"]')
        search_input.send_keys('брусника екатеринбург')
        search_button.click()

    with allure.step('находим линк'):
        link = chrome_driver.find_element_by_xpath('//a[@href="https://ekaterinburg.brusnika.ru/"]')
        link.click()

    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    with allure.step('Проверяем корректность Title страницы'):
        assert chrome_driver.title == 'Квартиры в новостройках от застройщика Брусника Екатеринбург'

    with allure.step('меняем город'):
        change=chrome_driver.find_element_by_xpath('//div[@class="header__city-current js-header-city"]')
        change.click()
        dif_city = chrome_driver.find_element_by_xpath('//div[@class="header__city"]//li[@class="header__city-item"]'
                                                       '//a[@href="http://tyumen.brusnika.ru"]')
        dif_city.click()
        assert chrome_driver.title == "Квартиры в новостройках от застройщика Брусника Тюмень"

    with allure.step('делаем скриншот'):
        allure.attach(chrome_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)


@allure.title('Проверка перехода по ссылке на сайте')
@allure.severity(Severity.CRITICAL)
def test_change_city_opera(opera_driver: WebDriver):

    with allure.step('ищем страницу сайта'):
        opera_driver.get('https://google.ru')
        search_input = opera_driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
        search_button = opera_driver.find_element_by_xpath('//div[@class="FPdoLc VlcLAe"]//input[@type="submit"]')
        search_input.send_keys('брусника екатеринбург')
        search_button.click()

    with allure.step('находим линк'):
        link = opera_driver.find_element_by_xpath('//a[@href="https://ekaterinburg.brusnika.ru/"]')
        link.click()

    opera_driver.switch_to.window(opera_driver.window_handles[1])
    with allure.step('Проверяем корректность Title страницы'):
        assert opera_driver.title == 'Квартиры в новостройках от застройщика Брусника Екатеринбург'

    with allure.step('меняем город'):
        change=opera_driver.find_element_by_xpath('//div[@class="header__city-current js-header-city"]')
        change.click()
        dif_city = opera_driver.find_element_by_xpath('//div[@class="header__city"]//li[@class="header__city-item"]'
                                                      '//a[@href="http://tyumen.brusnika.ru"]')
        dif_city.click()
        assert opera_driver.title == "Квартиры в новостройках от застройщика Брусника Тюмень"

    with allure.step('делаем скриншот'):
        allure.attach(opera_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)


@allure.title('Проверка перехода по ссылке на сайте')
@allure.severity(Severity.CRITICAL)
def test_change_city_firefox(firefox_driver: WebDriver):

    with allure.step('ищем страницу сайта'):
        firefox_driver.get('https://google.ru')
        search_input = firefox_driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
        search_button = firefox_driver.find_element_by_xpath('//div[@class="FPdoLc VlcLAe"]//input[@type="submit"]')
        search_input.send_kfirefox_eys('бруfirefox_сника екатеринбург')
        search_button.click()

    with allure.step('находим линк'):
        link = firefox_driver.find_element_by_xpath('//a[@href="https://ekaterinburg.brusnika.ru/"]')
        link.click()

    firefox_driver.switch_to.window(firefox_driver.window_handles[1])
    with allure.step('Проверяем корректность Title страницы'):
        assert firefox_driver.title == 'Квартиры в новостройках от застройщика Брусника Екатеринбург'

    with allure.step('меняем город'):
        change = firefox_driver.find_element_by_xpath('//div[@class="header__city-current js-header-city"]')
        change.click()
        dif_city = firefox_driver.find_element_by_xpath('//div[@class="header__city"]//li[@class="header__city-item"]'
                                                        '//a[@href="http://tyumen.brusnika.ru"]')
        dif_city.click()
        assert firefox_driver.title == "Квартиры в новостройках от застройщика Брусника Тюмень"

    with allure.step('делаем скриншот'):
        allure.attach(firefox_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)