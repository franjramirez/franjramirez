from selenium import webdriver
import time


def readScreens():
    response = "ggggg"
    driver = webdriver.Chrome(r".driver/chromedriver")
    driver.get("https://www.nytimes.com/games/wordle/index.html")
    driver.execute_script("window.open('https://www.nytimes.com/games/wordle/index.html', 'new_window')")
    driver.maximize_window()
    time.sleep(5)
    element = driver.find_element_by_class_name("close-icon")
    element.click()
    element = driver.find_element_by_name("q")
    
    return response

