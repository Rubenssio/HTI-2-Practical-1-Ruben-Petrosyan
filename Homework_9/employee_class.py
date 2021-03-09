class Employee:
    def __init__(self,
                 first_name, last_name=None,
                 *,
                 phone=None, email=None,  # validate when setting
                 trial=False,
                 join_date=None, leave_date=None,  # time object
                 salary=None,  # $ in the front when printing
                 gender=None  # can be only M or F
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
                    join_date='2020.12.25',
                    salary=2000000,
                    gender='M')

    print(emp1)
