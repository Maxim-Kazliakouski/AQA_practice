from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.MainPage_locators import MainPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.link = url

    def open_page(self, url):
        self.browser.get(url)

    def getting_attribute_from_element(self, locator, attribute):
        element = self.search_element(locator)
        output = element.get_attribute(attribute)
        return output

    def search_element(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}.")

    def click_on_element(self, locator, time=5):
        element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}.")
        element.click()

    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def removing_advertisement(self):
        close_adv_button = MainPageLocators.CLOSED_FIXED_BAN
        if close_adv_button:
            self.click_on_element(close_adv_button)
        else:
            print('There is no advertisement')

    def scrolling_for_one_screen(self):
        self.browser.execute_script("window.scrollTo(0, 1080)")
