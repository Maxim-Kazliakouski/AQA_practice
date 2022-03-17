from Locators.MainPage_locators import MainPageLocators
from Pages.BasePage import BasePage


class MainPage(BasePage):
    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def removing_advertisement(self):
        close_adv_button = MainPageLocators.CLOSED_FIXED_BAN
        if close_adv_button:
            self.click_on_element(close_adv_button)
        else:
            print('There is no advertisement')

    def switching_to_the_second_browser_tab(self):
        # method for recognizing current window id
        # print(browser.current_window_handle)
        windows = self.browser.window_handles
        # Switching to second tab
        self.browser.switch_to.window(windows[1])
