from tkinter import *
from tkinter import ttk
from IPython.display import display
from PIL import ImageTk, Image
import os
import random
import time
import textwrap


def play():
    for widget in root.winfo_children():
        widget.destroy()
    st = Label(text="Выберите вселенную:", font=("Arial", 14))
    st.pack()
    style = ttk.Style()
    style.configure("usual.TButton", font=("Arial", 14))
    universe_1 = ttk.Button(text="Сооружения", command=lambda: playing_field("build"), style="usual.TButton")
    universe_1.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_2 = ttk.Button(text="Древнегреческие боги", command=lambda: playing_field("gods"), style="usual.TButton")
    universe_2.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_3 = ttk.Button(text="Властелин колец", command=lambda: playing_field("hobbit"), style="usual.TButton")
    universe_3.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_4 = ttk.Button(text="Гарри Поттер", command=lambda: playing_field("hp"), style="usual.TButton")
    universe_4.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_5 = ttk.Button(text="Корпуса вышки", command=lambda: playing_field("hse"), style="usual.TButton")
    universe_5.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_6 = ttk.Button(text="Марвел", command=lambda: playing_field("marvel"), style="usual.TButton")
    universe_6.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_7 = ttk.Button(text="Символы МФА", command=lambda: playing_field("sound"), style="usual.TButton")
    universe_7.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_8 = ttk.Button(text="Животные фиклят", command=lambda: playing_field("pet"), style="usual.TButton")
    universe_8.pack(expand=True, fill=BOTH, padx=60, pady=5)
    universe_9 = ttk.Button(text="Brainrot animals", command=lambda: playing_field("br"), style="usual.TButton")
    universe_9.pack(expand=True, fill=BOTH, padx=60, pady=5)
    back = ttk.Button(text="Назад", command=main_page, style="usual.TButton")
    back.pack(expand=True, fill=BOTH, padx=60, pady=5)


def rule():
    for widget in root.winfo_children():
        widget.destroy()
    text1 = 'Перед началом игры вам нужно выбрать вселенную, персонажи из которой будут представлены на карточках. После выбора начнется игра.'
    st1 = Label(text=textwrap.fill(text1, width=60), justify='center', pady=10, font=("Arial", 14))
    st1.pack()
    text2 = 'Перед вами будет поле с 16 карточками, перевернутыми картинками вниз. Открывайте карточки попарно и запоминайте их расположение. Если картинки на них совпадают, карточки уходят из игры, если нет, карточки снова перевернутся. Игра закончится, когда вы найдете все пары.'
    st2 = Label(text=textwrap.fill(text2, width=60), justify='center', pady=10, font=("Arial", 14))
    st2.pack()
    text3 = 'Развивайте свою память и старайтесь закончить за минимальное время и как можно меньшее количество ходов!'
    st3 = Label(text=textwrap.fill(text3, width=60), justify='center', pady=10, font=("Arial", 14))
    st3.pack()
    text4 = 'Желаем удачи!'
    st4 = Label(text=textwrap.fill(text4, width=60), justify='center', pady=10, font=("Arial", 14))
    st4.pack()
    style = ttk.Style()
    style.configure("usual.TButton", font=("Arial", 14))
    back = ttk.Button(text="Назад", command=main_page, style="usual.TButton")
    back.pack(expand=True, fill=BOTH, padx=60, pady=50)


