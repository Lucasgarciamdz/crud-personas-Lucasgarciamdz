class Person:

    def __init__(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')

    def get_data(self):
        return f'Persona: {self.documento} - {self.apellido}, {self.nombre}'

    def write_data(self):
        with open("personal_data.txt", "w") as file:
            file.write(str(self.get_data()))
