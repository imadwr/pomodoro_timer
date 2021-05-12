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
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

# canvas
canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 120, image=tomato_img)
canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

# buttons
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# check marks

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
