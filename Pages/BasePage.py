from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException, \
    ElementClickInterceptedException
from Locators.MainPage_locators import MainPageLocators
import datetime


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
        try:
            finding_element = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}.")
            return finding_element
        except TimeoutException as err:
            print(f'There is no element by locator {locator}')
            raise err

    def click_on_element(self, locator, time=5):
        try:
            element = WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                          message=f"Can't find element by locator {locator}.")
            element.click()
        except ElementClickInterceptedException as err:
            print('The element not clickable')
            raise err

    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def removing_advertisement(self):
        close_adv_button = MainPageLocators.CLOSED_FIXED_BAN
        if close_adv_button:
            self.click_on_element(close_adv_button)
        else:
            print('There is no advertisement')

    def scroll_screen(self, parameters):
        # where necessary to set parameter by X-axis(1st value) and Y-axis(2nd value)
        self.browser.execute_script(f"window.scrollTo({parameters})")

    def browser_window_size(self, x, y):
        self.browser.set_window_size(x, y)

    def scrolling_for_one_screen(self):
        self.browser.execute_script("window.scrollTo(0, 1080)")

    def switching_to_the_second_browser_tab(self):
        # method for recognizing current window id
        # print(browser.current_window_handle)
        windows = self.browser.window_handles
        # Switching to second tab
        self.browser.switch_to.window(windows[1])

    def switching_to_the_first_browser_tab(self):
        # method for recognizing current window id
        # print(browser.current_window_handle)
        windows = self.browser.window_handles
        # Switching to second tab
        self.browser.switch_to.window(windows[0])

    def scaling_window(self, value_in_percent):
        self.browser.execute_script(f"document.body.style.transform = 'scale({value_in_percent})'")

    def is_element_present_on_the_page(self, locator, logs_elements_page):
        try:
            self.search_element(locator)
        except NoSuchElementException:
            logs_elements_page.error(f"There is no element on the page by the following locators{locator}")
        except TimeoutException:
            logs_elements_page.error(f"There is no element on the page by the following locators{locator}")
            return False
        return True

    def sending_keys_into_field(self, locator, content):
        field = self.search_element(locator)
        field.send_keys(content)

    def generating_text_to_list(self, output):
        generating_output = output.split('\n')
        return generating_output

    def making_screenshot(self):
        timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        self.browser.save_screenshot(f'/Volumes/Work/AQA_practice/Screenshots_error/{timestamp}.png')
