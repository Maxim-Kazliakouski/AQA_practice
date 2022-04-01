import time
import pytest
from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators
from Pages.ToolsQaMainPage import ToolsQaMainPage
from Tests.tests_ToolsQaMainPage.data_ToolsQaMainPage import TestDataToolsQaMainPage
from selenium.webdriver.common.action_chains import ActionChains
from Tests.tests_MainPage.conftest import browser


@pytest.mark.ToolsQaMainPage
class TestToolsQaMainPage:
    @pytest.mark.ToolsQaMainElements
    class Test_main_elements:
        def test_user_on_the_main_page(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            image_on_main_page = page.is_element_present_on_the_page(ToolsQaMainPageLocators.IMAGE_ON_MAIN_PAGE,
                                                                     logs_tool_qa_main_page)
            try:
                assert image_on_main_page, f"User isn't on the Tools Qa Main page {TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL}"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"User isn't on the Tools Qa Main page {TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL}")
                raise err

        def test_redirection_to_selenium_tab(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.SELENIUM_TRAINING_TAB)
            selenium_tab_url = page.getting_current_url()
            try:
                assert selenium_tab_url == TestDataToolsQaMainPage.SELENIUM_TRAINING_TAB_URL, \
                    f"User isn't on Selenium Training Tab '{TestDataToolsQaMainPage.SELENIUM_TRAINING_TAB_URL}', he is on {selenium_tab_url}"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"User isn't on Selenium Training Tab '{TestDataToolsQaMainPage.SELENIUM_TRAINING_TAB_URL}', he is on {selenium_tab_url}")
                raise err

        def test_redirection_to_demo_site_tab(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.DEMO_SITE)
            page.switching_to_the_second_browser_tab()
            demo_site_tab_url = page.getting_current_url()
            try:
                assert demo_site_tab_url == TestDataToolsQaMainPage.DEMO_SITE_URL, \
                    f"User isn't on Selenium Training Tab '{TestDataToolsQaMainPage.DEMO_SITE_URL}', he is on {demo_site_tab_url}"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"User isn't on Selenium Training Tab '{TestDataToolsQaMainPage.DEMO_SITE_URL}',he is on {demo_site_tab_url}")
                raise err

        def test_checking_tab(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.browser_window_size(1920, 1080)
            tabs = page.search_element(ToolsQaMainPageLocators.LIST_TAB).text
            tabs_list = page.generating_text_to_list(tabs)
            try:
                assert tabs_list == TestDataToolsQaMainPage.TABS_LIST, \
                    "The current tab list is {}, but the test list is {}".format(tabs_list,
                                                                                 TestDataToolsQaMainPage.TABS_LIST)
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error("The current tab list is {}, but the test list is {}".format(tabs_list,
                                                                                                          TestDataToolsQaMainPage.TABS_LIST))
                raise err

        def test_redirection_to_main_page_after_clicking_on_logo(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.SELENIUM_TRAINING_TAB)
            page.click_on_element(ToolsQaMainPageLocators.LOGO)
            main_page_url = page.getting_current_url()
            try:
                assert main_page_url == TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL, \
                    f"User isn't on main page '{TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL}'," \
                    f"he on the '{main_page_url}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"User isn't on main page '{TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL}',"
                    f"he on the '{main_page_url}'")
                raise err

        def test_opening_tutorial_menu(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_BUTTON)
            menu = page.is_element_present_on_the_page(ToolsQaMainPageLocators.TUTORIAL_MENU_OPEN,
                                                       logs_tool_qa_main_page)
            try:
                assert menu, "The TUTORIAL menu doesn't open"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error("The TUTORIAL menu doesn't open")
                raise err

        def test_closing_tutorial_menu(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_BUTTON)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_MENU_CLOSE)
            menu = page.is_element_present_on_the_page(ToolsQaMainPageLocators.TUTORIAL_MENU_OPEN,
                                                       logs_tool_qa_main_page)
            try:
                assert menu == False, "The TUTORIAL menu still open"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error("The TUTORIAL menu still open")
                raise err

    @pytest.mark.Tutorials
    class Test_tutorials:
        def test_checking_section_in_tutorial_menu(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_BUTTON)
            tutorial_list = page.search_element(ToolsQaMainPageLocators.TUTORIAL_MENU_CONTENT).text
            new_list = page.generating_text_to_list(tutorial_list)
            try:
                assert new_list == TestDataToolsQaMainPage.TUTORIAL_MENU_LIST, \
                    f"There was getting following list {new_list}," \
                    f"and it doesn't match with test list {TestDataToolsQaMainPage.TUTORIAL_MENU_LIST}"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"There was getting following list {new_list},"
                                             f"and it doesn't match with test list {TestDataToolsQaMainPage.TUTORIAL_MENU_LIST}")
                raise err

        section_name_ids = [f"Section:{t}" for t in TestDataToolsQaMainPage.TUTORIAL_MENU_LIST]

        @pytest.mark.parametrize('section_name, content, output_list', TestDataToolsQaMainPage.CONTENT_BY_SECTIONS,
                                 ids=section_name_ids)
        def test_checking_section_content(self, browser, logs_tool_qa_main_page, section_name, content, output_list):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_BUTTON)
            page.hovering_on_tutorial_section(section_name)
            time.sleep(1)
            section_list = page.search_element(content).text
            new_section_list = page.generating_text_to_list(section_list)
            try:
                assert new_section_list == output_list, \
                    f"There was getting the following content of {section_name} section {new_section_list}, " \
                    f"but test content is following {output_list}"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"There was getting the following content of {section_name} section {new_section_list}, "
                    f"but test content is following {output_list}")
                raise err
