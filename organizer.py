import os
from shutil import move
import sys
import PySimpleGUI as sg

dir = ""

types = ["midia","executables","pdfs","compacted","3D models"]
midia = ["png","gif","jpg","mp4","mkv","webp","mp3","svg","ico","psd","jpeg"]
compacted = ["zip","rar","7z"]
models = ["stl","obj","fbx","glb"]
executables = ["exe","msi"]

""" sg.LOOK_AND_FEEL_TABLE['EVA01'] = {
    'BACKGROUND': '#965fd4',
    'TEXT': '#e1b433',
    'INPUT': '#8bd450',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#3f6d4e',
    'BUTTON': ('#1d1a2f', '#3f6d4e'),
    'PROGRESS': ('#D1826B', '#CC8019'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 
    'PROGRESS_DEPTH': 0
    }

sg.theme("EVA01") """

def resource_path(relative_path):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, relative_path))


def organize(window):
    for t in types:
        os.makedirs(dir + "\\" + t, exist_ok=True)

    window["-LOG-"].update("")
    for file in os.listdir(dir):
        aux = str.split(file,".")
        aux.reverse()
        type = aux[0].lower()
        if(type in midia):
            try:
                move(dir+"\\"+ file, dir + "\\" + types[0])
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in executables):
            try:
                move(dir+"\\"+ file, dir + "\\" + types[1])
            except Exception as e:
                window["-LOG-"].print(e)
        if(type == "pdf"):
            try:
                move(dir+"\\"+ file, dir + "\\" + types[2])
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in compacted):
            try:
                move(dir + "\\"+ file, dir + "\\" + types[3])
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in models):
            try:
                move(dir + "\\"+ file, dir + "\\" + types[4])
            except Exception as e:
                window["-LOG-"].print(e)
    window["-LOG-"].print("DONE")

log_column = [
    [sg.Text("LOG")],
    [sg.Multiline(key="-LOG-",size=(30,22),disabled=True)]
]

viewer_column = [
    [sg.Text("Dir",key="-DIR-")],
    [sg.Multiline(key="-FILES-",size=(30,20),disabled=True)],
    [sg.Button("Organize"),sg.Button("Browse")],
]

layout = [
    [sg.Column(viewer_column), sg.VSeparator(),sg.Column(log_column)]
]

window = sg.Window(title="Simple Organizer", layout=layout,icon=resource_path("icon/papo.ico"))

while True:
    event, values = window.read()

    if event == "Organize":
        if dir!="":
            organize(window)
            filenames = list(filter(lambda x: os.path.isfile(dir + "\\" +x), os.listdir(dir)))
            window["-FILES-"].update("\n".join(filenames))
        else:
            sg.popup("Please specify a folder",title="Warning")

    if event == "Browse":
        dir = sg.PopupGetFolder("Browse",no_window=True)
        if dir != "":
            window["-DIR-"].update(dir)
            filenames = list(filter(lambda x: os.path.isfile(dir + "\\" +x), os.listdir(dir)))
            window["-FILES-"].update("\n".join(filenames))

    if event == sg.WIN_CLOSED:
        break

window.close()

