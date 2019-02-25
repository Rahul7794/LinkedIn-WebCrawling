import PySimpleGUI as sg
from SeleniumAutomating import linkedin_scrapping

form = sg.FlexForm('Linkedin Scrapping')  # begin with a blank form

layout = [
    [sg.Text('Please enter below details')],
    [sg.Text('Username', size=(15, 1)), sg.InputText()],
    [sg.Text('Password', size=(15, 1)), sg.InputText( password_char='*')],
    [sg.Text('Discipline', size=(15, 1)), sg.InputText()],
    [sg.Text('Companies', size=(15, 1)), sg.InputText()],
    [sg.Text('Locations', size=(15, 1)), sg.InputText()],
    [sg.Text('Job Title', size=(15, 1)), sg.InputText()],
    [sg.Text('Experience Between', size=(15, 1)), sg.InputText()],
    [sg.Text('Skill Set', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
button, values = form.Layout(layout).Read()
Companies = []
Locations = []
ExperienceBetween = []
job_title = []
skill_set = []
username = values[0]
password = values[1]
Discipline = values[2]
if values[3] is not None:
    Companies = values[3].split(",")
if values[4] is not None:
    Locations = values[4].split(",")
if values[5] is not None:
    job_title = values[5].split(",")
if values[6] is not None:
    ExperienceBetween = values[6].split("-")
if values[7] is not None:
    skill_set = values[7].split(",")

if button == "Submit":
    linkedin_scrapping(username, password, Discipline, Companies, Locations, job_title, ExperienceBetween, skill_set)

else:
    exit(0)

