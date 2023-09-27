import time
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logging.basicConfig(filename='exam_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_exam_monitoring(exam_url):

    driver = webdriver.Chrome() 
    driver.get(exam_url)

    while True:

        num_windows = len(driver.window_handles)

        if num_windows > 1:

            logging.info(f"Attempt to open a new tab/window detected at {driver.current_url}")
            
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            print("Attempt to open a new tab/window detected and reported to proctor")

        time.sleep(3)  

    driver.quit()

if __name__ == "__main__":
    exam_url = "https://www.youtube.com/channel/UC5yGWW1UOXBYkn2-DCI_g5g"  #exam URL
    start_exam_monitoring(exam_url)