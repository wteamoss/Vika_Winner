import tkinter as tk


usd_to_uah_rate = 37.5 

def convert_currency():
    try:
        usd_amount = float(entry_usd.get())
        uah_amount = usd_amount * usd_to_uah_rate
        label_result.config(text=f"{usd_amount} доларів = {uah_amount:.2f} гривень")
    except ValueError:
        label_result.config(text="Введіть правильну числову суму!")


window = tk.Tk()
window.title("Конвертер валют")


label_title = tk.Label(window, text="Конвертер доларів у гривні", font=("Arial", 16))
label_title.pack(pady=10)


label_prompt = tk.Label(window, text="Введіть суму в доларах:")
label_prompt.pack()

entry_usd = tk.Entry(window)
entry_usd.pack(pady=5)


button_convert = tk.Button(window, text="Конвертувати", command=convert_currency)
button_convert.pack(pady=10)


label_result = tk.Label(window, text="")
label_result.pack(pady=10)


window.mainloop()
