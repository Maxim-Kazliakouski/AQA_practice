from selenium.webdriver.common.by import By


class WidgetsLocators:
    # section name
    ACCORDIAN = 'Accordian'
    AUTO_COMPLETE = 'Auto Complete'
    DATE_PICKER = 'Date Picker'
    SLIDER = 'Slider'
    PROGRESS_BAR = 'Progress Bar'
    TOOL_TIPS = 'Tool Tips'
    MENU = 'Menu'

    # accordian section
    SECOND_ACCORDIAN = By.ID, 'section2Heading'
    SECOND_ACCORDIAN_CONTENT = By.CSS_SELECTOR, '#accordianContainer>div>div:nth-child(2)>div.collapse.show'
    FIRST_ACCORDIAN = By.ID, 'section1Heading'
    FIRST_ACCORDIAN_CONTENT = By.CSS_SELECTOR, '#accordianContainer>div>div:nth-child(1)>div.collapse.show'

    # autocomplete section
    MUL_COL_NAMES_FIELD = By.XPATH, "//input[@id='autoCompleteMultipleInput']"
    NAMES_LIST = By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div[2]'

    # date picker section
    SELECT_DATE = By.XPATH, "//input[@id='datePickerMonthYearInput']"
    FIFTH_DAY_IN_CALENDAR = By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]'
    CALENDAR_DATE = By.ID, 'datePickerMonthYearInput'
    # for date and time
    DATE_AND_TIME = By.XPATH, "//input[@id='dateAndTimePickerInput']"
    # ARROW_BUTTON_FOR_MONTH = By.CLASS_NAME, "react-datepicker__month-read-view--down-arrow"
    ARROW_BUTTON_FOR_MONTH = By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/span[1]'
    ARROW_BUTTON_FOR_YEAR = By.CLASS_NAME, "react-datepicker__year-read-view--down-arrow"
    ARROW_BUTTON_FOR_YEAR2 = By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[13]'
    YEAR_1991 = By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[11]"
    FIFTH_DAY = By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]'
    # TIME_15_15 = By.XPATH, "//li[contains(text(),'15:15')]"

    # for slider
    RUNNER = By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input'

    # for progress bar section
    START_BUTTON = By.XPATH, "//*[contains(text(),'Start')]"
    RESET_BUTTON = By.XPATH, "//*[contains(text(),'Reset')]"
    STOP_BUTTON = By.XPATH, "//*[contains(text(),'Stop')]"
    PROGRESS_BAR_PROCESS = By.CLASS_NAME, 'progress-bar.bg-info'

    # for tool tips section
    HOVER_ME_BUTTON = By.ID, 'toolTipButton'
    HOVER_ME_FIELD = By.ID, 'toolTipTextField'
    HOVER_LINK1 = By.XPATH, "//a[contains(text(),'Contrary')]"
    HOVER_LINK2 = By.XPATH, "//a[contains(text(),'1.10.32')]"
    TOOLTIP_TEXT = By.CLASS_NAME, 'tooltip-inner'

    # for menu section
    MAIN_ITEM_2 = By.XPATH, "//a[contains(text(),'Main Item 2')]"
    SUB_SUB_LIST = By.XPATH, "//a[contains(text(),'SUB SUB LIST »')]"
    DROPDOWN_LIST1 = By.XPATH, '//*[@id="nav"]/li[2]'
    DROPDOWN_LIST2 = By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul'






