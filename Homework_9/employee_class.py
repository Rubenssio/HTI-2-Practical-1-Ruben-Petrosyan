class Employee:
    def __init__(self,
                 first_name, last_name,
                 *,
                 phone=None, email=None,
                 trial=False,
                 join_date=None, leave_date=None,
                 salary=None,
                 gender=None
                 ):
        self.fist_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.trial = trial
        self.join_date = join_date
        self.leave_date = leave_date
        self.salary = salary
        self.gender = gender

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split()
        if len(values) != 2:
            raise ValueError(
                'Full name must be a first name followed by a last name,\n'
                'if either first or last name consists of more than one word,'
                'set the first name and the last name separately'
            )
        self.first_name, self.last_name = values

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'

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
    pass
