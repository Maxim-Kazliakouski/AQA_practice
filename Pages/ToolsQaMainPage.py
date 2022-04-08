import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException, \
    ElementClickInterceptedException
from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators
from Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Tests.tests_ToolsQaMainPage.conftest import logs_tool_qa_main_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ToolsQaMainPage(BasePage):
    def hovering_on_tutorial_section(self, name_section):
        action = ActionChains(self.browser)
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{name_section}')]")
        action.move_to_element(section).perform()

    def handling_categories_without_start_learning(self, list_for_gen):
        new_cat_list = []
        for i in list_for_gen:
            if i == 'Start Learning':
                continue
            else:
                new_cat_list.append(i)
        return new_cat_list

    def removing_advertisement(self):
        if self.getting_attribute_from_element(ToolsQaMainPageLocators.MODAL_WINDOW, 'aria-hidden') == 'false':
            self.click_on_element(ToolsQaMainPageLocators.CLOSE_ADV_SUGGESTION_BUTTON)
        else:
            pass

    def checking_carousel(self, capsys, logs_tool_qa_main_page):
        appearance = []
        n = 0
        while n < 10:
            self.removing_advertisement()
            try:
                visible_element_in_carousel = WebDriverWait(self.browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, f'//*[@id="tns1-item{n}"]')),
                    message="There is no such element in carousel, cause of it's hidden and doesn't appear yet")
                print(f'\nYes, there is "{n}" element!!!')
                print(self.search_element((By.XPATH, f'//*[@id="tns1-item{n}"]')).text)
                title = self.generating_text_to_list(visible_element_in_carousel.text)
                appearance.append(title[0])
                n += 1
                time.sleep(4)
            except TimeoutException as err:
                self.making_screenshot()
                logs_tool_qa_main_page.error('There is no such element in carousel')
                raise err

