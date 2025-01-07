from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Rewards(webdriver.Edge):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Rewards, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_traceb): #needs 4 args or will throw error
        if self.teardown:
            self.quit()
    
    def rewards_page(self):
        self.get("https://rewards.bing.com")

    def search_page(self):
        self.get('https://bing.com')
    
    def daily_boxes(self):
        daily1 = self.find_element(By.XPATH, '//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[1]')
        daily2 = self.find_element(By.XPATH, '//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[2]')
        daily3 = self.find_element(By.XPATH, '//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[3]')
    
        all_daily = [daily1, daily2, daily3]
        wait = WebDriverWait(self, 10)
        original_window = self.current_window_handle
        assert len(self.window_handles) == 1
        
        for element in all_daily:
            element.click()
            wait.until(EC.number_of_windows_to_be(2))

            for window_handle in self.window_handles:
                if window_handle != original_window:
                    self.switch_to.window(window_handle)
                    break
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "points-container")))
            finally:
                self.close()

        #Switch back to the old tab or window
            self.switch_to.window(original_window)

    def searches(self):
        from auto.phrases import top_search_terms as terms
        wait = WebDriverWait(self, 10)
        self.get("https://bing.com")
        #search_button = self.find_element(By.ID, "search_icon")
        #self.switch_to.alert.close()

        for term in terms:
            search_bar = self.find_element(By.ID, "sb_form_q")
            search_bar.clear()
            search_bar.send_keys(term)
            search_bar.submit()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,"points-container")))
            wait.until(EC.presence_of_element_located((By.ID, "sb_form_q")))
            #time.sleep(2)
        self.close()

    def activate(self):
        self.get("https://rewards.bing.com")
        wait = WebDriverWait(self, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"c-card-content")))
        #self.find_element(By.CLASS_NAME, "points-container").click()
        #wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promo_cont")))
        boxes = self.find_elements(By.CLASS_NAME, "rewards-card-container")
        #original_window = self.current_window_handle
        print(boxes)
        for box in boxes:
            try:
                box.click()
            except:
                pass
        self.close()

    def alert_handle(self):
        try:
            WebDriverWait(timeout=2).until(EC.alert_is_present())
            self.switch_to().alert().dismiss()
        except:
            pass



