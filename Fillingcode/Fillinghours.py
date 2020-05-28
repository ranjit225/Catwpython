import time

from selenium.webdriver import ActionChains

import Allfunction
from Allrepo import properties
from Allrepo.properties import driver



class fillinghrs:
    # def fillhrs(self, ):
    #     element=0
    #     list=driver.find_elements_by_xpath("//td[@style='text-align:center;']")
    #     value=len(list)
    #     text=driver.find_element_by_xpath("//td/div[@class='urTrcTitHdr' and text()='CATW - Time Entry']").is_displayed()
    #     try:
    #         if text==True:
    #             for enter in value:
    #                 if enter>= len(list)-2:

    def fillinghrss(self):
        rows = Allfunction.contriws(properties.path, "hrs")
        hours = Allfunction.UNPWD(properties.path, "hrs", rows, 1)
        elements=len(driver.find_elements_by_xpath("//td[@style='text-align:center;']"))
        print(elements)
        time.sleep(3)
        for r in range(1,elements):
            value=driver.find_element_by_xpath("//td[@style='text-align:center;']["+str(r)+"]").text
            print(value)
















