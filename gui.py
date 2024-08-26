from pathlib import Path
from build.commandsForApp import*

from tkinter import Tk, Canvas, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
#change path to where you store assets file
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x550")
window.configure(bg = "#81B29A")


canvas = Canvas(
    window,
    bg = "#81B29A",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    41.0,
    fill="#27231E",
    outline="")

canvas.create_text(
    10.0,
    9.0,
    anchor="nw",
    text="PowerShell Script Runner",
    fill="#FFF5F5",
    font=("Alice Regular", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getDate(entry_1),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=76.0,
    width=330.0,
    height=37.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getComputerInfo(entry_1),
    relief="flat"
)
button_2.place(
    x=360.0,
    y=76.0,
    width=330.0,
    height=37.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.0,
    328.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=51.0,
    y=148.0,
    width=598.0,
    height=358.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    667.0,
    22.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
