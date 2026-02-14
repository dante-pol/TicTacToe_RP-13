from src.model.entities import *

def show_field(cells: list[list[Cell]]):
    return (f"{cells[0][0].marker} | {cells[0][1].marker} | {cells[0][2].marker}\n"
            f"------------\n"
            f"{cells[1][0].marker} | {cells[1][1].marker} | {cells[1][2].marker}\n"
            f"------------\n"
            f"{cells[2][0].marker} | {cells[2][1].marker} | {cells[2][2].marker}\n")

def show_info(message: str):
    return f"{message}"