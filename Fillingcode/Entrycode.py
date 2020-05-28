import time

from selenium.webdriver.support.select import Select

from Allrepo import Locaters

class Selcectdropdown(object):
    def __init__(self,driver):
        self.driver = driver
    def selct_dropdown(self):
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(Locaters.Frame3)
        dropdown=Select(self.driver.find_element_by_name(Locaters.Dropdown_code))
        value=dropdown.select_by_value("775")


