from enum import Enum as Enum_


class Enum(Enum_):
    @classmethod
    def get_values(cls):
        return [value.value for value in cls]


class FixedExpensesEnum(Enum):
    ALQUILER = "Alquiler"
    GARAJE = "Garaje"
    OTROS = "Otros"


class CategoryExpenseEnum(Enum):
    FOOD = "Food"
    SHOPPING = "Shopping"
    WORK_SNACKS = "Work Snacks"
    GROCERIE = "Grocerie"
    EAT_OUT = "Eat_out"
    PHARMACY = "Pharmacy"
    HOLIDAY = "Holiday"
    EDUCATION = "Education"
    TRANSPORT = "Transport"
    GIFT = "Gift"
    OTHERS = "Others"
