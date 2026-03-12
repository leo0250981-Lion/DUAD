from __future__ import annotations
import PySimpleGUI as sg

from interfaces import main_window, add_category_window, add_movement_window
from logic import FinanceManager
from persistence import DATA_FILE, load_json, save_json


def movements_to_table_rows(fm: FinanceManager):
    rows = []
    for m in fm.movements:
        rows.append([m.date, m.title, f"{m.amount:.2f}", m.category, m.type])
    return rows


def autosave(fm: FinanceManager):
    save_json(DATA_FILE, fm.to_dict())


def load_manager() -> FinanceManager:
    data = load_json(DATA_FILE, default={})
    if not data:
        return FinanceManager()
    return FinanceManager.from_dict(data)


def main():
    fm = load_manager()
    window = main_window(movements_to_table_rows(fm))

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-EXIT-"):
            autosave(fm)
            break

        if event == "-REFRESH-":
            window["-TABLE-"].update(values=movements_to_table_rows(fm))

        if event == "-ADD_CAT-":
            w = add_category_window()
            while True:
                e, v = w.read()
                if e in (sg.WINDOW_CLOSED, "-CANCEL-"):
                    break
                if e == "-SAVE-":
                    try:
                        fm.add_category(v["-NAME-"], v["-COLOR-"])
                        autosave(fm)
                        sg.popup("Category added!", title="Success")
                        break
                    except Exception as ex:
                        sg.popup_error(str(ex))
            w.close()
            window["-TABLE-"].update(values=movements_to_table_rows(fm))

        if event in ("-ADD_EXP-", "-ADD_INC-"):
            kind = "Expense" if event == "-ADD_EXP-" else "Income"

            # Requirement: show error if no categories available
            if not fm.categories:
                sg.popup_error("No categories available. Please add a category first.")
                continue

            w = add_movement_window(kind, fm.list_categories())
            while True:
                e, v = w.read()
                if e in (sg.WINDOW_CLOSED, "-CANCEL-"):
                    break
                if e == "-SAVE-":
                    try:
                        if kind == "Income":
                            fm.add_income(
                                title=v["-TITLE-"],
                                amount=v["-AMOUNT-"],
                                category=v["-CATEGORY-"],
                                date_str=v["-DATE-"],
                            )
                        else:
                            fm.add_expense(
                                title=v["-TITLE-"],
                                amount=v["-AMOUNT-"],
                                category=v["-CATEGORY-"],
                                date_str=v["-DATE-"],
                            )

                        autosave(fm)
                        sg.popup(f"{kind} added!", title="Success")
                        break
                    except Exception as ex:
                        sg.popup_error(str(ex))
            w.close()
            window["-TABLE-"].update(values=movements_to_table_rows(fm))

    window.close()


if __name__ == "__main__":
    main()
