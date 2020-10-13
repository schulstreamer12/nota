from tkinter import *
import os

root = Tk()
root.title("CMJ_Notes")
root.geometry("700x550")

dirname, filename = os.path.split(os.path.abspath(__file__))
opened_file = ""
opened_folder_level1 = ""
opened_folder_level2 = ""

#FRAME BUTTONS
frame_buttons_1 = Frame(master=root, background="blue")
frame_buttons_1.place(x=0, y=0, width=700, height=30)

button_1_add = Button(master=frame_buttons_1, text="ADD")
button_1_add.place(x=0, y=0, width=35, height=25)
button_1_del = Button(master=frame_buttons_1, text="DEL")
button_1_del.place(x=40, y=0, width=35, height=25)
button_1_edit = Button(master=frame_buttons_1, text="EDIT")
button_1_edit.place(x=80, y=0, width=35, height=25)

frame_buttons_2 = Frame(master=root, background="blue")
frame_buttons_2.place(x=220, y=0, width=700, height=30)

button_2_add = Button(master=frame_buttons_2, text="ADD")
button_2_add.place(x=0, y=0, width=35, height=25)
button_2_del = Button(master=frame_buttons_2, text="DEL")
button_2_del.place(x=40, y=0, width=35, height=25)
button_2_edit = Button(master=frame_buttons_2, text="EDIT")
button_2_edit.place(x=80, y=0, width=35, height=25)

frame_buttons_3 = Frame(master=root, background="blue")
frame_buttons_3.place(x=440, y=0, width=700, height=30)

button_3_add = Button(master=frame_buttons_3, text="ADD")
button_3_add.place(x=0, y=0, width=35, height=25)
button_3_del = Button(master=frame_buttons_3, text="DEL")
button_3_del.place(x=40, y=0, width=35, height=25)
button_3_edit = Button(master=frame_buttons_3, text="EDIT")
button_3_edit.place(x=80, y=0, width=35, height=25)

#FRAME LISTBOXEN
frame_listboxen = Frame(master=root, background="red")
frame_listboxen.place(x=0, y=30, height=200, width=700)

listbox_1 = Listbox(master=frame_listboxen)
listbox_1.place(x=0, y=0, width=200, height=200)

scrollbar_listbox_1 = Scrollbar(master=frame_listboxen, orient="vertical")
scrollbar_listbox_1.config(command=listbox_1.yview)
listbox_1.config(yscrollcommand=scrollbar_listbox_1.set)
scrollbar_listbox_1.place(x=200, y=0, height=200)

listbox_2 = Listbox(master=frame_listboxen)
listbox_2.place(x=220, y=0, width=200, height=200)

scrollbar_listbox_2 = Scrollbar(master=frame_listboxen, orient="vertical")
scrollbar_listbox_2.config(command=listbox_2.yview)
listbox_2.config(yscrollcommand=scrollbar_listbox_2.set)
scrollbar_listbox_2.place(x=420, y=0, height=200)

listbox_3 = Listbox(master=frame_listboxen)
listbox_3.place(x=440, y=0, width=200, height=200)

scrollbar_listbox_3 = Scrollbar(master=frame_listboxen, orient="vertical")
scrollbar_listbox_3.config(command=listbox_3.yview)
listbox_3.config(yscrollcommand=scrollbar_listbox_3.set)
scrollbar_listbox_3.place(x=640, y=0, height=200)

#FRAME titlebar
frame_main = Frame(master=root, background="green")
frame_main.place(x=0, y=230, width=400, height=25)

def save_file(event):
    global opened_file
    text_file = open(opened_file, "w")
    text_file.write(main_text.get(1.0, END))
    saved_message = "Saved " + opened_file 
    status.config(text=saved_message)

root.bind('<F3>', save_file)

button_save = Button(master=frame_main, text="Save", command=save_file)
button_save.place(x=0, y=0, width=45, height=25)

label_filename = Label(master=frame_main, text="Test")
label_filename.place(x=250, y=0)

#TEXTBOX
main_text = Text(master=root)
main_text.place(x=0, y=260, width=680, height=400)

scrollbar_main_text = Scrollbar(master=root, orient="vertical")
scrollbar_main_text.config(command=main_text.yview)
main_text.config(yscrollcommand=scrollbar_main_text.set)
scrollbar_main_text.place(x=680, y=250, height=400)

#Status Bar
status = Label(master=root, text="Opened nota", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

def resize_main_text(sinn):
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    main_text_widget_width = window_width - 20
    main_text_widget_height = window_height - 275

    main_text.place(x=0, y=255, width=main_text_widget_width, height=main_text_widget_height)
    scrollbar_main_text.place(x=main_text_widget_width, y=255, height=main_text_widget_height)

root.bind('<Configure>',resize_main_text)

def list_root_directory(event):
    root = os.listdir("notes")

    listbox_1.delete(0, END)

    for items in root:
        listbox_1.insert(END, items)

root.bind('<F2>',list_root_directory)

def list_dir_1(event):
    global opened_file, opened_folder_level1
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)

    directory = os.path.join("notes" , value)

    if value.endswith(".txt"):

        text_file = open(directory, "r")
        stuff = text_file.read()
        main_text.delete("1.0", END)
        main_text.insert(END, stuff)
        opened_file = directory
        label_filename.config(text=directory)
        print("Opened File: " + opened_file)        
    else:
        folder_level2 = os.listdir(directory)
        listbox_2.delete(0, END)
        listbox_3.delete(0, END)
        for items in folder_level2:
            listbox_2.insert(0, items)
        opened_folder_level1 = value

listbox_1.bind('<<ListboxSelect>>', list_dir_1)

def list_dir_2(event):
    global opened_file, opened_folder_level1, opened_folder_level2
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)

    directory = os.path.join("notes" , opened_folder_level1, value)
    print("Ausgewählter Ordner: " + directory)

    if value.endswith(".txt"):

        text_file = open(directory, "r")
        stuff = text_file.read()
        main_text.delete("1.0", END)
        main_text.insert(END, stuff)
        opened_file = directory
        label_filename.config(text=directory)
        print("Opened File: " + opened_file)        
    else:
        folder_level3 = os.listdir(directory)
        listbox_3.delete(0, END)
        for items in folder_level3:
            listbox_3.insert(0, items)
        opened_folder_level2 = value

listbox_2.bind('<<ListboxSelect>>', list_dir_2)

mainloop()