import dataclasses
from typing import Tuple

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birthday: Tuple[str, str, str]
    first_subject: str
    second_subject: Tuple[str, str]
    hobby: str
    file_name: str
    address: str
    user_location: Tuple[str, str]

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