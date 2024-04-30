from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-list')
        self.root.geometry('750x500+400+200')

        self.labe1 = Label(self.root, text='To-Do-List-App',
                font='ariel, 25 bold', width=10,bd=5, bg='lightblue',fg='black')
        self.labe1.pack(side='top', fill= BOTH)

        self.label2 = Label(self.root, text='Add Task',
                font='ariel, 18 bold', width=10,bd=5, bg='lightblue',fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                font='ariel, 18 bold', width=10,bd=5, bg='lightblue',fg='black')
        self.label3.place(x=350, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=350, y=150)

        self.text = Text(self.root, bd=5, height=2, width=30, font="ariel, 10 bold")
        self.text.place(x=20, y=170)

        # Priority options
        self.priorities = ['High', 'Medium', 'Low']

        # Priority label and dropdown menu
        self.priority_label = Label(self.root, text='Priority:',
                                    font='ariel, 12 bold', bd=5, bg='lightblue', fg='black')
        self.priority_label.place(x=20, y=140)

        self.priority_var = StringVar(self.root)
        self.priority_var.set(self.priorities[0])  # Default priority
        self.priority_menu = OptionMenu(self.root, self.priority_var, *self.priorities)
        self.priority_menu.config(width=8, font='ariel, 10 bold')
        self.priority_menu.place(x=100, y=140)

        # Due date label and entry field
        self.due_date_label = Label(self.root, text='Due Date (YYYY-MM-DD):',
                                    font='ariel, 12 bold', bd=5, bg='lightblue', fg='black')
        self.due_date_label.place(x=20, y=200)

        self.due_date_entry = Entry(self.root, bd=5, width=15, font="ariel, 10 bold")
        self.due_date_entry.place(x=200, y=200)

        # Add button
        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                    width=10,bd=5, bg='lightblue', fg='black', command=self.add)  
        self.button.place(x=30, y=240)

        # Delete button
        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                    width=10,bd=5, bg='lightblue', fg='black', command=self.delete)  
        self.button2.place(x=30, y=340)

        self.button3 = Button(self.root, text="Mark as Completed", font='sarif, 12 bold',
                    width=15,bd=5, bg='lightblue', fg='black', command=self.mark_completed)  
        self.button3.place(x=20, y=300)
                
    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)

    def delete(self):
        delete_ = self.main_text.curselection()
        look = self.main_text.get(delete_)
        with open('data.txt', 'r+') as f:
            new_f = f.readlines()
            f.seek(0) 
            for line in new_f:
                item = str(look)
                if item not in line:
                    f.write(line) 
            f.truncate()
        self.main_text.delete(delete_)

    def mark_completed(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            item = self.main_text.get(selected_index)
            self.main_text.itemconfig(selected_index, {'fg': 'gray'})  # Change text color
            # Implement additional logic to update data file or mark task as completed in some other way


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__== "__main__":
    main()


