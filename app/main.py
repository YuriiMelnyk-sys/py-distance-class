from __future__ import annotations


class OnlineCourse:
    """Клас для представлення онлайн-курсу."""

    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Ініціалізація курсу.

        :param name: Назва курсу
        :param description: Опис курсу
        :param weeks: Тривалість у тижнях
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Перевести кількість днів у тижні (округлення вгору).

        :param days: Кількість днів
        :return: Кількість тижнів
        """
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Створити курс з словника.

        :param course_dict: Словник з ключами name, description, days
        :return: Об'єкт OnlineCourse
        """
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)

