import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture(scope='function')
def logs_main_page():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('./logfile.log', mode='a', delay=False)
    # Formatter class to set the format of log file
    formatter = logging.Formatter(
        "[%(asctime)s] -- [%(levelname)s][%(lineno)d]--[%(name)s->Tests_for_MainPAge]: \n%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    return logger


@pytest.fixture(scope='session')
def clearing_results_folder():
    print('\nClearing results folder...')
    time.sleep(2)
    os.system("rm -rf /Volumes/MacOS/Users/maxkazliakouski/.jenkins/workspace/POM_tests/allure-results/*")


def pytest_addoption(parser):
    parser.addoption('--browser.name', action='store', default='chrome',
                     help="Choose browser: chrome or safari")
    parser.addoption('--headmode', action='store', default='true',
                     help='Choose turn on or turn off headless mode')
    parser.addoption('--test_status', action='store', default=None,
                     help="Adding another test status")


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser.name')
    headless = request.config.getoption('headmode')
    print(f'\nStarting browser {browser_name}...')
    global browser
    # user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # here we set in commandline choosing for headless mode
        if headless == 'true':
            options = webdriver.ChromeOptions()
            # prefs = {"download.default_directory": "/Users/max_kazliakouski/Downloads/"}
            # options.add_experimental_option("prefs", prefs)
            # adding browser options!!! important
            # SETTING FOR ACTIVATING GOOGLE ACCOUNT
            # options.add_argument(
            #     "user-data-dir=/Users/max_kazliakouski/Library/Application Support/Google/Chrome/SeleniumProfile")
            # prefs = {"profile.default_content_setting_values.notifications": 2}
            # options.add_experimental_option("prefs", prefs)
            # options.add_argument("--disable-notifications")
            # options.add_argument('--remote-debugging-port=9222')
            # options.add_argument('--enable-javascript')
            # options.add_argument(
            #     "--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0'")
            # options.add_argument('--ignore-certificate-errors')
            # options.add_argument('--allow-insecure-localhost')
            # options.add_argument(
            #     "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = True
            # params for ordinary jenkins without docker!!!
            s = Service('Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)

            # params for docker
            options = webdriver.ChromeOptions()
            # prefs = {"download.default_directory": "/var/jenkins_home/workspace/all_test_cases/Downloads/"}
            # options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            # s = Service('/usr/local/bin/chromedriver')
            # browser = webdriver.Chrome(service=s, options=options)
            # browser.maximize_window()
            browser.set_window_size(1920, 1080)
            browser.implicitly_wait(5)
        else:
            # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options = webdriver.ChromeOptions()
            # SETTING FOR ACTIVATING GOOGLE ACCOUNT
            # options.add_argument("user-data-dir=/Users/max_kazliakouski/Library/Application Support/Google/Chrome/SeleniumProfile")
            # prefs = {"profile.default_content_setting_values.notifications": 2}
            # options.add_experimental_option("prefs", prefs)
            # options.add_argument(
                # "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = False
            # options.add_argument(
            #     "user-data-dir=/Users/max_kazliakouski/Library/Application Support/Google/Chrome/SeleniumProfile")
            # options.add_argument("--disable-notifications")
            s = Service('Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'mozila':
        if headless == 'true':
            options = webdriver.FirefoxOptions()
            options.headless = True
            s = Service('Tools/geckodriver')
            browser = webdriver.Firefox(service=s, options=options)
            # params for docker
            options = webdriver.FirefoxOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            options = webdriver.FirefoxOptions()
            options.headless = False
            s = Service('Tools/geckodriver')
            browser = webdriver.Firefox(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'opera':
        if headless == 'true':
            # options = webdriver.Opera
            # options.headless = True
            # s = Service('Tools/operadriver')
            browser = webdriver.Opera(executable_path='Tools/operadriver')
            # params for docker
            options = webdriver.Opera()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            options = webdriver.ChromeOptions()
            options.headless = False
            # s = Service('Tools/operadriver')
            # webdriver_service = service.Service('Tools/operadriver')
            # webdriver_service.start()
            # browser = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
            browser = webdriver.Chrome(executable_path='Tools/operadriver', options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'safari':
        s = Service('Tools/safaridriver')
        browser = webdriver.Safari(service=s)
        browser.maximize_window()
        browser.implicitly_wait(5)
        print(f'Start {browser_name} browser for test...')
    else:
        print(f'Browser {browser_name} still not implemented')

    yield browser
    print(f'\nQuit browser {browser_name}...')
    # browser quit don't fit for safari, get the error about refuse connection
    browser.quit()

    # return os.system('allure serve results')

# def parser(section, value):
#     config = ConfigParser()
#     config.read('/Volumes/Work/Parse_project/data_for_test/test_data_hw21.ini')
#     value = config.get(section, value)
#     return value


@pytest.fixture(scope='function')
def browser_xfail(request):
    browser_name = request.config.getoption('browser.name')
    # headless = request.config.getoption('headmode')
    print(f'\nStarting browser {browser_name}...')
    global browser
    headless = 'false'
    # user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # here we set in commandline choosing for headless mode
        if headless == 'true':
            # options = webdriver.ChromeOptions()
            # example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
            # options.add_experimental_option("prefs", prefs)
            # adding browser options!!! important
            # options.add_argument(
            #     "user-data-dir=/Users/max_kazliakouski/Library/Application Support/Google/Chrome/Default")
            # prefs = {"profile.default_content_setting_values.notifications": 2}
            # options.add_experimental_option("prefs", prefs)
            # options.add_argument("--disable-notifications")
            # options.add_argument(
            #     "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            # options.headless = True
            # s = Service('Tools/chromedriver')
            # browser = webdriver.Chrome(service=s, options=options)
            # params for docker
            options = webdriver.ChromeOptions()
            options.headless = True
            prefs = {"download.default_directory": "/var/jenkins_home/workspace/all_test_cases/Downloads/"}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            s = Service('/usr/local/bin/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            # options = webdriver.ChromeOptions()
            # options.add_argument(
            #     "user-data-dir=/Users/max_kazliakouski/Library/Application Support/Google/Chrome/SeleniumProfile")
            # prefs = {"profile.default_content_setting_values.notifications": 2}
            # options.add_experimental_option("prefs", prefs)
            # options.add_argument(
            # "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            # s = Service('Tools/chromedriver')
            # browser = webdriver.Chrome(service=s, options=options)
            options = webdriver.ChromeOptions()
            options.headless = False
            prefs = {"download.default_directory": "/var/jenkins_home/workspace/all_test_cases/Downloads/"}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            s = Service('/usr/local/bin/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'mozila':
        if headless == 'true':
            options = webdriver.FirefoxOptions()
            options.headless = True
            s = Service('Tools/geckodriver')
            browser = webdriver.Firefox(service=s, options=options)
            # params for docker
            options = webdriver.FirefoxOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            options = webdriver.FirefoxOptions()
            options.headless = False
            s = Service('Tools/geckodriver')
            browser = webdriver.Firefox(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'opera':
        if headless == 'true':
            options = webdriver.Opera
            options.headless = True
            browser = webdriver.Opera(executable_path='Tools/operadriver')
            # params for docker
            # options = webdriver.Opera()
            # options.add_argument('--no-sandbox')
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            options = webdriver.Opera()
            options.headless = False
            browser = webdriver.Opera(executable_path='Tools/operadriver')
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'safari':
        s = Service('Tools/safaridriver')
        browser = webdriver.Safari(service=s)
        browser.maximize_window()
        browser.implicitly_wait(5)
        print(f'Start {browser_name} browser for test...')
    else:
        print(f'Browser {browser_name} still not implemented')

    yield browser
    print(f'\nQuit browser {browser_name}...')
    # browser quit don't fit for safari, get the error about refuse connection
    browser.quit()