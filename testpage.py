from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    # — локатор поля ввода логина
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    # — локатор поля ввода пароля
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # — локатор кнопки логина
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")

    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")

    LOCATOR_CONTACT_US_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")



    LOCATOR_NAME_CONTACT = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")

    LOCATOR_EMAIL_CONTACT = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")

    LOCATOR_CONTENT_CONTACT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")

    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")



class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_contact_button(self):
        logging.info(f"Click Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name_contact(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NAME_CONTACT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME_CONTACT)
        login_field.clear()
        login_field.send_keys(word)

    def enter_email_contact(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_EMAIL_CONTACT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_CONTACT)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content_contact(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_CONTACT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT)
        login_field.clear()
        login_field.send_keys(word)

    def get_text_contact_us(self):
        text_contact_us = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_FIELD, time=3)
        text = text_contact_us.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_CONTACT_US_FIELD[1]}")
        return text

    def get_name_cont_text(self):
        name_cont_text = self.find_element(TestSearchLocators.LOCATOR_NAME_CONTACT, time=3)
        text = name_cont_text.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_NAME_CONTACT[1]}")
        return text

    def get_email_cont_text(self):
        email_cont_text = self.find_element(TestSearchLocators.LOCATOR_EMAIL_CONTACT, time=3)
        text = email_cont_text.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_EMAIL_CONTACT[1]}")
        return text

    def get_content_cont_text(self):
        content_cont_text = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT, time=3)
        text = content_cont_text.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_CONTENT_CONTACT[1]}")
        return text

    def click_contact_us_button(self):
        logging.info(f"Click Contact Us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in alert")
        return text