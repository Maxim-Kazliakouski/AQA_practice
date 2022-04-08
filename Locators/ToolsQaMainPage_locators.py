from selenium.webdriver.common.by import By


class ToolsQaMainPageLocators:
    # advertisement suggestion
    CLOSE_ADV_SUGGESTION_BUTTON = By.XPATH, '//*[@id="modal-1-content"]/button'
    MODAL_WINDOW = By.CSS_SELECTOR, "#advertisement-modal"
    ADVERTISE_URL = By.ID, 'advertisement-url'
    # cookies
    COOKIES = By.CLASS_NAME, 'gdpr-alert.show'
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
    # enroll yourself button
    ENROLL_YOURSELF_BUTTON = By.CLASS_NAME, "btn.btn-primary-shadow.btn-block"
    READ_MORE_BUTTON = By.CLASS_NAME, "new-training__read-more"
    # text on enroll form
    ENROLL_FORM = By.CLASS_NAME, 'text-center.upcoming__registration--heading'
    # text after clicking on read more button
    TEXT_READ_MORE = By.CLASS_NAME, 'enroll__why--trainer'
    # categories (10 items)
    CATEGORIES = By.XPATH, '/html/body/div[1]/div[2]/div/div/div'
    REDIRECT_TO_CATEGORY = By.XPATH, "//div[contains(text(),'Test Project')]"
    # articles carousel
    LATEST_ARTICLES_BUTTON = By.XPATH, "//a[contains(text(),'Latest Articles')]"
    LATEST_ARTICLES_INFO = By.XPATH, "//h1[contains(text(),'Recent Articles')]"
    NEXT_CAROUSEL_BUTTON = By.XPATH, "//button[contains(text(),'>')]"
    BACK_CAROUSEL_BUTTON = By.XPATH, "//button[contains(text(),'<')]"






