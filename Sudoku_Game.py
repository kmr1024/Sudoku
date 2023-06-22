import customtkinter as ctk
import numpy as np
import winsound
import tkinter as tk
import numpy as np

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()

app.geometry("520x560")
app.title("ctk simple_example.py")

app.title("Solve Sudoku")
frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=15, padx=30, fill="both", expand=True)

label_1 = ctk.CTkLabel(text="Solve Sudoku",master=frame_1, justify=ctk.LEFT,  font=ctk.CTkFont(size=20, weight="bold"))
label_1.pack(pady=5, padx=.1, anchor=tk.CENTER)



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
        
        
        text_cell[i*9+j].pack()
        text_cells.append(text_cell[i*9+j])
        text_cell[i*9+j].tag_configure("center", justify='center')
        text_cell[i*9+j].insert(tk.END,"","center")
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
def solve(a):
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
        except  :
            k=k+90
            break
    return(a)

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

def generate(SIZE):
    global samp_id,g,ind
    ind=np.arange(9*9)
    ind_new=ind
    numbers=np.arange(9)
    cell=np.random.choice(ind)
    num_to_insert=np.random.choice(numbers)
    g=np.zeros(9*9)
    g[cell]=num_to_insert
    g=g.reshape(9,9)
    g=solve(g)
    g=g.reshape(1,81)
    g=g[0]
    index=np.arange(81)
    
    samp_id=np.random.choice(index, size=SIZE, replace=False)
    g2=np.zeros(81)
    for m in range(len(text_cell)):
        text_cell[m].delete("0.0", tk.END)
    for l in range(len(samp_id)):
        idx=samp_id[l]
        text_cell[idx].tag_configure("color_tag", foreground="blue")
        text_cell[idx].tag_configure("center", justify="center")
        text_cell[idx].insert(tk.END,str(int(np.abs(g[idx]))),("color_tag","center"))

def show_sol():
    diff = np.setdiff1d(ind, samp_id)
    for m in diff:
        text_cell[m].delete("0.0", tk.END)
    for l in range(len(diff)):
        idx=diff[l]
        text_cell[idx].tag_configure("color_tag", foreground="green")
        text_cell[idx].tag_configure("center", justify="center")
        text_cell[idx].insert(tk.END,str(int(np.abs(g[idx]))),("color_tag","center"))        
        

frame_2 = ctk.CTkFrame(master=app)
frame_2.pack(pady=15, padx=30, fill="both", expand=True)

label_frame=ctk.CTkFrame(master=frame_2)
label_frame.configure(border_width=0)
label_frame.pack(fill="both", expand=True)

label_1 = ctk.CTkLabel(text="Choose the Difficulty",master=label_frame, justify=ctk.LEFT,  font=ctk.CTkFont(size=12, weight="normal"))
label_1.pack(pady=1, padx=.1, anchor=tk.CENTER)


button_frame = ctk.CTkFrame(frame_2)
button_frame.configure(border_width=0, width=200, height=20)
button_frame.pack()
button = ctk.CTkFrame(frame_2)
button.pack(pady=2,)
level=["Easy","Medium", "Hard"]
    #cells[0].place(relx=pos, rely=0.5, anchor=tk.CENTER)
   
button_1 = ctk.CTkButton(button_frame, command=lambda: generate(40),text=level[0])
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_1.pack(side="left",pady=0, padx=3)
button_2 = ctk.CTkButton(button_frame, command=lambda: generate(30),text=level[1])
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_2.pack(side="left",pady=0, padx=3)
button_3 = ctk.CTkButton(button_frame, command=lambda: generate(20),text=level[2])
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_3.pack(side="left",pady=0, padx=3)
button_4 = ctk.CTkButton(button, command=lambda: show_sol(),text="Show_Solution")
#button_1.grid(row=0, column=0, pady=10, padx=10)
button_4.pack(side="top",pady=2, padx=2)

app.mainloop()
