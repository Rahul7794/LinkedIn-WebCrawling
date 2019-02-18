import json
from time import sleep
from selenium.webdriver.support.select import Select

def linkedinLogin(userName, passWord,driver):
    driver.get('https://www.linkedin.com')
    sleep(0.5)

    username = driver.find_element_by_class_name('login-email')
    username.send_keys(userName)
    sleep(0.5)

    password = driver.find_element_by_class_name('login-password')
    password.send_keys(passWord)
    sleep(0.5)

    log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    log_in_button.click()
    sleep(0.5)


def profileScraping(links, driver):
#links =['https://www.linkedin.com/recruiter/profile/411313749,lOfU,CAP?searchController=smartSearch&searchId=7470520893&pos=66&total=4943&searchCacheKey=27a14462-eb94-4dc0-b58e-a32e2c948885%2CXLuM&searchRequestId=e8a0d05f-6dfe-40a5-9678-3b7e32da7b54%2CkhRh&searchSessionId=7470520893&origin=PAGE&memberAuth=411313749%2ClOfU%2CCAP']
    for link in links:
        try:
            sleep(5)
            driver.get(link)
            sleep(5)
            name = driver.find_elements_by_xpath('//*[starts-with(@class,"profile-info")]/h1')
            firstName = name[0].text
            if firstName:
                firstName = firstName.strip()

            Jobtitle = driver.find_elements_by_xpath('//*[starts-with(@class,"position-header")]/h4/a')
            if not Jobtitle:
                firstJobtitle = "NA"
            else:
                firstJobtitle = Jobtitle[0].text


            Company = driver.find_elements_by_xpath('//*[starts-with(@class,"position-header")]/h5/a')
            if not Company:
                firstCompany = "NA"
            else:
                firstCompany = Company[0].text


            Duration = driver.find_elements_by_xpath('//*[starts-with(@class,"date-range")]/span[1]')
            if not Duration:
                firstDuration = "NA"
            else:
                firstDuration = Duration[0].text

            Location = driver.find_elements_by_xpath('//*[starts-with(@class,"date-range")]/span[2]')
            if not Location:
                firstLocation = "NA"
            else:
                firstLocation = Location[0].text

            Introduction = driver.find_elements_by_xpath('//*[starts-with(@class,"position last")]/p')
            if not Introduction:
                firstIntroduction = "NA"
            else:
                firstIntroduction = Introduction[0].text

            publicProfile = driver.find_elements_by_xpath('//*[starts-with(@class,"public-profile searchable")]')
            publicProfileLink = publicProfile[0].find_element_by_css_selector('a').get_attribute('href')
            result = """ Name: {name} \n Job Title: {JobTitle} \n Company: {Company} \n Duration: {Duration} \n Location: {Location} \n Introduction: {Introduction} \n URL: {URL} \n\n""".format(name=firstName, JobTitle=firstJobtitle,Company=firstCompany,Location=firstLocation,Duration=firstDuration,Introduction= firstIntroduction,URL=publicProfileLink)
            file1 = open("result.txt", 'a')
            file1.write(result)
        except Exception as e:
            pass

def addCompanies(driver):
    listOfCompanies = readFilePath("companiesToBeAdded")
    companiesIdentification = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/ul/li/span")
    companiesIdentification[0].click()
    counter=2
    sleep(2.0)
    for companies in listOfCompanies:
        enterComapnirsClick = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/form[2]/span[2]/span/input")
        enterComapnirsClick[0].send_keys(companies)
        sleep(2.0)

        companySelect = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/form[2]/span[2]/span/div/div/p")
        companySelect[0].click()
        sleep(2.0)

        addButton = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/ul/li[{number}]/button".format(number=counter))
        addButton[0].click()
        sleep(2.0)
        counter = counter+1
    currentCompanyelement = Select(driver.find_element_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/form/select"))
    currentCompanyelement.select_by_value("C")
    sleep(2.0)

def readFilePath(key):
    with open('config.json', 'r') as f:
        config = json.load(f)
        for i in key.split("."):
            if i in config:
                config = config[i]
            else:
                return None
        return config

def addYearOfExperince(driver):
    yearsOfExperienceIdentification= driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[10]/div/ul/li/span")
    yearsOfExperienceIdentification[0].click()
    sleep(2.0)

    yearsOfExperienceFirstColumn = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p/input[1]")
    yearsOfExperienceFirstColumn[0].clear()
    yearsOfExperienceFirstColumn[0].send_keys(readFilePath("YearOfExperienceFrom"))
    sleep(2.0)

    yearsOfExperienceSecondColumn = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p/input[2]")
    yearsOfExperienceSecondColumn[0].clear()
    yearsOfExperienceSecondColumn[0].send_keys(readFilePath("YearOfExperienceTo"))
    sleep(2.0)

    AddYOPButton = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p[2]/button[2]")
    AddYOPButton[0].click()

def addLocation(driver):
    locationSearchTab = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[2]/div/ul/li/span")
    locationSearchTab[0].click()
    sleep(2.0)

    locationToBeAdded = readFilePath("locationToBeAdded")
    for locations in locationToBeAdded:
        locationSearch2 = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[2]/div/form[2]/span[2]/span/input[2]")
        locationSearch2[0].send_keys(locations)
        sleep(2.0)


        locationSelect = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[2]/div/form[2]/span[2]/span/div/div/p")
        locationSelect[0].click()
        sleep(2.0)

    currentLocationelement = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[2]/div/fieldset/ul/li/label")
    currentLocationelement[0].click()
    sleep(2.0)

def addingJobTitles(driver):
    selectJobTitles = driver.find_elements_by_xpath("//*[@id='left-rail-facets']/li/div/ul/li/button")
    selectJobTitles[0].click()
    sleep(2.0)
    counter =2
    jobTitle = readFilePath("jobTitle")
    for jobTitles in jobTitle:
        typeJobTitles = driver.find_elements_by_xpath("//*[@id='left-rail-facets']/li/div/form[2]/span[2]/span/input")
        typeJobTitles[0].send_keys(jobTitles)
        sleep(2.0)

        selectJobTitles = driver.find_elements_by_xpath("//*[@id='left-rail-facets']/li/div/form[2]/span[2]/span/div/div/p")
        selectJobTitles[0].click()
        sleep(2.0)

        addButton = driver.find_elements_by_xpath("//*[@id='left-rail-facets']/li/div/ul/li[{counter}]/button".format(counter=counter))
        addButton[0].click()
        sleep(2.0)
        counter = counter+1

    currentJobelement=Select(driver.find_element_by_xpath("//*[@id='left-rail-outlet']/div[2]/ul/li/div/form/select"))
    currentJobelement.select_by_value("C")
    sleep(2.0)


def addSkills(driver):
    listOfSkills = readFilePath("skillsToBeAdded")
    skillsIdentification = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[3]/div/ul/li/span")
    skillsIdentification[0].click()
    counter=2
    sleep(2.0)
    for skills in listOfSkills:
        enterSkillsClick = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[3]/div/form[2]/span[2]/span/input")
        enterSkillsClick[0].send_keys(skills)
        sleep(2.0)

        skillsSelect = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[3]/div/form[2]/span[2]/span/div/div/p")
        skillsSelect[0].click()
        sleep(2.0)

        addButton = driver.find_elements_by_xpath("//*[@id='left-rail-facets-region']/ul/li[3]/div/ul/li[{number}]/button".format(number=counter))
        addButton[0].click()
        sleep(2.0)
        counter = counter+1
