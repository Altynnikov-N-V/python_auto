from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day: int
    month: str
    year: int
    subject: str
    hobby: str
    file_name: str
    address: str
    state: str
    city: str

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def date_of_birth(self) -> str:
        month, year, day = self.birthday
        return f'{int(day):02d} {month},{year}'

    @property
    def subjects(self) -> str:
        return f'{self.first_subject}, {self.second_subject[1]}'

    @property
    def state_city(self) -> str:
        state, city = self.user_location
        return f'{state} {city}'