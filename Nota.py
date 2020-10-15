from tkinter import *
from tkinter import simpledialog
import shutil
import os

root = Tk()
root.title("CMJ_Notes")
root.geometry("700x550")

dirname, filename = os.path.split(os.path.abspath(__file__))
opened_file = ""
opened_folder_level1 = ""
opened_folder_level2 = ""

def add_element(listbox):
    print(wert_folder_file.get())


    if listbox == "1":
        if wert_folder_file.get() == "folder":
            folder_name = simpledialog.askstring("Input", "Please give the folder a name:")

            folder_path = os.path.join("notes", folder_name)
            os.makedirs(folder_path)
            listbox_1.insert(END, folder_name)

            status.config(text="Created folder: " + folder_path)
            print("Create folder "+ folder_name+ " in textbox1 ")
        else:
            file_name = simpledialog.askstring("Input", "Please give the file a name:") + ".txt"

            file_path = os.path.join("notes", file_name)
            with open(file_path, "w") as file:
                file.write("")

            listbox_1.insert(END, file_name)
            
            status.config(text="Created file: " + file_path)
            print("Create file in textbox 1")
    elif listbox == "2":
        if wert_folder_file.get() == "folder":
            folder_name = simpledialog.askstring("Input", "Please give the folder a name:")

            folder_path = os.path.join("notes", opened_folder_level1, folder_name)
            os.makedirs(folder_path)
            listbox_2.insert(END, folder_name)

            status.config(text="Created folder: " + folder_path)
            print("Create folder "+ folder_name+ " in textbox2 ")
        else:
            file_name = simpledialog.askstring("Input", "Please give the file a name:") + ".txt"

            file_path = os.path.join("notes", opened_folder_level1,file_name)
            with open(file_path, "w") as file:
                file.write("")

            listbox_2.insert(END, file_name)

            status.config(text="Created file: " + file_path)
            print("Create file in textbox 2")
    elif listbox == "3":
        if wert_folder_file.get() == "folder":
            status.config(text="You cant make dictonarys up here! Haha Opfer")
        else:
            file_name = simpledialog.askstring("Input", "Please give the file a name:") + ".txt"

            file_path = os.path.join("notes", opened_folder_level1,opened_folder_level2,file_name)
            with open(file_path, "w") as file:
                file.write("")

            listbox_3.insert(END, file_name)

            status.config(text="Created file: " + file_path)
            print("Create file in textbox 2")

def delete_element(listbox):
    if listbox == "1":
        selected_item = listbox_1.get(listbox_1.curselection())
        selected_index = listbox_1.curselection()
        element_path = os.path.join("notes", selected_item)

        print("selected item 1: " + selected_item)
        deleted_status = "Deleted " + element_path

        if selected_item.endswith(".txt"):
            os.remove(element_path)
            
        else:
            shutil.rmtree(element_path)
        status.config(text=deleted_status)
        listbox_1.delete(selected_index)
            
    elif listbox == "2":
        selected_item = listbox_2.get(listbox_2.curselection())
        selected_index = listbox_2.curselection()
        element_path = os.path.join("notes", opened_folder_level1 ,selected_item)

        print("selected item 2: " + selected_item)
        deleted_status = "Deleted " + element_path

        if selected_item.endswith(".txt"):
            os.remove(element_path)
            
        else:
            shutil.rmtree(element_path)
        status.config(text=deleted_status)
        listbox_2.delete(selected_index)

    elif listbox == "3":
        selected_item = listbox_3.get(listbox_3.curselection())
        selected_index = listbox_3.curselection()
        element_path = os.path.join("notes", opened_folder_level1 , opened_folder_level2 ,selected_item)

        print("selected item 1: " + selected_item)
        deleted_status = "Deleted " + element_path

        if selected_item.endswith(".txt"):
            os.remove(element_path)
            
        else:
            shutil.rmtree(element_path)
        status.config(text=deleted_status)
        listbox_3.delete(selected_index)

#FRAME BUTTONS
frame_buttons_1 = Frame(master=root, background="blue")
frame_buttons_1.place(x=0, y=0, width=220, height=30)

