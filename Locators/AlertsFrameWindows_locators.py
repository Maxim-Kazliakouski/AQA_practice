from selenium.webdriver.common.by import By


class AlertsFrameWindowsLocators:
    # section name
    BROWSER_WINDOW = 'Browser Windows'
    ALERTS = 'Alerts'
    FRAMES = 'Frames'
    MODAL_DIALOGS = 'Modal Dialogs'

    # for browser windows section
    NEW_TAB_BUTTON = By.ID, 'tabButton'
    INFO_FROM_NEW_TAB = By.ID, 'sampleHeading'
    NEW_WINDOW = By.ID, 'windowButton'
    NEW_WINDOW_MESSAGE = By.ID, 'messageWindowButton'

    # for alerts section
    ORDINARY_ALERT_BUTTON = By.ID, 'alertButton'
    DELAY_ALERT_BUTTON = By.ID, 'timerAlertButton'
    CONFIRM_BOX_ALERT = By.ID, 'confirmButton'
    CONFIRM_ALERT_RESULT = By.ID, 'confirmResult'
    TEXT_ALERT = By.ID, 'promtButton'
    TEXT_ALERT_RESULT = By.ID, 'promptResult'

    # for frame section
    FIRST_IFRAME = By.ID, 'frame1'
    TEXT_FIRST_IFRAME = By.ID, 'sampleHeading'
    SECOND_IFRAME = By.ID, 'frame2'
    TEXT_SECOND_IFRAME = By.ID, 'sampleHeading'

    # for modal dialogs
    SMALL_MODAL_BUTTON = By.ID, 'showSmallModal'
    SMALL_MODAL_WINDOW = By.XPATH, '//body/div[4]/div[1]/div[1]'
    INFO_SMALL_MODAL = By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]'
    CLOSE_BUTTON = By.ID, 'closeSmallModal'
    CLOSE_X_BUTTON = By.XPATH, "//span[contains(text(),'×')]"








