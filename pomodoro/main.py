from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset() :
    window.after_cancel(timer)
    timer_text.config(text= "Timer" , fg = GREEN)
    canvas.itemconfig(countdown_text , text= "00:00")
    tick.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer() :
    global reps
    wm = WORK_MIN
    sb = SHORT_BREAK_MIN
    lb = LONG_BREAK_MIN
    reps += 1

    if reps % 2 == 0 :
        count_down(sb * 60)
        timer_text.config(text ="break" , fg = PINK)
    elif reps % 8 == 0 :
        count_down(lb *60)
        timer_text.config(text ="break" , fg = RED)
    else :
        count_down(wm * 60)
        timer_text.config(text ="work" , fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count) :
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(countdown_text, text = f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000 , count_down , count - 1)
    else :
        start_timer()
        if reps % 2 == 0 and reps % 8 != 0 :
            tick_text = ""
            tick_text += "✔"
            tick.config(text = tick_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 , bg=YELLOW)


canvas = Canvas(width=200 , height=224 , bg=YELLOW , highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100 , 112 ,image = photo)
countdown_text = canvas.create_text(100 , 130 , font=(FONT_NAME, 35, "bold"), fill= "white" , text="00:00")
canvas.grid(column = 1 , row = 1)
timer_text = Label(text="Timer" , fg=GREEN , font=(FONT_NAME , 40 , "bold") , bg=YELLOW)
timer_text.grid(column = 1 , row = 0)
start_button = Button(text="Start" , width=6 , command=start_timer)
start_button.grid(column = 0 , row = 2)
reset_button = Button(text="Reset" , width=6 , command= reset)
reset_button.grid(column = 2 , row = 2)
tick = Label(bg=YELLOW , fg=GREEN , font=(FONT_NAME , 10 , "bold"))
tick.grid(column = 1 , row = 3)




window.mainloop()
