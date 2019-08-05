from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui as pgui
import time

driver_path = 'REPLACE_ME_YOUR_DRIVER_PATH'
driver = webdriver.Chrome(driver_path)
driver.get(
    'https://www.e-typing.ne.jp/app/jsa_std/typing.asp?t=trysc.trysc.trysc.std.0&u=&s=1')
button = driver.find_element_by_id("start_btn")
button.click()
time.sleep(1)
pgui.press(keys="space", presses=1)
time.sleep(3)
for i in range(15):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    temp = soup.find("div", id="app")
    main = temp.find("div", id="sentenceText")
    txt = main.get_text()
    pgui.typewrite(txt)
    time.sleep(0.575)
