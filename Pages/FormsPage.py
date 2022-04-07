from Locators.FormsPage_locators import FormsPageLocators
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Tests.tests_FormsPage.data_FormsPage import TestDataFormsPage


class FormsPage(BasePage):
    def go_to_section(self, section_name):
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{section_name}')]")
        section.click()

    def sending_keys_into_field(self, locator, content):
        field = self.search_element(locator)
        field.send_keys(content)

    def choosing_radio_button(self, radiobutton_name):
        radiobutton = self.browser.find_element(By.XPATH, f"//label[contains(text(),'{radiobutton_name}')]")
        radiobutton.click()

    def choosing_date_from_calendar(self, month, year):
        self.click_on_element(FormsPageLocators.CALENDAR)
        select_month = Select(self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        select_month.select_by_visible_text(month)
        select_year = Select(self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        select_year.select_by_visible_text(year)
        # select day not dynamic, because of it's hard to choose certain day
        self.click_on_element(FormsPageLocators.FIVEth_SEPTEMBER)

    def choosing_checkbox(self, checkbox_name):
        checkbox = self.browser.find_element(By.XPATH, f"//label[contains(text(),'{checkbox_name}')]")
        checkbox.click()

    def select_state(self, state_name):
        state_list = self.browser.find_element(By.XPATH, "//div[contains(text(),'Select State')]")
        state_list.click()
        state = self.browser.find_element(By.XPATH, f"//div[contains(text(),'{state_name}')]")
        state.click()

    def select_city(self, city_name):
        city_list = self.browser.find_element(By.XPATH, "//div[contains(text(),'Select City')]")
        city_list.click()
        city = self.browser.find_element(By.XPATH, f"//div[contains(text(),'{city_name}')]")
        city.click()

    def uploading_file(self):
        upload_button = self.search_element(FormsPageLocators.UPLOAD_BUTTON)
        upload_button.send_keys('/var/jenkins_home/workspace/all_test_cases/eng.srt')
        upload_button.send_keys('/Volumes/Work/AQA_practice/eng.srt')

    def filling_form(self):
        self.browser.execute_script("document.body.style.transform = 'scale(0.55)'")
        self.sending_keys_into_field(FormsPageLocators.FIRST_NAME, TestDataFormsPage.FIRST_NAME)
        self.sending_keys_into_field(FormsPageLocators.LAST_NAME, TestDataFormsPage.LAST_NAME)
        self.sending_keys_into_field(FormsPageLocators.EMAIL, TestDataFormsPage.EMAIL)
        self.choosing_radio_button('Female')
        self.sending_keys_into_field(FormsPageLocators.MOBILE_NUMBER, "12345678910")
        self.choosing_date_from_calendar('September', '1991')
        # self.choosing_checkbox('Sports')
        # self.choosing_checkbox('Music')
        self.uploading_file()
        self.sending_keys_into_field(FormsPageLocators.CURRENT_ADDRESS, "Minsk, Pobediteley avenue 100")
        self.select_state('NCR')
        self.select_city('Gurgaon')
        self.click_on_element(FormsPageLocators.SUBMIT_BUTTON)









