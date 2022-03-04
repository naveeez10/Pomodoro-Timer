from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def time_reset():
    window.after_cancel(timer)
    main.config(text="Timer",fg = GREEN)
    canvas.itemconfig(timer_text,text = "00:00")
    check_box.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
checkmark = ""
def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        checkmark = ""
        if reps % 2 != 0 and reps % 8 != 0:
            for i in range(0,(reps // 2) + 1):
                checkmark = ''.join((checkmark,'✔'))
        check_box.config(text = checkmark)
        decide()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def decide():
    work_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    global reps
    if(reps != 0):
        return
    reps += 1    
    now = reps % 8
    if now == 0:
        main.config(text = "Break Time",fg = RED,font=(FONT_NAME,40,"bold"),bg=YELLOW)
        count_down(long_break_sec)
    elif now % 2 == 0:
        main.config(text = "Break Time",fg = PINK,font=(FONT_NAME,40,"bold"),bg=YELLOW)
        count_down(short_break_sec)
    else:
        main.config(text = "Work Time",fg = GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)
        count_down(work_sec)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)

main = Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)
main.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

check_box = Label(text=checkmark)
check_box.grid(row=3,column=1)

start_butt=Button(text="Start",width=6,command=(decide))
start_butt.grid(row=2,column=0)

reset_butt=Button(text="Reset",width=6,command = time_reset)
reset_butt.grid(row=2,column=2)


window.mainloop()
