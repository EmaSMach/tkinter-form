from tkinter import Tk, Frame, Entry, END
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


class MainWindow(Frame):
    def __init__(self, controller=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.title("Ingresar Datos")
        self.controller = controller
        self.make_widgets()

    def make_widgets(self):
        self.lbl_name = ttk.Label(self, text='Nombre:')
        self.lbl_surname = ttk.Label(self, text='Apellido:')
        self.lbl_address = ttk.Label(self, text='Dirección:')
        self.lbl_phone = ttk.Label(self, text='Tel/Cel:')

        self.en_name = ttk.Entry(self)
        self.en_surname = ttk.Entry(self)
        self.en_address = ttk.Entry(self)
        self.en_phone = ttk.Entry(self)

        self.btn_cancel = ttk.Button(self, text='Cancelar',
                                     command=self.on_cancel)
        self.btn_save = ttk.Button(self, text='Guardar',
                                   command=self.on_save)

        # placing
        self.lbl_name.grid(row=0, column=0)
        self.lbl_surname.grid(row=1, column=0)
        self.lbl_address.grid(row=2, column=0)
        self.lbl_phone.grid(row=3, column=0)

        self.en_name.grid(row=0, column=1)
        self.en_surname.grid(row=1, column=1)
        self.en_address.grid(row=2, column=1)
        self.en_phone.grid(row=3, column=1)

        self.btn_cancel.grid(row=4, column=0)
        self.btn_save.grid(row=4, column=1)

        # binding
        self.en_name.bind("<Return>", self.on_en_name_down_or_return)
        self.en_name.bind("<Down>", self.on_en_name_down_or_return)
        self.en_surname.bind("<Return>", self.on_en_surname_down_or_return)
        self.en_surname.bind("<Down>", self.on_en_surname_down_or_return)
        self.en_surname.bind("<Up>", self.on_en_surname_up)
        self.en_address.bind("<Return>", self.on_en_address_down_or_return)
        self.en_address.bind("<Down>", self.on_en_address_down_or_return)
        self.en_address.bind("<Up>", self.on_en_address_up)
        self.en_phone.bind("<Return>", self.on_en_phone_return)
        self.en_phone.bind("<Up>", self.on_en_phone_up)

    def on_save(self):
        self.controller.save()

    def on_cancel(self):
        self.master.destroy()

    def get_data(self):
        data = {
            'name': self.en_name.get(),
            'surname': self.en_surname.get(),
            'address': self.en_address.get() if self.en_address.get() else None,
            'phone': self.en_phone.get() if self.en_phone.get() else None,
        }
        return data

    def clear_fields(self):
        children = self.winfo_children()
        for child in children:
            if isinstance(child, Entry):
                child.delete(0, END)
        self.en_name.focus()

    def show_message(self, title, message):
        showinfo(title=title, message=message)

    def show_error(self, title, message):
        showerror(title=title, message=message)

    # ux functions
    def on_en_name_down_or_return(self, event):
        self.en_surname.focus()

    def on_en_surname_down_or_return(self, event):
        self.en_address.focus()

    def on_en_address_down_or_return(self, event):
        self.en_phone.focus()

    def on_en_phone_return(self, event):
        self.btn_save.invoke()

    def on_en_address_up(self, event):
        self.en_surname.focus()

    def on_en_phone_up(self, event):
        self.en_address.focus()

    def on_en_surname_up(self, event):
        self.en_name.focus()


def main():
    root = Tk()
    w = MainWindow(root)
    w.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
