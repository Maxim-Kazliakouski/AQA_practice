import time
import pytest
import logging
import subprocess
import os
from Locators.ElementsPage_locators import ElementPageLocators
from Pages.ElementsPage import ElementsPage
from Tests.tests_ElementsPage.data_ElementsPage import TestDataElementsPage
from Tests.tests_MainPage.data_MainPage import TestDataMainPage
from Tests.tests_MainPage.conftest import browser


@pytest.fixture(scope='function')
def logs_elements_page():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('./logfile.log', mode='a', delay=False)
    # Formatter class to set the format of log file
    formatter = logging.Formatter(
        "[%(asctime)s] -- [%(levelname)s][(See error near the line -> %(lineno)d]--[%(name)s->tests_ElementPage]: \n%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    return logger


@pytest.fixture(scope='function')
def adding_email(browser):
    link = TestDataMainPage.ELEMENTS_PAGE_URL
    page = ElementsPage(browser, link)
    page.open_page(link)
    # adding function for blocking advertisement if it is
    page.removing_advertisement()
    page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
    page.entering_symbols_into_field(ElementPageLocators.EMAIL, TestDataElementsPage.EMAIL_POSITIVE)
    page.scrolling_for_one_screen()
    page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)


@pytest.fixture(scope='function')
def adding_fullname(browser):
    link = TestDataMainPage.ELEMENTS_PAGE_URL
    page = ElementsPage(browser, link)
    page.open_page(link)
    # adding function for blocking advertisement if it is
    page.removing_advertisement()
    page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
    page.entering_symbols_into_field(ElementPageLocators.FULL_NAME_FIELD, TestDataElementsPage.FULL_NAME)
    page.scrolling_for_one_screen()
    page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)


@pytest.fixture(scope='function')
def adding_current_address(browser):
    link = TestDataMainPage.ELEMENTS_PAGE_URL
    page = ElementsPage(browser, link)
    page.open_page(link)
    # adding function for blocking advertisement if it is
    page.removing_advertisement()
    page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
    page.entering_symbols_into_field(ElementPageLocators.CURRENT_ADDRESS, TestDataElementsPage.CURRENT_ADDRESS)
    page.scrolling_for_one_screen()
    page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)


@pytest.fixture(scope='function')
def adding_permanent_address(browser):
    link = TestDataMainPage.ELEMENTS_PAGE_URL
    page = ElementsPage(browser, link)
    page.open_page(link)
    # adding function for blocking advertisement if it is
    page.removing_advertisement()
    page.go_to_section(ElementPageLocators.TEXT_BOX_SECTION)
    page.entering_symbols_into_field(ElementPageLocators.PERMANENT_ADDRESS, TestDataElementsPage.PERMANENT_ADDRESS)
    page.scrolling_for_one_screen()
    page.click_on_element(ElementPageLocators.SUBMIT_BUTTON)


@pytest.fixture(scope='function')
def enable_checkbox_home(browser):
    link = TestDataElementsPage.CHECK_BOX_URL
    page = ElementsPage(browser, link)
    page.open_page(link)
    # adding function for blocking advertisement if it is
    page.removing_advertisement()
    page.click_on_element(ElementPageLocators.HOME_CHECK_BOX)


@pytest.fixture(scope='function')
def removing_file_after_downloading():
    print('Removing files, if they are after previous tests...')
    subprocess.run((['rm', '/Users/max_kazliakouski/Downloads/text.txt']))
    subprocess.run((['rm', '/Users/max_kazliakouski/Downloads/sampleFile.jpeg']))
    yield
    print('\nRemoving permanent files...')
    subprocess.run((['rm', '/Users/max_kazliakouski/Downloads/text.txt']))
    subprocess.run((['rm', '/Users/max_kazliakouski/Downloads/sampleFile.jpeg']))


@pytest.fixture(scope='session')
def clearing_results_folder():
    print('\nClearing results folder...')
    time.sleep(2)
    os.system("rm -rf /Volumes/MacOS/Users/maxkazliakouski/.jenkins/workspace/POM_tests/allure-results/*")
