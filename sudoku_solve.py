import customtkinter as ctk
import numpy as np
import winsound
import tkinter as tk
import numpy as np

customtk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtk.CTk()

app.geometry("444x600")
app.title("Customtk simple_example.py")

app.title("Solve Sudoku")
frame_1 = customtk.CTkFrame(master=app)
frame_1.pack(pady=15, padx=30, fill="both", expand=True)

label_1 = customtk.CTkLabel(text="Solve Sudoku",master=frame_1, justify=customtk.LEFT,  font=customtk.CTkFont(size=20, weight="bold"))
label_1.pack(pady=5, padx=.1, anchor=tk.CENTER)

label_1 = customtk.CTkLabel(text="Fill the board with given numbers",master=frame_1, justify=customtk.LEFT,  font=customtk.CTkFont(size=12, weight="normal"))
label_1.pack(pady=3, padx=.1, anchor=tk.CENTER)

cells_frame = tk.Frame(frame_1)
cells_frame.pack(pady=10)

text_cells = []

# Define styling options
cell_paddingx = 2
cell_paddingy = 2
cell_background = "blue"
cell_font = ("Arial", 30)
#cell_frame={}
text_cell={}
for i in range(9):
    row_frame = tk.Frame(cells_frame)
    row_frame.pack()
    if ((i%3==0) & (i>0)):
        cell_paddingy = 10
    else:
        cell_paddingy = 2    
    for j in range(9):
        if ((j%3==0) & (j>0)):
            cell_paddingx = 10
        else:
            cell_paddingx = 2
        n=i*9+j
        cell_frame = tk.Frame(row_frame, borderwidth=1, relief="solid", bg=cell_background)
        cell_frame.pack(side="left", padx=(cell_paddingx,2), pady=(cell_paddingy,2), anchor="w")

        text_cell[i*9+j] = tk.Text(cell_frame, height=1, width=2, font=cell_font)
        
        
        text_cell[n].pack()
        text_cells.append(text_cell[i*9+j])
        text_cell[n].tag_configure("center", justify='center')
        text_cell[n].delete("0.0", tk.END)
        text_cell[n].insert(tk.END,"","center")
        #text_cell.insert(tk.END,"0") 
def f(a,i,j,n):
    flag=0
    for l in range(3):
        for s in range(3):
            h=np.absolute(a[3*int((i)/3)+l][3*int((j)/3)+s])
            if((h==n) and ((3*int((i)/3)+l)!=i) and ((3*int((j)/3)+s)!=j)):
                flag=1
                
    for g in range(9):
        if((np.absolute(a[i][g])==n) and (g!=j)):
            flag=1
       
    for h in range(9):
        if((np.absolute(a[h][j])==n) and (h!=i)):
            flag=1
    return flag
def read():
    global a
    a=[]
    for i in range(len(text_cell)):
        num=str()
        num=str(text_cell[i].get("1.0","end-1c"))
        num=num+"0"
        #if ((num<1) or (num>9)):
            #break
        #else:
        if (len(num)>0):
            a=np.append(a,int(num[0]))
        else:
            a=np.append(a,0)
    a=a.reshape(9,9)

    k=0
    a=-a
    s=0
    reverse=-1
    while k<=80:
        try:
            while(a[int(k%9)][int(k/9)]<0):
                k=k-reverse
            i=int(k%9)
            j=int(k/9)
            if a[i][j]==0:
                a[i][j]=10
            n=a[i][j]-1
            fl=1
            while (fl==1):
                fl=f(a,i,j,n)
                n=n-1
            if(n<0):
                a[i][j]=0
                k=k-1
                reverse=1
            else:
                reverse=-1
                k=k+1
                a[i][j]=n+1
            s=s+1
        except Exception:
            k=k+90
            break
    c=a.reshape(1,81)
    c=c[0]
    print(c)
    for h in range(len(c)):
        if(c[h]>0):
            text_cell[h].tag_configure("color_tag", foreground="blue")
            text_cell[h].tag_configure("center", justify="center")
            text_cell[h].insert(tk.END,str(int(c[h])),("color_tag","center")) 

text_box = tk.Text(app, height=5, width=30)            
text_box.pack()

#cells[0].place(relx=pos, rely=0.5, anchor=tk.CENTER)
button_1 = customtk.CTkButton(app, command=lambda: read(),text="Solve")
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_1.pack(side="bottom",pady=20, padx=10)

'''
button_1 = customtk.CTkButton(master=frame_1, command=lambda: click(),text="Truth")
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_1.pack(side="right",pady=10, padx=10)
'''
'''
button_2 = customtk.CTkButton(app, command=lambda: click(itemsD,A),text="Dare")
#button_2.grid(row=0, column=1, pady=10, padx=10)
button_2.pack(side="left",pady=10, padx=10)
'''
app.mainloop()
