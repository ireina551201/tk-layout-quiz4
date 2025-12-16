import tkinter as tk

if __name__ == '__main__':
    
    # 主視窗建立
    window = tk.Tk()
    window.title('Tkinter Place')
    window.geometry('400x300')
    
    # Frame元件初始化
    lframe = tk.Frame(window ,bg='lightgreen')
    rframe = tk.Frame(window ,bg='lightblue')
    mtframe = tk.Frame(window ,bg='red')
    mmframe = tk.Frame(window ,bg='yellow')
    mbframe = tk.Frame(window ,bg='blue' ,height=30)

    # Frame佈局規劃
    lframe.place(x=0 ,y=0 ,relheight=1.0 ,relwidth=0.1)
    rframe.place(relx=1.0 ,anchor='ne' ,relheight=1.0 ,relwidth=0.1)
    mtframe.place(relx=0.5 ,anchor='n' ,relheight=0.2 ,relwidth=0.8)
    mbframe.place(relx=0.5 ,rely=1.0 ,anchor='s' ,relheight=0.1 ,relwidth=0.8)
    mmframe.place(relx=0.5 ,rely=0.2 ,anchor='n' ,relheight=0.7 ,relwidth=0.8)

    # Label元件初始化
    llabel = tk.Label(mtframe ,text='Left' ,font=('Arial' ,9) ,bg='white' ,fg='black')
    mlabel = tk.Label(mtframe ,text='Center' ,font=('Arial' ,9) ,bg='white' ,fg='black')
    rlabel = tk.Label(mtframe ,text='Right' ,font=('Arial' ,9) ,bg='white' ,fg='black')

    # Label佈局規劃

    llabel.place(y=5 ,relx=0.165 ,anchor='n')
    mlabel.place(y=5 ,relx=0.5 ,anchor='n')
    rlabel.place(y=5 ,relx=0.835 ,anchor='n')

    window.mainloop()