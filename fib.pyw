import tkinter; from tkinter import ttk, messagebox
import ctypes; ctypes.windll.shcore.SetProcessDpiAwareness (2)
import decimal as precision

#window setup:
app = tkinter.Tk ()

app.title ("Fibonacci")
app.resizable (False, False)
app.geometry ("400x300")

#fibonacci function:
def FIB_CALC (amount: str or int) -> None:
    try:
        precision.getcontext ().prec = 1 << 32
        amount = int (amount)
        
        a: int = precision.Decimal (0)
        b: int = precision.Decimal (1)

        for _ in range (amount - 1):
            a, b = b, a + b

        messagebox.showinfo (f"Result from {amount:,}:", f"{b:,}.")
    
    except Exception as E:
        messagebox.showerror ("Error", str (E).upper ())
        
#tkinter widgets:
ENTRY = ttk.Entry (app)
ENTRY.pack (pady = 20)

BUTTON = ttk.Button (app, text = "Calculate", command = lambda: FIB_CALC (ENTRY.get ()))
BUTTON.pack ()

#misc:
app.bind ("<Return>", lambda event: FIB_CALC (ENTRY.get ()))
app.bind ("<Escape>", lambda event: app.destroy () if messagebox.askquestion ("Exit", "Are you sure you want to quit?") == "yes" else None)

app.mainloop ()
