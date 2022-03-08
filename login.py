#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# step 1) Open Firefox
browser = webdriver.Chrome()

# step 2) Navigate to Facebook
browser.get("http://www.facebook.com")

# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_name("login")
username.send_keys("daniel@xlaccessories.com")
password.send_keys("Fa$587648")

# step 4) click login
submit.click()

# input keys content to search
search = browser.find_element_by_xpath("//div[@role='banner']//input")
search.send_keys("musical instruments")
search.send_keys(Keys.RETURN)

# click page category
pages = WebDriverWait(browser, 10).until(
    lambda b: b.find_element_by_xpath("//div[@role='region']//div[@data-visualcompletion='ignore-dynamic'][7]/a")
)
pages.click()

# click
articles = WebDriverWait(browser, 10).until(
    lambda b: b.find_element_by_xpath("//div[@role='article']//a[@role='link']")
)
name = articles.find_element_by_css_selector("a span").text
print("第[%s]个公司，名称：[%s]" % (1, name))

# for i, ele in enumerate(articles):
#     name = ele.find_element_by_css_selector("a span").text
#     print("第[%s]个公司，名称：[%s]" % (i+1, name))


