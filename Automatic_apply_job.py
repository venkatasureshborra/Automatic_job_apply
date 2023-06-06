from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



########  Note :  for every refresh this id are change it will only applied for the particular job       ############


driver_path=Service("D:/Selenium_for_chrome/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3574147931&f_AL=true&f_E=2&f_JT=F&f_TPR=r604800&keywords=python&refresh=true")
driver.find_element(By.LINK_TEXT,"Sign in").click()
time.sleep(5)
username=driver.find_element(By.NAME,"session_key").send_keys("YOUR-USERNAME")
password=driver.find_element(By.NAME,"session_password").send_keys("YOUR-PASSWORD",Keys.ENTER)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card span').click()
time.sleep(10)
next=driver.find_element(By.CLASS_NAME,'artdeco-button--primary')
next.click()
time.sleep(5)
next.click()
time.sleep(5)

yes=driver.find_element(By.XPATH,'//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3574147931-87654485-multipleChoice"]/div[1]/label')
yes.click()
driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3574147931-87654493-numeric"]').send_keys(f"{0}")
next.click()
time.sleep(3)
immediate_work=driver.find_element(By.XPATH,'//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3574147931-87654477-multipleChoice"]/div[1]/label').click()
next.click()
time.sleep(2)
next.click()
time.sleep(50)
driver.quit()


