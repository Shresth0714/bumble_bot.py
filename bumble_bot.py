from selenium import webdriver
from time import sleep
from pass1 import Username, Password

class Bumble():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://bumble.com')

        #base_window = self.driver.current_url[0]       

        sleep(2)

        log = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        log.click()

        sleep(8)
        #base_window = self.driver.window_handles[0]
        #self.driver.switch_to_window(base_window)

        log_fb = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
        log_fb.click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        sleep(2)

        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(Username)

        sleep(2)

        pass1 = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass1.send_keys(Password)

        logn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        logn.click()

        base_window = self.driver.window_handles[0]

        sleep(5)

        self.driver.switch_to_window(base_window)

        sleep(5)

    def like(self):
        like_bt = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/span/span')
        like_bt.click()
         
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_match()
                except:
                    None

    def close_match(self):
        match_pop = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div/span/span/span')
        match_pop.click()
    
bot = Bumble()
bot.login()
bot.auto_swipe()
