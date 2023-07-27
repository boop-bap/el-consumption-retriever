from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from threading import Timer
from selenium.common.exceptions import NoSuchElementException

import time


browser = webdriver.Chrome()


browser.get(('https://mano.eso.lt/'))

usernameField = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, "edit-name")))
passwordField = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'edit-pass')))
nextButton = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'edit-submit')))
acceptCookiesButton = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyButtonDecline')))


usernameField.send_keys(usernameStr)
passwordField.send_keys(passwordStr)

if acceptCookiesButton:
    acceptCookiesButton.click()

nextButton.click()


# Download
browser.get(('https://mano.eso.lt/consumption/history'))

def selectFrequencyAndDownload():
    dropdownForDataFrequency = Select(WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.NAME, 'display_type'))))
    dropdownForDataFrequency.select_by_index(2)

    formatBtn.click()

    checkIfDownloadAvailableBtn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Atnaujinti'][contains(@style, 'display: none')]")))
    # downloadBtn = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Atsisiųsti')]")))
    print(checkIfDownloadAvailableBtn)



    #  .until(expected_conditions.presence_of_element_located(
    # (By.XPATH, "//*[@id='inf-loader']/span[1][contains(@style, 'display: inline-block')]")))

    while not checkIfDownloadAvailableBtn:
        try:
            print(not checkIfDownloadAvailableBtn)
            checkIfDownloadAvailableBtn.click()
            time.sleep(5)
        except:
            print(not checkIfDownloadAvailableBtn)
            print(123123,"lalalal")
            time.sleep(5)

    # downloadBtn.click()
    # CheckIfDownloadAvailable.click()
    # edit-submit

dropdownForPeriod = Select(browser.find_element("xpath", "//select[@id='edit-period']"))
dropdownForProperty =  Select(browser.find_element("xpath", "//select[@id='edit-objects']"))
formatBtn = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='edit-submit']")))


dropdownForPeriod.select_by_index(4)
dropdownForProperty.select_by_index(1)


delayForFrequencySelectAndDownload = Timer(2.0, selectFrequencyAndDownload)
delayForFrequencySelectAndDownload.start()




while(True):
    pass