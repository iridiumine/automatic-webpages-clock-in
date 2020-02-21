#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from time import sleep
import schedule

usr_name = "********"
usr_password = "********"

def task():
    sleep(random.randint(15,30))
    driver = webdriver.Safari()
    
    driver.get("http://weixine.ustc.edu.cn/2020/")
    sleep(3)
    
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(3)
    
    driver.find_element_by_css_selector("a[href='/2020/caslogin'][class='btn']").click()
    driver.find_element_by_css_selector("a[href='/2020/caslogin'][class='btn']").send_keys(Keys.ENTER)
    sleep(5)
    
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(3)
    
    driver.find_element_by_css_selector("input[id='username'][class='input-box'][name='username'][type='text'][size='30']").clear()
    driver.find_element_by_css_selector("input[id='password'][class='input-box'][name='password'][type='password'][size='30']").clear()
    driver.find_element_by_css_selector("input[id='username'][class='input-box'][name='username'][type='text'][size='30']").send_keys(usr_name)
    sleep(3)
    driver.find_element_by_css_selector("input[id='password'][class='input-box'][name='password'][type='password'][size='30']").send_keys(usr_password)
    sleep(5)
    
    driver.find_element_by_css_selector("button[id='login'][type='submit'][onclick='return check();'][name='button'][class='btn ripple bottom-box-button-area-1']").click()
    driver.find_element_by_css_selector("button[id='login'][type='submit'][onclick='return check();'][name='button'][class='btn ripple bottom-box-button-area-1']").send_keys(Keys.ENTER)
    
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(3)
    
    driver.find_element_by_css_selector("button[type='submit'][id='report-submit-btn'][class='btn btn-primary']").click()
    driver.find_element_by_css_selector("button[type='submit'][id='report-submit-btn'][class='btn btn-primary']").send_keys(Keys.ENTER)
    sleep(5)
    driver.quit()
    
if __name__ == "__main__":
    schedule.every().day.at("16:49").do(task)
    while True:
        schedule.run_pending()
        
