import time

import pytest
from Locators.FormsPage_locators import FormsPageLocators
from Locators.MainPage_locators import MainPageLocators
from Pages.FormsPage import FormsPage
from Tests.tests_FormsPage.data_FormsPage import TestDataFormsPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage
from selenium.webdriver.common.by import By
from Tests.tests_MainPage.conftest import browser


class Test_FormsPage:
    @pytest.mark.FormsSection
    class Test_Forms:
        class Test_positive:
            @pytest.mark.user_on_page
            def test_user_on_the_forms_page(self, browser, logs_forms_page):
                link = TestDataMainPage.MAIN_PAGE_URL
                page = FormsPage(browser, link)
                page.open_page(link)
                page.removing_advertisement()
                page.click_on_element(MainPageLocators.FORMS_BUTTON)
                page.go_to_section(FormsPageLocators.PRACTICE_FORMS)
                forms_page_url = page.getting_current_url()
                try:
                    assert forms_page_url == TestDataFormsPage.FORMS_PAGE_URL,\
                        "User isn't on Forms Page"
                except AssertionError as err:
                    page.making_screenshot()
                    logs_forms_page.error("User isn't on Forms Page")
                    raise err

            def test_filling_form(self, browser, logs_forms_page):
                link = TestDataFormsPage.FORMS_PAGE_URL
                page = FormsPage(browser, link)
                page.open_page(link)
                page.removing_advertisement()
                page.filling_form()
                modal_window = page.search_element(FormsPageLocators.MODAL_WINDOW)
                try:
                    assert modal_window, "There is no modal window after clicking on submit button"
                except AssertionError as err:
                    page.making_screenshot()
                    logs_forms_page.error("There is no modal window after clicking on submit button")
                    raise err
