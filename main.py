from tkinter import *
import requests

quote = ""


def get_quote():
    """Access API, gets quote and updates Canvas text"""
    global quote
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


# Setting up the screen
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Setting background and texts to display
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Adding image and button layout
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()
window.mainloop()
