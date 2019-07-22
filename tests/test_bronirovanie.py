import allure
from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains


@allure.title('Проверка бронирования квартиры')
@allure.severity(Severity.CRITICAL)
def test_bronirovanie_chrome(chrome_driver: WebDriver):

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

    with allure.step('Переходим во вкладку Проекты'):
        projects=chrome_driver.find_elements_by_xpath('//li[@class="header__menu-item"]')
        projects[1].click()
        project_select = chrome_driver.find_element_by_xpath('//img[@src="/media/complex/map_icon/'
                                                             'shg_active_3vcd0Ir_gCwpuHn.svg"]')
        project_select.click()

    with allure.step('Переходим к выбору квартиры'):
        choice_aparts = chrome_driver.find_element_by_xpath('//div[@class="mobile-container"]'
                                                            '//a[@href="/flat/?complex=5"]')
        choice_aparts.click()

    with allure.step('Ставим фильтр по стоимости и выбираем квартиру'):
        filter_price = chrome_driver.find_elements_by_xpath('//div[@class="noUi-handle noUi-handle-upper"]')
        move = ActionChains(chrome_driver)
        move.click_and_hold(filter_price[0]).move_by_offset(-168, 0).release().perform()
        allure.attach(chrome_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)
        aparts = chrome_driver.find_elements_by_xpath('//a[@class="flat-type-card js-flat-type-card active"]')
        assert len(aparts) == 8
        apart = chrome_driver.find_element_by_xpath('//a[@href="/flat/13407/"]')
        apart.click()

    with allure.step('Бронируем квартиру'):
        button = chrome_driver.find_element_by_xpath('//div[@class="flat-d-about__button button js-show-popup"]')
        button.click()
        check = chrome_driver.find_element_by_xpath('//div[@class="form js-form-container active"]')
        assert check.is_displayed()

    with allure.step('делаем скриншот'):
        allure.attach(chrome_driver.get_screenshot_as_png(), name='ScreenShot1', attachment_type=AttachmentType.PNG)


@allure.title('Проверка бронирования квартиры')
@allure.severity(Severity.CRITICAL)
def test_bronirovanie_opera(opera_driver: WebDriver):

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

    with allure.step('Переходим во вкладку Проекты'):
        projects = opera_driver.find_elements_by_xpath('//li[@class="header__menu-item"]')
        projects[1].click()
        project_select = opera_driver.find_element_by_xpath('//img[@src="/media/complex/map_icon/'
                                                            'shg_active_3vcd0Ir_gCwpuHn.svg"]')
        project_select.click()

    with allure.step('Переходим к выбору квартиры'):
        choice_aparts = opera_driver.find_element_by_xpath('//div[@class="mobile-container"]'
                                                           '//a[@href="/flat/?complex=5"]')
        choice_aparts.click()

    with allure.step('Ставим фильтр по стоимости и выбираем квартиру'):
        filter_price = opera_driver.find_elements_by_xpath('//div[@class="noUi-handle noUi-handle-upper"]')
        move = ActionChains(opera_driver)
        move.click_and_hold(filter_price[0]).move_by_offset(-168, 0).release().perform()
        allure.attach(opera_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)
        aparts = opera_driver.find_elements_by_xpath('//a[@class="flat-type-card js-flat-type-card active"]')
        assert len(aparts) == 8
        apart = opera_driver.find_element_by_xpath('//a[@href="/flat/13407/"]')
        apart.click()

    with allure.step('Бронируем квартиру'):
        button = opera_driver.find_element_by_xpath('//div[@class="flat-d-about__button button js-show-popup"]')
        button.click()
        check = opera_driver.find_element_by_xpath('//div[@class="form js-form-container active"]')
        assert check.is_displayed()

    with allure.step('делаем скриншот'):
        allure.attach(opera_driver.get_screenshot_as_png(), name='ScreenShot1', attachment_type=AttachmentType.PNG)


@allure.title('Проверка бронирования квартиры')
@allure.severity(Severity.CRITICAL)
def test_bronirovanie_firefox(firefox_driver: WebDriver):

    with allure.step('ищем страницу сайта'):
        firefox_driver.get('https://google.ru')
        search_input = firefox_driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
        search_button = firefox_driver.find_element_by_xpath('//div[@class="FPdoLc VlcLAe"]//input[@type="submit"]')
        search_input.send_keys('брусника екатеринбург')
        search_button.click()

    with allure.step('находим линк'):
        link = firefox_driver.find_element_by_xpath('//a[@href="https://ekaterinburg.brusnika.ru/"]')
        link.click()

    firefox_driver.switch_to.window(firefox_driver.window_handles[1])
    with allure.step('Проверяем корректность Title страницы'):
        assert firefox_driver.title == 'Квартиры в новостройках от застройщика Брусника Екатеринбург'

    with allure.step('Переходим во вкладку Проекты'):
        projects = firefox_driver.find_elements_by_xpath('//li[@class="header__menu-item"]')
        projects[1].click()
        project_select = firefox_driver.find_element_by_xpath('//img[@src="/media/complex/map_icon/'
                                                            'shg_active_3vcd0Ir_gCwpuHn.svg"]')
        project_select.click()

    with allure.step('Переходим к выбору квартиры'):
        choice_aparts = firefox_driver.find_element_by_xpath('//div[@class="mobile-container"]'
                                                           '//a[@href="/flat/?complex=5"]')
        choice_aparts.click()

    with allure.step('Ставим фильтр по стоимости и выбираем квартиру'):
        filter_price = firefox_driver.find_elements_by_xpath('//div[@class="noUi-handle noUi-handle-upper"]')
        move = ActionChains(firefox_driver)
        move.click_and_hold(filter_price[0]).move_by_offset(-168, 0).release().perform()
        allure.attach(firefox_driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)
        aparts = firefox_driver.find_elements_by_xpath('//a[@class="flat-type-card js-flat-type-card active"]')
        assert len(aparts) == 8
        apart = firefox_driver.find_element_by_xpath('//a[@href="/flat/13407/"]')
        apart.click()

    with allure.step('Бронируем квартиру'):
        button = firefox_driver.find_element_by_xpath('//div[@class="flat-d-about__button button js-show-popup"]')
        button.click()
        check = firefox_driver.find_element_by_xpath('//div[@class="form js-form-container active"]')
        assert check.is_displayed()

    with allure.step('делаем скриншот'):
        allure.attach(firefox_driver.get_screenshot_as_png(), name='ScreenShot1', attachment_type=AttachmentType.PNG)