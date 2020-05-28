from selenium import webdriver
import unittest

class Envirnomentsetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.driver=webdriver.Chrome(r"C:\Users\rnarravula\PycharmProjects\Catwautomation\Drivers\chromedriver.exe")
       cls.driver.get("https://z4u0095.houston.dxccorp.net:4106/hps-ic-red(bD1lbiZjPTgwMCZ0PVpIUFNfSUM=)/default.htm")
       cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()




path=r"C:\Users\rnarravula\PycharmProjects\Catwautomation\TestData\excel.xlsx"
path2=r"C:\Users\rnarravula\PycharmProjects\Catwautomation\TestData\Book12.xlsx"

