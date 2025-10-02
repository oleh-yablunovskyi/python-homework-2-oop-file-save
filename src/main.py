from __future__ import annotations


class Student:
    def __init__(self, full_name: str, group_number: str, birth_date: str = "", address: str = "") -> None:
        self.full_name = full_name
        self.group_number = group_number
        self.birth_date = birth_date
        self.address = address

    # full_name
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("full_name must be a non-empty string")
        self.__full_name = value.strip()

    # group_number
    @property
    def group_number(self) -> str:
        return self.__group_number

    @group_number.setter
    def group_number(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("group_number must be a non-empty string")
        self.__group_number = value.strip()

    # birth_date
    @property
    def birth_date(self) -> str:
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value: str) -> None:
        if value is None:
            value = ""
        if not isinstance(value, str):
            raise ValueError("birth_date must be a string in YYYY-MM-DD or empty")
        self.__birth_date = value.strip()

    # address
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        if value is None:
            value = ""
        if not isinstance(value, str):
            raise ValueError("address must be a string")
        self.__address = value.strip()

def main() -> None:
    # Will be implemented later
    pass


if __name__ == "__main__":
    main()