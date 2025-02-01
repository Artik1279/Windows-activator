import tkinter as tk
from tkinter import ttk
import os
import ctypes

def on_start():
    selected_os = os_choice.get()
    if selected_os == 0:
        ctypes.windll.user32.MessageBoxW(None, "You must choose one of versions.", "Warning", 0x00000000 | 0x00000030)
        return
    
    yesno = ctypes.windll.user32.MessageBoxW(None, "Now the activation commands for your OS will be executed. Confirm by pressing OK.", "Confirmation",0x00000001 | 0x00000040)
    if yesno == 1:
        print("yes")
        if selected_os == 1:
            run(7)
        elif selected_os == 2:
            run(8)
        elif selected_os == 3:
            run(10)
    else:
        print("no")
        return

def run(version):
    if version == 10:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    elif version == 8:
        os.system("slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9")
    elif version == 7:
        os.system("slmgr /ipk FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4")
    os.system("slmgr /skms kms.digiboy.ir")
    os.system("slmgr /ato")
    ctypes.windll.user32.MessageBoxW(None, "Activation commands have been successfully executed! To fully apply the changes, reboot your PC.", "Executed!", 0x00000000 | 0x00000040)


root = tk.Tk()
root.title("KMS Activation Windows")
root.geometry("350x200")

selection_frame = ttk.Frame(root)
selection_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

os_choice = tk.IntVar()

label = ttk.Label(selection_frame, text="Select your OS version:", font=("Arial", 12))
label.grid(row=1, column=0, columnspan=2, pady=10)

radio_button_7 = ttk.Radiobutton(selection_frame, text="Windows 7", variable=os_choice, value=1)
radio_button_7.grid(row=4, column=0, columnspan=2, pady=1, sticky="w")

radio_button_8 = ttk.Radiobutton(selection_frame, text="Windows 8.1", variable=os_choice, value=2)
radio_button_8.grid(row=3, column=0, columnspan=2, pady=1, sticky="w")

radio_button_10 = ttk.Radiobutton(selection_frame, text="Windows 10/11", variable=os_choice, value=3)
radio_button_10.grid(row=2, column=0, columnspan=2, pady=1, sticky="w")


start_button = ttk.Button(selection_frame, text="Activate", command=on_start, width=25)
start_button.grid(row=5, column=0, columnspan=2, pady=20)


selection_frame.columnconfigure(0, weight=1)
selection_frame.columnconfigure(1, weight=1)


result_frame = ttk.Frame(root)
result_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

result_label = ttk.Label(result_frame, text="ATTENTION! Works only on Pro versions of the system!", font=("Arial", 10), anchor=tk.CENTER)
result_label.pack(fill=tk.X, padx=5, pady=5)


root.mainloop()