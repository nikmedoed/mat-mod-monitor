from selenium import webdriver
import os

def getBrowser():
    temp = os.getcwd()
    os.chdir('app')
    browser = webdriver.Chrome()
    os.chdir(temp)
    return browser

if __name__ == "__main__":
    getBrowser()