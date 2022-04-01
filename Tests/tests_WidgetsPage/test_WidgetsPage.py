import time
import pytest
from Locators.MainPage_locators import MainPageLocators
from Locators.WidgetsPage_locators import WidgetsLocators
from Pages.WidgetsPage import WidgetsPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage
from Tests.tests_WidgetsPage.data_WidgetsPage import TestDataWidgetsPage
from Tests.tests_MainPage.conftest import browser_xfail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.Widgets
class Test_WidgetsPage:
    @pytest.mark.Accordian
    class Test_accordian:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_accordian_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.scaling_window(0.5)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.go_to_section(WidgetsLocators.ACCORDIAN)
            accordian_url = page.getting_current_url()
            try:
                assert accordian_url == TestDataWidgetsPage.ACCORDIAN_URL, \
                    "The user isn't on the Accordian page"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("The user isn't on the Accordian page")
                raise err

        def test_accordian(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.ACCORDIAN_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.scrolling_for_one_screen()
            page.click_on_element(WidgetsLocators.SECOND_ACCORDIAN)
            second_accordion_on_page = page.is_element_present_on_the_page(WidgetsLocators.SECOND_ACCORDIAN_CONTENT,
                                                                           logs_widgets_page)
            try:
                assert second_accordion_on_page, "There is no second accordion after clicking on it"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("There is no second accordion after clicking on it")
                raise err

        def test_show_first_accordion_after_opening_page(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.ACCORDIAN_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            first_accordion_on_page = page.is_element_present_on_the_page(WidgetsLocators.FIRST_ACCORDIAN_CONTENT,
                                                                          logs_widgets_page)
            try:
                assert first_accordion_on_page, "There is no first accordion after getting on the page"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("There is no first accordion after getting on the page")
                raise err

    @pytest.mark.AutoComplete
    class Test_autocomplete:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_auto_complete_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            # page.scaling_window(0.5)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            page.go_to_section(WidgetsLocators.AUTO_COMPLETE)
            accordian_url = page.getting_current_url()
            try:
                assert accordian_url == TestDataWidgetsPage.AUTO_COMPLETE_URL, \
                    "The user isn't on the AutoComplete page"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("The user isn't on the AutoComplete page")
                raise err

        letter_ids = [f'Letter -> {t}' for t in TestDataWidgetsPage.LETTER_LIST]

        @pytest.mark.parametrize('letter, output_list',
                                 [(TestDataWidgetsPage.LETTER_LIST[0], TestDataWidgetsPage.LIST_FOR_B_LETTER),
                                  (TestDataWidgetsPage.LETTER_LIST[1], TestDataWidgetsPage.LIST_FOR_E_LETTER)],
                                 ids=letter_ids)
        def test_autocomplete(self, browser, logs_widgets_page, letter, output_list):
            link = TestDataWidgetsPage.AUTO_COMPLETE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.sending_keys_into_field(WidgetsLocators.MUL_COL_NAMES_FIELD, letter)
            text = page.search_element(WidgetsLocators.NAMES_LIST).text
            new_text = page.generating_text_to_list(text)
            try:
                assert new_text == output_list, \
                    f"There were getting the following list {new_text}, " \
                    f"but test list is following {output_list}"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"There were getting the following list {new_text}, "
                                        f"but test list is following {output_list}")
                raise err

    @pytest.mark.DatePicker
    class Test_datepicker:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_datepicker_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            page.go_to_section(WidgetsLocators.DATE_PICKER)
            date_picker_url = page.getting_current_url()
            try:
                assert date_picker_url == TestDataWidgetsPage.DATE_PICKER_URL, \
                    "The user isn't on the Picker Date page"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("The user isn't on the Picker Date page")
                raise err

        def test_select_date(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.DATE_PICKER_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.choosing_date_from_calendar('September', '1991')
            date = page.getting_attribute_from_element(WidgetsLocators.CALENDAR_DATE, 'value')
            try:
                assert date == TestDataWidgetsPage.DATE, f"The getting date is '{date}'," \
                                                         f" but should be '{TestDataWidgetsPage.DATE}'"
            except AssertionError as err:
                page.making_screenshot()
                raise err

        def test_select_date_and_time(self, browser_xfail, logs_widgets_page):
            link = TestDataWidgetsPage.DATE_PICKER_URL
            page = WidgetsPage(browser_xfail, link)
            page.open_page(link)
            page.removing_advertisement()
            page.choosing_date_and_time(number_of_month=9, year_for_choosing=1991, time='15:15')
            date_and_time = page.getting_attribute_from_element(WidgetsLocators.DATE_AND_TIME, 'value')
            try:
                assert date_and_time == TestDataWidgetsPage.DATE_AND_TIME, \
                    f"Getting date '{date_and_time}', doesn't match with test date '{TestDataWidgetsPage.DATE_AND_TIME}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"Getting date '{date_and_time}',"
                                        f" doesn't match with test date '{TestDataWidgetsPage.DATE_AND_TIME}'")
                raise err

    @pytest.mark.Slider
    class Test_slider:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_slider_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            page.go_to_section(WidgetsLocators.SLIDER)
            slider_url = page.getting_current_url()
            try:
                assert slider_url == TestDataWidgetsPage.SLIDER_URL, \
                    f"User isn't on the Slider page {TestDataWidgetsPage.SLIDER_URL}"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"User isn't on the Slider page {TestDataWidgetsPage.SLIDER_URL}")
                raise err

        def test_drag_and_drop(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.SLIDER_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            runner = page.search_element(WidgetsLocators.RUNNER)
            action = ActionChains(browser)
            # drag and drop method :50 - moving by X-axis; 0 - moving by Y-axis
            action.drag_and_drop_by_offset(runner, 50, 0).perform()
            runner_value = page.getting_attribute_from_element(WidgetsLocators.RUNNER, 'value')
            try:
                assert runner_value == TestDataWidgetsPage.RUNNER_POSITION, \
                    f"The runner on the '{runner_value}' position, but should be on '{TestDataWidgetsPage.RUNNER_POSITION}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(
                    f"The runner on the '{runner_value}' position, but should be on '{TestDataWidgetsPage.RUNNER_POSITION}'")
                raise err

    @pytest.mark.ProgressBar
    class Test_progressbar:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_progressbar_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            # page.scaling_window(0.5)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            # page.scrolling_for_one_screen()
            page.go_to_section(WidgetsLocators.PROGRESS_BAR)
            pr_bar = page.getting_current_url()
            try:
                assert pr_bar == TestDataWidgetsPage.PROGRESS_BAR_URL, \
                    f"User isn't on the Progress Bar page {TestDataWidgetsPage.PROGRESS_BAR_URL}, " \
                    f"currently user locates on the {pr_bar}"
            except AssertionError as err:
                page.making_screenshot()
                f"User isn't on the Progress Bar page '{TestDataWidgetsPage.PROGRESS_BAR_URL}', "
                f"currently user locates on the '{pr_bar}'"
                raise err

        def test_full_filling_of_progress_bar(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.PROGRESS_BAR_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(WidgetsLocators.START_BUTTON)
            # waiting for until progress bar fills
            time.sleep(12)
            reset_button_on_page = page.is_element_present_on_the_page(WidgetsLocators.RESET_BUTTON, logs_widgets_page)
            try:
                assert reset_button_on_page, "The progress bar isn't filled till the end, and 'Start' button " \
                                             "doesn't change on 'Reset' button"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("The progress bar isn't filled till the end, and 'Start' button "
                                        "doesn't change on 'Reset' button")
                raise err

        def test_reset_progress_bar(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.PROGRESS_BAR_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(WidgetsLocators.START_BUTTON)
            # waiting for until progress bar fills
            time.sleep(12)
            page.click_on_element(WidgetsLocators.RESET_BUTTON)
            process = page.getting_attribute_from_element(WidgetsLocators.PROGRESS_BAR_PROCESS, 'aria-valuenow')
            try:
                assert process == '0', f"The process hasn't been reset, because of the 'Reset' button doesn't appear"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"The process hasn't been reset, because of the 'Reset' button doesn't appear")
                raise err

        def test_appearance_stop_button(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.PROGRESS_BAR_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(WidgetsLocators.START_BUTTON)
            stop_button_on_page = page.is_element_present_on_the_page(WidgetsLocators.STOP_BUTTON, logs_widgets_page)
            try:
                assert stop_button_on_page, "The 'Stop' button doesnt appear after clicking on 'Start' button"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("The 'Stop' button doesnt appear after clicking on 'Start' button")
                raise err

    @pytest.mark.ToolTips
    class Test_tooltips:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_the_tooltips_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            page.scroll_screen(parameters='0, 800')
            page.go_to_section(WidgetsLocators.TOOL_TIPS)
            tool_tips_page = page.getting_current_url()
            try:
                assert tool_tips_page == TestDataWidgetsPage.TOOL_TIPS_URL, \
                    f"User isn't on the Progress Bar page {TestDataWidgetsPage.TOOL_TIPS_URL}, " \
                    f"currently user locates on the {tool_tips_page}"
            except AssertionError as err:
                page.making_screenshot()
                f"User isn't on the Progress Bar page '{TestDataWidgetsPage.TOOL_TIPS_URL}', "
                f"currently user locates on the '{tool_tips_page}'"
                raise err

        elements_ids = [f'{t}' for t in TestDataWidgetsPage.ELEMENTS_NAMES]

        @pytest.mark.parametrize('hovered_elements, tooltip_text, output_text',
                                 [(WidgetsLocators.HOVER_ME_BUTTON, WidgetsLocators.TOOLTIP_TEXT,
                                   TestDataWidgetsPage.TOOL_TIP_TEXT_HOVER_ON_ME_BUTTON),
                                  (WidgetsLocators.HOVER_ME_FIELD, WidgetsLocators.TOOLTIP_TEXT,
                                   TestDataWidgetsPage.TOOL_TIP_TEXT_HOVER_ON_FIELD),
                                  (WidgetsLocators.HOVER_LINK1, WidgetsLocators.TOOLTIP_TEXT,
                                   TestDataWidgetsPage.TOOL_TIP_TEXT_HOVER_ON_LINK1),
                                  (WidgetsLocators.HOVER_LINK2, WidgetsLocators.TOOLTIP_TEXT,
                                   TestDataWidgetsPage.TOOL_TIP_TEXT_HOVER_ON_LINK2)],
                                 ids=elements_ids)
        def test_hovered_tooltips(self, browser, logs_widgets_page, hovered_elements, tooltip_text, output_text):
            link = TestDataWidgetsPage.TOOL_TIPS_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.scaling_window(0.95)
            page.removing_advertisement()
            action = ActionChains(browser)
            hover_me_button = page.search_element(hovered_elements)
            action.move_to_element(hover_me_button).perform()
            time.sleep(1)
            hover_text = page.search_element(tooltip_text).text
            try:
                assert hover_text == output_text, \
                    f"The text after hovering on button '{hover_text}'" \
                    f" doesn't match with test text '{output_text}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"The text after hovering on button '{hover_text}'"
                                        f" doesn't match with test text {output_text}")
                raise err

    @pytest.mark.Menu
    class Test_menu:
        @pytest.mark.user_on_page
        @pytest.mark.xfail(reason='Necessary to restart again after test session')
        def test_user_on_menu_page(self, browser, logs_widgets_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            # adding function for blocking advertisement if it is
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.WIDGETS_BUTTON)
            page.browser.refresh()
            page.scroll_screen(parameters='0, 800')
            page.go_to_section(WidgetsLocators.MENU)
            text_box_section_url = page.getting_current_url()
            try:
                assert text_box_section_url == TestDataWidgetsPage.MENU_URL, "User isn't on menu section..."
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error("User isn't on menu section...")
                raise err

        def test_dropdown_after_hovering1(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.MENU_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            action = ActionChains(browser)
            main_item2_tab = page.search_element(WidgetsLocators.MAIN_ITEM_2)
            action.move_to_element(main_item2_tab).perform()
            dropdown_1 = page.search_element(WidgetsLocators.DROPDOWN_LIST1).text
            new_dropdown1_list = page.generating_text_to_list(dropdown_1)
            try:
                assert new_dropdown1_list == TestDataWidgetsPage.DROPDOWN_1,\
                    f"The current dropdown is '{new_dropdown1_list}', but should be '{TestDataWidgetsPage.DROPDOWN_1}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"The current dropdown is '{new_dropdown1_list}',"
                                        f" but should be {TestDataWidgetsPage.DROPDOWN_1}")
                raise err

        def test_dropdown_after_hovering2(self, browser, logs_widgets_page):
            link = TestDataWidgetsPage.MENU_URL
            page = WidgetsPage(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            action = ActionChains(browser)
            main_item2_tab = page.search_element(WidgetsLocators.MAIN_ITEM_2)
            action.move_to_element(main_item2_tab).perform()
            sub_sub_list = page.search_element(WidgetsLocators.SUB_SUB_LIST)
            action.move_to_element(sub_sub_list).perform()
            dropdown_2 = page.search_element(WidgetsLocators.DROPDOWN_LIST2).text
            new_dropdown2_list = page.generating_text_to_list(dropdown_2)
            try:
                assert new_dropdown2_list == TestDataWidgetsPage.DROPDOWN_2, \
                    f"The current dropdown is '{new_dropdown2_list}', but should be '{TestDataWidgetsPage.DROPDOWN_2}'"
            except AssertionError as err:
                page.making_screenshot()
                logs_widgets_page.error(f"The current dropdown is '{new_dropdown2_list}',"
                                        f" but should be '{TestDataWidgetsPage.DROPDOWN_2}'")
                raise err
