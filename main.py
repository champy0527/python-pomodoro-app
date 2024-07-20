from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#f1583f"
GREEN = "#359b44"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # Return to 25 once done debugging
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

sequence = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]
session_index = 0
work_sessions_completed = 0
timer = None
paused = False


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global session_index, work_sessions_completed
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    session_index = 0
    work_sessions_completed = 0
    num_checks = ""
    tick_label.config(text=num_checks)
    timer_label_text = "Timer"
    colour = GREEN
    timer_label.config(text=timer_label_text, fg=colour)


# ---------------------------- PAUSE AND UNPAUSE ----------------------------- #

def pause():
    global paused
    paused = not paused
    if paused:
        pause_unpause_btn.config(text="Unpause", fg="#359b44")
        window.after_cancel(timer)
    else:
        pause_unpause_btn.config(text="Pause", fg="#f36848")
        # Resume countdown with the remaining time by getting the existing time on screen
        current_time = canvas.itemcget(timer_text, 'text')
        # Split the current time by : because it is treated as a whole string
        current_time_list = current_time.split(":")
        # Convert the minutes and seconds to integer so that the start_timer will recalculate the time based on a string
        resume_minutes = int(current_time_list[0])
        resume_seconds = int(current_time_list[1])
        remaining_time = (resume_minutes * 60) + resume_seconds
        count_down(remaining_time)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global session_index, work_sessions_completed, paused
    if session_index % 2 == 1:
        """Updates the number of tick marks below"""
        work_sessions_completed += 1
        num_checks = "✔" * work_sessions_completed
        tick_label.config(text=num_checks)
        """Updates the text above whether BREAK or TIMER"""
        timer_label_text = "Break"
        colour = PINK
        if session_index == len(sequence) - 1:
            colour = RED
    elif session_index % 2 == 0:
        """Updates the text above whether BREAK or TIMER"""
        timer_label_text = "Timer"
        colour = GREEN
    timer_label.config(text=timer_label_text, fg=colour)
    count_down(sequence[session_index] * 60)  # Add the *60 to session index once done debugging


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global session_index, timer
    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    """Reflects the timer countdown on the widget"""
    countdown_text = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=countdown_text)
    if count > 0:
        if not paused:
            """Keeps the timer running"""
            timer = window.after(1000, count_down, count - 1)  # Use 1000 for 1 second interval
    else:
        session_index += 1
        if session_index >= len(sequence):
            if count > 0:
                timer = window.after(1000, count_down, count - 1)
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

spacing_label = Label(window, bg=YELLOW)
spacing_label.grid(column=1, row=2)

start_btn = Button(text="Start", highlightbackground=YELLOW, fg="#359b44", command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, fg="#f1583f", command=reset_timer)
reset_btn.grid(column=2, row=3)

pause_unpause_btn = Button(text="Pause", highlightbackground=YELLOW, fg="#f36848", command=pause)
pause_unpause_btn.grid(column=1, row=3)

tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
tick_label.grid(column=1, row=4)

window.mainloop()
