import json
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog

# Helper function
def finalizeEntry():
    if subjectID != "":
        subject = {}
        subject["id"] = subjectID
        subject["date"] = subjectDate
        subject["time"] = subjectTime
        subject["comments"] = comments
        subject["data"] = data
        subjects.append(subject)

# creating tkinter window 
root = Tk()
root.withdraw()
  
# Open file
filename = filedialog.askopenfilename(title="Select AZK file", filetypes=(("AZK", "*.azk"), ("All files", "*.*")))

try:
    
    fd = open(filename, "rb")
    row = 0
    lines = fd.readlines()
    entries = 0
    entry = 0
    subjects = []
    subjectID = ""
    comments = []
    data = []
    warnings = 0

    for line in lines:
        row = row + 1
        try:
            line = line.decode("ascii")
        except:
            line = "! Can't decode line number " + str(row) + " as ASCII."
        if line.strip() == "": # Skip empty lines
            None
        elif (line.find("Subjects incorporated")>=0):
            entries = int(line.partition(": ")[2])
            print("Reading " + str(entries) + " subjects...")
        elif (line.find("Subject ") >=0 ):
            subjectID = line.partition(",")[0].partition(" ")[2]
            subjectDate = line.split(" ")[2]
            subjectTime = line.split(" ")[3]
            dmdxVersion = line.split(" ")[7][:-1]
            comments = []
            data = []   
        elif line.find("**********") >= 0: # Subject splitter
            entry = entry + 1        
            root.update_idletasks() 
            finalizeEntry()
            subjectID = ""
        elif line.find("Item") >= 0: # Table headers
            None
        elif line.find("Data") >= 0: # Machine name
            None
        elif line.startswith("!"): # Experiment comments
            comments.append(line)
        elif (subjectID != ""):
            titles = ["Item", "Response Time", "Clock On Time"]
            data.append(dict(zip(titles,[token.strip() for token in line.split()])))
        else:
            print("Warning: experiment lines not linked to subject: " + line)
            warnings = warnings + 1
    
    finalizeEntry()
    fd.close()
    fd = open(filename[:-3]+"json", "w")
    fd.write(json.dumps(subjects, sort_keys=True, indent=4))
    fd.close()

    print("Done.")
    if warnings > 0:
        messagebox.showwarning("Warning", "Conversion to JSON completed with " + str(warnings) + " warnings.")
    else:
        messagebox.showinfo("Information", "Conversion to JSON completed!")

except Exception as ex:
    if hasattr(ex, 'message'):
        messagebox.showerror("Error", "Conversion to JSON failed!\n"+str(ex.message))
        print(ex.message)
    else:
        messagebox.showerror("Error", "Conversion to JSON failed!\n"+repr(ex))
        print(repr(ex))
finally:
    root.quit()
