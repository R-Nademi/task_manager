from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import IntVar, StringVar
from model.file_manager import *
from model.task import Task

task_list = []


def load_data():
    global task_list
    read_from_file()

    for task in task_list:
        table.insert("", END, values=task.to_tuple())


def reset_form():
    if task_list:
        id.set(max(task.id for task in task_list) + 1)
    else:
        id.set(1)
    title.set("")
    description.set("")
    start_time.set("")
    end_time.set("")
    assignee.set("")


def save_btn_click():
    task = Task(id.get(), title.get(), description.get(),
                start_time.get(), end_time.get(), assignee.get())
    errors = task.validate()
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        # Check if this is a new task or editing existing one
        existing_task = next((t for t in task_list if t.id == id.get()), None)
        if existing_task:
            msg.showerror("Error", "این شناسه قبلا استفاده شده است!")
        else:
            task_list.append(task)
            write_to_file(task_list)
            msg.showinfo("Saved", "تسک با موفقیت ذخیره شد")
            load_data()
            reset_form()


def table_select(event): # noqa
    selected = table.item(table.focus())["values"]
    if selected:
        id.set(selected[0])
        title.set(selected[1])
        description.set(selected[2])
        start_time.set(selected[3])
        end_time.set(selected[4])
        assignee.set(selected[5])


def edit_btn_click():
    selected_id = id.get()
    if not selected_id:
        msg.showerror("Error", "لطفاً یک تسک را انتخاب کنید")
        return

    # Find the task to edit
    task_index = None
    for i, task in enumerate(task_list):
        if task.id == selected_id:
            task_index = i
            break

    if task_index is not None:
        updated_task = Task(selected_id, title.get(), description.get(),
                            start_time.get(), end_time.get(), assignee.get())
        errors = updated_task.validate()
        if errors:
            msg.showerror("Errors", "\n".join(errors))
        else:
            task_list[task_index] = updated_task
            write_to_file(task_list)
            msg.showinfo("Updated", "تسک با موفقیت ویرایش شد")
            load_data()
            reset_form()
    else:
        msg.showerror("Error", "تسک انتخاب شده یافت نشد")


def remove_btn_click():
    selected_id = id.get()
    if not selected_id:
        msg.showerror("Error", "لطفاً یک تسک را انتخاب کنید")
        return

    confirm = msg.askyesno("Confirm", "آیا مطمئن هستید که می‌خواهید این تسک را حذف کنید؟")
    if confirm:
        for i, task in enumerate(task_list):
            if task.id == selected_id:
                del task_list[i]
                write_to_file(task_list)
                msg.showinfo("Deleted", "تسک با موفقیت حذف شد")
                load_data()
                reset_form()
                return

        msg.showerror("Error", "تسک انتخاب شده یافت نشد")


# GUI Setup
window = Tk()
window.title("مدیریت تسک‌ها")
window.geometry("1000x400")

# Variables
id = IntVar() # noqa
title = StringVar()
description = StringVar()
start_time = StringVar()
end_time = StringVar()
assignee = StringVar()

# Form Fields
Label(window, text="شناسه:").place(x=20, y=20)
Entry(window, textvariable=id, state="readonly").place(x=120, y=20)

Label(window, text="عنوان:").place(x=20, y=60)
Entry(window, textvariable=title).place(x=120, y=60)

Label(window, text="توضیحات:").place(x=20, y=100)
Entry(window, textvariable=description).place(x=120, y=100)

Label(window, text="زمان شروع:").place(x=20, y=140)
Entry(window, textvariable=start_time).place(x=120, y=140)

Label(window, text="زمان پایان:").place(x=20, y=180)
Entry(window, textvariable=end_time).place(x=120, y=180)

Label(window, text="مسئول:").place(x=20, y=220)
Entry(window, textvariable=assignee).place(x=120, y=220)

# Table
table = ttk.Treeview(window, columns=("id", "title", "desc", "start", "end", "assignee"), show="headings")
table.heading("id", text="شناسه")
table.heading("title", text="عنوان")
table.heading("desc", text="توضیحات")
table.heading("start", text="زمان شروع")
table.heading("end", text="زمان پایان")
table.heading("assignee", text="مسئول")

table.column("id", width=50)
table.column("title", width=120)
table.column("desc", width=200)
table.column("start", width=100)
table.column("end", width=100)
table.column("assignee", width=100)

table.bind("<<TreeviewSelect>>", table_select)
table.place(x=300, y=20, height=350)

# Buttons
Button(window, text="ذخیره", width=10, command=save_btn_click).place(x=20, y=260)
Button(window, text="ویرایش", width=10, command=edit_btn_click).place(x=120, y=260)
Button(window, text="حذف", width=10, command=remove_btn_click).place(x=20, y=300)
Button(window, text="جدید", width=10, command=reset_form).place(x=120, y=300)

# Initialize
load_data()
reset_form()

window.mainloop()