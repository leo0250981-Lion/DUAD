from __future__ import annotations
from datetime import date
import PySimpleGUI as sg


def today_str() -> str:
    return date.today().strftime("%d/%m/%Y")


def main_window(table_values):
    sg.theme("DarkBlue3")

    headings = ["Date", "Title", "Amount", "Category", "Type"]

    layout = [
        [sg.Text("Personal Finance Manager", font=("Arial", 16))],
        [
            sg.Button("Add Category", key="-ADD_CAT-"),
            sg.Button("Add Expense", key="-ADD_EXP-"),
            sg.Button("Add Income", key="-ADD_INC-"),
            sg.Button("Refresh", key="-REFRESH-"),
            sg.Button("Exit", key="-EXIT-"),
        ],
        [
            sg.Table(
                values=table_values,
                headings=headings,
                key="-TABLE-",
                auto_size_columns=True,
                justification="left",
                expand_x=True,
                expand_y=True,
                num_rows=12,
            )
        ],
        [sg.Text("Tip: Add at least one category before adding income/expense.")],
    ]

    return sg.Window("Finance Manager", layout, resizable=True, finalize=True)


def add_category_window():
    layout = [
        [sg.Text("Add Category", font=("Arial", 14))],
        [sg.Text("Name:"), sg.Input(key="-NAME-")],
        [sg.Text("Color (optional hex):"), sg.Input("#FFFFFF", key="-COLOR-", size=(12, 1)),
         sg.ColorChooserButton("Pick", target="-COLOR-")],
        [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-")],
    ]
    return sg.Window("Add Category", layout, modal=True, finalize=True)


def add_movement_window(kind: str, categories: list[str]):
    # kind: "Income" or "Expense"
    title = f"Add {kind}"

    layout = [
        [sg.Text(title, font=("Arial", 14))],
        [sg.Text("Date (dd/mm/yyyy):"), sg.Input(today_str(), key="-DATE-")],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", readonly=True, size=(25, 1))],
        [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-")],
    ]
    return sg.Window(title, layout, modal=True, finalize=True)
