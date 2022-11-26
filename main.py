from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

CLICK_TIME = 10

driver = webdriver.Chrome()


def click_golden_cookie():
    try:
        golden_cookie = driver.find_element(By.XPATH, '//div[@alt="Golden cookie"]')
        golden_cookie.click()
    except:
        pass


def clear_notifications():
    try:
        close_button = driver.find_element(By.XPATH, '//div[@class="framed close sidenote"]')
        close_button.click()
    except:
        pass


def buy_upgrades():
    try:
        upgrade = driver.find_element(By.ID, "upgrade0")
        upgrade_class = upgrade.get_attribute("class")
        if "enabled" in upgrade_class:
            upgrade.click()
    except:
        pass


def buy_products():
    try:
        upgrades = driver.find_elements(By.XPATH, f'//div[@class="product unlocked enabled"]')
        if upgrades:
            upgrades[-1].click()
    except:
        pass


def click_cookie():
    try:
        big_cookie = driver.find_element(By.ID, "bigCookie")
        big_cookie.click()
    except:
        print("Error clicking cookie..")


def main():
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    is_clicking = False

    while True:

        if keyboard.is_pressed("q"):
            time.sleep(0.5)
            break

        if keyboard.is_pressed("x"):
            time.sleep(0.5)
            if not is_clicking:
                is_clicking = True
                print("Clicking..")
            else:
                is_clicking = False
                print("Clicking Paused..")
        
        if is_clicking:
            click_golden_cookie()
            buy_upgrades()
            buy_products()
            clear_notifications()
            click_cookie()
    
    print("Program finished")


if __name__ == "__main__":
    main()
