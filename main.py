from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time


driver = webdriver.Chrome()


def initialize():
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(10)

    english = driver.find_element(By.ID, "langSelect-EN")
    english.click()
    time.sleep(5)

    load_saved_game()


def save_game():
    try:
        opt_button = driver.find_element(By.ID, "prefsButton")
        opt_button.click()
        time.sleep(1)

        export_button = driver.find_element(By.XPATH, '//a[contains(text(), "Export")]')
        export_button.click()
        time.sleep(1)

        text_field = driver.find_element(By.ID, "textareaPrompt")
        save_text = text_field.get_attribute("innerHTML")

        with open("save.txt", mode="w") as fp:
            fp.write(save_text)
        time.sleep(1)

        accept_button = driver.find_element(By.ID, "promptOption0")
        accept_button.click()
        time.sleep(1)

        opt_button.click()
        time.sleep(1)

        print("Save succesful.")
    except:
        print("Failed to save game.")


def read_save_file():
    try:
        open("save.txt")
    except FileNotFoundError:
        print("No saved game available.")
        return None
    else:
        with open("save.txt", mode="r") as fp:
            return fp.read()


def load_saved_game():
    saved_game = read_save_file()
    if saved_game:
        try:
            opt_button = driver.find_element(By.ID, "prefsButton")
            opt_button.click()
            time.sleep(1)

            load_button = driver.find_element(By.XPATH, '//a[contains(text(), "Import")]')
            load_button.click()
            time.sleep(1)

            text_field = driver.find_element(By.ID, "textareaPrompt")
            text_field.send_keys(saved_game)
            time.sleep(1)

            load_button = driver.find_element(By.ID, "promptOption0")
            load_button.click()
            time.sleep(1)

            opt_button.click()
            time.sleep(1)
        except:
            print("Failed to load saved game.")


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
    is_clicking = False

    initialize()

    while True:

        if keyboard.is_pressed(1):
            time.sleep(0.5)
            save_game()

        if keyboard.is_pressed(12):
            time.sleep(0.5)
            break

        if keyboard.is_pressed(7):
            time.sleep(0.5)
            if not is_clicking:
                is_clicking = True
                print("Clicking..")
            else:
                is_clicking = False
                print("Paused Clicking..")
        
        if is_clicking:
            click_golden_cookie()
            buy_upgrades()
            buy_products()
            clear_notifications()
            click_cookie()
    
    time.sleep(1)
    save_game()
    print("Program finished")


if __name__ == "__main__":
    main()
