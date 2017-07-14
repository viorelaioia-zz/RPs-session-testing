from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import Base
from tests import conftest


class Auth0(Base):
    _login_with_ldap_button_locator = (By.CSS_SELECTOR, '.auth0-lock-ldap-button.auth0-lock-ldap-big-button')
    _ldap_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-email .auth0-lock-input')
    _ldap_password_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-password .auth0-lock-input')
    _login_button_locator = (By.CSS_SELECTOR, '.auth0-lock-submit')
    _ldap_only_username_locator = (By.CSS_SELECTOR, 'div[class*="auth0-lock-input-username"] input')
    _ldap_only_password_locator = (By.CSS_SELECTOR, 'div[class*="auth0-lock-input-password"] input')

    _enter_passcode_button = (By.CSS_SELECTOR, '.passcode-label .positive.auth-button')
    _passcode_field_locator = (By.CSS_SELECTOR, '.passcode-label input[name="passcode"]')
    _duo_iframe_locator = (By.ID, 'duo_iframe')

    def login_with_ldap(self, email, password, ldap_only=False):
        if ldap_only:
            self.wait_for_element_visible(*self._ldap_only_username_locator)
            self.selenium.find_element(*self._ldap_only_username_locator).send_keys(email)
            self.selenium.find_element(*self._ldap_only_password_locator).send_keys(password)
        else:
            self.wait_for_element_visible(*self._login_with_ldap_button_locator)
            self.selenium.find_element(*self._login_with_ldap_button_locator).click()
            self.selenium.find_element(*self._ldap_email_field_locator).send_keys(email)
            self.selenium.find_element(*self._ldap_password_field_locator).send_keys(password)
        self.selenium.find_element(*self._login_button_locator).click()

    def enter_passcode(self, passcode):
        self.selenium.switch_to_frame('duo_iframe')
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.find_element(*self._passcode_field_locator).send_keys(passcode)
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.switch_to_default_content()

    def wait_for_passcode_to_change(self, secret_seed, current_passcode):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: conftest.passcode(secret_seed) != current_passcode)
