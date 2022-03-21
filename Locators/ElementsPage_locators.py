from selenium.webdriver.common.by import By


# section names
class ElementPageLocators:
    TEXT_BOX_SECTION = 'Text Box'
    CHECK_BOX_SECTION = 'Check Box'
    RADIO_BUTTON_SECTION = 'Radio Button'
    WEB_TABLES_SECTION = 'Web Tables'
    BUTTONS_SECTION = 'Buttons'
    LINKS_SECTION = 'Links'

    # TEXT_BOX_SECTION = By.XPATH, "//span[contains(text(),'Text Box')]"
    # CHECK_BOX_SECTION = By.XPATH, "//span[contains(text(),'Check Box')]"
    # RADIO_BUTTON_SECTION = By.XPATH, "//span[contains(text(),'Radio Button')]"

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

    # radio button section
    RB_YES = 'Yes'
    RB_IMPRESSIVE = 'Impressive'

    # web tables section
    EDIT_BUTTON = By.ID, 'edit-record-1'
    REGISTRATION_FORM = By.CLASS_NAME, 'modal-content'
    COMPLIANCE_DEPARTMENT = By.XPATH, "//div[contains(text(),'Compliance')]"
    ADD_BUTTON = By.ID, 'addNewRecordButton'
    TABLE_CONTENT = By.CLASS_NAME, 'rt-tbody'
    SEARCH_FIELD = By.XPATH, "//input[@id='searchBox']"
    FIRST_NAME_FIELD = By.ID, 'firstName'
    LAST_NAME_FIELD = By.ID, 'lastName'
    EMAIL_FIELD = By.ID, 'userEmail'
    AGE_FIELD = By.ID, 'age'
    SALARY_FIELD = By.ID, 'salary'
    DEPARTMENT_FIELD = By.ID, 'department'
    FIELD_VALIDATION = By.CLASS_NAME, 'was-validated'

    # buttons section
    DOUBLE_CLICK_ME_BUTTON = By.ID, 'doubleClickBtn'
    INFO_AFTER_DOUBLE_CLICKING = By.ID, 'doubleClickMessage'
    RIGHT_CLICK_BUTTON = By.ID, 'rightClickBtn'
    INFO_AFTER_RIGHT_CLICKING = By.ID, 'rightClickMessage'
    CLICK_BUTTON = By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button'
    INFO_AFTER_CLICKING_BUTTON = By.ID, 'dynamicClickMessage'

    # links section
    SIMPLE_LINK = By.ID, 'simpleLink'
    DYNAMIC_LINK = By.ID, 'dynamicLink'
    HOME_LINK = [SIMPLE_LINK, DYNAMIC_LINK]
    CREATED_LINK = By.ID, 'created'
    NO_CONTENT_LINK = By.ID, 'no-content'
    MOVED_LINK = By.ID, 'moved'
    BAD_REQUEST_LINK = By.ID, 'bad-request'
    UNAUTHORIZED_LINK = By.ID, 'unauthorized'
    FORBIDDEN_LINK = By.ID, 'forbidden'
    INVALID_URL_LINK = By.ID, 'invalid-url'
    INFO_MESSAGE = By.ID, 'linkResponse'













