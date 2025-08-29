#code of User Interface
from tkinter import*   #imports every module
from PIL import Image, ImageTk  #By installing pillow module we can integrate PNG/jpg image inside the tkinter
import speech_to_text
import action

root = Tk()
root.title("Pyra🤖")
root.geometry("550x650")
root.resizable(False,False)  #cant resize -> fixed size
root.config(bg = "#2E2D2D")

#functions
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "User --> " + str(user_val) + "\n")
    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok":
        root.destroy()


def delete():
    text.delete("1.0", "end")
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "User --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok":
          root.destroy()

#frame
frame = LabelFrame(root, padx = 100, pady=7, borderwidth=3, relief="raised" )
frame.config(bg="#2E2D2D")
frame.grid(row=0, column=1, padx=55, pady=10)  #grid method

#text label
text_label = Label(frame, text="Your Smart AI Assistant", font =("comic Sans ms",14,"bold"), bg="#CE4DDB")
text_label.grid(row=0,column=0, padx=10, pady=10)

#Image 
image = Image.open("image/assistant.jpg")
photo = ImageTk.PhotoImage(image)
image_label = Label(frame,image=photo)
image_label.grid(row = 1, column=0, pady=10)

#Adding some text widget
text = Text(root, font=("courior 10 bold"), bg = "#CE4DDB")
text.grid(row=2,column=0)
text.place(x=88, y=375, width = 375, height = 100)

#Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#Buttons
Button1 = Button(root, text="Ask", bg="#A59ADB",pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=55, y=550)

Button2 = Button(root, text="Delete", bg="#A59ADB",pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button2.place(x=215, y=550)

Button1 = Button(root, text="Send", bg="#A59ADB",pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button1.place(x=385, y=550)

root.mainloop()