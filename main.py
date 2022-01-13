import numpy as np
from matplotlib import pyplot as pl
import csv
import tkinter as tk

def load_data():
    #reads through the csv and gathers all the needed
    #data into several lists, which is then returned.
    with open("Vaccination data.csv","r") as file:
        reader = csv.reader(file)
        data_groups = []
        dose1 = []
        dose2 = []
        dose3 = []
        for row in reader:
            if row[0].startswith("#"):
                continue
            data_groups.append(row[0])
            dose1.append(float(row[1]))
            dose2.append(float(row[2]))
            dose3.append(float(row[3]))
    return data_groups,dose1,dose2,dose3

def create_graph():
    #a procedure to load, format and show the data from the csv.

    #load data from csv
    data_groups,dose1,dose2,dose3 = load_data()

    #creates the indexes (gaps between the bars)
    ind = np.arange(15)
    width = 0.25

    #ind+width allows for even spacing of the bars
    bar1 =  pl.bar(ind, dose1, width, color = 'y')
    bar2 =  pl.bar(ind+width, dose2, width, color='b')
    bar3 =  pl.bar(ind+width*2, dose3, width, color = 'g')

    #set axis labels and title
    pl.xlabel("Age Groups")
    pl.ylabel('Percentage of People with Vaccine Dose N')
    pl.title("Percentage of people with vaccines in different age groups")

    #set the ticks (words along x axis), add a key and then show the graph
    pl.xticks(ind+width,data_groups)
    pl.legend( (bar1, bar2,bar3), ('Dose 1','Dose 2','Dose 3') )

def save_graph():
    #a procedure that takes a filename, checks it and corrects it, then saves
    filename=entry.get()
    #check that the file name is not empty or just an extension
    if not filename.split(".")[0]:
        filename = "Covid_Anlysis" + filename #fixes name if needed
        tk.messagebox.showinfo(message="No filename entered.\nDefaulted to \"Covid_Analysis\"") #error box

    try: #attempts to save
        pl.savefig(filename)
    except ValueError: #changes file extension if needed. Any characters after the first . are discarded (data.2.png would become data.png)
        tk.messagebox.showinfo(message="Unsupported file type. Defaulted to \".png\"")
        pl.savefig(filename.split(".")[0]+".png")


#load data
create_graph()

#create a window
window = tk.Tk()
window.geometry('200x160')
window.title("Covid Analysis")

#create buttons
show = tk.Button(window,text='View Graph',width=10,command=pl.show).place(x=40,y=20)
save = tk.Button(window,text='Save Graph',width=10,command=save_graph).place(x=40,y=50)

#label
tk.Label(window,text="File Name:",width=12).place(x=44,y=82)
entry = tk.Entry(window,width=12)
entry.place(x=44,y=100)

#start window
window.mainloop()