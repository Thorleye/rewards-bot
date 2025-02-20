from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

actions = ActionChains(driver)

def control_click(element):
    actions.key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()

driver.get('https://bing.com')
driver.get('https://bing.com')
time.sleep(3)
     
driver.find_element(By.CLASS_NAME, 'points-container').click()

    # iframe web element
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="rewid-f"]/iframe')))
time.sleep(1)
    # buttons
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1
        
for box in driver.find_elements(By.CLASS_NAME, "promo_cont"):
    try:
    #print(box)
        actions.key_down(Keys.CONTROL).click(box).key_up(Keys.CONTROL).perform()
        time.sleep(1.5)
    except:
        pass

driver.close()

