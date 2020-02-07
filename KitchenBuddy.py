import tkinter as tk
import csv

def mainWindow():
    root = tk.Tk()
    root.geometry("800x800")
    root.title('Kitchen Buddy')

    addRecipeButton = tk.Button(root,text='Add Recipe', command=addRecipe)
    addRecipeButton.grid(row=0,column=1)


    root.mainloop()


def addRecipe():
    addRecipe = tk.Tk()
    addRecipe.geometry('800x800')
    addRecipe.title('Add Recipe')
    
    nameLabel = tk.Label(addRecipe, text='Recipe Name')
    nameLabel.grid(row=0,column=0)

    nameEntry = tk.Entry(addRecipe)
    nameEntry.grid(row=0,column=1)

    timeLabel = tk.Label(addRecipe,text='Cook Time')
    timeLabel.grid(row=1,column=0)

    timeEntry = tk.Entry(addRecipe)
    timeEntry.grid(row=1,column=1)
    
    x = 2

    for l in range(30):
        lab=tk.Label(addRecipe,text='Ingredient')
        lab.grid(row=x,column=0)
        x += 1

    rr = 2

    for u in range(30):
        lbl=tk.Label(addRecipe,text='Qty')
        lbl.grid(row=rr,column=2)
        rr += 1

    ing0=tk.Entry(addRecipe)
    ing1=tk.Entry(addRecipe)
    ing2=tk.Entry(addRecipe)
    ing3=tk.Entry(addRecipe)
    ing4=tk.Entry(addRecipe)
    ing5=tk.Entry(addRecipe)
    ing6=tk.Entry(addRecipe)
    ing7=tk.Entry(addRecipe)
    ing8=tk.Entry(addRecipe)
    ing9=tk.Entry(addRecipe)
    ing10=tk.Entry(addRecipe)
    ing11=tk.Entry(addRecipe)
    ing12=tk.Entry(addRecipe)
    ing13=tk.Entry(addRecipe)
    ing14=tk.Entry(addRecipe)
    ing15=tk.Entry(addRecipe)
    ing16=tk.Entry(addRecipe)
    ing17=tk.Entry(addRecipe)
    ing18=tk.Entry(addRecipe)
    ing19=tk.Entry(addRecipe)
    ing20=tk.Entry(addRecipe)
    ing21=tk.Entry(addRecipe)
    ing22=tk.Entry(addRecipe)
    ing23=tk.Entry(addRecipe)
    ing24=tk.Entry(addRecipe)
    ing25=tk.Entry(addRecipe)
    ing26=tk.Entry(addRecipe)
    ing27=tk.Entry(addRecipe)
    ing28=tk.Entry(addRecipe)
    ing29=tk.Entry(addRecipe)

    ing0.grid(row=2,column=1)
    ing1.grid(row=3,column=1)
    ing2.grid(row=4,column=1)
    ing3.grid(row=5,column=1)
    ing4.grid(row=6,column=1)
    ing5.grid(row=7,column=1)
    ing6.grid(row=8,column=1)
    ing7.grid(row=9,column=1)
    ing8.grid(row=10,column=1)
    ing9.grid(row=11,column=1)
    ing10.grid(row=12,column=1)
    ing11.grid(row=13,column=1)
    ing12.grid(row=14,column=1)
    ing13.grid(row=15,column=1)
    ing14.grid(row=16,column=1)
    ing15.grid(row=17,column=1)
    ing16.grid(row=18,column=1)
    ing17.grid(row=19,column=1)
    ing18.grid(row=20,column=1)
    ing19.grid(row=21,column=1)
    ing20.grid(row=22,column=1)
    ing21.grid(row=23,column=1)
    ing22.grid(row=24,column=1)
    ing23.grid(row=25,column=1)
    ing24.grid(row=26,column=1)
    ing25.grid(row=27,column=1)
    ing26.grid(row=28,column=1)
    ing27.grid(row=29,column=1)
    ing28.grid(row=30,column=1)
    ing29.grid(row=31,column=1)

    q0=tk.Entry(addRecipe)
    q1=tk.Entry(addRecipe)
    q2=tk.Entry(addRecipe)
    q3=tk.Entry(addRecipe)
    q4=tk.Entry(addRecipe)
    q5=tk.Entry(addRecipe)
    q6=tk.Entry(addRecipe)
    q7=tk.Entry(addRecipe)
    q8=tk.Entry(addRecipe)
    q9=tk.Entry(addRecipe)
    q10=tk.Entry(addRecipe)
    q11=tk.Entry(addRecipe)
    q12=tk.Entry(addRecipe)
    q13=tk.Entry(addRecipe)
    q14=tk.Entry(addRecipe)
    q15=tk.Entry(addRecipe)
    q16=tk.Entry(addRecipe)
    q17=tk.Entry(addRecipe)
    q18=tk.Entry(addRecipe)
    q19=tk.Entry(addRecipe)
    q20=tk.Entry(addRecipe)
    q21=tk.Entry(addRecipe)
    q22=tk.Entry(addRecipe)
    q23=tk.Entry(addRecipe)
    q24=tk.Entry(addRecipe)
    q25=tk.Entry(addRecipe)
    q26=tk.Entry(addRecipe)
    q27=tk.Entry(addRecipe)
    q28=tk.Entry(addRecipe)
    q29=tk.Entry(addRecipe)

    q0.grid(row=2,column=3)
    q1.grid(row=3,column=3)
    q2.grid(row=4,column=3)
    q3.grid(row=5,column=3)
    q4.grid(row=6,column=3)
    q5.grid(row=7,column=3)
    q6.grid(row=8,column=3)
    q7.grid(row=9,column=3)
    q8.grid(row=10,column=3)
    q9.grid(row=11,column=3)
    q10.grid(row=12,column=3)
    q11.grid(row=13,column=3)
    q12.grid(row=14,column=3)
    q13.grid(row=15,column=3)
    q14.grid(row=16,column=3)
    q15.grid(row=17,column=3)
    q16.grid(row=18,column=3)
    q17.grid(row=19,column=3)
    q18.grid(row=20,column=3)
    q19.grid(row=21,column=3)
    q20.grid(row=22,column=3)
    q21.grid(row=23,column=3)
    q22.grid(row=24,column=3)
    q23.grid(row=25,column=3)
    q24.grid(row=26,column=3)
    q25.grid(row=27,column=3)
    q26.grid(row=28,column=3)
    q27.grid(row=29,column=3)
    q28.grid(row=30,column=3)
    q29.grid(row=31,column=3)






    def save():
        fileName = nameEntry.get() + '.csv'
        for i in range(30):
            ing[i] = box.get()
        
        with open(fileName, 'w') as f:
            writer = csv.DictWriter

        pass

    saveButton = tk.Button(addRecipe, text='Save Recipe',command=save)
    saveButton.grid(row=33,column=0,pady=10)

mainWindow()
