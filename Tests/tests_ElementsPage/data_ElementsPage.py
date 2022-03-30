from Locators.ElementsPage_locators import ElementPageLocators


class TestDataElementsPage:
    # URLs
    TEXT_BOX_URL = 'https://demoqa.com/text-box'
    CHECK_BOX_URL = 'https://demoqa.com/checkbox'
    RADIO_BUTTON_URL = 'https://demoqa.com/radio-button'
    WEB_TABLES_URL = 'https://demoqa.com/webtables'
    BUTTONS_URL = 'https://demoqa.com/buttons'
    LINKS_URL = 'https://demoqa.com/links'
    MAIN_URL = 'https://demoqa.com/'
    UPLOAD_URL = 'https://demoqa.com/upload-download'

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
    CHECKBOX_LIST = ['home', 'desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 'angular', 'veu',
                     'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']
    ENABLE_PLUS_BUTTON = 'rct-icon rct-icon-expand-open'
    ENABLE_MINUS_BUTTON = 'rct-icon rct-icon-expand-close'
    CHECKBOX_LIST_WITHOUT_WORKSPACE_CHECKBOX = ['desktop', 'notes', 'commands', 'office', 'public', 'private',
                                                'classified', 'general', 'downloads', 'wordFile', 'excelFile']

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

    # for links page
    CREATED_URL = 'https://demoqa.com/created'
    NO_CONTENT_URL = 'https://demoqa.com/no-content'
    MOVED_URL = 'https://demoqa.com/moved'
    BAD_REQUEST_URL = 'https://demoqa.com/bad-request'
    UNAUTHORIZED_URL = 'https://demoqa.com/unauthorized'
    FORBIDDEN_URL = 'https://demoqa.com/forbidden'
    INVALID_URL = 'https://demoqa.com/invalid-url'
    REQUESTS = [(CREATED_URL, 201),
                (NO_CONTENT_URL, 204),
                (MOVED_URL, 301),
                (BAD_REQUEST_URL, 400),
                (UNAUTHORIZED_URL, 401),
                (FORBIDDEN_URL, 403),
                (INVALID_URL, 404)
                ]
    REQUESTS_FOR_GETTING_INFO_IDS = ['Created',
                                     'No Content',
                                     'Moved Permanently',
                                     'Bad Request',
                                     'Unauthorized',
                                     'Forbidden',
                                     'Not Found']
    REQUESTS_FOR_GETTING_INFO = [
        (ElementPageLocators.CREATED_LINK, 201, 'Created'),
        (ElementPageLocators.NO_CONTENT_LINK, 204, 'No Content'),
        (ElementPageLocators.MOVED_LINK, 301, 'Moved Permanently'),
        (ElementPageLocators.BAD_REQUEST_LINK, 400, 'Bad Request'),
        (ElementPageLocators.UNAUTHORIZED_LINK, 401, 'Unauthorized'),
        (ElementPageLocators.FORBIDDEN_LINK, 403, 'Forbidden'),
        (ElementPageLocators.INVALID_URL_LINK, 404, 'Not Found')
    ]
    HOME_LINKS_NAMES = ['SIMPLE_LINK', 'DYNAMIC_LINK']

    # for upload and download page
    DOWNLOAD_FILE_NAME = 'sampleFile.jpeg'
    UPLOAD_PATH = "C:\\fakepath\\eng.srt"
