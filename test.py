#!/usr/bin/env python3

# pylint: disable=undefined-variable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument(
    r'user-data-dir=/Users/machadoca/Library/Application Support/Google/Chrome'
)
options.add_argument(r'profile-directory=Default')

cls.driver = webdriver.Chrome(service=service, options=options)

# cls.get("https://google.com/")
cls.get('http://stackoverflow.com/')

body = cls.find_element_by_tag_name('body')
body.send_keys(Keys.CONTROL + 't')

cls.close()

print(body)
