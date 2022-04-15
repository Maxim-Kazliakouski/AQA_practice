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

    def choosing_element_in_carousel(self, content_name, logs_tool_qa_main_page):
        titles_list = []
        item = 0
        while content_name not in titles_list:
            self.removing_advertisement()
            content_list = self.search_element((By.XPATH, f'//*[@id="tns1-item{item}"]')).text
            title = self.generating_text_to_list(content_list)
            titles_list.append(title[0])
            self.click_on_element(ToolsQaMainPageLocators.NEXT_CAROUSEL_BUTTON)
            item += 1
            if item >= 10:
                break
        if content_name in titles_list:
            self.removing_advertisement()
            self.click_on_element(ToolsQaMainPageLocators.BACK_CAROUSEL_BUTTON)
            self.click_on_element((By.XPATH, f'//*[@id="tns1-item{item-1}"]'))
            el_on_page = self.is_element_visible_on_th_page((By.XPATH, f"//h1[contains(text(),'{content_name}')]"),
                                                            logs_tool_qa_main_page)
        else:
            el_on_page = 'There is no such content title in carousel'
        return el_on_page
