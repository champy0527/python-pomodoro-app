from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(103, 132, text="00:00", font=(FONT_NAME, 36, "bold"), fill="White")
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 48))
timer_label.config(padx=0, pady=0, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightbackground=YELLOW)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightbackground=YELLOW)
reset_btn.grid(column=2, row=2)

tick_label = Label(text="✔", bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)

window.mainloop()
