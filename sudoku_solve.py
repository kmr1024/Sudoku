import customtkinter as ctk
import numpy as np
import winsound
import tkinter as tk

# Set appearance mode and theme for customtkinter
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the main application window
app = ctk.CTk()

# Set the window size and title
app.geometry("444x600")
app.title("Customtk simple_example.py")

app.title("Solve Sudoku")

# Create and pack the main frame
frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=15, padx=30, fill="both", expand=True)

# Add a title label to the frame
label_1 = ctk.CTkLabel(text="Solve Sudoku", master=frame_1, justify=ctk.LEFT, font=ctk.CTkFont(size=20, weight="bold"))
label_1.pack(pady=5, padx=.1, anchor=tk.CENTER)

# Add a subtitle label to the frame
label_1 = ctk.CTkLabel(text="Fill the board with given numbers", master=frame_1, justify=ctk.LEFT, font=ctk.CTkFont(size=12, weight="normal"))
label_1.pack(pady=3, padx=.1, anchor=tk.CENTER)

# Create and pack a frame for the Sudoku cells
cells_frame = tk.Frame(frame_1)
cells_frame.pack(pady=10)

# Initialize a list to hold text widgets for each cell
text_cells = []

# Define styling options for the cells
cell_paddingx = 2
cell_paddingy = 2
cell_background = "blue"
cell_font = ("Arial", 30)

# Initialize a dictionary to hold the text widgets
text_cell = {}

# Create the 9x9 grid of Sudoku cells
for i in range(9):
    row_frame = tk.Frame(cells_frame)
    row_frame.pack()
    if ((i % 3 == 0) & (i > 0)):
        cell_paddingy = 10
    else:
        cell_paddingy = 2    
    for j in range(9):
        if ((j % 3 == 0) & (j > 0)):
            cell_paddingx = 10
        else:
            cell_paddingx = 2
        n = i * 9 + j
        cell_frame = tk.Frame(row_frame, borderwidth=1, relief="solid", bg=cell_background)
        cell_frame.pack(side="left", padx=(cell_paddingx, 2), pady=(cell_paddingy, 2), anchor="w")

        text_cell[i * 9 + j] = tk.Text(cell_frame, height=1, width=2, font=cell_font)
        text_cell[n].pack()
        text_cells.append(text_cell[i * 9 + j])
        text_cell[n].tag_configure("center", justify='center')
        text_cell[n].delete("0.0", tk.END)
        text_cell[n].insert(tk.END, "", "center")

# Function to check if placing number n at cell (i, j) is valid
def f(a, i, j, n):
    flag = 0
    for l in range(3):
        for s in range(3):
            h = np.absolute(a[3 * int((i) / 3) + l][3 * int((j) / 3) + s])
            if ((h == n) and ((3 * int((i) / 3) + l) != i) and ((3 * int((j) / 3) + s) != j)):
                flag = 1
                
    for g in range(9):
        if ((np.absolute(a[i][g]) == n) and (g != j)):
            flag = 1
       
    for h in range(9):
        if ((np.absolute(a[h][j]) == n) and (h != i)):
            flag = 1
    return flag

# Function to read the input from the Sudoku grid and solve the puzzle
def read():
    global a
    a = []
    for i in range(len(text_cell)):
        num = str(text_cell[i].get("1.0", "end-1c"))
        num = num + "0"
        if (len(num) > 0):
            a = np.append(a, int(num[0]))
        else:
            a = np.append(a, 0)
    a = a.reshape(9, 9)

    k = 0
    a = -a
    s = 0
    reverse = -1
    while k <= 80:
        try:
            while(a[int(k % 9)][int(k / 9)] < 0):
                k = k - reverse
            i = int(k % 9)
            j = int(k / 9)
            if a[i][j] == 0:
                a[i][j] = 10
            n = a[i][j] - 1
            fl = 1
            while (fl == 1):
                fl = f(a, i, j, n)
                n = n - 1
            if(n < 0):
                a[i][j] = 0
                k = k - 1
                reverse = 1
            else:
                reverse = -1
                k = k + 1
                a[i][j] = n + 1
            s = s + 1
        except Exception:
            k = k + 90
            break
    c = a.reshape(1, 81)
    c = c[0]
    print(c)
    for h in range(len(c)):
        if(c[h] > 0):
            text_cell[h].tag_configure("color_tag", foreground="blue")
            text_cell[h].tag_configure("center", justify="center")
            text_cell[h].insert(tk.END, str(int(c[h])), ("color_tag", "center")) 

# Add a button to trigger the Sudoku solver
button_1 = ctk.CTkButton(app, command=lambda: read(), text="Solve")
button_1.pack(side="bottom", pady=20, padx=10)

# Run the application
app.mainloop()
