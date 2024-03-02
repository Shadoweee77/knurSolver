from selenium import webdriver
from selenium.webdriver.common.by import By
import threading


def input_thread():
    global running
    while running:
        user_input = input("Enter 'q' to quit: ")
        if user_input.lower() == 'q':
            running = False
            break


driver = webdriver.Firefox()


driver.get("https://matemax.knur.club/")
start = driver.find_element(By.XPATH, '//button[text()="JAZDA!"]')
start.click()

solution_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/input')

running = True
input_thread = threading.Thread(target=input_thread)
input_thread.start()

while running:
    equation = driver.find_element(By.XPATH, '/html/body/div/div[2]/p[3]')
    solution_input.send_keys(eval(equation.text))

input_thread.join()
driver.quit()
