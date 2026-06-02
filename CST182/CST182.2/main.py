import matplotlib
import numpy as np
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) #NOTE TO PACK GRAPHS INTO FRAME
import sqlite3
import tkinter as tk
from tkinter import ttk
import pandas as pd
import defs

#NOTE GET FROM DEFS
deviceOptions = defs.deviceList
repairOptions = defs.repairOptions
statusOptions = defs.statusList

#NOTE TO KEEP LOGICAL ORDER OF CODE, TOP TO BOTTOM
def main():
    app = Application()
    app.mainloop()

#_______________________________________________________________ ROOT CLASS _______________________________________________________________#
#NOTE INITIALISES APPLICATION ROOT AND SETS UP FRAMES
class Application(tk.Tk, object):
    def __init__(self):
        super().__init__()
        self.title("Ticket Manager")

       #NOTE MAKE FULL SCREEN BY DEFAULT, NOT THE SAME AS .attributes(-Fullscreen, bool)
        self.state("zoomed")

       #NOTE WEIGTH THE GRID TO SACLE WITH RATIO
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

       #NOTE START SHOW ALL FRAME CLASS
        showAll_Frame = ShowAll(self)
        showAll_Frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

       #NOTE START TOOLBAR STATS CLASS
        toolbar_Frame = ToolBarStat(self)
        toolbar_Frame.grid(row=3, column=2, sticky="sew", padx=5, pady=5)



#_______________________________________________________________ CUSTOMER FORM CLASS _______________________________________________________________#
#NOTE INITIALISES NEW TICKET INPUT FRAME

