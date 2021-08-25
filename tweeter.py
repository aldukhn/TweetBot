from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="CHROMEDRIVER.EXE DIR") #Add the dirctory of Chromedriver that work with you chrome version.
driver.get("https://twitter.com/login")
sleep(3)
driver.find_element_by_name('session[username_or_email]').send_keys("USERNAME") # Add the user name of your twitter account
driver.find_element_by_name('session[password]').send_keys("PASSWORD") # Add the Password of your twitter account
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)
f = open("tweets.txt", 'r') #Write each tweet in line
for word in f:
    if word == "\n":
        continue
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(1)
    driver.find_element_by_class_name("notranslate").click()
    driver.find_element_by_class_name("notranslate").send_keys(word)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    sleep(5)

f.close()
