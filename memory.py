from tkinter import *
from tkinter import ttk

def play():
    for widget in root.winfo_children():
        widget.destroy()
    st = Label(text="Выберите вселенную:")
    st.pack()
    universe_1 = ttk.Button(text="Сооружения")
    universe_1.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_2 = ttk.Button(text="Древнегреческие боги")
    universe_2.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_3 = ttk.Button(text="Властелин колец")
    universe_3.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_4 = ttk.Button(text="Гарри Поттер")
    universe_4.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_5 = ttk.Button(text="Корпуса вышки")
    universe_5.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_6 = ttk.Button(text="Марвел")
    universe_6.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_7 = ttk.Button(text="Символы МФА")
    universe_7.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_8 = ttk.Button(text="Животные фиклят")
    universe_8.pack(expand=True, fill=BOTH, padx=60, pady=5)
    back = ttk.Button(text="Назад", command=main_page)
    back.pack(expand=True, fill=BOTH, padx=60, pady=5)

def rool():
    for widget in root.winfo_children():
        widget.destroy()
    st = Label(text="пупупу все будет")
    st.pack()
    back = ttk.Button(text="Назад", command=main_page)
    back.pack(expand=True, fill=BOTH, padx=60, pady=200)

def win():
    for widget in root.winfo_children():
        widget.destroy()
    st = Label(text="пупупу все будет")
    st.pack()
    back = ttk.Button(text="Назад", command=main_page)
    back.pack(expand=True, fill=BOTH, padx=60, pady=200)

def out():
    root.destroy()

def main_page():
    for widget in root.winfo_children():
        widget.destroy()
    label = Label(text="Добро пожаловать в Memory!")
    label.pack()
    playing = ttk.Button(text="Играть", command=play)
    playing.pack(expand=True, fill=BOTH, padx=60, pady=20)
    rools = ttk.Button(text="Правила игры", command=rool)
    rools.pack(expand=True, fill=BOTH, padx=60, pady=20)
    record = ttk.Button(text="Мои рекорды", command=win)
    record.pack(expand=True, fill=BOTH, padx=60, pady=20)
    ex = ttk.Button(text="Выход", command=out)
    ex.pack(expand=True, fill=BOTH, padx=60, pady=20)

root = Tk()
root.title("Memory")
root.geometry("600x500")
label = Label(text="Добро пожаловать в Memory!")
label.pack()
playing = ttk.Button(text="Играть", command=play)
playing.pack(expand=True, fill=BOTH, padx=60, pady=20)
rools = ttk.Button(text="Правила игры", command=rool)
rools.pack(expand=True, fill=BOTH, padx=60, pady=20)
record = ttk.Button(text="Мои рекорды", command=win)
record.pack(expand=True, fill=BOTH, padx=60, pady=20)
ex = ttk.Button(text="Выход", command=out)
ex.pack(expand=True, fill=BOTH, padx=60, pady=20)
root.mainloop()
