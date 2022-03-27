from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AlertsFrameWindows(BasePage):
    def go_to_section(self, section_name):
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{section_name}')]")
        section.click()

    def switch_to_alert_window(self):
        alert = self.browser.switch_to.alert
        return alert

    def getting_info_from_alert(self):
        alert_text = self.switch_to_alert_window().text
        return alert_text

    def input_text_into_alert(self, text_for_alert):
        alert = self.switch_to_alert_window()
        alert.send_keys(text_for_alert)
        alert.accept()

    def switch_to_iframe(self, locator):
        self.browser.switch_to.frame(self.search_element(locator))
