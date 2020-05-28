import time

from Allrepo import properties
from Allrepo import Locaters
class Logout(object):
    def __init__(self, driver):
     self.driver = driver
    def logout(self):
          self.driver.switch_to_default_content()
          self.driver.switch_to_frame(Locaters.frame1)
          signout=self.driver.find_element_by_partial_link_text(Locaters.Logout_button)
          if signout.is_displayed()==True:
              signout.click()
              time.sleep(3)
              print("Logged out of the application")
              return True
          else:
              print("unable to find the logout element")

