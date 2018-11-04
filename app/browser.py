from selenium import webdriver
import os

def getBrowser():
    temp = os.getcwd()
    # os.chdir(temp+'\\app')
    os.chdir('app')
    # print(os.getcwd())
    browser = webdriver.Chrome()
    os.chdir(temp)
    return browser

if __name__ == "__main__":
    getBrowser()