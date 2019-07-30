from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

    #initialize


while True:
    try:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        import random
        import time

        for p in range(200):
            startTime=time.time()
            print(p ,' -time')
            for x in range(1):
                a=random.randint(15,30)
            print (a)
            for f in range(2):
                for n in range(1):
                    u = random.randint(0,5)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--mute-audio")
            print("Opening chrome")
            driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://soundcloud.com/inspiron-285028880/sets/playstation")
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'r')
            for mn in range(4):
                st=time.time()
                driver.implicitly_wait(a)
                print("Changing track")
                driver.find_element_by_tag_name('body').send_keys(Keys.SHIFT+Keys.RIGHT)
                time.sleep(u)
                for k in range(3):
                    driver.implicitly_wait(u)
                    time.sleep(u)
                    m =random.randint(0,9)
                    print("Shift to ",m)
                    driver.find_element_by_tag_name('body').send_keys(m)
                    time.sleep(u)
                et=time.time()
                tie=et-st
                print(tie,"sec")
            driver.implicitly_wait(a)

            link = driver.find_element_by_link_text('Vansh Bordia')
            link.click()
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(m)
            endTime=time.time()
            ti=endTime-startTime
            print("it took -",ti,"sec")
            hj=random.randint(10,25)
            driver.get("https://www.youtube.com/watch?v=RQly8eEoaOw")
            time.sleep(a)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.get("https://www.youtube.com/watch?v=oaEwhjK-nFg")
            driver.implicitly_wait(a)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            time.sleep(hj)
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.get("https://www.youtube.com/watch?v=EiZMgWvmzq0")
            driver.implicitly_wait(a)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            time.sleep(hj)
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)           
            driver.get("https://www.youtube.com/watch?v=oaEwhjK-nFg")
            driver.implicitly_wait(a)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.find_element_by_tag_name('body').send_keys("l")
            time.sleep(hj)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.get("https://www.youtube.com/watch?v=MRF6RjDOwvI")
            time.sleep(2)
            driver.find_element_by_css_selector(".QvAa1").click()

            driver.implicitly_wait(hj)

            driver.close()

    except Exception:
        pass
        driver.close()
    
