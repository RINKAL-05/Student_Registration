import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# -----------------------------
# Functions
# -----------------------------

def submit_data():

    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    gender = gender_var.get()

    # Get selected course
    selected_course = course_listbox.curselection()

    if selected_course:
        course = course_listbox.get(selected_course[0])
    else:
        course = ""

    # Get hobbies
    hobbies = []

    if reading_var.get():
        hobbies.append("Reading")

    if music_var.get():
        hobbies.append("Music")

    if sports_var.get():
        hobbies.append("Sports")

    if gaming_var.get():
        hobbies.append("Gaming")

    # Validation
    if name == "":
        messagebox.showerror(
            "Error",
            "Please enter your name."
        )
        return

    if age == "":
        messagebox.showerror(
            "Error",
            "Please enter your age."
        )
        return

    if email == "":
        messagebox.showerror(
            "Error",
            "Please enter your email."
        )
        return

    if gender == "":
        messagebox.showerror(
            "Error",
            "Please select gender."
        )
        return

    if course == "":
        messagebox.showerror(
            "Error",
            "Please select a course."
        )
        return

    # Add data to table
    student_table.insert(
        "",
        "end",
        values=(
            len(student_table.get_children()) + 1,
            name,
            age,
            email,
            gender,
            course,
            ", ".join(hobbies)
        )
    )

    messagebox.showinfo(
        "Success",
        "Student registered successfully!"
    )

    clear_form()


def clear_form():

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    gender_var.set("")

    course_listbox.selection_clear(0, tk.END)

    reading_var.set(False)
    music_var.set(False)
    sports_var.set(False)
    gaming_var.set(False)


def exit_application():

    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit?"
    )

    if answer:
        root.destroy()


def show_about():

    messagebox.showinfo(
        "About",
        "Student Registration System\n"
        "Created using Python Tkinter"
    )


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("Student Registration System")
root.geometry("1000x700")

root.resizable(False, False)


# -----------------------------
# Menu
# -----------------------------

menu_bar = tk.Menu(root)

file_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

file_menu.add_command(
    label="Clear",
    command=clear_form
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=exit_application
)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)


help_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

help_menu.add_command(
    label="About",
    command=show_about
)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)

root.config(menu=menu_bar)


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="STUDENT REGISTRATION SYSTEM",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# -----------------------------
# Main Form Frame
# -----------------------------

form_frame = tk.Frame(root)

form_frame.pack(
    padx=20,
    pady=10
)


# -----------------------------
# Name
# -----------------------------

tk.Label(
    form_frame,
    text="Name:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

name_entry = tk.Entry(
    form_frame,
    width=35
)

name_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# -----------------------------
# Age
# -----------------------------

tk.Label(
    form_frame,
    text="Age:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

age_entry = tk.Entry(
    form_frame,
    width=35
)

age_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# -----------------------------
# Email
# -----------------------------

tk.Label(
    form_frame,
    text="Email:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

email_entry = tk.Entry(
    form_frame,
    width=35
)

email_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# -----------------------------
# Gender
# -----------------------------

tk.Label(
    form_frame,
    text="Gender:",
    font=("Arial", 12)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

gender_var = tk.StringVar()

gender_frame = tk.Frame(form_frame)

gender_frame.grid(
    row=3,
    column=1,
    sticky="w"
)

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male"
).pack(side="left")

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female"
).pack(side="left")

tk.Radiobutton(
    gender_frame,
    text="Other",
    variable=gender_var,
    value="Other"
).pack(side="left")


# -----------------------------
# Course Listbox
# -----------------------------

tk.Label(
    form_frame,
    text="Course:",
    font=("Arial", 12)
).grid(
    row=4,
    column=0,
    padx=10,
    pady=8,
    sticky="nw"
)

course_listbox = tk.Listbox(
    form_frame,
    height=4,
    width=32
)

course_listbox.grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)

courses = [
    "Python",
    "Data Science",
    "Web Development",
    "Data Analytics"
]

for course in courses:
    course_listbox.insert(
        tk.END,
        course
    )


# -----------------------------
# Hobbies
# -----------------------------

tk.Label(
    form_frame,
    text="Hobbies:",
    font=("Arial", 12)
).grid(
    row=5,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

hobbies_frame = tk.Frame(form_frame)

hobbies_frame.grid(
    row=5,
    column=1,
    sticky="w"
)

reading_var = tk.BooleanVar()
music_var = tk.BooleanVar()
sports_var = tk.BooleanVar()
gaming_var = tk.BooleanVar()


tk.Checkbutton(
    hobbies_frame,
    text="Reading",
    variable=reading_var
).pack(side="left")

tk.Checkbutton(
    hobbies_frame,
    text="Music",
    variable=music_var
).pack(side="left")

tk.Checkbutton(
    hobbies_frame,
    text="Sports",
    variable=sports_var
).pack(side="left")

tk.Checkbutton(
    hobbies_frame,
    text="Gaming",
    variable=gaming_var
).pack(side="left")


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Submit",
    width=12,
    command=submit_data
).pack(side="left", padx=5)


tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_form
).pack(side="left", padx=5)


tk.Button(
    button_frame,
    text="Exit",
    width=12,
    command=exit_application
).pack(side="left", padx=5)


# -----------------------------
# Student Table
# -----------------------------

table_frame = tk.Frame(root)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


columns = (
    "ID",
    "Name",
    "Age",
    "Email",
    "Gender",
    "Course",
    "Hobbies"
)

student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=8
)


for column in columns:

    student_table.heading(
        column,
        text=column
    )

    student_table.column(
        column,
        width=120
    )


student_table.pack(
    fill="both",
    expand=True
)


# -----------------------------
# Start Application
# -----------------------------

root.mainloop()