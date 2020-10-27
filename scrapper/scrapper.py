from selenium import webdriver
from time import sleep
import linkedin_sections.sections
import logging


class Scrapper:
    def __init__(self, username, pwd, discipline, companies, locations, designations, experience,
                 skills):
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)
        self.username = username
        self.password = pwd
        self.discipline = discipline
        self.companies = companies
        self.locations = locations
        self.designations = designations
        self.experience = experience
        self.skills = skills

    def scrap(self):
        driver = webdriver.Chrome(executable_path=r"../drivers/chromedriver.exe")
        sections = linkedin_sections.sections.LinkedInSection(driver)
        sections.linkedin_login(self.username, self.password)

        recruiterButton = driver.find_element_by_xpath('//*[@type="recruiter-app-icon"]')
        recruiterButton.click()
        sleep(1.5)

        driver.switch_to.window(driver.window_handles[1])
        sleep(10.0)

        search_button1 = driver.find_elements_by_xpath("//*[@id='overlay-form']/div/button")
        search_button1[0].click()
        sleep(0.5)

        search_query = driver.find_element_by_xpath("//*[@id='tt-freeform']/span[3]/span/input[2]")
        search_query.send_keys(self.discipline)

        submit_button = driver.find_element_by_xpath('//*[@type="submit"]')
        submit_button.click()
        sleep(2.5)

        sections.adding_job_titles(self.designations)

        sections.add_location(self.locations)

        sections.add_skills(self.skills)

        sections.add_companies(self.companies)

        sections.add_YOE(self.experience)
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

        sections.profile_scraping(links)
        driver.close()
