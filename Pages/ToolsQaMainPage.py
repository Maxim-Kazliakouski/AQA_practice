from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators
from Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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



