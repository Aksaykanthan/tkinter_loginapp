import tkinter

import customtkinter
import keyboard

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()

app.title("Logger")
app.state('zoomed') # Full Screen mode
app.overrideredirect(True) # Frameless
# app.wm_attributes('-topmost', True) # Always on top
# app.wm_attributes('-alpha', 0.9) # tranperent
# app.wm_attributes('-disabled', True) # disable Shortcuts
app.bind('<Alt_R><Pause>',lambda e :app.destroy()) # Closing Shortcut

def button_callback():
    print("Button click", purpose.get(),name.get(),password.get())

def hide_purpose():
    purpose.forget_pack()


big_frame = customtkinter.CTkFrame(master=app)
big_frame.pack(fill="both", expand=True)

frame_1 = customtkinter.CTkFrame(master=big_frame)
frame_1.pack(pady=20, padx=60, fill="both", expand=True, side=tkinter.LEFT)

frame_bg = tkinter.PhotoImage(file ='user.png')
pic = customtkinter.CTkLabel(frame_1, image=frame_bg)
# pic.place(x=0,y=0,relwidth=1,relheight=1)

frame_2 = customtkinter.CTkFrame(master=big_frame)
frame_2.pack(pady=20, padx=60, fill="both", expand=True, side=tkinter.RIGHT)

label_1 = customtkinter.CTkLabel(master=frame_2, justify=tkinter.LEFT,text = 'Sign Up')
label_1.grid(row = 0,column = 1)

name = customtkinter.CTkEntry(master=frame_2, placeholder_text="name")
name.grid(row = 1,column = 1)

password = customtkinter.CTkEntry(master=frame_2, placeholder_text="password")
password.grid(row = 2,column = 1)

role = customtkinter.CTkCheckBox(master=frame_2,text = 'login as Teacher',command =hide_purpose)
role.grid(row = 3,column = 1)

purpose = customtkinter.CTkComboBox(frame_2, values=["Preparing Question Paper", "Record Making", "Taking Notes"])
purpose.grid(row = 4,column = 1)

login_button = customtkinter.CTkButton(master=frame_2, command=button_callback,text = 'Login')
login_button.grid(row = 5,column = 1)

if __name__ == '__main__':
    app.mainloop()  
