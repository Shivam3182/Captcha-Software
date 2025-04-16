from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random
import string
import io

def generate_captcha_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_captcha_image(text):
    font = ImageFont.truetype("arial.ttf", 30)
    width, height = 160, 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for i in range(random.randint(1, 10)):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill='gray', width=1)

    draw.text((20, 10), text, font=font, fill=(0, 0, 0))

    return image

def refresh_captcha():
    global captcha_text
    captcha_text = generate_captcha_text()
    img = generate_captcha_image(captcha_text)
    img_tk = ImageTk.PhotoImage(img)
    captcha_label.config(image=img_tk)
    captcha_label.image = img_tk

def verify_captcha():
    user_input = entry.get()
    if user_input == captcha_text:
        result_label.config(text="Verified ✅", fg="green")
    else:
        result_label.config(text="Incorrect ❌", fg="red")

# GUI setup
root = Tk()
root.title("Captcha Software")
root.geometry("300x250")
root.resizable(False, False)

captcha_text = generate_captcha_text()
captcha_image = generate_captcha_image(captcha_text)
captcha_image_tk = ImageTk.PhotoImage(captcha_image)

captcha_label = Label(root, image=captcha_image_tk)
captcha_label.pack(pady=10)

entry = Entry(root, font=('Arial', 14))
entry.pack(pady=5)

verify_btn = Button(root, text="Verify", command=verify_captcha)
verify_btn.pack(pady=5)

refresh_btn = Button(root, text="Refresh Captcha", command=refresh_captcha)
refresh_btn.pack(pady=5)

result_label = Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()