def win():
    for widget in root.winfo_children():
        widget.destroy()
    global num_steps, time_sec, record

    new_frame = Frame(root)
    new_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    new_frame.grid_columnconfigure(0, weight=1)
    new_frame.grid_rowconfigure(0, weight=2)
    new_frame.grid_rowconfigure(1, weight=1)
    new_frame.grid_rowconfigure(2, weight=1)
    new_frame.grid_rowconfigure(3, weight=1)
    new_frame.grid_rowconfigure(4, weight=1)
    new_frame.grid_rowconfigure(5, weight=2)

    if record == 1:
        congrat = 'Поздравляем, вы побили рекорд!'
    elif len(curr_records()['steps']) == 1:
        congrat = 'Отличный результат!'
    else:
        congrat = 'Вы близки к цели!'

    congrats = Label(new_frame, text=congrat, font=("Arial", 20), pady=20)
    congrats.grid(row=0, column=0, sticky='nsew')
    congrats.config(anchor='center')
    if record == 0 or len(curr_records()['time']) == 1:
        curr_time = Label(new_frame, text=f"Время: {time_conv(time_sec)}", font=("Arial", 14), pady=20)
        curr_time.grid(row=1, column=0, sticky='nsew')
        curr_time.config(anchor='center')
    if len(curr_records()['time']) > 1:
        best_time = Label(new_frame, text=f'Лучшее время: {time_conv(curr_records()['time'][0])}', font=("Arial", 14),
                          pady=20)
        best_time.grid(row=2, column=0, sticky='nsew')
        best_time.config(anchor='center')
    if record == 0 or len(curr_records()['steps']) == 1:
        score = Label(new_frame, text=f'Количество ходов: {num_steps}', font=("Arial", 14), pady=20)
        score.grid(row=3, column=0, sticky='nsew')
        score.config(anchor='center')
    if len(curr_records()['steps']) > 1:
        best_score = Label(new_frame, text=f'Лучшее количество ходов: {curr_records()['steps'][0]}', font=("Arial", 14),
                           pady=20)
        best_score.grid(row=4, column=0, sticky='nsew')
        best_score.config(anchor='center')

    style = ttk.Style()
    style.configure("usual.TButton", font=("Arial", 14))
    back = ttk.Button(new_frame, text="Назад", command=main_page, style="usual.TButton")
    back.grid(row=5, column=0, sticky='nsew')
    back.config(anchor='center')


def time_conv(full_sec):
    minutes = int(full_sec / 60)
    seconds = int(full_sec % 60)
    return f"{minutes:02d}:{seconds:02d}"


def rec_storage():
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = Frame(root)
    main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=2)
    main_frame.grid_rowconfigure(2, weight=3)
    main_frame.grid_rowconfigure(3, weight=1)

    header = Label(main_frame, text='Мои рекорды', justify='center', font=("Arial", 14))
    header.grid(row=0, column=0, columnspan=2, sticky='nsew')

    t_head = Label(main_frame, text='Время', justify='center', font=("Arial", 14))
    t_head.grid(row=1, column=0, sticky='nsew')
    t_head.config(anchor='center')

    s_head = Label(main_frame, text=f'Количество\nходов', justify='center', font=("Arial", 14))
    s_head.grid(row=1, column=1, sticky='nsew')
    s_head.config(anchor='center')

    t_text = ''
    s_text = ''

    for i in range(len(curr_records()['time'])):
        t_text += f'{i + 1}. {time_conv(curr_records()['time'][i])}\n'
        # f'\n2. {time_conv(curr_records()['time'][1])}\n3. {time_conv(curr_records()['time'][2])}')
    for j in range(len(curr_records()['steps'])):
        s_text += f'{i + 1}. {curr_records()['steps'][j]}\n'
        # 2. {curr_records()['steps'][1]}\n3. {curr_records()['steps'][2]}'

    t_rec = Label(main_frame, text=t_text, justify='center', font=("Arial", 14))
    t_rec.grid(row=2, column=0, sticky='new')
    t_rec.config(anchor='center')

    s_rec = Label(main_frame, text=s_text, justify='center', font=("Arial", 14))
    s_rec.grid(row=2, column=1, sticky='new')
    s_rec.config(anchor='center')

    style = ttk.Style()
    style.configure("usual.TButton", font=("Arial", 14))
    back = ttk.Button(main_frame, text="Назад", command=main_page, style="usual.TButton")
    back.grid(row=3, column=0, columnspan=2, sticky='nsew')


def curr_records():
    default = {'time': [0], 'steps': [0]}
    try:
        if not os.path.exists('records.txt') or os.stat('records.txt').st_size == 0:
            with open('records.txt', 'w') as f:
                f.write(str(default))
            return default.copy()

        with open('records.txt', 'r') as f:
            content = f.read()
            return eval(content) if content else default.copy()
    except:
        return default.copy()


def out():
    root.destroy()


