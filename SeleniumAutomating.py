from selenium import webdriver
from time import sleep
from Scrapping import profileScraping, addCompanies, linkedinLogin, readFilePath, addYearOfExperince, addLocation,\
    addingJobTitles, addSkills

driver = webdriver.Chrome('C:/Users/rahul.singh/Downloads/chromedriver_win32/chromedriver')
userName = readFilePath("linkedinUserName")
password = readFilePath("linkedinPassword")
linkedinLogin(userName, password, driver)

recruiterButton = driver.find_element_by_xpath('//*[@type="recruiter-app-icon"]')
recruiterButton.click()
sleep(1.5)

driver.switch_to.window(driver.window_handles[1])
sleep(10.0)

search_button1 = driver.find_elements_by_xpath("//*[@id='overlay-form']/div/button")
search_button1[0].click()
sleep(0.5)

search_query = driver.find_element_by_xpath("//*[@id='tt-freeform']/span[3]/span/input[2]")
search_query.send_keys(readFilePath("searchKeyWord"))

submit_button = driver.find_element_by_xpath('//*[@type="submit"]')
submit_button.click()
sleep(2.5)

addingJobTitles(driver)

addLocation(driver)

addSkills(driver)

addCompanies(driver)


addYearOfExperince(driver)
sleep(10.0)

links = []
for i in range(0, 50):
    try:
        profileInformation = driver.find_elements_by_css_selector("[href*='/recruiter/profile']")
        for profileInformation1 in profileInformation:
            example1 = profileInformation1.get_attribute("href")
            links.append(example1)
        sleep(10.0)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        nextButton = driver.find_element_by_class_name('next')
        nextButton.click()
        sleep(10.0)
    except Exception as e:
        print(str(e))
        break

print(links)
profileScraping(links, driver)
driver.close()
