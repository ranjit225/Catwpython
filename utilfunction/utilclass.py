
class functionutil(object):
    def __init__(self,driver):
        self.driver=driver
    def ScreenShot(self,path):
        directory="C:/Users/rnarravula/PycharmProjects/Catwautomation/Screenshots"
        self.driver.get_screenshot_as_file(directory+path)
