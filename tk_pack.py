import tkinter as tk

if __name__ == '__main__':
    
    # 主視窗建立
    window = tk.Tk()
    window.title('Tkinter Pack')
    window.geometry('400x300')
    
    # frames設定
    lframe = tk.Frame(window ,bg='lightgreen' ,width=40)
    rframe = tk.Frame(window ,bg='lightblue' ,width=40)
    mtframe = tk.Frame(window ,bg='red' ,height=60 ,pady=5)
    mmframe = tk.Frame(window ,bg='yellow')
    mbframe = tk.Frame(window ,bg='blue' ,height=30)
    
    mtframe.pack_propagate(False)
    
    # labels設定
    llabel = tk.Label(mtframe ,text='Left' ,font=('Arial' ,9) ,bg='white')
    mlabel = tk.Label(mtframe ,text='Center' ,font=('Arial' ,9) ,bg='white')
    rlabel = tk.Label(mtframe ,text='Right' ,font=('Arial' ,9) ,bg='white')  
    
    # labels排列
    llabel.pack(side='left' ,anchor='n' ,expand=True)
    mlabel.pack(side='left' ,anchor='n' ,expand=True)
    rlabel.pack(side='left',anchor='n' ,expand=True)
    
    # frames排列
    lframe.pack(side='left'  ,fill='both')
    rframe.pack(side='right' ,fill='both')
    mtframe.pack(side='top' ,fill='both')
    mbframe.pack(side='bottom' ,fill='both')
    mmframe.pack(side='top' ,fill='both' ,expand=True)

    window.mainloop()