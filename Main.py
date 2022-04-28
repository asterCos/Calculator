import tkinter as tk

calculation = ""

## Calculation functons
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_calc.delete(1.0, "end")
    text_calc.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_calc.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_calc.insert(1.0, "ERROR")

def clear_field():
    global calculation
    calculation = ""
    text_calc.delete(1.0, "end")
    text_result.delete(1.0, "end")

def clear_last():
    global calculation
    calculation = ""
    text_calc.delete("end-2c")


## Window setup loop
root = tk.Tk()
root.title('Calculator')
root.iconbitmap(r"C:\Users\jlaw\Desktop\Code\Calculator\icon.ico")
root.resizable(width=False, height=False)
root.config(bg='#3D4252')

app_width = 460
app_height = 435
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


## Colors and Font
btn_grd = "#666F89"
back_grd = "#3D4252"
fr_grd = "#FFFFFF"
act_grd = "#D55E2D"
type = ("Bahnschrift", 14)


## Center app on screen
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

## Calculation window
text_calc = tk.Text(root, bd=4, relief=tk.RIDGE, height=2, width=38, font=type, bg=back_grd, fg=fr_grd, padx=12, pady=10)
text_calc.pack(pady=10)
text_calc.bind("<Key>", lambda e: "break")

## Result window
sum_frame = tk.Frame(root)
sum_frame.pack()
sum_frame.config(bg='#3D4252')

labelText=tk.StringVar()
labelText.set("Result: ")
labelDir=tk.Label(sum_frame, textvariable=labelText, height=4, bg=back_grd, fg=fr_grd, font=("Bahnschrift", 11))
labelDir.grid(row=0, column=0, padx=10)

text_result = tk.Text(sum_frame, relief=tk.FLAT, bd=4, height=1, width=24, font=type, bg=back_grd, fg=fr_grd)
text_result.grid(row=0, column=1, padx=2)

## Ignore padding and grid conflict
btn_frame = tk.Frame(root)
btn_frame.pack()
btn_frame.config(bg='#3D4252')

## 1st row
btn_1 = tk.Button(btn_frame, text="1", command=lambda: add_to_calculation(1), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_1.grid(row=0, column=0, padx=2)

btn_2 = tk.Button(btn_frame, text="2", command=lambda: add_to_calculation(2), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_2.grid(row=0, column=1, padx=2)

btn_3 = tk.Button(btn_frame, text="3", command=lambda: add_to_calculation(3), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_3.grid(row=0, column=2, padx=2)

## 2nd row
btn_4 = tk.Button(btn_frame, text="4", command=lambda: add_to_calculation(4), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_4.grid(row=1, column=0, pady=2, padx=2)

btn_5 = tk.Button(btn_frame, text="5", command=lambda: add_to_calculation(5), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_5.grid(row=1, column=1, pady=2, padx=2)

btn_6 = tk.Button(btn_frame, text="6", command=lambda: add_to_calculation(6), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_6.grid(row=1, column=2, pady=2, padx=2)

## 3rd row
btn_7 = tk.Button(btn_frame, text="7", command=lambda: add_to_calculation(7), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_7.grid(row=2, column=0, pady=2, padx=2)

btn_8 = tk.Button(btn_frame, text="8", command=lambda: add_to_calculation(8), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_8.grid(row=2, column=1, pady=2, padx=2)

btn_9 = tk.Button(btn_frame, text="9", command=lambda: add_to_calculation(9), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_9.grid(row=2, column=2, pady=2, padx=2)

## 4th row
btn_open = tk.Button(btn_frame, text="(", command=lambda: add_to_calculation("("), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_open.grid(row=3, column=0, pady=2, padx=2)

btn_0 = tk.Button(btn_frame, text="0", command=lambda: add_to_calculation(0), relief=tk.RIDGE, borderwidth=5, width=8, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, font=type)
btn_0.grid(row=3, column=1, pady=2, padx=2)

btn_close = tk.Button(btn_frame, text=")", command=lambda: add_to_calculation(")"), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_close.grid(row=3, column=2, pady=2, padx=2)

## 5th column
btn_plus = tk.Button(btn_frame, text="+", command=lambda: add_to_calculation("+"), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_plus.grid(row=0, column=3, pady=2, padx=2)

btn_minus = tk.Button(btn_frame, text="-", command=lambda: add_to_calculation("-"), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_minus.grid(row=1, column=3, pady=2, padx=2)

btn_mul = tk.Button(btn_frame, text="*", command=lambda: add_to_calculation("*"), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_mul.grid(row=2, column=3, pady=2, padx=2)

btn_div = tk.Button(btn_frame, text="/", command=lambda: add_to_calculation("/"), relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_div.grid(row=3, column=3, pady=2, padx=2)

## 5th row
btn_sum = tk.Button(btn_frame, text="=", command=evaluate_calculation, relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=18, font=type)
btn_sum.grid(row=4, column=2, columnspan=2, pady=2, padx=2)

btn_clear = tk.Button(btn_frame, text="C", command=clear_field, relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_clear.grid(row=4, column=0, pady=2, padx=2)

btn_clear_last = tk.Button(btn_frame, text="CE", command=clear_last, relief=tk.RIDGE, borderwidth=5, bg=btn_grd, fg=fr_grd, activebackground=act_grd, activeforeground=fr_grd, width=8, font=type)
btn_clear_last.grid(row=4, column=1, pady=2, padx=2)


root.mainloop()