from testpage import OperationsHelper
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    assert test_page.get_greetings_text() == f'Hello, {testdata["login"]}'


def test_step3(browser):
    logging.info("Test3 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.click_new_post_button()
    test_page.enter_title("TestTitle123")
    test_page.click_send_post_button()
    assert test_page.get_post_title_text() == "TestTitle123"


def test_step4(browser):
    logging.info("Test4 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.click_contact_form_button()
    test_page.enter_contact_form_name("TestName")
    test_page.enter_contact_form_mail("Test@mail.ru")
    test_page.enter_contact_form_content("Testing content.")
    test_page.click_send_contact_button()
    assert test_page.get_alert_text() == "Form successfully submitted"
