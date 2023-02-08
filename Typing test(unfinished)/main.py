import tkinter 
import random


LIST_OF_SENTENCES = ["Gaming is really a workout for your mind disguised as fun. Studies have shown that playing video games regularly may increase gray matter in the brain and boost brain connectivity. (Gray matter is associated with muscle control, memories, perception, and spatial navigation.)",

"Minecraft is a place where your creativity can run wild. There is no one way to play this game, and what this means is that it appeals to a grander audience.The main component of the game is that the developers give you just enough to do things in the game. This sets the driving force in motion for creativity: being given a limited number of resources and turning it into something jaw-dropping.",

"Hollow Knight is a classically styled 2D action adventure across a vast interconnected world. Explore twisting caverns, ancient cities and deadly wastes; battle tainted creatures and befriend bizarre bugs; and solve ancient mysteries at the kingdom's heart.",

"In the practical art of war, the best thing of all is to take the enemy's country whole and intact; to shatter and destroy it is not so good. So, too, it is better to recapture an army entire than to destroy it, to capture a regiment, a detachment or a company entire than to destroy them."]



window = tkinter.Tk()
window.geometry("600x400")
window.config(padx=20,pady=20,bg="#AAE3E2")

paraghraph = random.choice(LIST_OF_SENTENCES)
# getting a text
frame = tkinter.Frame(window)
frame.pack(padx=20,pady=20)

text = tkinter.Text(frame)
text.insert(tkinter.END, paraghraph)
text.config(state="disabled", height=10, font=("Courier New", 16, "bold"), wrap=tkinter.WORD)
text.pack()

# making an entry
def on_key(event):
    if event.keysym == "space":
        text = event.widget.get("1.0", "end-1c")
        word = text.split()[-1]
        if word in paraghraph:
            print("Correct!")
        else:
            print("Incorrect!")

typing_area = tkinter.Text(window)
typing_area.config(height=7, font=("Courier New", 16, "bold"), wrap=tkinter.WORD)
typing_area.bind("<Key>", on_key)
typing_area.pack()





window.mainloop()



