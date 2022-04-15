import time
import pytest
from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators
from Pages.ToolsQaMainPage import ToolsQaMainPage
from Tests.tests_ToolsQaMainPage.data_ToolsQaMainPage import TestDataToolsQaMainPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException, \
    ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from Tests.tests_MainPage.conftest import browser
from Tests.tests_MainPage.conftest import browser_xfail
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ToolsQaMainPage
class Suite_for_ToolsQaMainPage:  # checking that 'Suite' accepts for class name (check pytest.ini)
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

        def test_enroll_yourself_button(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 150')
            page.click_on_element(ToolsQaMainPageLocators.ENROLL_YOURSELF_BUTTON)
            text_in_reg_form = page.search_element(ToolsQaMainPageLocators.ENROLL_FORM).text
            reg_form = page.is_element_present_on_the_page(ToolsQaMainPageLocators.ENROLL_FORM, logs_tool_qa_main_page)
            try:
                assert reg_form, "User hasn't been redirected to the enroll form after clicking on enroll button"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error("User hasn't been redirected to the enroll form after clicking on enroll "
                                             "button")
                raise err

        def test_read_more_button(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 150')
            page.click_on_element(ToolsQaMainPageLocators.READ_MORE_BUTTON)
            text_read_more = page.is_element_present_on_the_page(ToolsQaMainPageLocators.TEXT_READ_MORE,
                                                                 logs_tool_qa_main_page)
            try:
                assert text_read_more, "User hasn't been redirected to the read more text after clicking on read more " \
                                       "button "
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    "User hasn't been redirected to the read more text after clicking on read more button")
                raise err

        @pytest.mark.skip(reason='In this site version there is no advertisement')
        def test_appearing_advertisement(self, browser_xfail, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser_xfail, link)
            page.open_page(link)
            # time sleep for appearing advertisement (appears after 5-6 secs)
            time.sleep(6)
            hide_advert_appearing = page.getting_attribute_from_element(ToolsQaMainPageLocators.MODAL_WINDOW,
                                                                        'aria-hidden')
            try:
                assert hide_advert_appearing == 'false', "The advertisement doesn't appear"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"The advertisement doesn't appear.\nSee Assertion error:\n{err}")
                raise err

        def test_appearing_cookies(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            cookies = page.is_element_present_on_the_page(ToolsQaMainPageLocators.COOKIES, logs_tool_qa_main_page)
            try:
                assert cookies, "There is no cookies on the page"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"There is no cookies on the page.\nSee Assertion error below:\n{err}")
                raise err

    @pytest.mark.Tutorials
    class Test_tutorials:
        def test_checking_section_in_tutorial_menu(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.click_on_element(ToolsQaMainPageLocators.TUTORIAL_BUTTON)
            # adding time sleep for docker test, cause without time doesn't work
            time.sleep(1)
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

    @pytest.mark.Categories
    class Test_categories:
        def test_categories_on_main_page(self, browser, capsys, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            # page.scroll_screen('0, 900')
            categ = page.search_element(ToolsQaMainPageLocators.CATEGORIES).text
            new_categ = page.generating_text_to_list(categ)
            categories = page.handling_categories_without_start_learning(new_categ)
            try:
                assert categories == TestDataToolsQaMainPage.CATEGORIES, "There more or less categories then should be, " \
                                                                         "please check with test data categories and " \
                                                                         "web-site "
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error("There more or less categories then should be, "
                                             "please check with test data categories and web-site."
                                             f"\nSee assertion error: \n{err}")
                raise err

        cat_ids = [f'Category: {t}' for t in TestDataToolsQaMainPage.CATEGORIES]

        @pytest.mark.parametrize('category_name, text_on_category_page',
                                 TestDataToolsQaMainPage.ALL_CATEGORIES_FOR_PARAMETRIZE, ids=cat_ids)
        def test_redirection_to_all_categories(self, browser, logs_tool_qa_main_page, category_name,
                                               text_on_category_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 700')
            page.browser.find_element(By.XPATH,
                                      f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[{category_name}]/div[2]/div[1]").click()
            categ_text_locator = By.XPATH, f"//h1[contains(text(),'{text_on_category_page}')]"
            cat_text_on_page = page.is_element_present_on_the_page(categ_text_locator, logs_tool_qa_main_page)
            try:
                assert cat_text_on_page, f"There is no such text '{text_on_category_page}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(
                    f"There is no such text '{text_on_category_page}' \nSee assertion error:\n{err}")
                raise err

    @pytest.mark.ArticlesCarousel
    class Test_articles_carousel:
        def test_redirection_to_latest_articles(self, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scrolling_for_one_screen()
            page.click_on_element(ToolsQaMainPageLocators.LATEST_ARTICLES_BUTTON)
            last_articles_info = page.is_element_present_on_the_page(ToolsQaMainPageLocators.LATEST_ARTICLES_INFO,
                                                                     logs_tool_qa_main_page)
            try:
                assert last_articles_info, "User isn't on the last articles page"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"User isn't on the last articles page. See Assertion error:\n{err}")
                raise err

        def test_carousel_with_topics(self, capsys, browser, logs_tool_qa_main_page):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 1350')
            appearance = []
            n = 0
            while n < 10:
                page.removing_advertisement()
                try:
                    visible_element_in_carousel = WebDriverWait(page.browser, 1).until(
                        EC.visibility_of_element_located((By.XPATH, f'//*[@id="tns1-item{n}"]')),
                        message="There is no such element in carousel, cause of it's hidden and doesn't appear yet")
                    # with capsys.disabled():
                    #     print(f'\nYes, there is "{n}" element in carousel!!!', end='\n')
                    #     print(page.search_element((By.XPATH, f'//*[@id="tns1-item{n}"]')).text)
                    title = page.generating_text_to_list(visible_element_in_carousel.text)
                    appearance.append(title[0])
                    n += 1
                    time.sleep(4)
                except TimeoutException as err:
                    page.making_screenshot()
                    logs_tool_qa_main_page.error('There is no such element in carousel')
                    raise err
            try:
                assert appearance == TestDataToolsQaMainPage.CONTENT_LIST_IN_CAROUSEL, "The content in carousel " \
                                            "and in test data is different, please check web-site and test data"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"The content in carousel and in test data is different,"
                                             f" please check web-site and test data.\nSee Assertion error:\n{err}")
                raise err

        buttons_ids = [f'Button-{t}' for t in TestDataToolsQaMainPage.BUTTONS_IN_CAROUSEL]

        @pytest.mark.parametrize('buttons, article', TestDataToolsQaMainPage.CAROUSEL_BUTTONS_FOR_PARAMETRIZE,
                                 ids=buttons_ids)
        def test_next_back_button_in_carousel(self, browser, logs_tool_qa_main_page, buttons, article):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 1350')
            n = 0
            while n < 5:
                page.removing_advertisement()
                page.click_on_element(buttons)
                n += 1
            visible_el_in_carousel = page.is_element_visible_on_th_page((By.XPATH, f'//*[@id="tns1-item{article}"]'),
                                                                        logs_tool_qa_main_page)
            try:
                assert visible_el_in_carousel, "There is no such element after clicking on Next carousel button"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"There is no such element after clicking on Next carousel button."
                                             f"\nSee Assertion error:\n{err}")
                raise

        @pytest.mark.parametrize('articles', TestDataToolsQaMainPage.CONTENT_LIST_IN_CAROUSEL)
        def test_checking_articles_content(self, browser, logs_tool_qa_main_page, articles):
            link = TestDataToolsQaMainPage.TOOLS_QA_MAIN_PAGE_URL
            page = ToolsQaMainPage(browser, link)
            page.open_page(link)
            page.scroll_screen('0, 1350')
            el_in_carousel = page.choosing_element_in_carousel(articles, logs_tool_qa_main_page)
            try:
                assert el_in_carousel == True, "There is no such element in carousel or redirection doesn't work"
            except AssertionError as err:
                page.making_screenshot()
                logs_tool_qa_main_page.error(f"There is no such element in carousel or redirection doesn't work."
                                             f"\nSee Assertion error:\n{err}")
                raise err
