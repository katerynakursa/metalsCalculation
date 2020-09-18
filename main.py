import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        labelSplav = tk.Label(root, text='Выберите сплав:')
        labelSplav.pack(side=tk.TOP)

        comboSplav = ttk.Combobox(root, values=['бронза', 'латунь', 'оцс', 'припой'], state='readonly')
        comboSplav.pack(side=tk.TOP)

        labelMarkaSplava = tk.Label(root, text='Выберите марку сплава:')
        labelMarkaSplava.pack(side=tk.TOP)

        comboSplav = ttk.Combobox(root, values=['Л63', 'ЛС59-1'], state='readonly')
        comboSplav.pack(side=tk.TOP)

        self.tree = ttk.Treeview(self, columns=('elements', 'cu', 'zn'), height=1, show='headings')

        self.tree.column('elements', width=150, anchor=tk.CENTER)
        self.tree.column('cu', width=150, anchor=tk.CENTER)
        self.tree.column('zn', width=150, anchor=tk.CENTER)

        self.tree.heading('elements', text='Химические элементы')
        self.tree.heading('cu', text='Cu')
        self.tree.heading('zn', text='Zn')

        self.tree.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Расчет металлов')
    root.geometry('800x450+300+200')
    root.resizable(False, False)
    root.mainloop()