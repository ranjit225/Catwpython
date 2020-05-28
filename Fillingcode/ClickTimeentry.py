import time

from Allrepo import Locaters


class clickTimeEntry(object):
    def __init__(self,driver):
        self.driver= driver
    def element_to_clicktimeentery(self):
        self.driver.switch_to_frame(Locaters.Frame2)
        timeentrylimk= self.driver.find_element_by_partial_link_text(Locaters.Time_Entry_link)
        if timeentrylimk.is_displayed() == True:
            timeentrylimk.click()
            print("time entry link has been cliecked")
            return True
        else:
            print("clicking on time entry link has been failed")
            return False

    def click_continuebutton(self):
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(Locaters.Frame3)
        time.sleep(3)
        continuebutton = self.driver.find_element_by_xpath(Locaters.Continue_Button_insideframe)
        if continuebutton.is_displayed() == True:
            continuebutton.click()
            print("click on continue button")
            return True
        else:
            print("clicking on continue is failed")
            return False






