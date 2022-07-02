from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# add ublock origin chrome extension so no ads will appear
chrome_options = Options()
chrome_options.add_extension("C:\\Users\\Diego\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\cjpalhdlnbpafiamejdnhcphjbkeiagm\\1.43.0_0.crx")

#open the cookie clicker webpage
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# wait for page to load
driver.implicitly_wait(5)
# choose the language for the game
language_select = driver.find_element(By.CLASS_NAME, "langSelectButton")
language_select.click()
# clear notification about collecting cookies
cc_alert = driver.find_element(By.CLASS_NAME, "cc_btn")
cc_alert.click()
#close back up game save notification
driver.find_element(By.CLASS_NAME, "close").click()
driver.find_element(By.CLASS_NAME, "close").click()


### Start of actual cookie clicker automation script ###
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
# make a list and load all elements with id "productPrice"
# then we do a for loop that starts at 1 and goes to 0 that way we upgrade the most expensive item first
# for example, grandma costs 100 so once our cookie count reaches 100 we prioritize her over curser
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range (1, -1, -1)]

actions = ActionChains(driver)

for i in range(5000):
    actions.double_click(cookie).perform()
    upgrade_actions = ActionChains(driver)
    count = float(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions.move_to_element(item).click().perform()

