import os
import shutil
import PySimpleGUI as sg

dir = ""

midia = ["png","gif","jpg","mp4","mkv","webp","mp3","svg","ico","psd","jpeg"]
compacted = ["zip","rar","7z"]
models = ["stl"]
executables = ["exe","msi"]

def organize(window):
    window["-LOG-"].update("")
    for file in os.listdir(dir):
        aux = str.split(file,".")
        aux.reverse()
        type = aux[0].lower()
        if(type in midia):
            try:
                shutil.move(dir+"\\"+ file,"F:\\midia")
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in executables):
            try:
                shutil.move(dir+"\\"+ file,"F:\\executaveis")
            except Exception as e:
                window["-LOG-"].print(e)
        if(type == "pdf"):
            try:
                shutil.move(dir+"\\"+ file,"F:\\pdfs")
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in compacted):
            try:
                shutil.move(dir + "\\"+ file,"F:\\zips")
            except Exception as e:
                window["-LOG-"].print(e)
        if(type in models):
            try:
                shutil.move(dir + "\\"+ file,"F:\\3D")
            except Exception as e:
                window["-LOG-"].print(e)
    window["-LOG-"].print("DONE")

sg.theme("DarkBrown4")

log_column = [
    [sg.Text("LOG")],
    [sg.Multiline(key="-LOG-",size=(30,22),disabled=True)]
]

viewer_column = [
    [sg.Text("Dir",key="-DIR-")],
    [sg.Multiline(key="-FILES-",size=(30,20),disabled=True)],
    [sg.Button('Organize'),sg.Button('Browse')],
]

layout = [
    [sg.Column(viewer_column), sg.VSeparator(),sg.Column(log_column)]
]

window = sg.Window(title="Simple Organizer", layout=layout,icon="organizado.ico")

while True:             
    event, values = window.read()

    if event == 'Organize':
        if dir!="":
            organize(window)

    if event == 'Browse':
        foldername = sg.PopupGetFolder("Browse",no_window=True)
        if foldername:
            window['-DIR-'].update(foldername)
            dir = foldername
            filenames = sorted(os.listdir(foldername))
            window['-FILES-'].update("\n".join(filenames))

    if event == sg.WIN_CLOSED:
        break

window.close()

