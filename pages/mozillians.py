from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.auth0 import Auth0
from pages.base import Base


class Mozillians(Base):
    _sign_in_button = (By.ID, 'nav-login')
    _logout_menu_item_locator = (By.ID, 'nav-logout')
    _profile_menu_locator = (By.CSS_SELECTOR, '#nav-main > a.dropdown-toggle')
    _dropdown_menu_locator = (By.CSS_SELECTOR, 'ul.dropdown-menu')

    def __init__(self, selenium, url):
        Base.__init__(self, selenium)
        self.go_to_url(url)

    @property
    def is_logout_menu_item_present(self):
        return self.is_element_present(*self._logout_menu_item_locator)

    def login_with_ldap(self, email, password, passcode):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, passcode)

    def click_logout(self):
        self.click_options()
        self.selenium.find_element(*self._logout_menu_item_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_logout_menu_item_present)

    def click_options(self):
        self.selenium.find_element(*self._profile_menu_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.find_element(*self._dropdown_menu_locator))
