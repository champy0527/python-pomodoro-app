from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10  # Return to 25 once done debugging
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

sequence = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]
session_index = 0
work_sessions_completed = 0


# ---------------------------- TIMER RESET ------------------------------- #

# def reset_timer():
#     minutes = "00"
#     seconds = "00"
#     text = str(minutes) + ":" + str(seconds)
#     canvas.itemconfig(timer_text, text=text)
#     count = -1
#     if count > -1:
#         window.after(1000, count_down, count - 1)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global session_index, work_sessions_completed
    if session_index % 2 == 1:
        work_sessions_completed += 1
        print(work_sessions_completed)
        timer_label_text = "Break"
    elif session_index % 2 == 0:
        timer_label_text = "Timer"
    timer_label.config(text=timer_label_text)
    count_down(sequence[session_index])  # Add the *60 to session index once done debugging


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global session_index, work_sessions_completed
    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    countdown_text = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=countdown_text)
    if count > -1:
        window.after(200, count_down, count - 1)  # Use 1000 for 1 second interval
    else:
        session_index += 1
        if session_index >= len(sequence):
            if count > 0:
                window.after(500, count_down, count - 1)
            canvas.itemconfig(timer_text, text="00:00")
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(103, 132, text="00:00", font=(FONT_NAME, 36, "bold"), fill="White")
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 48))
timer_label.config(padx=0, pady=0, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightbackground=YELLOW)
reset_btn.grid(column=2, row=2)

tick_label = Label(text="✔", bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)

window.mainloop()
