from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Standups(Base):
    _sign_in_button_locator = (By.CSS_SELECTOR, 'a[href="/accounts/login/"]')
    _sign_in_to_standup_button_locator = (By.CSS_SELECTOR, '.btn.login-button')
    _logout_button_locator = (By.ID, 'logout-link')
    _user_menu_locator = (By.CSS_SELECTOR, '#user-menu img')

    def __init__(self, selenium, url):
        super(Standups, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button_locator).click()
        self.wait_for_element_visible(*self._sign_in_to_standup_button_locator)
        self.selenium.find_element(*self._sign_in_to_standup_button_locator).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def click_logout(self):
        self.selenium.find_element(*self._user_menu_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()
