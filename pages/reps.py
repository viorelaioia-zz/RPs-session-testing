from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Reps(Base):
    _sign_in_button = (By.CSS_SELECTOR, '#login-menu-locator a')
    _logout_button_locator = (By.CSS_SELECTOR, '#logout-menu-locator a[href="/oidc/logout/"]')

    def __init__(self, selenium, url):
        super(Reps, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()
