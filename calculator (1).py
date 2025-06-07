import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "×":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:
                raise ZeroDivisionError("Chia cho 0 không hợp lệ!")
            result = num1 / num2
        else:
            raise ValueError("Vui lòng chọn phép toán!")

        result_label.config(text=f"Kết quả: {result:.2f}")
    except ValueError as e:
        if str(e).startswith("Vui lòng chọn"):
            messagebox.showerror("Lỗi", str(e))
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
    except ZeroDivisionError as e:
        messagebox.showerror("Lỗi", str(e))

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_var.set("+") 
    result_label.config(text="Kết quả: ")

root = tk.Tk()
root.title("MÁY TÍNH ĐƠN GIẢN")
root.geometry("400x500")  
root.configure(bg="#D3D3D3")  


frame = tk.Frame(root, bg="#DDD8D8", padx=20, pady=20, relief="flat", bd=0)
frame.pack(pady=20, padx=20, fill="both", expand=True)


tk.Label(frame, text="Số thứ nhất:", bg="#FFFFFF", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w")
entry1 = tk.Entry(frame, width=20, font=("Arial", 14), bd=1, relief="solid")
entry1.grid(row=1, column=0, pady=5)


tk.Label(frame, text="Số thứ hai:", bg="#FFFFFF", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="w")
entry2 = tk.Entry(frame, width=20, font=("Arial", 14), bd=1, relief="solid")
entry2.grid(row=3, column=0, pady=5)


operation_frame = tk.Frame(frame, bg="#FFFFFF")
operation_frame.grid(row=4, column=0, pady=10)

operation_var = tk.StringVar(value="+")
operations = ["+", "-", "×", "÷"]
for i, op in enumerate(operations):
    tk.Radiobutton(operation_frame, text=op, variable=operation_var, value=op, bg="#B4B1B1", font=("Arial", 12), indicatoron=0, width=5, bd=1, relief="solid").grid(row=0, column=i, padx=5)

result_label = tk.Label(frame, text="Kết quả: ", bg="#FFFFFF", font=("Arial", 12, "bold"))
result_label.grid(row=5, column=0, pady=10)

tk.Button(frame, text="Tính", command=calculate, bg="#D3D3D3", font=("Arial", 12), bd=1, relief="solid", width=10).grid(row=6, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset, bg="#D3D3D3", font=("Arial", 12), bd=1, relief="solid", width=10).grid(row=7, column=0, pady=10)


root.mainloop()