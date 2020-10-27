import PySimpleGUI as sg
import logging

from scrapper.scrapper import Scrapper


class DialogBox:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)

    def create(self):
        form = sg.FlexForm('Linkedin Scrapping')
        layout = [
            [sg.Text('Please enter below details')],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
            [sg.Text('Discipline', size=(15, 1)), sg.InputText()],
            [sg.Text('Companies', size=(15, 1)), sg.InputText()],
            [sg.Text('Locations', size=(15, 1)), sg.InputText()],
            [sg.Text('Job Title', size=(15, 1)), sg.InputText()],
            [sg.Text('Experience Between', size=(15, 1)), sg.InputText()],
            [sg.Text('Skill Set', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
        button, values = form.Layout(layout).Read()
        companies = []
        locations = []
        experience_between = []
        job_title = []
        skill_set = []
        username = values[0]
        password = values[1]
        discipline = values[2]
        if values[3] is not None:
            companies = values[3].split(",")
        if values[4] is not None:
            locations = values[4].split(",")
        if values[5] is not None:
            job_title = values[5].split(",")
        if values[6] is not None:
            experience_between = values[6].split("-")
        if values[7] is not None:
            skill_set = values[7].split(",")

        scrapper = Scrapper(username, password, discipline, companies, locations, job_title, experience_between,
                            skill_set)
        if button == "Submit":
            scrapper.scrap()
        else:
            exit(0)
