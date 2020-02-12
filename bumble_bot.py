from selenium import webdriver
from time import sleep
from pass1 import Username, Password

#creating a new class
class Bumble():
    def __init__(self):  #initializing Google chrome browser
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://bumble.com') #opening the website    

        sleep(2)

        log = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        log.click() #locating the login icon and clicking on it

        sleep(8)

        log_fb = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
        log_fb.click() #locating the facebook login option and clicking on it

        self.driver.switch_to.window(self.driver.window_handles[1]) #move sceen to the fb login popup

        sleep(2)

        email = self.driver.find_element_by_xpath('//*[@id="email"]') 
        email.send_keys(Username) #passing the username

        sleep(2)

        pass1 = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass1.send_keys(Password) #passing the password

        logn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        logn.click() #clicking on the login option

        base_window = self.driver.window_handles[0]  #switching the handles

        sleep(5)

        self.driver.switch_to_window(base_window)  #switching back to the base window

        sleep(5)

    def like(self):  #creating like finctionality
        like_bt = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/span/span')
        like_bt.click()
         
    def auto_swipe(self):  #creating an auto swipe loop for automating like option
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_match()
                except:
                    None

    def close_match(self):   #handeling match exceptions
        match_pop = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div/span/span/span')
        match_pop.click()
    
bot = Bumble()
bot.login()
bot.auto_swipe()
