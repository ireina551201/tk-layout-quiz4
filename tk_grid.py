import tkinter as tk

if __name__ == '__main__':
    
    # 主視窗建立
    window = tk.Tk()
    window.title('Tkinter Grid')
    window.geometry('400x300')
    
    # Frame元件初始化
    lframe = tk.Frame(window ,bg='lightgreen' ,width=40)
    rframe = tk.Frame(window ,bg='lightblue' ,width=40)
    mtframe = tk.Frame(window ,bg='red' ,height=60,pady=5)
    mmframe = tk.Frame(window ,bg='yellow')
    mbframe = tk.Frame(window ,bg='blue' ,height=30)

    # Frame佈局規劃
    lframe.grid(row=0 ,column=0 ,rowspan=3 ,sticky='nsew')
    mtframe.grid(row=0,column=1 ,sticky='nesw')
    rframe.grid(row=0 ,column=2 ,rowspan=3 ,sticky='nsew')
    mmframe.grid(row=1 ,column=1 ,sticky='nesw')
    mbframe.grid(row=2 ,column=1 ,sticky='nesw')

    # Frame佈局設定
    window.grid_rowconfigure(1 ,weight=1)
    window.grid_columnconfigure(1 ,weight=1)

    # Label元件初始化
    llabel = tk.Label(mtframe ,text='Left' ,font=('Arial' ,9) ,bg='white' ,fg='black')
    mlabel = tk.Label(mtframe ,text='Center' ,font=('Arial' ,9) ,bg='white' ,fg='black')
    rlabel = tk.Label(mtframe ,text='Right' ,font=('Arial' ,9) ,bg='white' ,fg='black')

    # Label佈局規劃
    llabel.grid(row=0 ,column=0 ,sticky='n')
    mlabel.grid(row=0 ,column=1 ,sticky='n')
    rlabel.grid(row=0 ,column=2 ,sticky='n')
    
    # Label佈局設定
    mtframe.grid_propagate(False)
    mtframe.grid_columnconfigure((0,1,2) ,weight=1)
    mtframe.grid_rowconfigure(0 ,weight=1)

    window.mainloop()