from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    windows.after_cancel(timer)
    labeltimer.config(text="Timer", fg = GREEN)
    canvas.itemconfig(timertext, text=f"00:00")
    checklist["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_Sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        labeltimer.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_Sec)
        labeltimer.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        labeltimer.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    #canvas memiliki perlakuan yang berbeda tidak bisa seperti label
    canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checklist["text"] = mark

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100,pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224, bg = YELLOW, highlightthickness=0)
tomatoimg = PhotoImage(file="./15. Pomodoro-App/tomato.png")
canvas.create_image(100,112, image=tomatoimg)
timertext = canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME,26,"bold"))
canvas.grid(column=1, row=1)


labeltimer = Label(text="Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME,35,"bold"))
labeltimer.grid(column=1, row=0)

startbutton = Button(text="Start", command=start_timer)
startbutton.grid(column=0, row=2)

resetbutton = Button(text="Reset", command=reset_timer)
resetbutton.grid(column=2, row=2)

checklist = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,15))
checklist.grid(column=1, row=3)
windows.mainloop()