class InputForm(tk.Tk):
    def __init__(self,  ):
        super().__init__()
        self.title("New Ticket")

        #SETUP FRAME
        self.columnconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)


       #NOTE TICKET VALUES
        self.ticketID = defs.GenerateUniqueID() #NOTE GENERATE FRESH ID
        self.name = str
        self.dropOffDate = str
        self.pickupDate = str
        self.device = str
        self.diagnosis = str
        self.repair = str
        self.notes = str

        self.status = str #TODO IMPLEMENT
        self.costs = float
        self.time = float


       #ID ENTRY
       #NOTE GENEATES UNIQUE ID ON FRESH TICKET
        self.idLabel = tk.Label(self, text="Ticket ID")
        self.idLabel.grid(row=0, column=1, sticky="ew")

        self.idEntry = ttk.Entry(self)
        self.idEntry.grid(row=0, column=0, sticky="ew")
        self.idEntry.bind("<Return>", self.save_ticket)
        self.idEntry.insert(0, self.ticketID)


       #NAME ENTRY
        self.nameLabel = tk.Label(self, text="Customer Name")
        self.nameLabel.grid(row=1, column=1, sticky="ew")

        self.nameEntry = ttk.Entry(self)
        self.nameEntry.grid(row=1, column=0, sticky="ew")
        self.nameEntry.bind("<Return>", self.save_ticket)
        self.nameEntry.insert(0, "Enter Name")


       #DROP OFF DATE ENTRY
        self.dropOffLabel = tk.Label(self, text="Drop Off Date")
        self.dropOffLabel.grid(row=2, column=1, sticky="ew")

        self.dropDateEntry = ttk.Entry(self)
        self.dropDateEntry.grid(row=2, column=0, sticky="ew")
        self.dropDateEntry.bind("<Return>", self.save_ticket)
        self.dropDateEntry.insert(0, "Enter Date")


       #PICKUP DATE ENTRY
        self.pickUpLabel = tk.Label(self, text="Pick Up Date")
        self.pickUpLabel.grid(row=3, column=1, sticky="ew")

        self.pickupDateEntry = ttk.Entry(self)
        self.pickupDateEntry.grid(row=3, column=0, sticky="ew")
        self.pickupDateEntry.bind("<Return>", self.save_ticket)
        self.pickupDateEntry.insert(0, "Enter Date")


       #DEVICE ENTRY
       #NOTE DROP DOWN LIST
        self.deviceLabel = tk.Label(self, text="Selected Device")
        self.deviceLabel.grid(row=4, column=1, sticky="ew")

        self.selected_value = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.selected_value, values=deviceOptions)
        self.combo.grid(row=4, column=0, sticky="ew")
        self.combo.current(0)  #SET DEFAULT VALUE


       #DIAGNOSIS ENTRY
        self.diagnosisLabel = tk.Label(self, text="Diagnosis")
        self.diagnosisLabel.grid(row=5, column=1, sticky="ew")

        self.diagnosisEntry = ttk.Entry(self)
        self.diagnosisEntry.grid(row=5, column=0, sticky="ew")
        self.diagnosisEntry.bind("<Return>", self.save_ticket)
        self.diagnosisEntry.insert(0, "HDMI")


       #REPAIRS ENTRY
       #NOTE DROP DOWN LIST
        self.repairsLabel = tk.Label(self, text="Repairs")
        self.repairsLabel.grid(row=6, column=1, sticky="ew")

        self.selected_value2 = tk.StringVar()
        self.combo2 = ttk.Combobox(self, textvariable=self.selected_value2, values=repairOptions)
        self.combo2.grid(row=6, column=0, sticky="ew")
        self.combo2.current(0)  #SET DEFAULT VALUE


       #NOTES ENTRY
        self.notesLabel = tk.Label(self, text="Repair Notes")
        self.notesLabel.grid(row=10, column=1, sticky="ew")

        self.notesText_box = tk.Text(self, height=5, width=40, wrap='word')
        self.notesText_box.grid(row=10, column=0, sticky="ew")
        self.notesText_box.insert(tk.END, "Enter Repair Notes Here...")


        #TIME ENTRY
        self.timeLabel = tk.Label(self, text="Estimated Time")
        self.timeLabel.grid(row=7, column=1, sticky="ew")

        self.timeEntry = ttk.Entry(self)
        self.timeEntry.grid(row=7, column=0, sticky="ew")
        self.timeEntry.insert(0, "1.5")

        #COST ENTRY
        self.costLabel = tk.Label(self, text="Cost")
        self.costLabel.grid(row=8, column=1, sticky="ew")

        self.costEntry = ttk.Entry(self)
        self.costEntry.grid(row=8, column=0, sticky="ew")
        self.costEntry.insert(0, "150.00")

       #STATUS ENTRY
       #NOTE DROP DOWN LIST
        self.statusLabel = tk.Label(self, text="Select Status")
        self.statusLabel.grid(row=9, column=1, sticky="ew")

        self.statusCombo = ttk.Combobox(self, values=statusOptions)
        self.statusCombo.grid(row=9, column=0, sticky="ew")
        self.statusCombo.current(0)  #SET DEFAULT VALUE



       #NOTE CELL TO PACK BUTTONS LOCALLY
        container_frame = tk.Frame(self)
        container_frame.grid(row=11, column=0)

       #NOTE BUTTONS
       #ADD TO LIST BUTTON
        self.save_btn = ttk.Button(container_frame, text="Save", command=self.save_ticket)
        self.save_btn.pack(side=tk.LEFT, padx=5)


       #CLEAR LIST BUTTON
        self.clear_btn = ttk.Button(container_frame, text="Clear", command=self.clear_list)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

       #CANCEL BUTTON
        self.cancel_btn = ttk.Button(container_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

       #EXPORT BUTTON
        self.export_btn = ttk.Button(container_frame, text="Export", command=self.export_ticket)
        self.export_btn.pack(side=tk.LEFT, padx=5)



   #NOTE BUTTON FUNCTIONS
    def save_ticket(self, _event=None):
        text = self.nameEntry.get()

        #NOTE VALIDATE DATES
        isValidDate = defs.ValidateDate(self.dropDateEntry.get())

        #TODO CHECK BOTH DATES THEN CONTINUE IF BOTH ARE VALID
        if isValidDate == True:
            print("True")
        else:
            print("False")
            #TODO ADD ERROR CATCH

        if text:
            self.notesText_box.insert(tk.END, text)
            #self.nameEntry.delete(0, tk.END)

            #NOTE SET VARIABLES FROM ENTRIES
            self.ticketID = self.idEntry.get()
            self.name = self.nameEntry.get()
            self.dropOffDate = self.dropDateEntry.get()
            self.pickupDate = self.pickupDateEntry.get()
            self.device = self.combo.current()
            self.diagnosis = self.diagnosisEntry.get()
            self.repair = self.combo2.current()
            self.notes = self.notesText_box.get("1.0", "end-1c")
            self.time = self.timeEntry.get()
            self.costs = self.costEntry.get()
            self.status = self.statusCombo.current()


           #NOTE SEND "TICKET DATA" TO WRITE TICKET DEF
            defs.NewTicket(self.ticketID, self.name, self.dropOffDate, self.pickupDate, self.device, self.diagnosis, self.repair, self.notes, self.time, self.costs, self.status)

           # TODO refresh DB



    def clear_list(self):
        #NOTE CLEAR ALL ENTRY FIELDS
        self.idEntry.delete(0, tk.END)
        self.nameEntry.delete(0, tk.END)
        self.dropDateEntry.delete(0, tk.END)
        self.pickupDateEntry.delete(0, tk.END)
        self.combo.delete(0, tk.END)
        self.diagnosisEntry.delete(0, tk.END)
        self.combo2.delete(0, tk.END)
        self.notesText_box .delete("0.0", tk.END)

    def cancel(self):
        #NOTE CLOSE WINDOW
        self.destroy()

    #NOTE SAVE TO TXT AND SEND TO PRINTER
    def export_ticket(self):
        dataToExport = self.ticketID, self.name, self.dropOffDate, self.pickupDate, self.device, self.diagnosis, self.repair, self.notes, self.time, self.costs, self.status
        defs.PrintTicket(dataToExport)



#_______________________________________________________________ OPEN FORM CLASS _______________________________________________________________#
#NOTE OPEN EXISTING TICKET
class OpenForm(tk.Tk):
    def __init__(self, ticketID, name, dropOffDate, pickupDate, device, diagnosis, repair, notes, time, costs, status):
        super().__init__()


        #SETUP FRAME
        self.columnconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)


       #NOTE TICKET VALUES TO BE LOADED
        self.ticketID = ticketID
        self.name = name
        self.dropOffDate = dropOffDate
        self.pickupDate = pickupDate
        self.device = device
        self.diagnosis = diagnosis
        self.repair = repair
        self.notes = notes
        self.time = time
        self.costs = costs
        self.status = status


        #NOTE ASSIGN UNIQUE TITLE
        self.title("Ticket: " + self.ticketID + " " + self.name)

       #ID ENTRY
       #NOTE GENEATES UNIQUE ID ON FRESH TICKET
        self.idLabel = tk.Label(self, text="Ticket ID")
        self.idLabel.grid(row=0, column=1, sticky="ew")

        self.idEntry = ttk.Entry(self)
        self.idEntry.grid(row=0, column=0, sticky="ew")
        ##self.idEntry.bind("<Return>", self.save_ticket)
        self.idEntry.insert(0, self.ticketID)
        self.idEntry.config(state="readonly")

       #NAME ENTRY
        self.nameLabel = tk.Label(self, text="Customer Name")
        self.nameLabel.grid(row=1, column=1, sticky="ew")

        self.nameEntry = ttk.Entry(self)
        self.nameEntry.grid(row=1, column=0, sticky="ew")
        #self.nameEntry.bind("<Return>", self.save_ticket)
        self.nameEntry.insert(0,  self.name)
        self.nameEntry.config(state="readonly")


       #DROP OFF DATE ENTRY
        self.dropOffLabel = tk.Label(self, text="Drop Off Date")
        self.dropOffLabel.grid(row=2, column=1, sticky="ew")

        self.dropDateEntry = ttk.Entry(self)
        self.dropDateEntry.grid(row=2, column=0, sticky="ew")
       # self.dropDateEntry.bind("<Return>", self.save_ticket)
        self.dropDateEntry.insert(0, self.dropOffDate)
        self.dropDateEntry.config(state="readonly")

       #PICKUP DATE ENTRY
        self.pickUpLabel = tk.Label(self, text="Pick Up Date")
        self.pickUpLabel.grid(row=3, column=1, sticky="ew")

        self.pickupDateEntry = ttk.Entry(self)
        self.pickupDateEntry.grid(row=3, column=0, sticky="ew")
        #self.pickupDateEntry.bind("<Return>", self.save_ticket)
        self.pickupDateEntry.insert(0, self.pickupDate)
        self.pickupDateEntry.config(state="readonly")

       #DEVICE ENTRY
       #NOTE DROP DOWN LIST
        self.deviceLabel = tk.Label(self, text="Selected Device")
        self.deviceLabel.grid(row=4, column=1, sticky="ew")

        self.selected_value = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.selected_value, values=deviceOptions)
        self.combo.grid(row=4, column=0, sticky="ew")
        self.combo.current(0)  #SET DEFAULT VALUE



       #DIAGNOSIS ENTRY
        self.diagnosisLabel = tk.Label(self, text="Diagnosis")
        self.diagnosisLabel.grid(row=5, column=1, sticky="ew")

        self.diagnosisEntry = ttk.Entry(self)
        self.diagnosisEntry.grid(row=5, column=0, sticky="ew")
        #self.diagnosisEntry.bind("<Return>", self.save_ticket)
        self.diagnosisEntry.insert(0, self.diagnosis)
        self.diagnosisEntry.config(state="readonly")


       #REPAIRS ENTRY
       #NOTE DROP DOWN LIST
        self.repairsLabel = tk.Label(self, text="Repairs")
        self.repairsLabel.grid(row=6, column=1, sticky="ew")

        self.selected_value2 = tk.StringVar()
        self.combo2 = ttk.Combobox(self, textvariable=self.selected_value2, values=repairOptions)
        self.combo2.grid(row=6, column=0, sticky="ew")
        self.combo2.current(0)  #SET DEFAULT VALUE


        #NOTES ENTRY
        self.notesLabel = tk.Label(self, text="Repair Notes")
        self.notesLabel.grid(row=10, column=1, sticky="ew")

        self.notesText_box = tk.Text(self, height=5, width=40, wrap='word')
        self.notesText_box.grid(row=10, column=0, sticky="ew")
        self.notesText_box.insert(tk.END, "Enter Repair Notes Here...")

        #TIME ENTRY
        self.timeLabel = tk.Label(self, text="Estimated Time")
        self.timeLabel.grid(row=7, column=1, sticky="ew")

        self.timeEntry = ttk.Entry(self)
        self.timeEntry.grid(row=7, column=0, sticky="ew")
        self.timeEntry.insert(0, "1.5")
        self.timeEntry.config(state="readonly")

        #COST ENTRY
        self.costLabel = tk.Label(self, text="Cost")
        self.costLabel.grid(row=8, column=1, sticky="ew")

        self.costEntry = ttk.Entry(self)
        self.costEntry.grid(row=8, column=0, sticky="ew")
        self.costEntry.insert(0, "150.00")
        self.costEntry.config(state="readonly")

       #STATUS ENTRY
       #NOTE DROP DOWN LIST
        self.statusLabel = tk.Label(self, text="Select Status")
        self.statusLabel.grid(row=9, column=1, sticky="ew")


        self.statusCombo = ttk.Combobox(self, values=statusOptions)
        self.statusCombo.grid(row=9, column=0, sticky="ew")
        self.statusCombo.current(0)  #SET DEFAULT VALUE
        self.statusCombo.config(state="readonly")


       #NOTE CELL TO PACK BUTTONS LOCALLY
        container_frame = tk.Frame(self)
        container_frame.grid(row=11, column=0)

       #NOTE BUTTONS
       #SAVE BUTTON
        self.save_btn = ttk.Button(container_frame, text="Save", command = self.save_ticket)
        self.save_btn.pack(side=tk.LEFT, padx=5)

       #EDIT LIST BUTTON
        self.edit_btn = ttk.Button(container_frame, text="Edit", command = self.edit_ticket)
        self.edit_btn.pack(side=tk.LEFT, padx=5)

       #CANCEL BUTTON
        self.cancel_btn = ttk.Button(container_frame, text="Cancel", command = self.cancel)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

       #EXPORT BUTTON
        self.export_btn = ttk.Button(container_frame, text="Export", command = self.export_ticket)
        self.export_btn.pack(side=tk.LEFT, padx=5)
       #TODO ADD FUNCTIONS TO EDIT AND SAVE

    #NOTE ENABLE FIELDS
    def edit_ticket(self): #TODO ADD NEW VARIABLES
        self.idEntry.config(state="normal")
        self.nameEntry.config(state="normal")
        self.dropDateEntry.config(state="normal")
        self.pickupDateEntry.config(state="normal")

        self.diagnosisEntry.config(state="normal")

        self.notesText_box.config(state="normal")
        self.costEntry.config(state="normal")
        self.timeEntry.config(state="normal")


    def cancel(self):
        #NOTE CLOSE WINDOW
        self.destroy()



    def save_ticket(self, _event=None):
        text = self.nameEntry.get()

        #NOTE VALIDATE DATES
        isValidDate1 = defs.ValidateDate(self.dropDateEntry.get())
        isValidDate2 = defs.ValidateDate(self.pickupDateEntry.get())

        #TODO CHECK BOTH DATES THEN CONTINUE IF BOTH ARE VALID
        if isValidDate1 == True and isValidDate2 == True:
            print("True")
            if text:
                #NOTE SET VARIABLES FROM ENTRIES
                self.ticketID = self.idEntry.get()
                self.name = self.nameEntry.get()
                self.dropOffDate = self.dropDateEntry.get()
                self.pickupDate = self.pickupDateEntry.get()
                self.device = self.combo.current()
                self.diagnosis = self.diagnosisEntry.get()
                self.repair = self.combo2.current()
                self.notes = self.notesText_box.get("1.0", "end-1c")
                self.time = self.timeEntry.get()
                self.costs = self.costEntry.get()
                self.status = self.statusCombo.current()
                defs.NewTicket(self.ticketID, self.name, self.dropOffDate, self.pickupDate, self.device, self.diagnosis, self.repair, self.notes, self.time, self.costs, self.status)

        else:
            print("BAD DATE")
            #TODO ADD ERROR CATCH


           # TODO refresh DB

    #NOTE SAVE TO TXT AND SEND TO PRINTER
    def export_ticket(self):
        dataToExport = self.ticketID, self.name, self.dropOffDate, self.pickupDate, self.device, self.diagnosis, self.repair, self.notes, self.time, self.costs, self.status
        defs.PrintTicket(dataToExport)


