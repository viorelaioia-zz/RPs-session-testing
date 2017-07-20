from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Moderator(Base):
    _login_button = (By.CSS_SELECTOR, 'a[class="login btn btn-primary"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href="/oidc/logout/"]')

    def __init__(self, selenium, url):
        super(Moderator, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._login_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)
