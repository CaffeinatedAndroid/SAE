#NOTE WRITE COMPLETED
#NOTE LOAD COMPLETED
#NOTE EDIT COMPLETED
#TODO EXPORT
#TODO FILTER
#TODO GRAPHS

from datetime import datetime
import os
import sqlite3
import random


#DEPRICATED
repairOptions = ["HDMI", "BATTERY", "USB", "LCD", "JOYSTICKS", "IC", "DAMAGED TRACE", "OTHER"]
statusList = ["Pending","Finished","ReadyForPickup"]
deviceList = ["XboxOne","XboxSeries","Switch", "SteamDeck","PS4","PS5"]


#NOTE CREATE DATABASE
def CreateSQLDatabase():


    if os.path.exists('repair_tickets.db') == False:
        connection_obj = sqlite3.connect('repair_tickets.db')

        cursor_obj = connection_obj.cursor()

        cursor_obj.execute("DROP TABLE IF EXISTS REPAIR_TICKETS")

        cursor_obj.execute("""CREATE TABLE REPAIR_TICKETS(
            Ticket VARCHAR(255),
            Name VARCHAR(255),
            DropOffDate VARCHAR(255),
            PickupDate VARCHAR(255),
            Device VARCHAR(255),
            Diagnosis VARCHAR(255),
            Repair VARCHAR(255),
            Notes VARCHAR(255),
            Time FLOAT,
            Cost FLOAT,
            Status VARCHAR(255))
            """)

        connection_obj.commit()
        connection_obj.close
        print("Database Created")

    else:
        return




#NOTE NEW TICKET
def NewTicket( ticketID, name, dropOffDate, pickupDate, device, diagnosis, repair, notes, time, costs, status):
    connection_obj = sqlite3.connect('repair_tickets.db')
    cursor_obj = connection_obj.cursor()


    #NOTE Insert data into the table using column names NOTE ADDED UNIQUE ID TODO FIX DATA
    cursor_obj.execute("INSERT INTO REPAIR_TICKETS (Ticket, Name ,DropOffDate, PickupDate, Device, Diagnosis, Repair, Notes, Time, Cost, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (ticketID, name, dropOffDate, pickupDate, device, diagnosis, repair, notes, time, costs, status))

    print("Data Inserted in the table: ")
    cursor_obj.execute("SELECT * FROM REPAIR_TICKETS")
    for row in cursor_obj.fetchall():
        print(row)

    connection_obj.commit()
    connection_obj.close()
    return


#NOTE IN PROGRESS OF MIGRATING FROM MAIN.PY TODO
def ShowAll():
    connection_obj = sqlite3.connect('repair_tickets.db')
    cursor_obj = connection_obj.cursor()
    searchFor = "SELECT * FROM repair_tickets"
    cursor_obj.execute(searchFor)
    results = cursor_obj.fetchall()
    for row in results:
        print(row)

    cursor_obj.close()
    connection_obj.close()

    return results



#NOTE GET THE DATA FROM ALL TICKET IDs
def GetTicketData(selectedTicketID):
    selected = selectedTicketID
    connection_obj = sqlite3.connect('repair_tickets.db')
    cursor_obj = connection_obj.cursor()
    data = cursor_obj.fetchall()

    # Commit changes and close connection
    connection_obj.commit()
    connection_obj.close()
    return data


#NOTE DELETE ROW VIA TICKET ID
def DeleteTicket(selection):
    connection_obj = sqlite3.connect('repair_tickets.db')
    cursor_obj = connection_obj.cursor()
    print(selection)
    data = cursor_obj.fetchall()

    delete = "DELETE FROM repair_tickets WHERE Ticket LIKE ?" #NOTE SELECT SPECIFIC TICKET
    cursor_obj.execute(delete, ('%' + selection + '%',))
    cursor_obj.close()
    connection_obj.commit()
    connection_obj.close()
    print("Ticket Deleted", selection)
    return


#NOTE SEARCH FOR ROWS MATCHING TEXT
def SearchTicket(searchTerm):

    searchResults = searchTerm
    connection_obj = sqlite3.connect('repair_tickets.db')
    cursor_obj = connection_obj.cursor()
    print(searchResults)
    searchFor = "SELECT * FROM repair_tickets WHERE Ticket LIKE ? OR Name LIKE ? OR DropOffDate LIKE ? OR PickupDate LIKE ? OR Device LIKE ? OR Diagnosis LIKE ? OR Repair LIKE ? OR Notes LIKE ? OR Time LIKE ? OR Cost LIKE ? OR Status LIKE ?" #TODO ADD NEW VARIABLES
    cursor_obj.execute(searchFor, ('%' + searchResults + '%', '%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%','%' + searchResults + '%'))

    results = cursor_obj.fetchall()
    for row in results:
        print(row)

    cursor_obj.close()
    connection_obj.close()

    return results


#NOTE VALIDATE DATE FORMATING USING DATETIME
def ValidateDate(date_Data):
    valid = bool
    try:
        dateObject = datetime.strptime(date_Data, '%d/%m/%Y')
        valid = True
        return valid

    except ValueError:
        return valid



#NOTE GENERATE UNIQUE ID
def GenerateUniqueID():

    random_numbers = []
    #TODO CHECK AGAINST SQL DATABASE

    #NOTE Generate 2 unique 3 digit numbers and check if it is free to use
    while len(random_numbers) < 2:
        num = random.randint(100, 999)
        if num not in random_numbers:
            random_numbers.append(num)

    newID = ''.join(map(str, random_numbers))
    #NOTE RETURN NEW ID TO USER FORM
    return newID



#NOTE SEND DATA TO PRINTER
#TODO ADD PRINT WINDOW
#TODO ADD FORMATTING
def PrintTicket(dataToPrint):
    nameList = ["TicketID", "Name", "DropOffDate", "PickupDate", "Device", "Diagnosis", "Repair", "Notes", "Time", "Costs", "Status"]
    count = 0
    file_path = r"ticketDB\ "+dataToPrint[0]+".txt"
    if os.path.exists(file_path):
        print('file already exists')
    else:
        # create a file
        with open(file_path, 'w') as fp:
            # uncomment if you want empty file
            for item in dataToPrint:
                fp.write(nameList[count]+":\n")
                fp.write(item+"\n\n")
                count += 1

            fp.close()
            os.startfile(file_path, "print")

    return


#NOTE TESTING
GenerateUniqueID()
#PrintTicket()
CreateSQLDatabase()
