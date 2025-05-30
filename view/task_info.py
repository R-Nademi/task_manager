from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import IntVar, StringVar
from model.file_manager import *
from model.task import Task

task_list = [] # todo :
# read_from_file()



def load_data(task_list):
    task_list = read_from_file()


    for row in table.get_children():
        table.delete(row)
    for task in task_list:
        table.insert("", END, values=task.to_tuple())


def reset_form():
    id.set(len(task_list) + 1)
    title.set("")
    description.set("")
    start_time.set("")
    end_time.set("")
    assignee.set("")
    load_data(task_list)


def save_btn_click():
    task = Task(id.get(), title.get(), description.get(), start_time.get()
            , end_time.get(), assignee.get())
    errors = task.validate()
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "task saved")
        task_list.append(task)
        write_to_file( task_list)
        reset_form()


def table_select(x):
    selected = table.item(table.focus())["values"]
    if selected:
        selected_task = Task(*selected)
        if selected_task:
            id.set(selected_task.id)
            title.set(selected_task.title)
            description.set(selected_task.description)
            start_time.set(selected_task.star_time)
            end_time.set(selected_task.end_time)
            assignee.set(selected_task.assignee)


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("task Info")
window.geometry("800x270")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# title
Label(window, text="title").place(x=20, y=60)
title = StringVar()
Entry(window, textvariable=title).place(x=80, y=60)

# description
Label(window, text="description").place(x=20, y=100)
description = StringVar()
Entry(window, textvariable=description).place(x=80, y=100)

# start_time
Label(window, text="start_time").place(x=20, y=140)
start_time = StringVar()
Entry(window, textvariable=start_time).place(x=80, y=140)

# end-time
Label(window, text="end_time").place(x=20, y=140)
end_time = StringVar()
Entry(window, textvariable=end_time).place(x=80, y=140)

# assignee
Label(window, text="assignee").place(x=20, y=140)
assignee = StringVar()
Entry(window, textvariable=end_time).place(x=80, y=140)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="title")
table.heading(3, text="description")
table.heading(4, text="start time")
table.heading(5, text="end time")
table.heading(6, text="assignee")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()

window.mainloop()
