from selenium import webdriver
from time import sleep
from secrets import email
from secrets import pw

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        #Go to site
        self.driver.get('https://tinder.com')
        sleep(2)

        #Click login button
        login_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button")
        login_btn.click()
        sleep(2)

        #Log in with FB
        fb_btn = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
        fb_btn.click()
        sleep(3)
        
        #Switch to pop-up window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        #Enter email
        self.driver.find_element_by_xpath('//*[@id="email"]')\
            .send_keys(email)
        
        #Enter password
        self.driver.find_element_by_xpath('//*[@id="pass"]')\
            .send_keys(pw)
        
        #click login button
        login_btn = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]")
        login_btn.click()

        sleep(2)
        self.driver.switch_to_window(base_window)
        sleep(2)

        popup1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup1.click()
        sleep(1)
        
        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()
        sleep(1)
        
    
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        #/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button
        #//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button

        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        #//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        try:
                            self.close_gold()
                        except Exception:
                            self.close_super()

    def close_gold(self):
        goldpop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
        goldpop.click()

    def close_super(self):
        superpop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
        superpop.click()

    def close_popup(self):
        popup3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        #//*[@id="modal-manager"]/div/div/div[2]/button[2]
        #//*[@id="modal-manager"]/div/div/div/div[3]/button[2]

        #/html/body/div[2]/div/div/button[2]
        #//*[@id="modal-manager"]/div/div/button[2]
        popup3.click()

        #//*[@id="modal-manager"]/div/div/button[2]

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('')
        match_popup.click()
    
    
        
bot = TinderBot()
print("Initializing...")
bot.login()
print("Logged in...")
print("Commence swiping...")
sleep(4)
bot.auto_swipe()
