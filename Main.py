from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)

#height label
height_label = Label(text="Enter Your Height (cm)",font=("Arial",12,"bold"))
height_label.config(pady=10)
height_label.pack()

#height entry
height_entry = Entry()
height_entry.pack()

#weight label
weight_label = Label(text="Enter Your Weight (kg)",font=("Arial",12,"bold"))
weight_label.config(pady=10)
weight_label.pack()

#weight entry
weight_entry = Entry()
weight_entry.pack()

#Button
def calculate():
    try:
        bmi = int(weight_entry.get()) / (int(height_entry.get())/100) ** 2 
        if bmi < 18:
            result = f"Your BMI: {bmi:.2f}\nResult: Underweight"
        elif 18.5 <= bmi < 24.9:
            result = f"Your BMI: {bmi:.2f}\nResult: Normal Weight"
        elif 25 <= bmi < 29.9:
            result = f"Your BMI: {bmi:.2f}\nResult: Overweight"
        elif 30 <= bmi < 34.9:
            result = f"Your BMI: {bmi:.2f}\nResult: Obesity Class 1"
        elif 35 <= bmi < 39.9:
            result = f"Your BMI: {bmi:.2f}\nResult: Obesity Class 2"
        elif 40 <= bmi:
            result = f"Your BMI: {bmi:.2f}\nResult: Obesity Class 3"
        result_label.config(text=result)
    except ValueError:
        result= "Enter a valid number!"
        result_label.config(text=result)


calculate_button = Button(text="Calculate",command=calculate)
calculate_button.config(width=20,height=1)
calculate_button.pack(pady=10)

# result label
result_label = Label(text="", font=("Arial", 12, "bold"))
result_label.config(pady=20)
result_label.pack()

window.mainloop()