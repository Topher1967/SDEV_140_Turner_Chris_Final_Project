"""Assignment:
1: Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures.
The user should be able to enter a Celsius temperature, click a button, then see the
equivalent Fahrenheit temperature. Use the following formula to make the conversion(30 points):

F = 9/5 * C + 32

F is the Fahrenheit temperature, and C is the Celsius temperature.

You should sallow the user to enter a generic temperature,
and have two buttons -- one to treat the input as Fahrenheit and convert it to Celsius;
and one to treat the input as Celsius and convert it to Fahrenheit. """ 

#Function to destroy the Window
def exit():
    window.destroy()
# Function to convert Celcius to Farenheit 
def convert():
    myText = var.get()
    
    if myText == "F to C":
        f = int(e1.get())
        c = 5/9 *( f - 32)
        t1.config(state='normal')
        t1.delete('1.0', tk.END)
        t1.insert(tk.END,c)
        t1.config(state='disabled')
    else:
        c = int(e1.get())
        f = ((c*9)/(5))+32
        t1.config(state='normal')
        t1.delete('1.0', tk.END)
        t1.insert(tk.END,f)
        t1.config(state='disabled')

    
#Import tkinter set main Window
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#7dadfa")
window.resizable(width=False,height=False)
window.title('Celsius to Fahrenheit Converter!')
var = tk.StringVar() 
#Adding labels
l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 15),fg="white",bg="#0951b5")
l2= tk.Label(window,text="Enter temperature: ",font=("Arial", 10,"bold"),fg="white",bg="#2b7ced")
l3= tk.Label(window,text="Temperature is: ",font=("Arial", 10,"bold"),fg="white",bg="#2b7ced")
 
empty_l1 = tk.Label(window,bg="#7dadfa")
empty_l2 = tk.Label(window,bg="#7dadfa")
empty_l3 = tk.Label(window,bg="#7dadfa")
empty_l4 = tk.Label(window,bg="#7dadfa")
#Input for temperature 
e1= tk.Entry(window,font=('Arial',10))





#Buttons,radio buttons and text box
btn2 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)
r1 = tk.Radiobutton(window, text='Convert Celsius to Farenheit', variable=var, value='C to F', command=convert)

r2 = tk.Radiobutton(window, text='Convert Farenheit to Celsius', variable=var, value='F to C', command=convert)
r1.select()

 
t1=tk.Text(window,state="disabled",width=15,height=0)
# Pack for button and text box alignment 
l1.pack()
empty_l3.pack()
l2.pack()
e1.pack()
empty_l1.pack()
r1.pack()
r2.pack()
empty_l4.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()

#Infinite loop 
window.mainloop()
