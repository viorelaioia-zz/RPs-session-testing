from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base


class Reps(Base):
    _sign_in_button = (By.CSS_SELECTOR, '#login-menu-locator a')
    _logout_button_locator = (By.CSS_SELECTOR, '#logout-menu-locator a[href="/oidc/logout/"]')

    def __init__(self, selenium, url):
        super(Reps, self).__init__(selenium)
        self.go_to_url(url)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

    def enter_passcode(self, secret_seed):
        auth = Auth0(self.selenium)
        auth.enter_passcode(secret_seed)

    def wait_for_passcode_to_change(self, secret_seed, current_passcode):
        auth = Auth0(self.selenium)
        auth.wait_for_passcode_to_change(secret_seed, current_passcode)
