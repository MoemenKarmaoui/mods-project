import customtkinter
import os
import threading
import requests
def save_path(path):
    with open("saved_path.txt", "w") as file:
        file.write(path)

def load_path():
    try:
        with open("saved_path.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def choose_path():
    chosen_path = customtkinter.filedialog.askdirectory()
    if chosen_path:
        path_var.set(chosen_path)
        save_path(chosen_path)

mods = {
    "carryon-forge-1.20.1-2.1.0.1.jar":"https://www.curseforge.com/api/v1/mods/274259/files/4628675/download",
    "CobbleForDays-1.8.0.jar":"https://www.curseforge.com/api/v1/mods/349460/files/4653625/download",
    "constructionwand-1.20.1-2.11.jar":"https://www.curseforge.com/api/v1/mods/399558/files/4684054/download",
    "flib-1.20.1-0.0.7.jar":"https://www.curseforge.com/api/v1/mods/661261/files/4647711/download",
    "ironchest-1.20.1-14.4.4.jar":"https://www.curseforge.com/api/v1/mods/228756/files/4614852/download",
    "ironfurnaces-1.20.1-4.1.3.jar":"https://www.curseforge.com/api/v1/mods/237664/files/4796731/download",
    "jei-1.20.1-forge-15.2.0.27.jar":"https://www.curseforge.com/api/v1/mods/238222/files/4712868/download",
    "journeymap-1.20.1-5.9.16-forge.jar":"https://www.curseforge.com/api/v1/mods/32274/files/4841242/download",
    "MoreVanillaArmor-1.20.1-5.1.0.jar":"https://www.curseforge.com/api/v1/mods/350955/files/4585003/download",
    "SimpleStorageNetwork-1.20.1-1.10.0.jar":"https://www.curseforge.com/api/v1/mods/268495/files/4648868/download",
    "EnchantmentDescriptions-Forge-1.20.1-17.0.9.jar":"https://www.curseforge.com/api/v1/mods/250419/files/4911103/download",
    "Bookshelf-Forge-1.20.1-20.1.6.jar":"https://www.curseforge.com/api/v1/mods/228525/files/4808092/download"
}
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def download_file(url, save_path):
    response = requests.get(url, stream=True)

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
def download_missing_mods(root2):
    for mod_name, mod_url in mods.items():
        mod_path = os.path.join(load_path(), f"{mod_name}")
        if not os.path.exists(mod_path):
            download_file(mod_url, mod_path)
    root2.destroy()
def check ():
    root2 = customtkinter.CTk()
    root2.geometry("500x650+400+20")
    root2.title("download manager")
    frame1 = customtkinter.CTkFrame(master=root2)
    frame1.pack(padx=15, pady=10, fill="both", expand=True)
    if os.path.exists(load_path() + "/carryon-forge-1.20.1-2.1.0.1.jar"):
        carry = customtkinter.CTkLabel(master=frame1, text="carryon-forge-1.20.1-2.1.0.1", font=("aloevera", 20),text_color='green')
        carry.pack(padx=12, pady=10)
        d1 = True
    else:
        carry = customtkinter.CTkLabel(master=frame1, text="carryon-forge-1.20.1-2.1.0.1", font=("aloevera", 20),text_color='red')
        carry.pack(padx=12, pady=10)
        d1 = False
    if os.path.exists(load_path() + "/CobbleForDays-1.8.0.jar"):
        cob = customtkinter.CTkLabel(master=frame1, text="CobbleForDays-1.8.0", font=("aloevera", 20), text_color='green')
        cob.pack(padx=12, pady=10)
        d2 = True
    else:
        cob = customtkinter.CTkLabel(master=frame1, text="CobbleForDays-1.8.0", font=("aloevera", 20), text_color='red')
        cob.pack(padx=12, pady=10)
        d2 = False

    if os.path.exists(load_path() + "/constructionwand-1.20.1-2.11.jar"):
        wand = customtkinter.CTkLabel(master=frame1, text="constructionwand-1.20.1-2.11", font=("aloevera", 20),text_color='green')
        wand.pack(padx=12, pady=10)
        d3= True
    else:
        wand = customtkinter.CTkLabel(master=frame1, text="constructionwand-1.20.1-2.11", font=("aloevera", 20),text_color='red')
        wand.pack(padx=12, pady=10)
        d3 = False
    if os.path.exists(load_path() + "/flib-1.20.1-0.0.7.jar"):
        lib = customtkinter.CTkLabel(master=frame1, text="flib-1.20.1-0.0.7", font=("aloevera", 20), text_color='green')
        lib.pack(padx=12, pady=10)
        d4= True
    else:
        lib = customtkinter.CTkLabel(master=frame1, text="flib-1.20.1-0.0.7", font=("aloevera", 20), text_color='red')
        lib.pack(padx=12, pady=10)
        d4 = False

    if os.path.exists(load_path() + "/ironchest-1.20.1-14.4.4.jar"):
        chest = customtkinter.CTkLabel(master=frame1, text="ironchest-1.20.1-14.4.4", font=("aloevera", 20),text_color='green')
        chest.pack(padx=12, pady=10)
        d5= True
    else:
        chest = customtkinter.CTkLabel(master=frame1, text="ironchest-1.20.1-14.4.4", font=("aloevera", 20), text_color='red')
        chest.pack(padx=12, pady=10)
        d5 = False

    if os.path.exists(load_path() + "/jei-1.20.1-forge-15.2.0.27.jar"):
        jei = customtkinter.CTkLabel(master=frame1, text="jei-1.20.1-forge-15.2.0.27", font=("aloevera", 20),text_color='green')
        jei.pack(padx=12, pady=10)
        d6= True
    else:
        jei = customtkinter.CTkLabel(master=frame1, text="jei-1.20.1-forge-15.2.0.27", font=("aloevera", 20), text_color='red')
        jei.pack(padx=12, pady=10)
        d6 = False

    if os.path.exists(load_path() + "/journeymap-1.20.1-5.9.16-forge.jar"):
        map = customtkinter.CTkLabel(master=frame1, text="journeymap-1.20.1-5.9.16-forge", font=("aloevera", 20),text_color='green')
        map.pack(padx=12, pady=10)
        d7= True
    else:
        map = customtkinter.CTkLabel(master=frame1, text="journeymap-1.20.1-5.9.16-forge", font=("aloevera", 20),text_color='red')
        map.pack(padx=12, pady=10)
        d7 = False

    if os.path.exists(load_path() + "/MoreVanillaArmor-1.20.1-5.1.0.jar"):
        armo = customtkinter.CTkLabel(master=frame1, text="MoreVanillaArmor-1.20.1-5.1.0", font=("aloevera", 20),text_color='green')
        armo.pack(padx=12, pady=10)
        d8= True
    else:
        armo = customtkinter.CTkLabel(master=frame1, text="MoreVanillaArmor-1.20.1-5.1.0", font=("aloevera", 20),text_color='red')
        armo.pack(padx=12, pady=10)
        d8 = False

    if os.path.exists(load_path() + "/SimpleStorageNetwork-1.20.1-1.10.0.jar"):
        stor = customtkinter.CTkLabel(master=frame1, text="SimpleStorageNetwork-1.20.1-1.10.0", font=("aloevera", 20),text_color='green')
        stor.pack(padx=12, pady=10)
        d9= True
    else:
        stor = customtkinter.CTkLabel(master=frame1, text="SimpleStorageNetwork-1.20.1-1.10.0", font=("aloevera", 20),text_color='red')
        stor.pack(padx=12, pady=10)
        d9 = False

    if os.path.exists(load_path() + "/Bookshelf-Forge-1.20.1-20.1.6.jar"):
        book = customtkinter.CTkLabel(master=frame1, text="Bookshelf-Forge-1.20.1-20.1.6", font=("aloevera", 20),text_color='green')
        book.pack(padx=12, pady=10)
        d10= True
    else:
     book = customtkinter.CTkLabel(master=frame1, text="Bookshelf-Forge-1.20.1-20.1.6", font=("aloevera", 20),text_color='red')
     book.pack(padx=12, pady=10)
     d10 = False

    if os.path.exists(load_path() + "/ironfurnaces-1.20.1-4.1.3.jar"):
        fur = customtkinter.CTkLabel(master=frame1, text="ironfurnaces-1.20.1-4.1.3", font=("aloevera", 20),text_color='green')
        fur.pack(padx=12, pady=10)
        d11= True
    else:
        fur = customtkinter.CTkLabel(master=frame1, text="ironfurnaces-1.20.1-4.1.3", font=("aloevera", 20), text_color='red')
        fur.pack(padx=12, pady=10)
        d11 = False

    if os.path.exists(load_path() + "/EnchantmentDescriptions-Forge-1.20.1-17.0.9.jar"):
        Ench = customtkinter.CTkLabel(master=frame1, text="EnchantmentDescriptions-Forge-1.20.1-17.0.9",font=("aloevera", 20), text_color='green')
        Ench.pack(padx=12, pady=10)
        d12= True
    else:
        Ench = customtkinter.CTkLabel(master=frame1, text="EnchantmentDescriptions-Forge-1.20.1-17.0.9", font=("aloevera", 20),text_color='red')
        Ench.pack(padx=12, pady=10)
        d12 = False
    if d1 == True and d2 == True and d3 == True and d4 == True and d5 == True and d6 == True and d7 == True and d8 == True and d9 == True and d10 == True and d11 == True and d12 == True :
        CBut = customtkinter.CTkButton(master=frame1, text="Mods Complete (close)", font=("Mouldy Cheese", 15),text_color="#A20183", command=lambda :[root.destroy(),root2.destroy()])
        CBut.pack(padx=12, pady=10, fill="x")
    else :
        DBut = customtkinter.CTkButton(master=frame1, text="Download missing Mods", font=("Mouldy Cheese", 15),text_color="#A20183", command=lambda :download_missing_mods(root2))
        DBut.pack(padx=12, pady=10, fill="x")
    root2.mainloop()



root = customtkinter.CTk()
root.geometry("500x350+450+200")
root.title("Main Home")
initial_path = load_path()
path_var = customtkinter.StringVar(value=initial_path)
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=25, pady=25,  fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Moemen mods checker",font=("aloevera", 20),text_color='#A20183')
label.pack(padx=12, pady=10)
pathB = customtkinter.CTkButton(master=frame, text="Choose The Path ",command=choose_path,font=("Mouldy Cheese",15),text_color="#A20183")
pathB.pack(padx=12, pady=10)
pathT = customtkinter.CTkEntry(master=frame,textvariable=path_var,font=("Mouldy Cheese",15),text_color="#A20183")
pathT.pack(padx=12, pady=10,fill="x")
But = customtkinter.CTkButton(master=frame,text="Check Mods",font=("Mouldy Cheese",15),text_color="#A20183",command=check)
But.pack(padx=12, pady=10,fill="x")
root.mainloop()

