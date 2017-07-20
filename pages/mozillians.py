from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Mozillians(Base):
    _sign_in_button = (By.ID, 'nav-login')
    _logout_menu_item_locator = (By.ID, 'nav-logout')
    _profile_menu_locator = (By.CSS_SELECTOR, '#nav-main > a.dropdown-toggle')
    _username_locator = (By.CSS_SELECTOR, '.username')
    _dropdown_menu_locator = (By.CSS_SELECTOR, 'ul.dropdown-menu')

    def __init__(self, selenium, url):
        super(Mozillians, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_menu_item_present(self):
        return self.is_element_present(*self._logout_menu_item_locator)

    @property
    def is_username_displayed(self):
        return self.is_element_visible(*self._username_locator)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def click_logout(self):
        self.click_options()
        self.selenium.find_element(*self._logout_menu_item_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_logout_menu_item_present)

    def click_options(self):
        self.selenium.find_element(*self._profile_menu_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.find_element(*self._dropdown_menu_locator))
