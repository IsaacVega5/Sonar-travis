

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from fun import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("385x202")
window.configure(bg = "#D6E4E5")
window.title("Matriz transposer")

canvas = Canvas(
    window,
    bg = "#D6E4E5",
    height = 202,
    width = 385,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    37.0,
    32.0,
    anchor="nw",
    text="Ingrese su matriz:",
    fill="#497174",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    257.0,
    35.0,
    anchor="nw",
    text="Matriz resultado:",
    fill="#497174",
    font=("Inter Bold", 12 * -1)
)

canvas.create_rectangle(
    37.0,
    60.0,
    57.0,
    80.0,
    fill="#EFF5F5",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_1 = canvas.create_image(
    52.0,
    75.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=42.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_2 = canvas.create_image(
    90.0,
    75.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=80.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_3 = canvas.create_image(
    128.0,
    75.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=118.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_4 = canvas.create_image(
    52.0,
    112.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=42.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_5 = canvas.create_image(
    90.0,
    112.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=80.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_6 = canvas.create_image(
    128.0,
    112.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=118.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_7 = canvas.create_image(
    52.0,
    149.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=42.0,
    y=134.0,
    width=20.0,
    height=28.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_8 = canvas.create_image(
    90.0,
    149.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=80.0,
    y=134.0,
    width=20.0,
    height=28.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_9 = canvas.create_image(
    128.0,
    149.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=118.0,
    y=134.0,
    width=20.0,
    height=28.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_10 = canvas.create_image(
    266.0,
    75.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_10.place(
    x=256.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_11 = canvas.create_image(
    304.0,
    75.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_11.place(
    x=294.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_12 = canvas.create_image(
    342.0,
    75.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_12.place(
    x=332.0,
    y=60.0,
    width=20.0,
    height=28.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_13 = canvas.create_image(
    266.0,
    112.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_13.place(
    x=256.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_14 = canvas.create_image(
    304.0,
    112.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_14.place(
    x=294.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_15 = canvas.create_image(
    342.0,
    112.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_15.place(
    x=332.0,
    y=97.0,
    width=20.0,
    height=28.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_16 = canvas.create_image(
    266.0,
    149.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_16.place(
    x=256.0,
    y=134.0,
    width=20.0,
    height=28.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_17 = canvas.create_image(
    304.0,
    149.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_17.place(
    x=294.0,
    y=134.0,
    width=20.0,
    height=28.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_01.png"))
entry_bg_18 = canvas.create_image(
    342.0,
    149.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#EFF5F5",
    fg="#000716",
    highlightthickness=0,
    state='disabled' 
)
entry_18.place(
    x=332.0,
    y=134.0,
    width=20.0,
    height=28.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_txt([entry_1, entry_2, entry_3,entry_4, entry_5, entry_6,entry_7, entry_8, entry_9],
                               [entry_10, entry_11, entry_12,
                               entry_13, entry_14, entry_15,
                               entry_16,entry_17, entry_18]),
    relief="flat"
)
button_1.place(
    x=166.0,
    y=127.0,
    width=60.0,
    height=37.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: transpose_mx_gui([entry_1, entry_2, entry_3,
                                      entry_4, entry_5, entry_6,
                                      entry_7, entry_8, entry_9],
                                     [entry_10, entry_11, entry_12,
                                      entry_13, entry_14, entry_15,
                                      entry_16, entry_17, entry_18]),
    relief="flat"
)
button_2.place(
    x=167.0,
    y=62.0,
    width=60.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
