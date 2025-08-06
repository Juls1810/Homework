from selenium import webdriver
from mainpageCalc import MainPage


def test_calc():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.calc_waits(45)
    main_page.output_value()
    main_page.waiter()
    main_page.close_driver()