#_______________________________________________________________ SHOW ALL CLASS _______________________________________________________________#
#NOTE SOW ALL TICKETS FRAME

class ShowAll(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #SETUP FRAME
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

       #NOTE SHOW DATABASE
        conn = sqlite3.connect('repair_tickets.db')
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Ticket, Name ,DropOffDate, PickupDate, Device, Diagnosis, Repair, Notes, Time, Cost, Status FROM REPAIR_TICKETS")
        rows = cursor_obj.fetchall()


        #NOTE DISPLAY SQL RESULTS AS A TREE WIDGET
        columns = [description[0] for description in cursor_obj.description]
        self.tree = ttk.Treeview(self, selectmode='browse', columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=50)

        # 4. Insert Data
        for row in rows:
            self.tree.insert("", tk.END, values=row)

        self.tree.grid(row=1, column=0, sticky="nsew")
        conn.close()


       #NOTE SEARCH ENTRY
        self.filterEntry = ttk.Entry(self)
        self.filterEntry.grid(row=0, column=0, sticky="ew")
        self.filterEntry.insert(0, "Find...")


       #NOTE CELL TO PACK BUTTONS LOCALLY
        self.container_frame = tk.Frame(self)
        self.container_frame.grid(row=1, column=1, sticky="nsew")


       #NOTE BUTTONS
       #SEARCH BUTTON
        self.search_btn = ttk.Button(self, text="Search", command= self.search_tickets)
        self.search_btn.grid(row=0, column=1, padx=5, sticky= "new")

       #CREATE NEW TICKET
        self.new_btn = ttk.Button(self.container_frame, text="New", command= InputForm)
        self.new_btn.pack(side=tk.TOP, padx=5)

       #SELECT BUTTON

        self.select_btn = ttk.Button(self.container_frame, text="Select", command= self.RetrieveDatabase)
        self.select_btn.pack(side=tk.TOP, padx=5)

       #DELETE BUTTON
        self.delete_btn = ttk.Button(self.container_frame, text="Delete", command= self.delete_item)
        self.delete_btn.pack(side=tk.TOP, padx=5)

       #REFRESH BUTTON
        self.refresh_btn = ttk.Button(self.container_frame, text="Refresh", command= self.RetrieveDatabase)
        self.refresh_btn.pack(side=tk.TOP, padx=5)


       #SHOW STATS WINDOW
        self.stats_btn = ttk.Button(self.container_frame, text="Stats", command= GraphBox)
        self.stats_btn.pack(side=tk.BOTTOM, padx=5)


       #SHOW INFO
        self.info_btn = ttk.Button(self.container_frame, text="Info", command= InfoPanel)
        self.info_btn.pack(side=tk.BOTTOM, padx=5)


        #NOTE RETRIEVE COLUMN NAME AND REQUEST FROM SQL DATABASE ON DOUBLE CLICK
        self.tree.bind("<Double-1>", self.select_item)

    #NOTE SEARCH FOR TICKET
    def search_tickets(self): # NOTE FIND ALL OF CERTAIN TERM

        result = defs.SearchTicket(self.filterEntry.get())
        print(result)


        for item in self.tree.get_children():
            self.tree.delete(item)

        #NOTE PARSES RESULT INTO CORRECT FORMAT AND SENDS TO TREE
        count = 0
        for row in result:
            self.tree.insert("", tk.END, values=result[count])
            count += 1
        self.tree.bind("<Double-1>", self.select_item) #NOTE REBIND TO RESET ACTION
        return



    #NOTE REFRESH DATABASE VIEW
    def RetrieveDatabase(self): #TODO MOVE TO DEFS
        conn = sqlite3.connect('repair_tickets.db')
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Ticket, Name ,DropOffDate, PickupDate, Device, Diagnosis, Repair, Notes, Time, Cost, Status FROM REPAIR_TICKETS")
        rows = cursor_obj.fetchall()

        columns = [description[0] for description in cursor_obj.description]

        #NOTE DISPLAY SQL RESULTS AS A TREE WIDGET
        self.tree = ttk.Treeview(self, selectmode='browse', columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=50)

        for row in rows:
            self.tree.insert("", tk.END, values=row)

        self.tree.grid(row=1, column=0, sticky="nsew")

        #TODO ASSIGN TEXT TO COMBOBOX PREVIEW


        conn.commit()
        conn.close()
        self.tree.bind("<Double-1>", self.select_item) #NOTE REBIND TO RESET ACTION


    #NOTE GET ITEM ON DOUBLE CLICK
    def select_item(self, event):
        self.selected_ids = self.tree.identify_column(event.x)
        self.selectedRowID = self.tree.focus()


        #NOTE GET TICKET DATA
        if self.selectedRowID and self.selected_ids:
            selected = self.tree.item(self.selectedRowID, "value")
            value = selected
            print("VALUES TO BE PARSED " ,value)
            OpenForm(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10])
            print(value)
            #defs.AddToDatabase()
            self.RetrieveDatabase()
            self.tree.bind("<Double-1>", self.select_item) #NOTE REBIND TO RESET ACTION
        return

    def delete_item(self):

        self.selection = self.tree.selection()

        if not self.selection:
            messagebox.showwarning("No Selection", "Please select an item first.") #NOTE ADD TO ERROR CHECKS
            return

        self.item_id = self.selection[0]
        self.item_data = self.tree.item(self.item_id)
        self.values = self.item_data.get('values')


        self.selectedTicketID = self.values[0]

        defs.DeleteTicket(str(self.selectedTicketID))
        self. RetrieveDatabase()



