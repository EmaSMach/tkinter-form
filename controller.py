from tkinter import Tk

from views.main_window import MainWindow
from models import Client
from db import Session, engine

session = Session()


class Controller:
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view

    def save(self):
        data = self.view.get_data()
        new_client = self.model(id=None, 
                                name=data['name'],
                                surname=data['surname'], 
                                address=data['address'],
                                phone=data['phone'])
        if new_client.is_valid():
            session.add(new_client)
            session.commit()
            self.view.show_message('Guardado', f'{new_client} guardado con éxito')
            self.view.clear_fields()
        else:
            self.view.show_error(
                'Error', 'Los datos ingresados son incorrectos')


def main():
    root = Tk()
    controller = Controller()
    view = MainWindow(controller=controller)
    model = Client
    controller.model = model
    controller.view = view
    view.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
