from __future__ import annotations

from abc import ABC, abstractmethod
from statistics import mean
from typing import Any, Dict, List, Optional


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


class Performance(ABC):
    def __init__(self, subjects: List[str], scores: List[float]) -> None:
        self.subjects = subjects
        self.scores = scores

    @property
    def subjects(self) -> List[str]:
        return list(self.__subjects)

    @subjects.setter
    def subjects(self, value: List[str]) -> None:
        if not isinstance(value, list) or not all(isinstance(x, str) and x.strip() for x in value):
            raise ValueError("subjects must be a list of non-empty strings")
        self.__subjects = [x.strip() for x in value]

    @property
    def scores(self) -> List[float]:
        return list(self.__scores)

    @scores.setter
    def scores(self, value: List[float]) -> None:
        if not isinstance(value, list) or not all(isinstance(x, (int, float)) for x in value):
            raise ValueError("scores must be a list of numbers")
        self.__scores = [float(x) for x in value]

    @abstractmethod
    def average_score(self) -> float:
        ...


class ActualPerformance(Performance):
    def __init__(self, subjects: List[str], scores: List[float]) -> None:
        super().__init__(subjects, scores)
        self.__validate_alignment()

    def __validate_alignment(self) -> None:
        if len(self.subjects) != len(self.scores):
            raise ValueError("subjects and scores must have the same length")
        for s in self.scores:
            if s < 0 or s > 100:
                raise ValueError("each score must be in range 0..100")

    def average_score(self) -> float:
        return float(mean(self.scores)) if self.scores else 0.0


class DesiredPerformance(Performance):
    def __init__(self, subjects: List[str], desired_scores: List[float], target_average: Optional[float] = None) -> None:
        super().__init__(subjects, desired_scores)
        self.target_average = target_average

    @property
    def desired_scores(self) -> List[float]:
        return self.scores

    @property
    def target_average(self) -> Optional[float]:
        return self.__target_average

    @target_average.setter
    def target_average(self, value: Optional[float]) -> None:
        if value is None:
            self.__target_average = None
            return
        if not isinstance(value, (int, float)):
            raise ValueError("target_average must be a number or None")
        if value < 0 or value > 100:
            raise ValueError("target_average must be in range 0..100")
        self.__target_average = float(value)

    def average_score(self) -> float:
        if self.__target_average is not None:
            return float(self.__target_average)
        return float(mean(self.desired_scores)) if self.desired_scores else 0.0


class StudentData:
    def __init__(self, student: Student, actual: ActualPerformance, desired: DesiredPerformance) -> None:
        self.__student = student
        self.__actual = actual
        self.__desired = desired

    @property
    def student(self) -> Student:
        return self.__student

    @property
    def actual(self) -> ActualPerformance:
        return self.__actual

    @property
    def desired(self) -> DesiredPerformance:
        return self.__desired

    def to_dict(self) -> Dict[str, Any]:
        return {
            "student": {
                "full_name": self.student.full_name,
                "group_number": self.student.group_number,
                "birth_date": self.student.birth_date,
                "address": self.student.address,
            },
            "actual_performance": {
                "subjects": self.actual.subjects,
                "scores": self.actual.scores,
                "average_score": round(self.actual.average_score(), 2),
            },
            "desired_performance": {
                "desired_scores": self.desired.desired_scores,
                "desired_average_score": round(self.desired.average_score(), 2),
            },
        }


def main() -> None:
    # Will be implemented later
    pass


if __name__ == "__main__":
    main()