#_______________________________________________________________ TOOLBAR STAT CLASS TODO _______________________________________________________________#

class ToolBarStat(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

       #NOTE CELL TO PACK LOCALLY
        container_frame = tk.Frame(self)
        container_frame.grid(row=0, column=1, sticky="ew")

       #NOTE OPEN TICKETS TODO
        self.openLabel = ttk.Label(container_frame, text="Open Tickets:")
        self.openLabel.pack(side=tk.LEFT, padx=20)


       #NOTE CLOSED TICKETS TODO
        self.closedLabel = ttk.Label(container_frame, text="Closed Tickets:")
        self.closedLabel.pack(side=tk.LEFT, padx=20)


       #NOTE PENDING PICKUP TODO
        self.pendingLabel = ttk.Label(container_frame, text="Pending Pickup:")
        self.pendingLabel.pack(side=tk.LEFT, padx=20)


#_______________________________________________________________ INFO PANEL CLASS TODO _______________________________________________________________#

class InfoPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Information")
        #NOTE INFORMATION PANEL TODO

        self.new_btn = ttk.Button(self, text="New", command= InputForm)
        self.new_btn.grid(row=0, column=0, sticky= "nw")



#_______________________________________________________________ GRAPH CLASS TODO _______________________________________________________________#

class GraphBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Statistics Viewer")
        #SETUP FRAME
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.RetrieveDatabase()
        #TODO CLEAN DATA TO DISPLAY
        #TODO ADD MULTIPLE GRAPHS


    #TESTING GET GRAPH DATA
    def RetrieveDatabase(self): #TODO MOVE TO DEFS
        conn = sqlite3.connect('repair_tickets.db')
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Ticket, Name ,DropOffDate, PickupDate, Device, Diagnosis, Repair, Notes, Time, Cost, Status FROM REPAIR_TICKETS")
        rows = cursor_obj.fetchall()

        columns = [description[0] for description in cursor_obj.description]
        conn.commit()
        conn.close()



        keys = ['Ticket', 'Name' ,'DropOffDate', 'PickupDate', 'Device', 'Diagnosis', 'Repair', 'Notes', 'Time', 'Cost', 'Status']
        values = columns
        #data = dict(zip(keys, values))


        df = pd.DataFrame(data=rows, columns=keys)
        #print(df)
        data = df.values.tolist()

        devicesList = df['Device'].tolist()

        deviceNames = defs.deviceList

        print(devicesList)
        matchedList = []

        for item in devicesList:
            if item == '0':
                matchedList.append("Xbox")
            elif item == "1":
                matchedList.append("PS4")
            elif item == "2":
                matchedList.append("PS5")
            elif item == "-1":
                matchedList.append("STEAM DECK")
            else:
                matchedList.append("SWITCH")


        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, master=self)


        #create axes
        axes = self.figure.add_subplot()

        #NOTE TODO Y LABEL NEEDS TO BE COUNT
        xLabel = matchedList
        yLabel = matchedList

        #create the barchart
        axes.bar(xLabel, yLabel) # NOTE PLOT DATA
        axes.set_title('Device Distribution')
        axes.set_ylabel('Number')

        self.figure_canvas.get_tk_widget().grid(row= 0, column =0)




#_______________________________________________________________   START APP   _______________________________________________________________#
if __name__ == "__main__":
    main()

