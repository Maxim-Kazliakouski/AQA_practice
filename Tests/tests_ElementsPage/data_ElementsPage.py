class TestDataElementsPage:
    # URLs
    TEXT_BOX_URL = 'https://demoqa.com/text-box'
    CHECK_BOX_URL = 'https://demoqa.com/checkbox'
    RADIO_BUTTON_URL = 'https://demoqa.com/radio-button'
    WEB_TABLES_URL = 'https://demoqa.com/webtables'
    BUTTONS_URL = 'https://demoqa.com/buttons'
    LINKS_URL = 'https://demoqa.com/links'
    MAIN_URL = 'https://demoqa.com/'

    # for text box section
    FULL_NAME = ['ABCDEFGHIJKLMNOPQRSTUVWZYZ',
                 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'.lower(),
                 '1234567890',
                 '!@#$%^&*()_+-{}"|:"±§`,.<>?']

    EMAIL_POSITIVE = ['user@mail.com',
                      '1.23@m_ail.com',
                      '1_23@mail.com',
                      '1_23@ma.il.com',
                      '123@m_ail.com'
                      ]
    EMAIL_NEGATIVE = ['@mail.com',
                      '123mail.com',
                      '123@.com',
                      '123@mail.c',
                      '123@mail',
                      '12 3@mail.com',
                      '123@',
                      ]
    CURRENT_ADDRESS = 'c.Minsk, str.Gaja 100, 24'
    PERMANENT_ADDRESS = 'c.Moscow, str.Parkovaya 50, 40'

    # for check box section
    ENABLE_CHECKBOX_HOME = 'rct-icon rct-icon-check'
    CHECKBOX_LIST = ['home', 'desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 'angular', 'veu', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']
    ENABLE_PLUS_BUTTON = 'rct-icon rct-icon-expand-open'
    ENABLE_MINUS_BUTTON = 'rct-icon rct-icon-expand-close'
    CHECKBOX_LIST_WITHOUT_WORKSPACE_CHECKBOX = ['desktop', 'notes', 'commands', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']

    # for web tables
    # data for creating new record
    FIRST_NAME = 'Max'
    LAST_NAME = 'Kazliakouski'
    EMAIL = '123@mail.com'
    AGE = 30
    SALARY = 2000
    DEPARTMENT = 'IT'

    # for buttons page
    MESSAGE_AFTER_DOUBLE_CLICKING = 'You have done a double click'
    MESSAGE_AFTER_RIGHT_CLICKING = 'You have done a right click'
    MESSAGE_AFTER_CLICK_BUTTON = 'You have done a dynamic click'








