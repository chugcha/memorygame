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


def playing_field(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("600x500+300+50")
    root.resizable(False, False)

    # чекнуть пути потом
    card_1 = PhotoImage(file='photos/build/build_1.png')
    card_2 = PhotoImage(file='photos/build/build_2.png')
    card_3 = PhotoImage(file='photos/build/build_3.png')
    card_4 = PhotoImage(file='photos/build/build_4.png')
    card_5 = PhotoImage(file='photos/build/build_5.png')
    card_6 = PhotoImage(file='photos/build/build_6.png')
    card_7 = PhotoImage(file='photos/build/build_7.png')
    card_8 = PhotoImage(file='photos/build/build_8.png')
    button_image = PhotoImage(file='photos/button image.png')

    list_images = [card_1, card_1, card_2, card_2, card_3, card_3, card_4, card_4,
                   card_5, card_5, card_6, card_6, card_7, card_7, card_8, card_8]

    list_closed_cards = []
    num_opened_cards = 0
    num_steps = 0
    num_win = 0
    first_opened = None
    second_opened = None

    label = Label(root, text=f'Количество ходов: {num_steps}')
    label.pack(side=BOTTOM, pady=10)
    label_kmoves = Label(text=f'Количество ходов: {num_steps}', font=('Arial', 12))
    label_kmoves.pack(side=BOTTOM, pady=10)

    game_pole = Frame(root)
    game_pole.pack(expand=True, fill=BOTH, padx=10, pady=10)

    for i in range(4):
        game_pole.grid_rowconfigure(i, weight=1)
    for i in range(6):
        game_pole.grid_columnconfigure(i, weight=1)

    for i in range(4):
        for j in range(4):
            button = Button(
                game_pole,
                image=button_image,
                background="#667E91",
            )
            button.grid(
                row=j,
                column=i,
                sticky="nsew",
                padx=2,
                pady=2,
            )
            button.open = False
            list_closed_cards.append(button)

            for j in range(5, 6):
                if i == 0 or i == 1:
                    if i == 0:
                        lbl_text = 'время'
                    if i == 1:
                        lbl_text = 'лучшее время:'
                    label = Label(game_pole, text=lbl_text, background="#FFBBB9")
                    label.grid(row=i, сolumn=j - 1, columnspan=2, padx=10, pady=20, sticky='nsew')
            else:
                if i == 2:
                    but_text = 'пауза'
                elif i == 3:
                    but_text = 'домой'
                button = Button(game_pole, text=but_text, background="#FFBBB9")
                button.grid(row=i, column=j - 1, columnspan=2, padx=10, pady=20, sticky='nsew')

    for card in list_closed_cards:
        img = random.choice(list_images)
        card.image = img
        list_images.remove(img)


second_opened = ''

#label_2 = Label(background='white')
#label_2.place(relx=.5, rely=.5, anchor="center")
#label_2.pack(side=BOTTOM, pady=10)

def pair():
    global list_closed_cards, first_opened, second_opened, num_win, label_2
    label_2.config(text='Пара!', font=('Arial', 16), foreground='red')

    def get_rgb(rgb): # это для подобранного цвета
        return "#%02x%02x%02x" % rgb

    def closer():
        first_opened.config(
            image='',
            state="disabled",
            background=get_rgb((174, 210, 227)), # цвет
            activebackground=get_rgb((174, 210, 227))
        )
        second_opened.config(
            image='',
            state="disabled",
            background=get_rgb((174, 210, 227)),
            activebackground=get_rgb((174, 210, 227))
        )
        first_opened.found = True
        second_opened.found = True
        global num_win
        num_win += 1
        window.after(1500, lambda: label_2.config(text=''))

        if num_win == 8:
            label_win = Label(
                window,
                text='Вы нашли все пары!',
                font=('Arial', 16),
                bg="white"
            )
            label_win.place(relx=0.5, rely=0.5, anchor="center")

    window.after(100, closer)

def not_pair():
    global list_closed_cards, label_2, num_win
    for i in list_closed_cards:
        i['image'] = button_image # чтобы не менялось
        i.open = False
    label_2.config(text='Не пара!', font=('Arial', 16), foreground='red')
    window.after(1500, lambda: label_2.config(text=''))


def open_card(event):
    global num_opened_cards, first_opened, second_opened, list_closed_cards, list_found_pairs, num_steps
    if event.widget.open:
        return
    try:
        if num_opened_cards == 0:
            event.widget['image'] = event.widget.image
            num_steps += 1
            label_kmoves.config(text = f'Количество ходов: {num_steps}', font=('Arial', 12))
            event.widget.open = True
            num_opened_cards = 1
            first_opened = event.widget
            list_closed_cards.remove(first_opened)

        elif num_opened_cards == 1 and event.widget.open == False:
            if event.widget == first_opened: # чтобы он нажатие 2 раза на одну кнопку воспринимал как 1 раз
                return
            event.widget.open = True
            event.widget['image'] = event.widget.image
            num_steps += 1
            label_kmoves.config(text=f'Количество ходов: {num_steps}', font=('Arial', 12))
            if event.widget['image'] == first_opened['image']:
                second_opened = event.widget
                list_closed_cards.remove(second_opened)
                window.after(500, pair)
            else:
                list_closed_cards.append(first_opened)
                window.after(500, not_pair)
            num_opened_cards = 0
    except Exception:
        pass


root.bind('<Button-1>', open_card)

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
