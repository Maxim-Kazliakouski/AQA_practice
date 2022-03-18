import time
import pytest
from selenium.common.exceptions import TimeoutException
from Locators.ElementsPage_locators import ElementPageLocators
from Locators.MainPage_locators import MainPageLocators
from Pages.ElementsPage import ElementsPage
from Pages.MainPage import MainPage
from Tests.tests_ElementsPage.data_ElementsPage import TestDataElementsPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage


class Test_ElementsPage:
    @pytest.mark.TextBoxSection
    class Test_TextBox:
        class Test_positive:
            def test_user_is_on_the_text_box_section(self, browser, logs_elements_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = MainPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                text_box_section_url = page.getting_current_url()
                try:
                    assert text_box_section_url == TestDataElementsPage.TEXT_BOX_URL, "User isn't on text book section..."
                except AssertionError as err:
                    logs_elements_page.error("User isn't on text book section...")
                    raise err

            @pytest.mark.parametrize('full_names', TestDataElementsPage.FULL_NAME)
            def test_checking_full_name_field(self, browser, logs_elements_page, full_names):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.FULL_NAME_FIELD, full_names)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                full_name = page.search_element(ElementPageLocators.OUTPUT_NAME).text
                page.generating_text_to_list(full_name)
                try:
                    assert full_name == f'Name:{full_names}', "The entering username and outputting doesn't match"
                except AssertionError as err:
                    logs_elements_page.error("The entering username and outputting doesn't match")
                    raise err

            def test_checking_email_field(self, browser, logs_elements_page):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.EMAIL, TestDataElementsPage.EMAIL_POSITIVE)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                email = page.search_element(ElementPageLocators.OUTPUT_EMAIL).text
                page.generating_text_to_list(email)
                try:
                    assert email == f'Email:{TestDataElementsPage.EMAIL_POSITIVE}', "The entering username and outputting doesn't match"
                except AssertionError as err:
                    logs_elements_page.error("The entering username and outputting doesn't match")
                    raise err

            def test_checking_current_address_field(self, browser, logs_elements_page):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.CURRENT_ADDRESS,
                                                 TestDataElementsPage.CURRENT_ADDRESS)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                current_address = page.search_element(ElementPageLocators.OUTPUT_CURRENT_ADDRESS).text
                try:
                    assert current_address == f'Current Address :{TestDataElementsPage.CURRENT_ADDRESS}', \
                        "The entering current address and outputting doesn't match"
                except AssertionError as err:
                    logs_elements_page.error("The entering current address and outputting doesn't match")
                    raise err

            def test_checking_permanent_address_field(self, browser, logs_elements_page):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.PERMANENT_ADDRESS,
                                                 TestDataElementsPage.PERMANENT_ADDRESS)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                current_address = page.search_element(ElementPageLocators.OUTPUT_PERMANENT_ADDRESS).text
                try:
                    assert current_address == f'Permananet Address :{TestDataElementsPage.PERMANENT_ADDRESS}', \
                        "The entering current address and outputting doesn't match"
                except AssertionError as err:
                    logs_elements_page.error("The entering current address and outputting doesn't match")
                    raise err

            def test_checking_disappearing_output_fullname_after_clearing_email_field(self, browser, logs_elements_page,
                                                                                      adding_fullname):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.clearing_symbols_from_field(ElementPageLocators.FULL_NAME_FIELD)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                try:
                    page.search_element(ElementPageLocators.OUTPUT_NAME)
                    logs_elements_page.error('The output fullname still displaying')
                    email = True
                except TimeoutException:
                    email = False
                assert email == False, 'The output fullname still displaying'

            def test_checking_disappearing_output_email_after_clearing_email_field(self, browser, logs_elements_page,
                                                                                   adding_email):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.clearing_symbols_from_field(ElementPageLocators.EMAIL)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                try:
                    page.search_element(ElementPageLocators.OUTPUT_EMAIL)
                    logs_elements_page.error('The output email still displaying')
                    email = True
                except TimeoutException:
                    email = False
                assert email == False, 'The output email still displaying'

            def test_checking_disappearing_output_current_address_after_clearing_field(self, browser,
                                                                                       logs_elements_page,
                                                                                       adding_current_address):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.clearing_symbols_from_field(ElementPageLocators.CURRENT_ADDRESS)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                try:
                    page.search_element(ElementPageLocators.OUTPUT_CURRENT_ADDRESS)
                    logs_elements_page.error('The output current address still displaying')
                    address = True
                except TimeoutException:
                    address = False
                assert address == False, 'The output current address still displaying'

            def test_checking_disappearing_output_permanent_address_after_clearing_field(self, browser,
                                                                                         logs_elements_page,
                                                                                         adding_permanent_address):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.clearing_symbols_from_field(ElementPageLocators.PERMANENT_ADDRESS)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                try:
                    page.search_element(ElementPageLocators.OUTPUT_PERMANENT_ADDRESS)
                    logs_elements_page.error('The output permanent address still displaying')
                    address = True
                except TimeoutException:
                    address = False
                assert address == False, 'The output permanent address still displaying'

        class Test_negative:
            @pytest.mark.parametrize('wrong_emails', TestDataElementsPage.EMAIL_NEGATIVE)
            def test_checking_email_field(self, browser, logs_elements_page, wrong_emails):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.EMAIL, TestDataElementsPage.EMAIL_NEGATIVE)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                red_email_field = page.search_element(ElementPageLocators.WRONG_RED_EMAIL_FIELD)
                red_field = page.checking_is_red_field_appear(red_email_field)
                try:
                    assert red_field == True, \
                        "The entering email was accepted by validation email field, but shouldn't be"
                except AssertionError as err:
                    logs_elements_page.error(
                        "The entering email was accepted by validation email field, but shouldn't be")
                    raise err

    @pytest.mark.CheckBoxSection
    class Test_CheckBox:
        class Test_positive:
            def test_user_is_on_the_check_box_section(self, browser, logs_elements_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = MainPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
                page.click_on_element(ElementPageLocators.CHECK_BOX_SECTION)
                check_box_section_url = page.getting_current_url()
                try:
                    assert check_box_section_url == TestDataElementsPage.CHECK_BOX_URL, \
                        "User isn't on check box section..."
                except AssertionError as err:
                    logs_elements_page.error("User isn't on check box section...")
                    raise err

            def test_clicking_on_checkbox_home(self, browser, logs_elements_page):
                link = TestDataElementsPage.CHECK_BOX_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.HOME_CHECK_BOX)
                check_box = page.search_element(ElementPageLocators.HOME_CHECK_ENABLE_DISABLE)
                enable_checkbox = check_box.get_attribute('class')
                try:
                    assert enable_checkbox == TestDataElementsPage.ENABLE_CHECKBOX_HOME, "The checkbox 'HOME' still unchecked"
                except AssertionError as err:
                    logs_elements_page.error("The checkbox 'HOME' still unchecked")
                    raise err

            def test_appearing_additional_info_after_checking_inbox(self, browser, logs_elements_page,
                                                                    enable_checkbox_home):
                link = TestDataElementsPage.CHECK_BOX_URL
                page = ElementsPage(browser, link)
                new_checkbox_list = page.getting_info_about_selected_checkboxes()
                try:
                    assert new_checkbox_list == TestDataElementsPage.CHECKBOX_LIST, \
                        "The checkbox lists doesn't match with testdata, check test data and data on the website"
                except AssertionError as err:
                    logs_elements_page.error(
                        "The checkbox lists doesn't match with testdata, check test data and data on the website")
                    raise err

            def test_plus_button(self, browser, logs_elements_page, enable_checkbox_home):
                link = TestDataElementsPage.CHECK_BOX_URL
                page = ElementsPage(browser, link)
                page.click_on_element(ElementPageLocators.PLUS_BUTTON)
                status_plus_button = page.getting_attribute_from_element(ElementPageLocators.PLUS_BUTTON_ON_OFF,
                                                                         'class')
                print(status_plus_button)
                try:
                    assert status_plus_button == TestDataElementsPage.ENABLE_PLUS_BUTTON, \
                        "The plus button doesn't expand the all checkboxes list"
                except AssertionError as err:
                    logs_elements_page.error("The plus button doesn't expand the all checkboxes list")
                    raise err

            @pytest.mark.webtest
            def test_minus_button(self, browser, logs_elements_page):
                link = TestDataElementsPage.CHECK_BOX_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.PLUS_BUTTON)
                page.click_on_element(ElementPageLocators.MINUS_BUTTON)
                status_minus_button = page.getting_attribute_from_element(ElementPageLocators.PLUS_BUTTON_ON_OFF,
                                                                          'class')
                try:
                    assert status_minus_button == TestDataElementsPage.ENABLE_MINUS_BUTTON, \
                        "The minus button doesn't work and checkboxes list still appears"
                except AssertionError as err:
                    logs_elements_page.error("The minus button doesn't work and checkboxes list still appears")
                    raise err

            def test_partly_chosen_checkboxes(self, browser, logs_elements_page, enable_checkbox_home):
                link = TestDataElementsPage.CHECK_BOX_URL
                page = ElementsPage(browser, link)
                page.click_on_element(ElementPageLocators.PLUS_BUTTON)
                page.click_on_checkbox('WorkSpace')
                chosen_checkboxes = page.getting_info_about_selected_checkboxes()
                try:
                    assert chosen_checkboxes == TestDataElementsPage.CHECKBOX_LIST_WITHOUT_WORKSPACE_CHECKBOX,\
                    "The checkbox list doesn't match with test data, please compare the checkbox list on the webpage and in test data "
                except AssertionError as err:
                    logs_elements_page.error("The checkbox list doesn't match with test data, please compare the checkbox list on the webpage and in test data ")
                    raise err

