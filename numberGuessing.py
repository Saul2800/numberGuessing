import tkinter as tk
import random

num=random.randint(1,10)
guess=None
print(num)


#make a def to take another random number
def newrandom():
    global num
    num=random.randint(110)
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    random_color = random.choice(colors)
    window.configure(bg=random_color)
    label0.configure(background=random_color)
    label1.configure(background=random_color)   #change the color of label and window
    label2.configure(background=random_color)



def submit():
    global guess
    print(num)

    numberIn = numberInput.get()
    if numberIn.isdigit() and 1 <= int(numberIn) <= 10:
        label1.config(text="Number: " + numberIn)
        guess = int(numberIn)
        if guess!=num:
            label2.config(text="Nope, try again!")
        else:
            label2.config(text="YES you WIN!\nNow Try other")
            print("You win")
            newrandom()


    else:
        label1.config(text="Input a number from  1 to 10.")


#---------------------------------------------------
# TKINTER
window = tk.Tk()
window.geometry("400x200")
window.title("Guess the number")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="grey")
font_size = 14 
font = ("Arial", font_size)  # font and size

#---------------------------------------------------

# Make the title
label0 = tk.Label(window,text="Guess the number from 1 to 10", background="grey", font=font)
label0.pack()

# make the txt input
numberInput = tk.Entry(window,font=font,background="white")
numberInput.pack()

# make the button
buttonSubmit = tk.Button(window, text="OK", command=submit,padx=25,pady=15)
buttonSubmit.pack()

# make the label for show the input number
label1 = tk.Label(window, background="grey")
label1.pack()

#make the label for imput if you win or not
label2 = tk.Label(window, background="grey",font=font)
label2.pack()

#loop
window.mainloop()
