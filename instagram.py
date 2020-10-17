from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from instagramUserInfo import email,password

class Instagram:

    def __init__(self,mail,parola):
        self.driverProfile=webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option('prefs',{'intl.accept_languages': 'en,en_US'})
        self.mail=mail
        self.parola=parola
        self.driver=webdriver.Chrome(chrome_options=self.driverProfile)
    def login(self):
        self.driver.maximize_window()

        self.driver.get("https://www.instagram.com/accounts/login")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.mail)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.parola)

        time.sleep(2)

        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
    def getFollowers(self):
        try:
            self.login()
        except:
            print("Login Fail")
        
        time.sleep(4)

        profile_photo_sign=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        ActionChains(self.driver).move_to_element(profile_photo_sign).click(profile_photo_sign).perform() 

        profile_link=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]")

        ActionChains(self.driver).move_to_element(profile_link).click(profile_link).perform()
        time.sleep(3)
        self.driver.maximize_window()
        followers=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        ActionChains(self.driver).move_to_element(followers).click(followers).perform()
        time.sleep(3)
        dialog=self.driver.find_element_by_css_selector("._1XyCr")

        followerCount=len(dialog.find_elements_by_tag_name('li'))

        action=ActionChains(self.driver)
        print("Processing...")
        while True:
            dialog.click()

            for _ in range(10):
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(1)

            newCount=len(dialog.find_elements_by_tag_name('li'))

            if newCount==followerCount:
                break
            else:
                followerCount=newCount
                time.sleep(1)

        followers_list=dialog.find_elements_by_tag_name('li')
        for follower in followers_list:
            name=follower.find_element_by_css_selector(".FPmhX.notranslate._0imsa ").get_attribute("href")
            print(name)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(2)
        profile_photo_sign=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        ActionChains(self.driver).move_to_element(profile_photo_sign).click(profile_photo_sign).perform() 
        time.sleep(1)
        log_out_link=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div")
        ActionChains(self.driver).move_to_element(log_out_link).click(log_out_link).perform()
        time.sleep(2)
        self.driver.close()
    def followRandomUsers(self):
        try:
            self.login()
        except:
            print("Login Fail")
        time.sleep(3)
        search_button=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")

        search_button.send_keys("instagram")
        time.sleep(2)
        links=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div").find_elements_by_tag_name("a")

        time.sleep(2)
        ActionChains(self.driver).move_to_element(links[0]).click(links[0]).perform()
        time.sleep(2)

        followers=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        ActionChains(self.driver).move_to_element(followers).click(followers).perform()
        time.sleep(2)

        users_to_follow=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div").find_elements_by_tag_name("li")

        for user in users_to_follow:
            button=user.find_element_by_tag_name("button")
            if button.text=="Follow":
                button.click()
            time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(2)
        profile_photo_sign=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        ActionChains(self.driver).move_to_element(profile_photo_sign).click(profile_photo_sign).perform() 
        time.sleep(2)
        log_out_link=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div")
        ActionChains(self.driver).move_to_element(log_out_link).click(log_out_link).perform()
        time.sleep(2)
        self.driver.close()
    def write_followers_to_file(self):

        try:
            self.login()
        except:
            print("Giriş Başarısız")
        
        time.sleep(4)

        profile_photo_sign=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        ActionChains(self.driver).move_to_element(profile_photo_sign).click(profile_photo_sign).perform() 

        profile_link=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]")

        ActionChains(self.driver).move_to_element(profile_link).click(profile_link).perform()
        time.sleep(3)
        self.driver.maximize_window()
        followers=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        ActionChains(self.driver).move_to_element(followers).click(followers).perform()
        time.sleep(3)
        dialog=self.driver.find_element_by_css_selector("._1XyCr")

        followerCount=len(dialog.find_elements_by_tag_name('li'))

        action=ActionChains(self.driver)
        while True:
            dialog.click()

            for _ in range(10):
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(1)

            newCount=len(dialog.find_elements_by_tag_name('li'))

            if newCount==followerCount:
                break
            else:
                followerCount=newCount
                time.sleep(1)

        followers_list=dialog.find_elements_by_tag_name('li')
        followers_lists=[]
        for follower in followers_list:
            name=follower.find_element_by_css_selector(".FPmhX.notranslate._0imsa ").get_attribute("href")
            followers_lists.append(name)
        print("Processing...")
        with open("followers.txt","w") as file:
            for item in followers_lists:
                file.write(item+"\n")

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(2)
        profile_photo_sign=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        ActionChains(self.driver).move_to_element(profile_photo_sign).click(profile_photo_sign).perform() 
        time.sleep(1)
        log_out_link=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div")
        ActionChains(self.driver).move_to_element(log_out_link).click(log_out_link).perform()
        time.sleep(2)
        self.driver.close()
        print("Done. Go to followers.txt file")
insta=Instagram(email,password)

while True:
    secim=input("1-Show Followers\n2-Auto Follow\n3-Save Followers To A File\n4-Çıkış\nInput: ")

    if secim=="4":
        break
    else:
        if secim=="1":
            print(insta.getFollowers())
        elif secim=="2":
            insta.followRandomUsers()
        elif secim=="3":
            insta.write_followers_to_file()
        else:
            print("Wrong Input")