from selenium.webdriver.common.by import By


class AlertsFrameWindowsLocators:
    # section name
    BROWSER_WINDOW = 'Browser Windows'
    ALERTS = 'Alerts'

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