def main_page():
    for widget in root.winfo_children():
        widget.destroy()

    label = Label(text="Добро пожаловать в Memory!", font=("Arial", 14))
    label.pack()
    style = ttk.Style()
    style.configure("usual.TButton", font=("Arial", 14))
    playing = ttk.Button(text="Играть", style="usual.TButton", command=play)
    playing.pack(expand=True, fill=BOTH, padx=60, pady=20)
    rules = ttk.Button(text="Правила игры", style="usual.TButton", command=rule)
    rules.pack(expand=True, fill=BOTH, padx=60, pady=20)
    if 0 not in curr_records()['time']:
        record = ttk.Button(text="Мои рекорды", style="usual.TButton", command=rec_storage)
        record.pack(expand=True, fill=BOTH, padx=60, pady=20)
    ex = ttk.Button(text="Выход", style="usual.TButton", command=out)
    ex.pack(expand=True, fill=BOTH, padx=60, pady=20)


def playing_field(world):
    def count(number=3):
        for widget in root.winfo_children():
            widget.destroy()
        label = Label(root, text=f'{number}', font=("Arial", 100, "bold"))
        label.place(relx=0.5, rely=0.5, anchor='center')
        if number > 0:
            root.after(1000, count, number - 1)
        else:
            game(world)

    root.after(0, count)


