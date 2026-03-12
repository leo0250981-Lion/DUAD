from __future__ import annotations
from datetime import datetime, date

DATE_FMT = "%d/%m/%Y"


def validate_non_empty(text: str, field_name: str) -> str:
    if text is None or str(text).strip() == "":
        raise ValueError(f"{field_name} cannot be empty")
    return str(text).strip()


def validate_amount(value, field_name: str = "amount") -> float:
    try:
        num = float(value)
    except (TypeError, ValueError):
        raise TypeError(f"{field_name} must be a number")
    return num


def validate_date_ddmmyyyy(date_str: str) -> str:
    validate_non_empty(date_str, "date")
    try:
        datetime.strptime(date_str, DATE_FMT)
    except ValueError:
        raise ValueError("Invalid date format (use dd/mm/yyyy)")
    return date_str


def validate_not_future(date_str: str) -> str:
    validate_date_ddmmyyyy(date_str)
    d = datetime.strptime(date_str, DATE_FMT).date()
    if d > date.today():
        raise ValueError("Date cannot be in the future")
    return date_str
