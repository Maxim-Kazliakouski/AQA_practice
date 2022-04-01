from Locators.ToolsQaMainPage_locators import ToolsQaMainPageLocators


class TestDataToolsQaMainPage:

    TOOLS_QA_MAIN_PAGE_URL = 'https://www.toolsqa.com/'
    SELENIUM_TRAINING_URL = 'https://www.toolsqa.com/selenium-training/'
    SELENIUM_TRAINING_TAB_URL = 'https://www.toolsqa.com/selenium-training?q=headers'
    DEMO_SITE_URL = 'https://demoqa.com/'
    # the tabs list
    TABS_LIST = ['HOME', 'SELENIUM TRAINING', 'DEMO SITE', 'ABOUT']
    # tutorial menu list
    TUTORIAL_MENU_LIST = ['QA Practices',
                          'Front-End Testing Automation',
                          'Back-End Testing Automation',
                          'Mobile Testing Automation',
                          'Frameworks & Libraries',
                          'DevOps Tools',
                          'Cross Browser Testing',
                          'Non-Functional Testing',
                          'Programming Language']
    # tutorial sections:
    content = ToolsQaMainPageLocators.LIST_OF_SECTION_CONTENT
    QA_PRACTICES = ['ISTQB Preparation', 'Software Testing', 'Agile & Scrum']
    FE_TEST_AUTOMATION = ['Cypress', 'Protractor', 'Selenium in Java', 'TestProject', 'Katalon Studio', 'Selenium C Sharp']
    BE_TEST_AUTOMATION = ['Rest Assured', 'Postman', 'SOAPUI']
    MOBILE_TEST_AUTOMATION = ['Appium Studio']
    FRAMEWORKS_LIB = ['Cucumber', 'TestNG', 'SpecFlow', 'Junit', 'Extent report - Cucumber (TestNG)']
    DEVOPS_TOOLS = ['Maven', 'Git', 'Docker']
    CROSS_BROWSER_TEST = ['LambdaTest', 'Cross Browser Testing - Smartbear', 'Browserling']
    NON_FUNC_TESTING = ['JMeter']
    PROGRAM_LANG = ['Java', 'Data Structures', 'Python', 'JavaScript']
    # for parametrize test for tutorial section
    CONTENT_BY_SECTIONS = [(TUTORIAL_MENU_LIST[0], content, QA_PRACTICES),
                           (TUTORIAL_MENU_LIST[1], content, FE_TEST_AUTOMATION),
                           (TUTORIAL_MENU_LIST[2], content, BE_TEST_AUTOMATION),
                           (TUTORIAL_MENU_LIST[3], content, MOBILE_TEST_AUTOMATION),
                           (TUTORIAL_MENU_LIST[4], content, FRAMEWORKS_LIB),
                           (TUTORIAL_MENU_LIST[5], content, DEVOPS_TOOLS),
                           (TUTORIAL_MENU_LIST[6], content, CROSS_BROWSER_TEST),
                           (TUTORIAL_MENU_LIST[7], content, NON_FUNC_TESTING),
                           (TUTORIAL_MENU_LIST[8], content, PROGRAM_LANG)]







