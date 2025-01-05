from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Rewards(webdriver.Edge):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Rewards, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_traceb): #needs 4 args or will throw error
        if self.teardown:
            self.quit()
    
    def landing_page(self):
        self.get("https://rewards.bing.com")
    
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