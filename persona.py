class Persona:

    def __init__(self, documento=1, apellido='Torvalds', nombre='Linus'):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def display(self):
        return f'Persona: {self.documento} - {self.apellido}, {self.nombre}'


class PersonaService:

    def input(self, persona=Persona()):
        persona.documento = int(input('Ingrese documento: '))
        persona.apellido = input('Ingrese apellido: ')
        persona.nombre = input('Ingrese nombre: ')
