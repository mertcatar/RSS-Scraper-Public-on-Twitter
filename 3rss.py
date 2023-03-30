#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import os
import feedparser
import glob


# Create Firefox profile with private browsing mode
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

# Set up Firefox driver with private browsing profile
driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path=GeckoDriverManager().install())

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)


search_bar = driver.find_element(By.NAME, "text")
search_bar.click()
search_bar.send_keys("Simple_Breaking")
search_bar.send_keys(Keys.ENTER)
time.sleep(7)
search_bar_2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
# search_bar_2.send_keys(Keys.TAB)
search_bar_2.send_keys("hotmail1A")
search_bar_2.send_keys(Keys.ENTER)
time.sleep(7)


feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"

feed = feedparser.parse(feed_url)

first_entry1 = feed.entries[0]

# Get the first word of the RSS feed title
filename1 = first_entry1.title.split()[0]

# Get the path to the Desktop directory
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Create the output file path
output_file = os.path.join(desktop_path, f"{filename1}.txt")

# Open the file and write the output to it
with open(output_file, 'w') as file:
        file.write(first_entry1.title)


    
feed_url = "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml"

feed = feedparser.parse(feed_url)

first_entry2 = feed.entries[0]


# Get the first word of the RSS feed title
filename2 = first_entry2.title.split()[0]

# Get the path to the Desktop directory
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Create the output file path
output_file = os.path.join(desktop_path, f"{filename2}.txt")

# Open the file and write the output to it
with open(output_file, 'w') as file:
     file.write(first_entry2.title)



feed_url = "http://rss.cnn.com/rss/edition_us.rss"

feed = feedparser.parse(feed_url)

first_entry3 = feed.entries[0]

# Get the first word of the RSS feed title
filename3 = first_entry3.title.split()[0]

# Get the path to the Desktop directory
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Create the output file path
output_file = os.path.join(desktop_path, f"{filename3}.txt")

# Open the file and write the output to it
with open(output_file, 'w') as file:
     file.write(first_entry3.title)

search_bar_3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
search_bar_3.click()
time.sleep(7)
search_bar_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
search_bar_4.send_keys(first_entry3.title)
search_bar_5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
search_bar_5.click()
time.sleep(3)


driver.get("https://twitter.com/compose/tweet")
# search_bar_3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
# search_bar_3.click()
time.sleep(3)
search_bar_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
search_bar_4.send_keys(first_entry2.title)
search_bar_5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
search_bar_5.click()
time.sleep(3)


driver.get("https://twitter.com/compose/tweet")
# search_bar_3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
# search_bar_3.click()
time.sleep(3)
search_bar_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
search_bar_4.send_keys(first_entry1.title)
search_bar_5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
search_bar_5.click()
time.sleep(7)

