import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class Base(object):

    def __init__(self, selenium):
        self.selenium = selenium
        self.timeout = 60

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def wait_for_element_visible(self, *locator):
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception(':'.join(locator) + " is not visible")

    def refresh_page(self):
        self.selenium.refresh()

    def go_to_url(self, url):
        self.selenium.get(url)
