from selenium.webdriver.common.by import By


class FormsPageLocators:
    # section name
    PRACTICE_FORMS = 'Practice Form'

    # fields
    FIRST_NAME = By.ID, 'firstName'
    LAST_NAME = By.ID, 'lastName'
    EMAIL = By.ID, 'userEmail'
    CALENDAR = By.ID, 'dateOfBirthInput'
    FIVEth_SEPTEMBER = By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]'
    UPLOAD_BUTTON = By.XPATH, "//input[@id='uploadPicture']"
    CURRENT_ADDRESS = By.ID, "currentAddress"
    MOBILE_NUMBER = By.ID, "userNumber"
    SUBMIT_BUTTON = By.XPATH, "//button[@id='submit']"
    MODAL_WINDOW = By.XPATH, "//body/div[4]/div[1]/div[1]"




