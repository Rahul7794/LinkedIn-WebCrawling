from time import sleep
import logging
from selenium.webdriver.support.select import Select


class LinkedInSection:
    def __init__(self, driver):
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)
        self._driver = driver

    def linkedin_login(self, user_name, pass_word):
        self._driver.get('https://www.linkedin.com')
        sleep(0.5)

        username = self._driver.find_element_by_class_name('login-email')
        username.send_keys(user_name)
        sleep(0.5)

        password = self._driver.find_element_by_class_name('login-password')
        password.send_keys(pass_word)
        sleep(0.5)

        log_in_button = self._driver.find_element_by_xpath('//*[@type="submit"]')
        log_in_button.click()
        sleep(0.5)

    def profile_scraping(self, links):
        for link in links:
            try:
                sleep(5)
                self._driver.get(link)
                sleep(5)
                name = self._driver.find_elements_by_xpath('//*[starts-with(@class,"profile-info")]/h1')
                firstName = name[0].text
                if firstName:
                    firstName = firstName.strip()

                Jobtitle = self._driver.find_elements_by_xpath('//*[starts-with(@class,"position-header")]/h4/a')
                if not Jobtitle:
                    firstJobtitle = "NA"
                else:
                    firstJobtitle = Jobtitle[0].text

                Company = self._driver.find_elements_by_xpath('//*[starts-with(@class,"position-header")]/h5/a')
                if not Company:
                    firstCompany = "NA"
                else:
                    firstCompany = Company[0].text

                Duration = self._driver.find_elements_by_xpath('//*[starts-with(@class,"date-range")]/span[1]')
                if not Duration:
                    firstDuration = "NA"
                else:
                    firstDuration = Duration[0].text

                Location = self._driver.find_elements_by_xpath('//*[starts-with(@class,"date-range")]/span[2]')
                if not Location:
                    firstLocation = "NA"
                else:
                    firstLocation = Location[0].text

                Introduction = self._driver.find_elements_by_xpath('//*[starts-with(@class,"position last")]/p')
                if not Introduction:
                    firstIntroduction = "NA"
                else:
                    firstIntroduction = Introduction[0].text

                publicProfile = self._driver.find_elements_by_xpath('//*[starts-with(@class,"public-profile '
                                                                    'searchable")]')
                publicProfileLink = publicProfile[0].find_element_by_css_selector('a').get_attribute('href')
                result = """Name: {name} \n Job Title: {JobTitle} \n Company: {Company} \n Duration: {Duration} \n 
                Location: {Location} \n Introduction: {Introduction} \n URL: {URL} \n\n""".format(
                    name=firstName, JobTitle=firstJobtitle, Company=firstCompany, Location=firstLocation,
                    Duration=firstDuration, Introduction=firstIntroduction, URL=publicProfileLink)
                file1 = open("result/candidates.txt", 'a')
                file1.write(result)
            except Exception:
                pass

    def add_companies(self, Companies_list):
        listOfCompanies = Companies_list
        companiesIdentification = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[4]/div/ul/li/span")
        companiesIdentification[0].click()
        counter = 2
        sleep(2.0)
        for companies in listOfCompanies:
            enterComapniesClick = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[4]/div/form[2]/span[2]/span/input")
            enterComapniesClick[0].send_keys(companies)
            sleep(2.0)

            companySelect = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[4]/div/form[2]/span[2]/span/div/div/p")
            companySelect[0].click()
            sleep(2.0)

            addButton = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[4]/div/ul/li[{number}]/button".format(number=counter))
            addButton[0].click()
            sleep(2.0)
            counter = counter + 1
        currentCompanyelement = Select(
            self._driver.find_element_by_xpath("//*[@id='left-rail-facets-region']/ul/li[4]/div/form/select"))
        currentCompanyelement.select_by_value("C")
        sleep(2.0)

    def add_YOE(self, ExperienceBetween):
        yearsOfExperienceIdentification = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[10]/div/ul/li/span")
        yearsOfExperienceIdentification[0].click()
        sleep(2.0)

        yearsOfExperienceFirstColumn = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p/input[1]")
        yearsOfExperienceFirstColumn[0].clear()
        yearsOfExperienceFirstColumn[0].send_keys(ExperienceBetween[0])
        sleep(2.0)

        yearsOfExperienceSecondColumn = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p/input[2]")
        yearsOfExperienceSecondColumn[0].clear()
        yearsOfExperienceSecondColumn[0].send_keys(ExperienceBetween[1])
        sleep(2.0)

        AddYOPButton = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[10]/div/form[2]/div/div/p[2]/button[2]")
        AddYOPButton[0].click()

    def add_location(self, Locations_list):
        locationSearchTab = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[2]/div/ul/li/span")
        locationSearchTab[0].click()
        sleep(2.0)

        locationToBeAdded = Locations_list
        for locations in locationToBeAdded:
            locationSearch2 = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[2]/div/form[2]/span[2]/span/input[2]")
            locationSearch2[0].send_keys(locations)
            sleep(2.0)

            locationSelect = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[2]/div/form[2]/span[2]/span/div/div/p")
            locationSelect[0].click()
            sleep(2.0)

        currentLocationelement = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[2]/div/fieldset/ul/li/label")
        currentLocationelement[0].click()
        sleep(2.0)

    def adding_job_titles(self, job_title):
        selectJobTitles = self._driver.find_elements_by_xpath("//*[@id='left-rail-facets']/li/div/ul/li/button")
        selectJobTitles[0].click()
        sleep(2.0)
        counter = 2
        jobTitle = job_title
        for jobTitles in jobTitle:
            typeJobTitles = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets']/li/div/form[2]/span[2]/span/input")
            typeJobTitles[0].send_keys(jobTitles)
            sleep(2.0)

            selectJobTitles = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets']/li/div/form[2]/span[2]/span/div/div/p")
            selectJobTitles[0].click()
            sleep(2.0)

            addButton = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets']/li/div/ul/li[{counter}]/button".format(counter=counter))
            addButton[0].click()
            sleep(2.0)
            counter = counter + 1

        currentJobelement = Select(
            self._driver.find_element_by_xpath("//*[@id='left-rail-outlet']/div[2]/ul/li/div/form/select"))
        currentJobelement.select_by_value("C")
        sleep(2.0)

    def add_skills(self, skill_set):
        listOfSkills = skill_set
        skillsIdentification = self._driver.find_elements_by_xpath(
            "//*[@id='left-rail-facets-region']/ul/li[3]/div/ul/li/span")
        skillsIdentification[0].click()
        counter = 2
        sleep(2.0)
        for skills in listOfSkills:
            enterSkillsClick = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[3]/div/form[2]/span[2]/span/input")
            enterSkillsClick[0].send_keys(skills)
            sleep(2.0)

            skillsSelect = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[3]/div/form[2]/span[2]/span/div/div/p")
            skillsSelect[0].click()
            sleep(2.0)

            addButton = self._driver.find_elements_by_xpath(
                "//*[@id='left-rail-facets-region']/ul/li[3]/div/ul/li[{number}]/button".format(number=counter))
            addButton[0].click()
            sleep(2.0)
            counter = counter + 1