def game(world):
    global num_opened_cards, list_closed_cards, first_opened, second_opened, \
        num_win, label_2, num_steps, label_kmoves, root, label_win, sw

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600+350+60")
    root.resizable(True, True)

    num_images = random.sample(range(1, len(os.listdir(f'photos/{world}')) + 1), 8)
    list_images = []
    for i in num_images:
        list_images.extend([ImageTk.PhotoImage(Image.open(f'photos/{world}/{world}_{i}.jpg'))] * 2)
    button_image = ImageTk.PhotoImage(Image.open('photos/button image.png'))
    para_image = ImageTk.PhotoImage(Image.open('photos/para image.png'))

    list_closed_cards = []
    num_opened_cards = 0
    num_steps = 0
    num_win = 0
    label_kmoves = Label(text=f'Количество ходов: {num_steps}', font=('Arial', 14))
    label_kmoves.pack(side=BOTTOM, pady=0.2)

    game_pole = Frame(root)
    game_pole.pack(expand=True, fill=BOTH, padx=10, pady=10)

    for i in range(4):
        game_pole.grid_rowconfigure(i, weight=1)
    for i in range(6):
        game_pole.grid_columnconfigure(i, weight=1)

    list_closed_cards = []

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
            button.found = False
            list_closed_cards.append(button)

        for j in range(5, 6):
            if i == 0 or i == 1:
                if i == 0:
                    sw = StopWatch(game_pole)
                    sw.grid(
                        row=i,
                        column=j - 1,
                        columnspan=2,
                        padx=10,
                        pady=20,
                        sticky='nsew'
                    )

                if i == 1:
                    lbl_text = f'ЛУЧШЕЕ ВРЕМЯ:\n{time_conv(curr_records()['time'][0])}'
                    label = Label(
                        game_pole,
                        text=lbl_text,
                        background="#FFBBB9",
                        font=('Arial', 11)
                    )
                    label.grid(
                        row=i,
                        column=j - 1,
                        columnspan=2,
                        padx=10,
                        pady=20,
                        sticky='nsew'
                    )
            else:
                if i == 2:
                    but_text = 'ПАУЗА'
                    but_com = pause
                elif i == 3:
                    but_text = 'ДОМОЙ'
                    but_com = main_page
                button = Button(
                    game_pole,
                    text=but_text,
                    background="#FFBBB9",
                    font=('Arial', 12),
                    command=but_com
                )
                button.grid(
                    row=i,
                    column=j - 1,
                    columnspan=2,
                    padx=10,
                    pady=20,
                    sticky='nsew'
                )

    for l in list_closed_cards:
        k = random.choice(list_images)
        l.image = k
        list_images.remove(k)

    second_opened = ''

    label_2 = Label(root, text='')
    label_2.pack(side=TOP)

    sw.Start()

    def pair():
        global list_closed_cards, first_opened, second_opened, num_win, label_2, \
            num_opened_cards, num_steps, label_kmoves, sw
        label_2.config(text='Пара!', font=('Arial', 14), foreground='red')
        root.after(1500, lambda: label_2.config(text=''))

        def get_rgb(rgb):
            return "#%02x%02x%02x" % rgb

        def closer():
            global first_opened, second_opened, label_win, sw
            first_opened.config(
                image=para_image,
                state="disabled",
            )
            second_opened.config(
                image=para_image,
                state="disabled",
            )
            first_opened.found = True
            second_opened.found = True
            global num_win, sw
            num_win += 1
            root.after(1500, lambda: label_2.config(text=''))

            if num_win == 8:
                sw.Stop()
                label_win = Label(
                    root,
                    text='Вы нашли все пары!',
                    font=('Arial', 16),
                    bg="white"
                )
                label_win.place(relx=0.5, rely=0.5, anchor="center")

                global time_sec
                time_sec = sw._elapsedtime

                global record
                record = 0
                dict_results = curr_records()
                if 0 in dict_results['time']:
                    dict_results['time'].remove(0)
                if len(dict_results['time']) > 0 and time_sec < min(dict_results['time']):
                    record = 1
                dict_results['time'].append(time_sec)
                dict_results['time'].sort()
                if len(dict_results['time']) > 3:
                    dict_results['time'].pop()
                if 0 in dict_results['steps']:
                    dict_results['steps'].remove(0)
                if len(dict_results['steps']) > 0 and num_steps < min(dict_results['steps']):
                    record = 1

                dict_results['steps'].append(num_steps)
                dict_results['steps'].sort()
                if len(dict_results['steps']) > 3:
                    dict_results['steps'].pop()

                with open('records.txt', 'w', encoding='utf-8') as record_file_view:
                    record_file_view.write(str(dict_results))

                root.after(1500, win)

        root.after(100, closer)

    def not_pair():
        global list_closed_cards, label_2, num_win, first_opened, second_opened, \
            num_opened_cards, num_steps, label_kmoves, game_pole, sw
        for i in list_closed_cards:
            i['image'] = button_image
            i.open = False
        label_2.config(text='Не пара!', font=('Arial', 14), foreground='red')
        root.after(1500, lambda: label_2.config(text=''))

    def open_card(event):
        global num_opened_cards, first_opened, second_opened, list_closed_cards, list_found_pairs, \
            num_steps, label_2, label_kmoves, game_pole, root, widget, sw
        if event.widget.open:
            return

        try:
            if num_opened_cards == 0:
                event.widget['image'] = event.widget.image
                num_steps += 1
                label_kmoves.config(text=f'Количество ходов: {num_steps}', font=('Arial', 12))
                event.widget.open = True
                num_opened_cards = 1
                first_opened = event.widget
                list_closed_cards.remove(first_opened)

            elif num_opened_cards == 1 and event.widget.open is False:
                if event.widget == first_opened:
                    return
                event.widget.open = True
                event.widget['image'] = event.widget.image
                num_steps += 1
                label_kmoves.config(text=f'Количество ходов: {num_steps}', font=('Arial', 12))
                if event.widget.image == first_opened.image:
                    second_opened = event.widget
                    list_closed_cards.remove(second_opened)
                    root.after(500, pair)
                else:
                    list_closed_cards.append(first_opened)
                    root.after(500, not_pair)
                num_opened_cards = 0
        except Exception:
            pass

    root.bind('<Button-1>', open_card)


class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()

        self.makeWidgets()

    def makeWidgets(self):
        l = ttk.Label(
            self,
            textvariable=self.timestr,
            font=('Arial', 14),
            anchor='center',
            justify='center'
        )
        self._setTime(self._elapsedtime)
        l.pack(fill=BOTH, expand=True)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def pause():
    global sw, root
    sw.Stop()
    pause_button = Button(root, text="ПАУЗА")
    pause_button.config(font=("Arial", 100, "bold"), command=lambda b=pause_button: [b.destroy(), sw.Start()])
    pause_button.place(relx=0, rely=0, relwidth=1, relheight=1)
    pass


def check():
    pass


root = Tk()
root.title("Memory")
root.geometry("800x600+350+60")
main_page()
root.mainloop()
