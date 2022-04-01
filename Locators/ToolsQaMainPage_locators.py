from selenium.webdriver.common.by import By


class ToolsQaMainPageLocators:
    # advertisement suggestion
    CLOSE_ADV_SUGGESTION_BUTTON = By.XPATH, '//*[@id="modal-1-content"]/button'
    MODAL_WINDOW = By.ID, 'advertisement-modal'
    ADVERTISE_URL = By.ID, 'advertisement-url'
    COOKIE = By.ID, 'cookie-policy-modal'
    #
    PAGEINFO = By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div"
    IMAGE_ON_MAIN_PAGE = By.CLASS_NAME, 'learner'
    # tabs
    LIST_TAB = By.XPATH, '/html/body/header/nav/div/div/div[3]/div/div[1]/ul'
    SELENIUM_TRAINING_TAB = By.XPATH, "//a[@href='/selenium-training?q=headers']"
    DEMO_SITE = By.XPATH, "//a[@href='https://demoqa.com']"
    # logo
    LOGO = By.CLASS_NAME, 'tools-qa-header__logo'
    # tutorial button
    TUTORIAL_BUTTON = By.CLASS_NAME, 'navbar__tutorial-menu'
    TUTORIAL_MENU_OPEN = By.CLASS_NAME, 'overlay-open'
    TUTORIAL_MENU_CLOSE = By.CLASS_NAME, 'navbar__tutorial-menu--menu-bars'
    # tutorial section
    TUTORIAL_MENU_CONTENT = By.CLASS_NAME, 'first-generation'
    QA_PRACTICES = By.XPATH, "//span[contains(text(),'QA Practices')]"
    LIST_OF_SECTION_CONTENT = By.XPATH, '/html/body/nav/div/div/div[2]/div'
