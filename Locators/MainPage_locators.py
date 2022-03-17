from selenium.webdriver.common.by import By


class MainPageLocators:
    #buttons
    ELEMENTS_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]'
    FORMS_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]'
    ALERTS_FRAMES_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]'
    WIDGETS_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]'
    INTERACTIONS_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]'
    BOOK_STORE_APP_BUTTON = By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]'
    #
    MAIN_PAGE_LOGO = By.XPATH, '//*[@id="app"]/header/a'
    CLOSED_FIXED_BAN = By.ID, 'close-fixedban'
    SELENIUM_CERTIFICATION_BANNER = By.CLASS_NAME, 'banner-image'
    SECTIONS = By.XPATH, '//*[@id="app"]/div/div/div[2]/div'


