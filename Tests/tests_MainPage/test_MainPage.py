from Locators.MainPage_locators import MainPageLocators
from Locators.ToolsQaMainPage import ToolsQaMainPage
from Pages.MainPage import MainPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage
from Tests.tests_ToolsQaMainPage.data_ToolsQaMainPage import TestDataToolsQaMainPage


class Test_MainPage:
    class Test_positive:
        def test_user_on_the_main_page(self, browser, logs_main_page):
            """This case checks, that user is on main page https://demoqa.com"""
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            main_page_url = page.getting_current_url()
            try:
                assert main_page_url == TestDataMainPage.MAIN_PAGE_URL, \
                    "The user isn't on the main page 'https://demoqa.com'"
            except AssertionError as err:
                logs_main_page.error("The user isn't on the main page 'https://demoqa.com'")
                raise err

        def test_redirection_to_the_main_page_after_clicking_on_logo(self, browser, logs_main_page):
            """This case checks, that after clicking on main page logo user redirects to the main page"""
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.ELEMENTS_PAGE_URL, \
                    "User isn't on the https://demoqa.com/elements page"
            except AssertionError as err:
                logs_main_page.error("User isn't on the https://demoqa.com/elements page")
                raise err
            page.click_on_element(MainPageLocators.MAIN_PAGE_LOGO)
            main_page_url = page.getting_current_url()
            try:
                assert main_page_url == TestDataMainPage.MAIN_PAGE_URL, \
                    "The user isn't on the main page 'https://demoqa.com'"
            except AssertionError as err:
                logs_main_page.error("The user isn't on the main page 'https://demoqa.com'")
                raise err

        def test_redirection_to_selenium_cert_training_page_by_clicking_on_banner(self, browser, logs_main_page):
            """This case checks that after clicking on banner SELENIUM user redirects to the certification page"""
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.SELENIUM_CERTIFICATION_BANNER)
            page.switching_to_the_second_browser_tab()
            page.search_element(ToolsQaMainPage.PAGEINFO)
            selenium_cert_training_url = page.getting_current_url()
            try:
                assert selenium_cert_training_url == TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL, \
                    "The user isn't on the main page 'https://www.toolsqa.com/selenium-training/'"
            except AssertionError as err:
                logs_main_page("The user isn't on the main page 'https://www.toolsqa.com/selenium-training/'")
                raise err

        def test_checking_sections(self, browser, logs_main_page):
            """This case checks that there are all sections on the main page"""
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            getting_sections = page.search_element(MainPageLocators.SECTIONS).text
            sections = getting_sections.split('\n')
            try:
                assert sections == TestDataMainPage.SECTIONS, \
                    'There is no one of the section...check the sections on the page'
            except AssertionError as err:
                logs_main_page('There is no one of the section...check the sections on the page')
                raise err

        def test_redirections_to_elements_page(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the elements page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ELEMENTS_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.ELEMENTS_PAGE_URL,\
                    "User isn't on the ELEMENTS PAGE https://demoqa.com/elements"
            except AssertionError as err:
                logs_main_page.error("User isn't on the ELEMENTS PAGE https://demoqa.com/elements")
                raise err

        def test_redirections_to_forms_page(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the forms page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.FORMS_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.FORMS_PAGE_URL,\
                    "User isn't on the FORMS PAGE https://demoqa.com/forms"
            except AssertionError as err:
                logs_main_page.error("User isn't on the FORMS PAGE https://demoqa.com/forms")
                raise err

        def test_redirections_to_alerts_frames_page(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the alerts, frames page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ALERTS_FRAMES_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.ALERTS_FRAMES_URL,\
                    "User isn't on the ALERTS, FRAMES PAGE https://demoqa.com/alertsWindows"
            except AssertionError as err:
                logs_main_page.error("User isn't on the ALERTS, FRAMES PAGE https://demoqa.com/alertsWindows")
                raise err

        def test_redirections_to_widgets_page(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the widgets page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.WIDGETS_URL,\
                    "User isn't on the WIDGETS PAGE https://demoqa.com/widgets"
            except AssertionError as err:
                logs_main_page.error("User isn't on the WIDGETS PAGE https://demoqa.com/widgets")
                raise err

        def test_redirections_to_interactions(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the interactions page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.INTERACTIONS_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.INTERACTIONS_URL,\
                    "User isn't on the INTERACTIONS PAGE https://demoqa.com/interaction"
            except AssertionError as err:
                logs_main_page.error("User isn't on the INTERACTIONS PAGE https://demoqa.com/interaction")
                raise err

        # @pytest.mark.webtest
        def test_redirections_to_book_store_page(self, browser, logs_main_page):
            """This case checks that user can be able to redirect to the book store page """
            link = TestDataMainPage.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.BOOK_STORE_APP_BUTTON)
            elements_page_url = page.getting_current_url()
            try:
                assert elements_page_url == TestDataMainPage.BOOK_STORE_APP_URL,\
                    "User isn't on the BOOK STORE PAGE https://demoqa.com/books"
            except AssertionError as err:
                logs_main_page.error("User isn't on the BOOK STORE PAGE https://demoqa.com/books")
                raise err
