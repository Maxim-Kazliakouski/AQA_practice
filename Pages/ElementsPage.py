from Locators.ElementsPage_locators import ElementPageLocators
from Pages.BasePage import BasePage


class ElementsPage(BasePage):
    def switching_to_the_second_browser_tab(self):
        # method for recognizing current window id
        # print(browser.current_window_handle)
        windows = self.browser.window_handles
        # Switching to second tab
        self.browser.switch_to.window(windows[1])

    # def entering_symbols_into_field_fullname(self, symbols):
    #     user_name_field = self.search_element(ElementPageLocators.FULL_NAME_FIELD)
    #     user_name_field.send_keys(symbols)

    def generating_text_to_list(self, output):
        generating_output = output.split('\n')
        return generating_output

    def entering_symbols_into_field(self, field_locator, symbols):
        email_field = self.search_element(field_locator)
        email_field.send_keys(symbols)

    def clearing_symbols_from_field(self, field_locator):
        field = self.search_element(field_locator)
        field.clear()

    # def clearing_symbols_into_fullname_field(self):
    #     fullname_field = self.search_element(ElementPageLocators.FULL_NAME_FIELD)
    #     fullname_field.clear()

    def checking_is_red_field_appear(self, field):
        if field:
            field = True
        else:
            field = False
        return field

    def generating_checkbox_info(self, output):
        new_output = output[1:]
        return new_output

    def getting_info_about_selected_checkboxes(self):
        checkbox_list = self.search_element(ElementPageLocators.INFO_AFTER_ENABLE_CHECKBOX_HOME).text
        generating_checkbox_list = self.generating_text_to_list(checkbox_list)
        new_checkbox_list = self.generating_checkbox_info(generating_checkbox_list)
        return new_checkbox_list