button_1_add = Button(master=frame_buttons_1, text="ADD", command= lambda:add_element("1"))
button_1_add.place(x=0, y=0, width=35, height=25)
button_1_del = Button(master=frame_buttons_1, text="DEL", command= lambda:delete_element("1"))
button_1_del.place(x=40, y=0, width=35, height=25)
button_1_edit = Button(master=frame_buttons_1, text="EDIT")
button_1_edit.place(x=80, y=0, width=35, height=25)

button_1_move_left = Button(master=frame_buttons_1, text="<")
button_1_move_left.place(x=175, y=0, width=20, height=25)

button_1_move_right = Button(master=frame_buttons_1, text=">")
button_1_move_right.place(x=195, y=0, width=20, height=25)

frame_buttons_2 = Frame(master=root, background="blue")
frame_buttons_2.place(x=220, y=0, width=220, height=30)

button_2_add = Button(master=frame_buttons_2, text="ADD", command= lambda:add_element("2"))
button_2_add.place(x=0, y=0, width=35, height=25)
button_2_del = Button(master=frame_buttons_2, text="DEL", command= lambda:delete_element("2"))
button_2_del.place(x=40, y=0, width=35, height=25)
button_2_edit = Button(master=frame_buttons_2, text="EDIT")
button_2_edit.place(x=80, y=0, width=35, height=25)

button_2_move_left = Button(master=frame_buttons_2, text="<")
button_2_move_left.place(x=175, y=0, width=20, height=25)

button_2_move_right = Button(master=frame_buttons_2, text=">")
button_2_move_right.place(x=195, y=0, width=20, height=25)

frame_buttons_3 = Frame(master=root, background="blue")
frame_buttons_3.place(x=440, y=0, width=300, height=30)

button_3_add = Button(master=frame_buttons_3, text="ADD", command= lambda:add_element("3"))
button_3_add.place(x=0, y=0, width=35, height=25)
button_3_del = Button(master=frame_buttons_3, text="DEL", command= lambda:delete_element("3"))
button_3_del.place(x=40, y=0, width=35, height=25)
button_3_edit = Button(master=frame_buttons_3, text="EDIT")
button_3_edit.place(x=80, y=0, width=35, height=25)

wert_folder_file = StringVar()

radio_folder = Radiobutton(master=frame_buttons_3, text="Folder", value="folder", variable=wert_folder_file)
radio_folder.place(x=120, y=0)

radio_file = Radiobutton(master=frame_buttons_3, text="File", value="file", variable=wert_folder_file)
radio_file.place(x=185, y=0)

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
frame_main.place(x=0, y=230, width=700, height=25)

def save_file(event):
    global opened_file
    text_file = open(opened_file, "w")
    text_file.write(main_text.get(1.0, END))
    saved_message = "Saved file " + opened_file 
    status.config(text=saved_message)

root.bind('<F3>', save_file)

button_save = Button(master=frame_main, text="Save", command=lambda:save_file("fuck_arguments_needed"))
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
    listbox_2.delete(0, END)
    listbox_3.delete(0, END)
    for items in root:
        listbox_1.insert(END, items)

    status.config(text="Reloaded Elements")

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

        loaded_message = "Loaded file " + opened_file
        status.config(text=loaded_message)       
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
        loaded_message = "Loaded file " + opened_file
        status.config(text=loaded_message)        
    else:
        folder_level3 = os.listdir(directory)
        listbox_3.delete(0, END)

        for items in folder_level3:
            listbox_3.insert(0, items)
        opened_folder_level2 = value

listbox_2.bind('<<ListboxSelect>>', list_dir_2)

def list_dir_3(event):
    global opened_file, opened_folder_level1, opened_folder_level2
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)

    directory = os.path.join("notes" , opened_folder_level1, opened_folder_level2, value)
    print("Ausgewählter Ordner: " + directory)

    text_file = open(directory, "r")
    stuff = text_file.read()
    main_text.delete("1.0", END)
    main_text.insert(END, stuff)

    opened_file = directory

    label_filename.config(text=directory)
    loaded_message = "Loaded file " + opened_file
    status.config(text=loaded_message)
    print("Opened File: " + opened_file)        

listbox_3.bind('<<ListboxSelect>>', list_dir_3)

def open_explorer(event):
    dirname, filename = os.path.split(os.path.abspath(__file__))
    dirname = os.path.join(dirname,"notes")
    os.system(f'start {os.path.realpath(dirname)}')

root.bind('<F4>', open_explorer)
mainloop()