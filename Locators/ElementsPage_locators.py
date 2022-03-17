from selenium.webdriver.common.by import By


# section
class ElementPageLocators:
    TEXT_BOX_SECTION = By.XPATH, "//span[contains(text(),'Text Box')]"
    CHECK_BOX_SECTION = By.XPATH, "//span[contains(text(),'Check Box')]"

# subsection in section ELEMENTS
    # text box section
    FULL_NAME_FIELD = By.ID, 'userName'
    EMAIL = By.ID, 'userEmail'
    CURRENT_ADDRESS = By.XPATH, "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = By.ID, 'permanentAddress'
    SUBMIT_BUTTON = By.ID, 'submit'
    OUTPUT_NAME = By.CSS_SELECTOR, '#name'
    OUTPUT_EMAIL = By.CSS_SELECTOR, '#email'
    WRONG_RED_EMAIL_FIELD = By.CLASS_NAME, 'mr-sm-2.field-error.form-control'
    OUTPUT_CURRENT_ADDRESS = By.XPATH, "//p[@id='currentAddress']"
    OUTPUT_PERMANENT_ADDRESS = By.XPATH, "//p[@id='permanentAddress']"

    # check box section
    HOME_CHECK_BOX = By.CLASS_NAME, 'rct-checkbox'
    HOME_CHECK_ENABLE_DISABLE = By.CSS_SELECTOR, '#tree-node>ol>li>span>label>span.rct-checkbox>svg'
    INFO_AFTER_ENABLE_CHECKBOX_HOME = By.ID, "result"
    PLUS_BUTTON = By.XPATH, '//*[@id="tree-node"]/div/button[1]'
    PLUS_BUTTON_ON_OFF = By.CSS_SELECTOR, '#tree-node>ol>li>span>button>svg'
    MINUS_BUTTON = By.XPATH, '//*[@id="tree-node"]/div/button[2]'

