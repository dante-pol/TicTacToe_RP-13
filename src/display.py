from src.model.entities import *

def show_field(cells: list[list[Cell]]):
    return (f"{cells[0][0].get_marker()} | {cells[0][1].get_marker()} | {cells[0][2].get_marker()}\n"
            f"------------\n"
            f"{cells[1][0].get_marker()} | {cells[1][1].get_marker()} | {cells[1][2].get_marker()}\n"
            f"------------\n"
            f"{cells[2][0].get_marker()} | {cells[2][1].get_marker()} | {cells[2][2].get_marker()}\n")

def show_error():
    pass

def show_info(message: str):
    return f"{message}"