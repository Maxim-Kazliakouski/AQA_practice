import time
import pytest
from Locators.AlertsFrameWindows_locators import AlertsFrameWindowsLocators
from Locators.MainPage_locators import MainPageLocators
from Pages.AlertsFrameWindows import AlertsFrameWindows
from Tests.tests_AlertsFrameWindows.data_AlertsFrameWindows import TestDataAlertsFrameWindows
from Tests.tests_MainPage.data_MainPage import TestDataMainPage


class Test_AlertsFrameWindows:
    @pytest.mark.BrowserWindows
    class Test_BrowserWindows:
        def test_user_on_the_browser_windows_page(self, browser, logs_alerts_frame_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ALERTS_FRAMES_BUTTON)
            page.scrolling_for_one_screen()
            page.go_to_section(AlertsFrameWindowsLocators.BROWSER_WINDOW)
            browser_windows_page_url = page.getting_current_url()
            try:
                assert browser_windows_page_url == TestDataAlertsFrameWindows.BROWSER_WINDOWS_URL, \
                    "User isn't on Browser Windows Page"
            except AssertionError as err:
                logs_alerts_frame_page.error("User isn't on Browser Windows")
                raise err

        def test_new_tab(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.BROWSER_WINDOWS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.NEW_TAB_BUTTON)
            page.switching_to_the_second_browser_tab()
            text = page.search_element(AlertsFrameWindowsLocators.INFO_FROM_NEW_TAB).text
            page.browser.close()
            page.switching_to_the_first_browser_tab()
            try:
                assert text == TestDataAlertsFrameWindows.INFO_NEW_TAB, \
                    f"There is no such text like '{TestDataAlertsFrameWindows.INFO_NEW_TAB}' or user" \
                    f"isn't on the new tab"
            except AssertionError as err:
                logs_alerts_frame_page.error(
                    f"There is no such text like '{TestDataAlertsFrameWindows.INFO_NEW_TAB}' or user" \
                    f"isn't on the new tab")
                raise err

        def test_new_window(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.BROWSER_WINDOWS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.NEW_WINDOW)
            page.switching_to_the_second_browser_tab()
            text = page.search_element(AlertsFrameWindowsLocators.INFO_FROM_NEW_TAB).text
            try:
                assert text == TestDataAlertsFrameWindows.INFO_NEW_TAB, \
                    f"There is no such text like '{TestDataAlertsFrameWindows.INFO_NEW_TAB}' or user" \
                    f"isn't on the new window"
            except AssertionError as err:
                logs_alerts_frame_page.error(
                    f"There is no such text like '{TestDataAlertsFrameWindows.INFO_NEW_TAB}' or user"
                    f"isn't on the new window")
                raise err

    @pytest.mark.Alerts
    class Test_Alerts:
        def test_user_on_the_browser_windows_page(self, browser, logs_alerts_frame_page):
            link = TestDataMainPage.MAIN_PAGE_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(MainPageLocators.ALERTS_FRAMES_BUTTON)
            page.scrolling_for_one_screen()
            page.go_to_section(AlertsFrameWindowsLocators.ALERTS)
            alerts_page_url = page.getting_current_url()
            try:
                assert alerts_page_url == TestDataAlertsFrameWindows.ALERTS_URL, \
                    "User isn't on Alerts Page"
            except AssertionError as err:
                logs_alerts_frame_page.error("User isn't on Alerts Windows")
                raise err

        def test_ordinary_alert(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.ALERTS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.ORDINARY_ALERT_BUTTON)
            alert_text = page.getting_info_from_alert()
            try:
                assert alert_text == TestDataAlertsFrameWindows.ORDINARY_ALERT_INFO, \
                    "User doesn't click on button or there is no any alert window"
            except AssertionError as err:
                logs_alerts_frame_page.error("User doesn't click on button or there is no any alert window")
                raise err

        @pytest.mark.xfail(reason='This case better launch with headmode=true')
        def test_alert_with_delay(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.ALERTS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.DELAY_ALERT_BUTTON)
            # use time sleep, because of appearing alert with delay
            time.sleep(6)
            alert_text = page.getting_info_from_alert()
            try:
                assert alert_text == TestDataAlertsFrameWindows.DELAY_ALERT_INFO, \
                    "User doesn't click on button or there is no any alert window"
            except AssertionError as err:
                logs_alerts_frame_page.error("User doesn't click on button or there is no any alert window")
                raise err

        def test_alert_with_confirm_box_ok(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.ALERTS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.CONFIRM_BOX_ALERT)
            alert = page.browser.switch_to.alert
            alert.accept()
            text = page.search_element(AlertsFrameWindowsLocators.CONFIRM_ALERT_RESULT).text
            try:
                assert text == TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_OK, \
                    f"User doesn't click on confirm button in alert message and there is no any confirmation" \
                    f" message like '{TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_OK}'"
            except AssertionError as err:
                logs_alerts_frame_page.error(f"User doesn't click on confirm button in alert message and there is"
                                             f" no any confirmation message like"
                                             f" '{TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_OK}'")
                raise err

        def test_alert_with_confirm_box_cancel(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.ALERTS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.CONFIRM_BOX_ALERT)
            alert = page.browser.switch_to.alert
            alert.dismiss()
            text = page.search_element(AlertsFrameWindowsLocators.CONFIRM_ALERT_RESULT).text
            try:
                assert text == TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_CANCEL, \
                    f"User doesn't click on confirm button in alert message and there is no any confirmation" \
                    f" message like '{TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_CANCEL}'"
            except AssertionError as err:
                logs_alerts_frame_page.error(f"User doesn't click on confirm button in alert message and there is"
                                             f" no any confirmation message like"
                                             f" '{TestDataAlertsFrameWindows.CONFIRM_ALERT_RESULT_CANCEL}'")
                raise err

        def test_alert_with_confirm_box_text(self, browser, logs_alerts_frame_page):
            link = TestDataAlertsFrameWindows.ALERTS_URL
            page = AlertsFrameWindows(browser, link)
            page.open_page(link)
            page.removing_advertisement()
            page.click_on_element(AlertsFrameWindowsLocators.TEXT_ALERT)
            page.input_text_into_alert(TestDataAlertsFrameWindows.TEXT_FOR_ALERT)
            result = page.search_element(AlertsFrameWindowsLocators.TEXT_ALERT_RESULT).text
            try:
                assert result == f'You entered {TestDataAlertsFrameWindows.TEXT_FOR_ALERT}', \
                    "The alert text doesn't match with entered or alert window doesn't appear"
            except AssertionError as err:
                logs_alerts_frame_page.error("The alert text doesn't match with entered or alert window doesn't appear")
                raise err








