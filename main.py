from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time


for i in range(60):
    driver = webdriver.Chrome(executable_path = './Driver/chromedriver.exe')
    driver.get("{{ url }}")
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/button').send_keys(Keys.ENTER)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[5]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/rating-question/div/div/div/div/div/div[3]/div/div/span[1]/span"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/nav/div/div/div/div[1]/div/button[1]"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[4]/nav/div/div/div/div[1]/div/button[1]"))).click()
    time.sleep(2)
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[5]/div/span"))).click()
    time.sleep(2)
    driver.close()
