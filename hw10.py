from datetime import date


class Enterprise:
    pass



class People:
    def __init__(self, surname: str, name: str, patronymic: str, date_birth: date, number: int):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.date_birth = date_birth
        self.number = number


class Employee(People):
    def __init__(
            self, surname: str, name: str, patronymic: str, date_birth: date, number: int,
            id: int, department_code: int, salary: float):
        super().__init__(self, surname, name, patronymic, date_birth, number)
        self.id = id
        self.department_code = department_code
        self.salary = salary
