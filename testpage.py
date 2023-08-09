from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)



class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

    def get_text(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator[1]
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception("Exception while click")
            return None
        logging.debug(f"Find text '{text}' in {element_name}")
        return text

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator[1]
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {element_name} not found.')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operating with {element_name}")
            return False
        logging.debug(f"Send '{word}' to element {element_name}")
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator[1]
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception while click")
            return False
        logging.debug(f"Click {element_name}")
        return True

    # Enter
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"], word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], word, description="post title form")

    def enter_contact_form_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME_FIELD"], word,
                                   description="name in contact form")

    def enter_contact_form_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_MAIL_FIELD"], word,
                                   description="mail in contact form")

    def enter_contact_form_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                   description="content in contact form")

    # Click
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BUTTON"], description="login button")

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BUTTON"], description="create new post button")

    def click_send_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND_BUTTON"], description="send contact form button")
        time.sleep(testdata["wait"])

    def click_send_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SEND_POST_BUTTON"], description="send post button")
        time.sleep(testdata["wait"])

    def click_contact_form_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_FORM_BUTTON"], description="contact us button")
        time.sleep(testdata["wait"])

    # Get
    def get_error_text(self):
        return self.get_text(TestSearchLocators.ids["LOCATOR_ERROR_HEADER"], description="error field")

    def get_greetings_text(self):
        return self.get_text(TestSearchLocators.ids["LOCATOR_GREETINGS_TEXT"], description="greetings field")

    def get_post_title_text(self):
        return self.get_text(TestSearchLocators.ids["LOCATOR_POST_TITLE"], description="post title field")

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            logging.info(f"Find text '{text}' in alert message")
            return text
        except:
            logging.exception("Exception with alert")
            return None
