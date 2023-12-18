from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# Note, Instagram will update it's website. So the CSS Selectors and XPATH may change. #

SIMILAR_ACCOUNT= 'nasa'  # Change this to an account of your choice
USERNAME= '' # Your UserName
PASSWORD= '' # Your Password


class InstaFollower:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3.2)
        # LOGIN
        email=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        email.send_keys(USERNAME)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(1.8)
        password.send_keys(Keys.ENTER)
        time.sleep(4.3)
        # Click "Save info" to Save-login info prompt
        save_login_prompt = self.driver.find_element(By.XPATH,"//button[text()='Save info']")
        if save_login_prompt:
            save_login_prompt.click()
            

        time.sleep(3.7)
        # Dismiss notifications popup
        # turn_off_notifications = self.driver.find_element(By.XPATH,'/html/body')
        # turn_off_notifications.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
        self.driver.find_element(By.XPATH,"//button[text()='Not Now']").click()
    
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(7.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            # using Javascript to - scroll the top of the modal (popup) element by the height of the modal (popup)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[text()='Cancel']")
                cancel_button.click()
      
