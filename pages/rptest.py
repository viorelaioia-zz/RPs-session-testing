from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base


class RpTest(Base):
    _sign_in_button = (By.CSS_SELECTOR, '.btn-signin.btn-signin-charcoal')

    _logout_button_locator = (By.CSS_SELECTOR, '#main-content a[href="/logout"]')

    def __init__(self, selenium, url):
        super(RpTest, self).__init__(selenium)
        self.go_to_url(url)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)

    def enter_passcode(self, secret_seed):
        auth = Auth0(self.selenium)
        auth.enter_passcode(secret_seed)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

    def passcode(self, secret_seed):
        auth = Auth0(self.selenium)
        return auth.passcode(secret_seed)
