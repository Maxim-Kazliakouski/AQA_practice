import time
from Locators.FormsPage_locators import FormsPageLocators
from Locators.WidgetsPage_locators import WidgetsLocators
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class WidgetsPage(BasePage):
    def go_to_section(self, section_name):
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{section_name}')]")
        section.click()

    def choosing_date_from_calendar(self, month, year):
        self.click_on_element(WidgetsLocators.SELECT_DATE)
        select_month = Select(self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        select_month.select_by_visible_text(month)
        select_year = Select(self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        select_year.select_by_visible_text(year)
        # select day not dynamic, because of it's hard to choose certain day
        self.click_on_element(WidgetsLocators.FIFTH_DAY_IN_CALENDAR)

    def choosing_date_and_time(self, number_of_month, year_for_choosing, time_in_schedule):
        self.click_on_element(WidgetsLocators.DATE_AND_TIME)
        time.sleep(1.5)
        self.click_on_element(WidgetsLocators.ARROW_BUTTON_FOR_MONTH)
        month = self.browser.find_element(By.XPATH, f"//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[{number_of_month}]")
        month.click()
        self.click_on_element(WidgetsLocators.ARROW_BUTTON_FOR_YEAR)
        year = None
        while year != str(year_for_choosing+1):
            year = self.search_element(WidgetsLocators.YEAR_1991).text
            self.click_on_element(WidgetsLocators.ARROW_BUTTON_FOR_YEAR2)
        self.click_on_element(WidgetsLocators.YEAR_1991)
        self.click_on_element(WidgetsLocators.FIFTH_DAY)
        time_in_calendar = self.browser.find_element(By.XPATH, f"//li[contains(text(),'{time_in_schedule}')]")
        time_in_calendar.click()







