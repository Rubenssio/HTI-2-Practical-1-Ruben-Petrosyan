class Employee:
    def __init__(self, f_name, l_name,
                 *,
                 phone=None, email=None,
                 trial=False,
                 join_date=None, leave_date=None,
                 salary=None,
                 gender=None):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.email = email
        self.trial = trial
        self.join_date = join_date
        self.leave_date = leave_date
        self.salary = salary
        self.gender = gender

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split()
        if len(values) != 2:
            raise ValueError(
                'Full name must be a first name followed by a last name,\n'
                'if either first or last name consists of more than one word, set them separately'
            )
        self.f_name, self.l_name = values


if __name__ == '__main__':
    pass
