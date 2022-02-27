# Создание пользовательского интерфейса 



def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return int(input('value = '))



# label = Label(root, text='0', width=35)
# label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# button = Button(root, text='CE', command=lambda text='CE': click(text))
# button.grid(row=1, column=3, sticky="nsew")
# for row in range(4):
   # for col in range(4):
       # button = Button(root, text=buttons[row][col],
               # command=lambda row=row, col=col: click(buttons[row][col]))
       # button.grid(row=row + 2, column=col, sticky="nsew")

# root.grid_rowconfigure(6, weight=1)
# root.grid_columnconfigure(4, weight=1)

# root.mainloop()