import tkinter
import time
import tkinter.messagebox


window = tkinter.Tk()
window.geometry("800x600")
window.config(padx=20,pady=20)
window.state("zoomed")
window.title("DANGEROUS TEXT EDITOR")
Title = tkinter.Label(window,padx=20,pady=20,text="DANGEROUS TEXT EDITOR",font=("OPEN SANS",30,"bold"))
Title.pack()

text_area = tkinter.Text(window,width=500,wrap="word",font=("OPEN SANS",16))
text_area.pack()
text_area.focus()
last_key_release = time.time()

def on_key_release(event):
    global last_key_release
    last_key_release = time.time()

text_area.bind("<KeyRelease>", on_key_release)






while True:
    if time.time() - last_key_release > 3:
        window.config(background="#FF97C1")
        Title.config(background="#FF97C1")
        if time.time() - last_key_release > 5:
            window.config(background="#FF5858")
            Title.config(background="#FF5858")
            if time.time() - last_key_release > 7:
                window.config(background="#E0144C")
                Title.config(background="#E0144C")
                if time.time() - last_key_release > 10:
                    text_area.delete("1.0", "end")
                    last_key_release = time.time()
                    message = tkinter.messagebox.showinfo(title="LOL",message="OOPS IT TOOK YOU TOO LONG")
                    time.sleep(1)
    else:
        window.config(background="#F0F0F0")
        Title.config(background="#F0F0F0")

    
    window.update()



window.mainloop()