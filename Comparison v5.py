# Importing Libraries of Tkinter, Matplotlib and Pandas
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Importing datasets (dataset has been combined from data recieved on RBI site)
df = pd.read_csv(filepath_or_buffer="C:\states.csv")

#Function which plots the various categories in bar plots of states
def plot():
    fig = Figure(figsize=(12,5)) # Canvas size.

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)
    fig.clear()

    option = dropdown_var.get() # Obtains the dropdown variable

    ax = fig.add_subplot(111) # Axes
    df_clean = df.dropna(subset=[option]) # Removes any null values if they exist. Data Cleaning

    mean_val = df_clean[option].mean() # Mean
    sum_val = df_clean[option].sum() # Sum

    india_rate = df_clean[option].mean() 

    df_clean.groupby('State')[option].sum().plot(kind='bar', ax=ax)

    ax.axhline(y=india_rate, color='green', linestyle='--', label ="India")  # Draws a dashed line showing what India's average is

    # X-Axis remains 'State' for all plots. Y-Axis, Title and Data Summary changes.

    if option == "Population": # Population
        ax.set_ylabel("Population")
        ax.set_title("Population Comparison")
        stats_label.config(text=f"\nTotal Population of India: {sum_val}")
    elif option == "Sex Ratio": # Sex Ratio
        ax.set_ylabel("Sex Ratio")
        ax.set_title("Sex Ratio")
        stats_label.config(text=f"\nAverage Sex Ratio in India: {mean_val}")
    elif option == "Literacy Rate": # Literacy Rate
        ax.set_ylabel(" Literacy Rate")
        ax.set_title(" Literacy Rate Comparison")
        stats_label.config(text=f"\nAverage Literacy Rate in India: {mean_val}")
    elif option == "Population density": # Population Density
        ax.set_ylabel("Population density")
        ax.set_title("Population density Comparison")
        stats_label.config(text=f"\nPopulation Density in India: {mean_val}")
    elif option == "Birth Rate": # Birth Rate
        ax.set_ylabel("Birth Rate")
        ax.set_title("Birth Rate Comparison")
        stats_label.config(text=f"\nAverage Birth Rate in India: {mean_val}")
    elif option == "Death Rate": # Death Rate
        ax.set_ylabel("Death Rate")
        ax.set_title("Death Rate Comparison")
        stats_label.config(text=f"\nAverage Death Rate in India: {mean_val}")
    elif option == "Fertility Rate": # Fertility Rate
        ax.set_ylabel("Fertility Rate")
        ax.set_title("Fertility Rate Comparison")
        stats_label.config(text=f"\nAverage Fertility Rate in India: {mean_val}")
    else:
        pass # Blank

    ax.legend()

root = tk.Tk() # Initializing the tkinter interface
root.title("Python Mini-Project: 16010422070 & 16010422078") # Title showcased in tkinter interface
root.config(bg="#F5F5F5") # Color-tone is kept light 

# To get size of window in height and width
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to screen size
window_width = screen_width
window_height = screen_height

# Calculate position coordinates
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

# Setting window size and position on screen
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Options made available through the dataset
options = ['Population','Sex Ratio','Literacy Rate','Population density','Birth Rate','Death Rate','Fertility Rate']

dropdown_var = tk.StringVar() #All options are in string format and hence when 'get' is used, It will obtain a string 
dropdown_var.set(options[0]) # Default option is Population

dropdown = tk.OptionMenu(root, dropdown_var, *options)  #Initializing the dropdown/ optionmenu
dropdown.config(bg="#A0A0A0", fg="#000000")
dropdown.grid(row=0, column=0, columnspan=3) # Placement

# Creating Buttons

plot_button = tk.Button(root, text="Plot", command=plot, bg= "#4B8BBE", fg="#FFFFFF", height=3, width=20)
plot_button.grid(row=1, column=0, padx=10, pady=10) # Placement of the plot button

quit_button = tk.Button(root,text = "End", command = root.destroy, bg= "#4B8BBE", fg="#FFFFFF", height=3, width=20)
quit_button.grid(row=1, column=2, padx=10, pady=10) # Placement of the quit button

# Blank Label so that we can utilize it when the function is called / button is pressed.

stats_label = tk.Label(root, text="",  bg="#F5F5F5", fg="#000000")
stats_label.grid(row=3, column=0, columnspan=2) # Placement for where the analysis will come. 

# Putting all of it on the screen.
root.mainloop()