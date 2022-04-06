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
    # categories on main page
    CATEGORIES = ['Test Project', 'Katalon', 'ISTQB', 'Scrum', 'Git', 'Protractor', 'Selenium', 'Rest Assured', 'Postman', 'Cucumber']
    TEST_PROJECT_TEXT = 'TestProject Tutorial'
    KATALON_TEXT = 'Katalon Studio Tutorial'
    ISTQB_TEXT = 'ISTQB Foundation Level Syllabus 2018'
    SCRUM_TEXT = 'Agile & Scrum Tutorial'
    GIT_TEXT = 'Git Tutorial'
    PROTRACTOR_TEXT = 'Protractor Tutorial'
    SELENIUM_TEXT = 'Selenium Tutorial'
    REST_ASSURED_TEXT = 'Rest Assured Tutorial'
    POSTMAN_TEXT = 'Postman Tutorial'
    CUCUMBER_TEXT = 'Cucumber Tutorial'
    # ALL_CATEGORIES_FOR_PARAMETRIZE = [(CATEGORIES[0], TEST_PROJECT_TEXT),
    #                                   (CATEGORIES[1], KATALON_TEXT),
    #                                   (CATEGORIES[2], ISTQB_TEXT),
    #                                   (CATEGORIES[3], SCRUM_TEXT),
    #                                   (CATEGORIES[4], GIT_TEXT),
    #                                   (CATEGORIES[5], PROTRACTOR_TEXT),
    #                                   (CATEGORIES[6], SELENIUM_TEXT),
    #                                   (CATEGORIES[7], REST_ASSURED_TEXT),
    #                                   (CATEGORIES[8], POSTMAN_TEXT),
    #                                   (CATEGORIES[9], CUCUMBER_TEXT)
    #                                   ]
    ALL_CATEGORIES_FOR_PARAMETRIZE = [(1, TEST_PROJECT_TEXT),
                                      (2, KATALON_TEXT),
                                      (3, ISTQB_TEXT),
                                      (4, SCRUM_TEXT),
                                      (5, GIT_TEXT),
                                      (6, PROTRACTOR_TEXT),
                                      (7, SELENIUM_TEXT),
                                      (8, REST_ASSURED_TEXT),
                                      (9, POSTMAN_TEXT),
                                      (10, CUCUMBER_TEXT)
                                      ]






