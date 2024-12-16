from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from datetime import datetime
import os
import sys


def get_assets_path():
    
    if hasattr(sys, "_MEIPASS"):
        
        return Path(sys._MEIPASS) / "assets" / "frame0"
    else:
        
        return Path(__file__).parent / "assets" / "frame0"

ASSETS_PATH = get_assets_path(
    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def calculate_days():
    
    start_date = entry_1.get()
    end_date = entry_3.get()

    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        
        delta = end_date_obj - start_date_obj
        days_difference = delta.days

        entry_2.delete(0, "end")  
        entry_2.insert(0, str(days_difference))  
    except ValueError:
        entry_2.delete(0, "end")
        entry_2.insert(0, "Invalid date format")


window = Tk()
window.geometry("430x280")
window.configure(bg="#5DB92F")


canvas = Canvas(
    window,
    bg="#5DB92F",
    height=280,
    width=430,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)


canvas.create_text(
    222.0,
    36.0,
    anchor="nw",
    text="Tanggal Awal :",
    fill="#000000",
    font=("Inter Black", 12 * -1)
)

canvas.create_text(
    222.0,
    113.0,
    anchor="nw",
    text="Tanggal Akhir :",
    fill="#000000",
    font=("Inter Black", 12 * -1)
)

canvas.create_text(
    222.0,
    193.0,
    anchor="nw",
    text="Hasil:",
    fill="#000000",
    font=("Inter Black", 12 * -1)
)

def load_image(image_path: Path):
    if image_path.exists():
        return PhotoImage(file=image_path)
    else:
        print(f"Error: Gambar tidak ditemukan di {image_path}")
        return None


entry_image_1 = load_image(relative_to_assets("entry_1.png"))
if entry_image_1:
    entry_bg_1 = canvas.create_image(337.5, 200.5, image=entry_image_1)

entry_image_3 = load_image(relative_to_assets("entry_3.png"))
if entry_image_3:
    entry_bg_3 = canvas.create_image(316.5, 154.0, image=entry_image_3)

entry_image_2 = load_image(relative_to_assets("entry_2.png"))
if entry_image_2:
    entry_bg_2 = canvas.create_image(316.5, 76.0, image=entry_image_2)

button_image_1 = load_image(relative_to_assets("button_1.png"))
if button_image_1:
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=calculate_days,
        relief="flat"
    )
    button_1.place(x=222.0, y=232.0, width=81.0, height=31.0)

image_image_1 = load_image(relative_to_assets("image_1.png"))
if image_image_1:
    image_1 = canvas.create_image(111.0, 140.0, image=image_image_1)


entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=222.0, y=61.0, width=189.0, height=28.0)


entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place(x=222.0, y=139.0, width=189.0, height=28.0)


entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=264.0, y=186, width=147.0, height=29.0)

window.resizable(False, False)
window.mainloop()
