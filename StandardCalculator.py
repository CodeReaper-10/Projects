from tkinter import *

root = Tk()
root.title("Standard Calculator")
root.configure(bg="#abbdc2")
dexpr = ""
expr = ""
inputFieldDisplay = StringVar()
inp_fld = Entry(root, width=35, text = inputFieldDisplay, borderwidth=5, fg="white", bg="#545454")
inp_fld.grid(row=0, column=0, columnspan=4, padx=15, pady=15)
inp_fld.insert(0, 0)

def butn_clk(op):
    global expr
    global dexpr
    if op == "**0.5" and expr != "":
        dexpr = "√" + str("(" + dexpr + ")")
        inputFieldDisplay.set(dexpr)
        expr = "(" + expr + ")" + str(op)
    elif op == "**0.5" and expr == "":
        expr = "0"
        dexpr = "√" + str("(" + expr + ")")
        inputFieldDisplay.set(dexpr)
        expr = "(" + expr + ")" + str(op)
    elif op == "**2" and expr != "":
        dexpr = str("(" + dexpr + ")") + "^2"
        inputFieldDisplay.set(dexpr)
        expr = "(" + expr + ")" + str(op)
    elif op == "**2" and expr == "":
        expr = "0"
        dexpr = str("(" + expr + ")") + "^2"
        inputFieldDisplay.set(dexpr)
        expr = "(" + expr + ")" + str(op)
    elif op == "**(-1)" and expr != "":
        dexpr = "1/" + str("(" + dexpr + ")")
        inputFieldDisplay.set(dexpr)
        expr = "(" + expr + ")" + str(op)
    elif op == "**(-1)" and expr == "":
        inputFieldDisplay.set("Cannot divide by zero")
    elif op == "*(-1)":
        if expr != "":
            expr = expr + str(op)
            evaluate()
    else:
        dexpr = expr + str(op)
        expr = expr + str(op)
        inputFieldDisplay.set(expr)

def clr_mem():
    global expr
    global dexpr
    expr = ""
    dexpr = ""
    inputFieldDisplay.set("0")

def evaluate():
    global expr
    global dexpr
    if expr != "":
        result = str(eval(expr))
        inputFieldDisplay.set(result)
        expr = result
        dexpr = result
    else:
        inp_fld.delete(0, END)
        inp_fld.insert(0, 0)

butn0 = Button(root, text="0", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(0))
butn1 = Button(root, text="1", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(1))
butn2 = Button(root, text="2", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(2))
butn3 = Button(root, text="3", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(3))
butn4 = Button(root, text="4", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(4))
butn5 = Button(root, text="5", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(5))
butn6 = Button(root, text="6", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(6))
butn7 = Button(root, text="7", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(7))
butn8 = Button(root, text="8", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(8))
butn9 = Button(root, text="9", padx="25", pady="10", bg="#ccfffe", command=lambda: butn_clk(9))
butn10 = Button(root, text="÷", padx="25", pady="10", bg="#b7abc2", command=lambda: butn_clk("/"))
butn11 = Button(root, text="×", padx="25", pady="10", bg="#b7abc2", command=lambda: butn_clk("*"))
butn12 = Button(root, text="-", padx="26", pady="10", bg="#b7abc2", command=lambda: butn_clk("-"))
butn13 = Button(root, text="+", padx="25", pady="10", bg="#b7abc2", command=lambda: butn_clk("+"))
butn14 = Button(root, text="=", padx="25", pady="35", bg="#7ba377", command=evaluate)
butn15 = Button(root, text="+/-", padx="19", pady="10", bg="#d1c19d", command=lambda: butn_clk("*(-1)"))
butn16 = Button(root, text=".", padx="26", pady="10", bg="#d1c19d", command=lambda: butn_clk("."))
butn17 = Button(root, text="CLEAR", padx="76", pady="12", bg="#ab052c", fg="white", command=clr_mem)
butn18 = Button(root, text="1/x", padx="20", pady="10", bg="#d1c19d", command=lambda: butn_clk("**(-1)"))
butn19 = Button(root, text="x^2", padx="18", pady="10", bg="#d1c19d", command=lambda: butn_clk("**2"))
butn20 = Button(root, text="√x", padx="20", pady="10", bg="#d1c19d", command=lambda: butn_clk("**0.5"))

butn0.grid(row=5, column=1)
butn1.grid(row=4, column=0)
butn2.grid(row=4, column=1)
butn3.grid(row=4, column=2)
butn4.grid(row=3, column=0)
butn5.grid(row=3, column=1)
butn6.grid(row=3, column=2)
butn7.grid(row=2, column=0)
butn8.grid(row=2, column=1)
butn9.grid(row=2, column=2)
butn10.grid(row=1, column=3)
butn11.grid(row=2, column=3)
butn12.grid(row=3, column=3)
butn13.grid(row=4, column=3)
butn14.grid(row=5, column=3, rowspan=2)
butn15.grid(row=5, column=0)
butn16.grid(row=5, column=2)
butn17.grid(row=6, column=0, columnspan=3)
butn18.grid(row=1, column=0)
butn19.grid(row=1, column=1)
butn20.grid(row=1, column=2)

root.mainloop()
