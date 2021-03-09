from datetime import date

from Homework_7.validator import validate_phone_number
from Homework_7.validator import validate_email


class Employee:
    def __init__(self,
                 first_name, last_name=None,
                 *,
                 phone=None, email=None,
                 trial=False,
                 join_date=None, leave_date=None,
                 salary=None,
                 gender=None
                 ):
        if last_name is None:
            self.full_name = first_name
        else:
            self.first_name = first_name
            self.last_name = last_name
        self.phone = phone
        self.email = email
        self.trial = trial
        self.join_date = join_date
        self.leave_date = leave_date
        self.salary = salary
        self.gender = gender

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value.strip()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value.strip()

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.strip().split()
        if len(values) != 2:
            raise ValueError(
                'Full name must be a first name followed by a last name,\n'
                '\t\t\tif either first or last name consists of more than one word,\n'
                '\t\t\tset the first name and the last name separately'
            )
        self.__first_name, self.__last_name = values

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if validate_phone_number(value.strip()):
            self.__phone = value.strip()
        else:
            raise ValueError('Phone number is not a valid Armenian phone number')

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if validate_email(value.strip()):
            self.__email = value.strip()
        else:
            raise ValueError('Email address is not a valid email address')

    @property
    def join_date(self):
        return self.__join_date

    @join_date.setter
    def join_date(self, value):
        if value:
            try:
                value = value.strip()
                separator = '-'
                for char in value:
                    if not char.isdigit():
                        separator = char
                        break
                value = list(map(int, value.split(separator)))
                self.__join_date = date(value[0], value[1], value[2])
            except (ValueError, IndexError):
                raise ValueError('The date must be in yyyy-mm-dd format')
        else:
            self.__join_date = None

    @property
    def leave_date(self):
        return self.__leave_date

    @leave_date.setter
    def leave_date(self, value):
        if value:
            try:
                value = value.strip()
                separator = '-'
                for char in value:
                    if not char.isdigit():
                        separator = char
                        break
                value = list(map(int, value.split(separator)))
                self.__leave_date = date(value[0], value[1], value[2])
            except (ValueError, IndexError):
                raise ValueError('The date must be in yyyy-mm-dd format')
        else:
            self.__leave_date = None

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value:
            if value.strip().upper() == 'M':
                self.__gender = 'M'

            elif value.strip().upper() == 'F':
                self.__gender = 'F'

            else:
                raise ValueError("Gender can be either 'M' or 'F'")
        else:
            self.__gender = None

    def __repr__(self):
        return f"""<Employee: {self.full_name.upper()}>
        \r\tPhone number: {self.phone}
        \r\t  Work Email: {self.email}
        \r\t       Trial: {'Passed' if self.trial else 'Not Passed'}
        \r\t   Join Date: {self.join_date}
        \r\t  Leave Date: {self.leave_date}
        \r\t      Salary: {'Classified' if self.salary else None}
        \r\t      Gender: {self.gender}"""

    def __bool__(self):
        return self.trial

    def __eq__(self, other):
        return self.email == other.email or self.phone == other.phone

    def __ne__(self, other):
        return not (self.email == other.email or self.phone == other.phone)

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary


if __name__ == '__main__':
    emp1 = Employee('Aram', 'Khachaturian',
                    phone='077123456',
                    email='Aram@yahoo.com',
                    trial=True,
                    join_date='2020-12-25',
                    salary=2000000,
                    gender='M')

    print(emp1)
