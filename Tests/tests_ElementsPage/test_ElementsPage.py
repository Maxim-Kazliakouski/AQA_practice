import os
import time
import pytest
import requests
import subprocess
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException
from selenium.common.exceptions import TimeoutException
from Locators.ElementsPage_locators import ElementPageLocators
from Locators.MainPage_locators import MainPageLocators
from Pages.ElementsPage import ElementsPage
from Tests.tests_ElementsPage.data_ElementsPage import TestDataElementsPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage
from Tests.tests_MainPage.conftest import browser


@pytest.mark.ElementsPage
class Test_ElementsPage:
    @pytest.mark.TextBoxSection
    class Test_TextBox:
        class Test_positive:
            @pytest.mark.user_on_page
            def test_user_is_on_the_text_box_section(self, browser, logs_elements_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
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
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
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

            @pytest.mark.parametrize('emails', TestDataElementsPage.EMAIL_POSITIVE)
            def test_checking_email_field(self, browser, logs_elements_page, emails):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.EMAIL, emails)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                email = page.search_element(ElementPageLocators.OUTPUT_EMAIL).text
                page.generating_text_to_list(email)
                try:
                    assert email == f'Email:{emails}', \
                        "The entering username and outputting doesn't match"
                except AssertionError as err:
                    logs_elements_page.error("The entering username and outputting doesn't match")
                    raise err

            def test_checking_current_address_field(self, browser, logs_elements_page):
                link = TestDataMainPage.ELEMENTS_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
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
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
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
                page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
                page.entering_symbols_into_field(ElementPageLocators.EMAIL, TestDataElementsPage.EMAIL_NEGATIVE)
                page.scrolling_for_one_screen()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                red_email_field = page.search_element(ElementPageLocators.WRONG_RED_EMAIL_FIELD)
                red_field = page.checking_is_red_field_appear(red_email_field)
                try:
                    assert red_field, \
                        "The entering email was accepted by validation email field, but shouldn't be"
                except AssertionError as err:
                    logs_elements_page.error(
                        "The entering email was accepted by validation email field, but shouldn't be")
                    raise err

    @pytest.mark.CheckBoxSection
    class Test_CheckBox:
        class Test_positive:
            @pytest.mark.user_on_page
            def test_user_is_on_the_check_box_section(self, browser, logs_elements_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
                page.go_to_section(ElementPageLocators.CHECK_BOX_SECTION)
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
                    assert enable_checkbox == TestDataElementsPage.ENABLE_CHECKBOX_HOME, \
                        "The checkbox 'HOME' still unchecked"
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
                    assert chosen_checkboxes == TestDataElementsPage.CHECKBOX_LIST_WITHOUT_WORKSPACE_CHECKBOX, \
                        "The checkbox list doesn't match with test data, please compare the checkbox list on the " \
                        "webpage and in test data "
                except AssertionError as err:
                    logs_elements_page.error(
                        "The checkbox list doesn't match with test data, please compare the checkbox list on the "
                        "webpage and in test data ")
                    raise err

    @pytest.mark.RadioButtonSection
    class Test_RadioButton:
        @pytest.mark.user_on_page
        def test_user_on_the_radiobutton_page(self, browser, logs_elements_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            page.go_to_section(ElementPageLocators.RADIO_BUTTON_SECTION)
            radio_button_url = page.getting_current_url()
            try:
                assert radio_button_url == TestDataElementsPage.RADIO_BUTTON_URL, \
                    "User isn't on the radio button page https://demoqa.com/radio-button"
            except AssertionError as err:
                logs_elements_page.error("User isn't on the radio button page https://demoqa.com/radio-button")
                raise err

        def test_getting_info_after_checking_radiobutton(self, browser, logs_elements_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            page.go_to_section(ElementPageLocators.RADIO_BUTTON_SECTION)
            page.click_on_radiobutton(ElementPageLocators.RB_YES)
            text_result = page.getting_text_after_choosing_radiobutton(ElementPageLocators.RB_YES, logs_elements_page)
            try:
                assert text_result == ElementPageLocators.RB_YES, \
                    f"The radio button {ElementPageLocators.RB_YES} hasn't been chosen"
            except AssertionError as err:
                logs_elements_page.error(f"The radio button {ElementPageLocators.RB_YES} hasn't been chosen")
                raise err

    @pytest.mark.WebTablesSection
    class Test_WebTablesSection:
        class Test_positive:
            @pytest.mark.user_on_page
            def test_user_on_the_radiobutton_page(self, browser, logs_elements_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
                page.scrolling_for_one_screen()
                page.go_to_section(ElementPageLocators.WEB_TABLES_SECTION)
                web_tables_url = page.getting_current_url()
                try:
                    assert web_tables_url == TestDataElementsPage.WEB_TABLES_URL, \
                        "User isn't on the web tables page https://demoqa.com/webtables"
                except AssertionError as err:
                    logs_elements_page.error("User isn't on the web tables page https://demoqa.com/webtables")
                    raise err

            def test_registration_form_appears(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.EDIT_BUTTON)
                element_on_page = page.is_element_present_on_the_page(ElementPageLocators.REGISTRATION_FORM,
                                                                      logs_elements_page)
                try:
                    assert element_on_page, "The registration form isn't appeared"
                except AssertionError as err:
                    logs_elements_page.error("The registration form isn't appeared")
                    raise err

            def test_deleting_records(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.deleting_records(2)
                department = page.is_element_present_on_the_page(ElementPageLocators.COMPLIANCE_DEPARTMENT,
                                                                 logs_elements_page)
                try:
                    assert department == False, "The 'COMPLIANCE' department still on the page"
                except AssertionError as err:
                    logs_elements_page.error("The 'COMPLIANCE' department still on the page")
                    raise err

            def test_adding_button(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                reg_form = page.is_element_present_on_the_page(ElementPageLocators.REGISTRATION_FORM,
                                                               logs_elements_page)
                try:
                    assert reg_form, "The Registration form doesn't appear, 'ADD' button doesn't work"
                except AssertionError as err:
                    logs_elements_page.error("The Registration form doesn't appear, 'ADD' button doesn't work")
                    raise err

            def test_searching(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.sending_keys_into_search_field(ElementPageLocators.SEARCH_FIELD, 'Kierra')
                content = page.search_element(ElementPageLocators.TABLE_CONTENT).text
                gen_content_to_list = page.generating_text_to_list(content)
                table_content = list(page.splitting_list_by_6chunks(gen_content_to_list))
                final_table_content = table_content[:-1]
                amount_of_records = len(final_table_content)
                try:
                    assert amount_of_records == 1, "There is should be 1 record with Name=Kierra"
                except AssertionError as err:
                    logs_elements_page.error("There is should be 1 record with Name=Kierra")
                    raise err
                try:
                    assert final_table_content[0][0] == 'Kierra', "There in no such incoming after searching"
                except AssertionError as err:
                    logs_elements_page.error(f"There in no such incoming '{final_table_content[0][0]}' after searching")
                    raise err

            def test_adding_new_record(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                content = page.search_element(ElementPageLocators.TABLE_CONTENT).text
                gen_content_to_list = page.generating_text_to_list(content)
                table_content = list(page.splitting_list_by_6chunks(gen_content_to_list))
                final_table_content = table_content[:-1]
                amount_of_records = len(final_table_content)
                try:
                    assert amount_of_records == 4, "The record wasn't added"
                except AssertionError as err:
                    logs_elements_page.error("The record wasn't added")
                    raise err
                try:
                    assert final_table_content[3][0] == TestDataElementsPage.FIRST_NAME, "The record wasn't added"
                except AssertionError as err:
                    logs_elements_page.error(
                        f"The added name '{final_table_content[3][0]}' doesn't match with test data name"
                        f" '{TestDataElementsPage.FIRST_NAME}'")
                    raise err

        class Test_negative:
            def test_adding_new_record_without_first_name(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_first_name()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without first name, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without first name, it's wrong")
                    raise err

            def test_adding_new_record_without_last_name(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_last_name()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without last name, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without last name, it's wrong")
                    raise err

            def test_adding_new_record_without_email(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_email()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without email, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without email, it's wrong")
                    raise err

            def test_adding_new_record_without_age(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_age()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without age, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without age, it's wrong")
                    raise err

            def test_adding_new_record_without_salary(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_salary()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without salary, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without salary, it's wrong")
                    raise err

            def test_adding_new_record_without_department(self, browser, logs_elements_page):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_department()
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, "The user has been created without department, it's wrong"
                except AssertionError as err:
                    logs_elements_page.error("The user has been created without department, it's wrong")
                    raise err

            @pytest.mark.parametrize('emails', TestDataElementsPage.EMAIL_NEGATIVE)
            def test_emails_field(self, browser, logs_elements_page, emails):
                link = TestDataElementsPage.WEB_TABLES_URL
                page = ElementsPage(browser, link)
                page.open_page(link)
                # adding function for blocking advertisement if it is
                page.removing_advertisement()
                page.click_on_element(ElementPageLocators.ADD_BUTTON)
                page.adding_new_record_without_email()
                page.sending_keys_into_search_field(ElementPageLocators.EMAIL, emails)
                page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)
                ui_validation = page.is_element_present_on_the_page(ElementPageLocators.FIELD_VALIDATION,
                                                                    logs_elements_page)
                try:
                    assert ui_validation, f"The user has been created with incorrect email -> {emails}"
                except AssertionError as err:
                    logs_elements_page.error(f"The user has been created with incorrect email -> {emails}")
                    raise err

    @pytest.mark.ButtonsSection
    class Test_ButtonsSection:
        @pytest.mark.user_on_page
        def test_user_on_the_buttons_page(self, browser, logs_elements_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            page.scrolling_for_one_screen()
            page.go_to_section(ElementPageLocators.BUTTONS_SECTION)
            buttons_url = page.getting_current_url()
            try:
                assert buttons_url == TestDataElementsPage.BUTTONS_URL, \
                    "User isn't on the buttons page https://demoqa.com/buttons"
            except AssertionError as err:
                logs_elements_page.error("User isn't on the buttons page https://demoqa.com/buttons")
                raise err

        def test_getting_info_after_double_click_button(self, browser, logs_elements_page):
            link = TestDataElementsPage.BUTTONS_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.double_clicking(ElementPageLocators.DOUBLE_CLICK_ME_BUTTON)
            message = page.getting_info(ElementPageLocators.INFO_AFTER_DOUBLE_CLICKING)
            try:
                assert message == TestDataElementsPage.MESSAGE_AFTER_DOUBLE_CLICKING, \
                    "There is no information message(or incorrect message) after double clicking"
            except AssertionError as err:
                logs_elements_page.error("There is no information message(or incorrect message) after double clicking")
                raise err

        def test_getting_info_after_right_click_button(self, browser, logs_elements_page):
            link = TestDataElementsPage.BUTTONS_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.right_click(ElementPageLocators.RIGHT_CLICK_BUTTON)
            message = page.getting_info(ElementPageLocators.INFO_AFTER_RIGHT_CLICKING)
            try:
                assert message == TestDataElementsPage.MESSAGE_AFTER_RIGHT_CLICKING, \
                    "There is no information message(or incorrect message) after clicking on right click button"
            except AssertionError as err:
                logs_elements_page.error("There is no information message(or incorrect message)"
                                         " after clicking on right click button")
                raise err

        def test_getting_info_after_click_button(self, browser, logs_elements_page):
            link = TestDataElementsPage.BUTTONS_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(ElementPageLocators.CLICK_BUTTON)
            message = page.getting_info(ElementPageLocators.INFO_AFTER_CLICKING_BUTTON)
            time.sleep(5)
            try:
                assert message == TestDataElementsPage.MESSAGE_AFTER_CLICK_BUTTON, \
                    "There is no information message(or incorrect message) after clicking on button"
            except AssertionError as err:
                logs_elements_page.error("There is no information message(or incorrect message)"
                                         " after clicking on button")
                raise err

    @pytest.mark.LinksSection
    class Test_LinksSection:
        @pytest.mark.user_on_page
        def test_user_on_the_links_page(self, browser, logs_elements_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            page.scrolling_for_one_screen()
            page.go_to_section(ElementPageLocators.LINKS_SECTION)
            links_url = page.getting_current_url()
            try:
                assert links_url == TestDataElementsPage.LINKS_URL, \
                    "User isn't on the links page https://demoqa.com/links"
            except AssertionError as err:
                logs_elements_page.error("User isn't on the links page https://demoqa.com/links")
                raise err

        # for beautifully displaying test data in console
        link_ids = [f'{t}' for t in TestDataElementsPage.HOME_LINKS_NAMES]

        @pytest.mark.parametrize('links', ElementPageLocators.HOME_LINKS_NAMES, ids=link_ids)
        def test_open_links_in_new_tabs(self, browser, logs_elements_page, links):
            link = TestDataElementsPage.LINKS_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.browser.refresh()
            page.click_on_element(links)
            page.switching_to_the_second_browser_tab()
            current_url = page.getting_current_url()
            page.browser.close()
            page.switching_to_the_first_browser_tab()
            try:
                assert current_url == TestDataElementsPage.MAIN_URL, \
                    "The url in second tab doesn't match with https://demoqa.com/"
            except AssertionError as err:
                raise err

        @pytest.mark.parametrize('requests_api, response_api', TestDataElementsPage.REQUESTS)
        def test_api_created_request(self, browser, logs_elements_page, requests_api, response_api):
            response = requests.get(requests_api)
            status_code = response.status_code
            try:
                assert status_code == response_api, \
                    f"The item hasn't been created, status code {status_code}"
            except AssertionError as err:
                logs_elements_page.error(f"The item hasn't been created, status code {status_code}")
                raise err

        req_ids = [f'{t}' for t in TestDataElementsPage.REQUESTS_FOR_GETTING_INFO_IDS]

        @pytest.mark.webtest
        @pytest.mark.parametrize('locator, status_code, status_text', TestDataElementsPage.REQUESTS_FOR_GETTING_INFO,
                                 ids=req_ids)
        def test_getting_message_after_api_request(self, browser, logs_elements_page, locator, status_code,
                                                   status_text):
            link = TestDataElementsPage.LINKS_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.scrolling_for_one_screen()
            page.click_on_element(locator)
            info = page.getting_info(ElementPageLocators.INFO_MESSAGE)
            try:
                assert info == f"Link has responded with staus {status_code} and status text {status_text}", \
                    f"There is no info after clicking on link, user gets {status_code} {status_text}"
            except AssertionError as err:
                logs_elements_page.error(
                    f"There is no info after clicking on link, user gets {status_code} {status_text}")
                raise err

    @pytest.mark.UploadDownloadSection
    class TestUploadDownload:
        @pytest.mark.user_on_page
        def test_user_on_the_uploaddownload_page(self, browser, logs_elements_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            page.scrolling_for_one_screen()
            page.go_to_section(ElementPageLocators.UPLOAD_SECTION)
            upload_url = page.getting_current_url()
            try:
                assert upload_url == TestDataElementsPage.UPLOAD_URL, \
                    "User isn't on the upload page https://demoqa.com/upload-download"
            except AssertionError as err:
                logs_elements_page.error("User isn't on the upload page https://demoqa.com/upload-download")
                raise err

        def test_downloading_file(self, browser, logs_elements_page, removing_file_after_downloading):
            link = TestDataElementsPage.UPLOAD_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(ElementPageLocators.DOWNLOAD_BUTTON)
            # necessary time for downloading file from the site
            time.sleep(4)
            content = page.getting_content_list_from_downloading_folder()
            downloads_folder_content = page.generating_text_to_list(content)
            try:
                assert TestDataElementsPage.DOWNLOAD_FILE_NAME in downloads_folder_content,\
                    f"There is no '{TestDataElementsPage.DOWNLOAD_FILE_NAME}" \
                    f" in download folder' file hasn't been download"
            except AssertionError as err:
                logs_elements_page.error(
                    f"There is no '{TestDataElementsPage.DOWNLOAD_FILE_NAME}'"
                    f" in download folder' file hasn't been download")
                raise err

        def test_uploading_file(self, browser, logs_elements_page):
            link = TestDataElementsPage.UPLOAD_URL
            page = ElementsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            upload_button = page.search_element(ElementPageLocators.UPLOAD_BUTTON)
            upload_button.send_keys('/Volumes/Work/AQA_practice/eng.srt')
            info = page.getting_info_after_uploading_file(logs_elements_page)
            try:
                assert info == TestDataElementsPage.UPLOAD_PATH,\
                    "There is no any info after uploading file"
            except AssertionError as err:
                logs_elements_page.error("There is no any info after uploading file")
                raise err
