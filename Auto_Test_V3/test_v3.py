"""
AutoTest V3.
Esta versión hará lo mismo que la versión 2, pero con ficheros XML.
Se adjunta un fichero XML de muestra.

Tened en cuenta que el atributo name correspondiente a la pregunta podría no estar
y en este caso el nombre de la pregunta es la cadena vacía.

Autor: Héctor Cevallos Paredes
"""
import xml.etree.ElementTree as ET


class Question:
    def __init__(self, name, statement, options, points=1):
        self.__name = name
        self.__statement = statement
        self.__options = options
        self.__points = points

    @property
    def name(self):
        return self.__name

    @property
    def statement(self):
        return self.__statement

    @property
    def options(self):
        return self.__options

    @property
    def points(self):
        return self.__points

    def get_score(self, chosen_option):
        return self.__points * self.__options[chosen_option][1]


# Function para cargar las preguntas desde el archivo XML.

def load_questions_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    questions = []
    for q_elem in root.findall('question'):
        name = q_elem.get('name', '')
        base_score = float(q_elem.get('base_score', 1))
        statement = q_elem.find('statement').text.strip()
        options = [(opt.text.strip(), float(opt.get('weight'))) for opt in q_elem.findall('options/option')]
        question = Question(name, statement, options, base_score)
        questions.append(question)

    return questions


# Function para crear el test

def take_exam(questions):
    score = 0

    for i, question in enumerate(questions):
        print(f"Pregunta {i + 1}. {question.statement}")
        for j, option in enumerate(question.options):
            print(f"{j + 1}. {option[0]}")

        chosen_option = input("Indique la opción correcta (Pulse Intro para dejarla en blanco): ")

        if chosen_option:
            chosen_option = int(chosen_option) - 1
            score += question.get_score(chosen_option)

    return score


# Función principal actualizada para cargar las preguntas desde un archivo XML
def main():
    questions = load_questions_xml("questions.xml")
    score = take_exam(questions)
    print(f"Puntuación obtenida: {score} puntos.")


if __name__ == "__main__":
    main()
