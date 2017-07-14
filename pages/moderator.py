from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base


class Moderator(Base):
    _login_button = (By.CSS_SELECTOR, 'a[class="login btn btn-primary"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href="/oidc/logout/"]')

    def __init__(self, selenium, url):
        super(Moderator, self).__init__(selenium)
        self.go_to_url(url)

    def logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._login_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)

    def enter_passcode(self, secret_seed):
        auth = Auth0(self.selenium)
        auth.enter_passcode(secret_seed)

    def wait_for_passcode_to_change(self, secret_seed, current_passcode):
        auth = Auth0(self.selenium)
        auth.wait_for_passcode_to_change(secret_seed, current_passcode)
