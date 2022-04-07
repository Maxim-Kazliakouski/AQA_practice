from selenium.webdriver.common.by import By
from Locators.ElementsPage_locators import ElementPageLocators
from Pages.BasePage import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException
from selenium.webdriver import ActionChains
from Tests.tests_ElementsPage.data_ElementsPage import TestDataElementsPage
import subprocess


class ElementsPage(BasePage):
    def switching_to_the_second_browser_tab(self):
        # method for recognizing current window id
        # print(browser.current_window_handle)
        windows = self.browser.window_handles
        # Switching to second tab
        self.browser.switch_to.window(windows[1])

    # def entering_symbols_into_field_fullname(self, symbols):
    #     user_name_field = self.search_element(ElementPageLocators.FULL_NAME_FIELD)
    #     user_name_field.send_keys(symbols)

    def generating_text_to_list(self, output):
        generating_output = output.split('\n')
        return generating_output

    def entering_symbols_into_field(self, field_locator, symbols):
        email_field = self.search_element(field_locator)
        email_field.send_keys(symbols)

    def clearing_symbols_from_field(self, field_locator):
        field = self.search_element(field_locator)
        field.clear()

    # def clearing_symbols_into_fullname_field(self):
    #     fullname_field = self.search_element(ElementPageLocators.FULL_NAME_FIELD)
    #     fullname_field.clear()

    def checking_is_red_field_appear(self, field):
        if field:
            field = True
        else:
            field = False
        return field

    def generating_checkbox_info(self, output):
        new_output = output[1:]
        return new_output

    def getting_info_about_selected_checkboxes(self):
        checkbox_list = self.search_element(ElementPageLocators.INFO_AFTER_ENABLE_CHECKBOX_HOME).text
        generating_checkbox_list = self.generating_text_to_list(checkbox_list)
        new_checkbox_list = self.generating_checkbox_info(generating_checkbox_list)
        return new_checkbox_list

    def click_on_checkbox(self, checkbox_name):
        checkbox = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{checkbox_name}')]")
        checkbox.click()

    def go_to_section(self, section_name):
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{section_name}')]")
        section.click()

    def click_on_radiobutton(self, radiobutton_name):
        radiobutton = self.browser.find_element(By.XPATH, f"//label[contains(text(),'{radiobutton_name}')]")
        radiobutton.click()

    def getting_text_after_choosing_radiobutton(self, radiobutton_name, logs_elements_page):
        try:
            radiobutton = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{radiobutton_name}')]")
            return radiobutton.text
        except NoSuchElementException as err:
            logs_elements_page.error('There is no such element like info from radiobutton')
            raise err

    def is_element_present_on_the_page(self, locator, logs_elements_page):
        try:
            self.search_element(locator)
        except NoSuchElementException:
            logs_elements_page.error(f"There is no element on the page by the following locators{locator}")
        except TimeoutException:
            logs_elements_page.error(f"There is no element on the page by the following locators{locator}")
            return False
        return True

    def deleting_records(self, record_number):
        delete_button = self.browser.find_element(By.ID, f"delete-record-{record_number}")
        delete_button.click()

    def splitting_list_by_6chunks(self, content, chunk=6):
        for i in range(0, len(content), chunk):
            yield content[i:i + chunk]
        return content

    def sending_keys_into_search_field(self, locator, content):
        search_field = self.search_element(locator)
        search_field.send_keys(content)

    def adding_new_record(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_first_name(self):
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_last_name(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_email(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_age(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_salary(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.DEPARTMENT_FIELD, TestDataElementsPage.DEPARTMENT)

    def adding_new_record_without_department(self):
        self.sending_keys_into_search_field(ElementPageLocators.FIRST_NAME_FIELD, TestDataElementsPage.FIRST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.LAST_NAME_FIELD, TestDataElementsPage.LAST_NAME)
        self.sending_keys_into_search_field(ElementPageLocators.EMAIL_FIELD, TestDataElementsPage.EMAIL)
        self.sending_keys_into_search_field(ElementPageLocators.AGE_FIELD, TestDataElementsPage.AGE)
        self.sending_keys_into_search_field(ElementPageLocators.SALARY_FIELD, TestDataElementsPage.SALARY)

    def double_clicking(self, locator):
        action = ActionChains(self.browser)
        element = self.browser.find_element(*locator)
        action.double_click(element).perform()

    def getting_info(self, locator):
        result = self.search_element(locator).text
        return result

    def right_click(self, locator):
        action = ActionChains(self.browser)
        element = self.browser.find_element(*locator)
        action.context_click(element).perform()

    # def getting_content_list_from_downloading_folder(self):
    #     with open('/Users/max_kazliakouski/Downloads/text.txt', 'w') as f:
    #         subprocess.run(['ls', '/Users/max_kazliakouski/Downloads'], stdout=f, text=True)
    #     with open('/Users/max_kazliakouski/Downloads/text.txt', 'r') as l:
    #         text = l.read()
    #     return text

    def getting_content_list_from_downloading_folder(self):
        with open('/var/jenkins_home/workspace/all_test_cases/Downloads/text.txt', 'w') as f:
            subprocess.run(['ls', '/var/jenkins_home/workspace/all_test_cases/Downloads'], stdout=f, text=True)
        with open('/var/jenkins_home/workspace/all_test_cases/Downloads/text.txt', 'r') as l:
            text = l.read()
        return text

    def getting_info_after_uploading_file(self, logs_elements_page):
        try:
            info = self.search_element(ElementPageLocators.INFO_MESSAGE_AFTER_UPLOADING_FILE).text
        except AssertionError as err:
            logs_elements_page.error('There is no any info about uploaded file')
            raise err
        return info
