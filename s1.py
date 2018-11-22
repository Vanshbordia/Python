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
            print(p,' -time')
            for x in range(1):
                a=random.randint(15,30)
            print (a)
            for f in range(2):
                for n in range(1):
                    u = random.randint(0,5)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--mute-audio")
            print("Opening chrome")
            driver = webdriver.Chrome(chrome_options=chrome_options)

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
            driver.get("https://www.youtube.com/watch?v=aRs3zF4zc4A&feature=youtu.be")
            time.sleep(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.get("https://www.youtube.com/watch?v=2-cJWKL4dcE")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            time.sleep(hj)
            driver.implicitly_wait(hj)
            driver.get("https://www.youtube.com/watch?v=wR6C-oDBZ-4")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            driver.implicitly_wait(hj)
            driver.find_element_by_tag_name('body').send_keys("l")
            time.sleep(hj)
            driver.get("https://www.instagram.com/p/Bo3xJ5RFz46/")
            time.sleep(2)
            driver.find_element_by_css_selector(".QvAa1").click()

            driver.implicitly_wait(hj)

            driver.close()

    except Exception:
        pass
        driver.close()
    else:
        #break
        driver.close()
