from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators
from Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ToolsQaMainPage(BasePage):
    def hovering_on_tutorial_section(self, name_section):
        action = ActionChains(self.browser)
        section = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{name_section}')]")
        action.move_to_element(section).perform()



