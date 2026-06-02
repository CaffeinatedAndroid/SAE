import os
import Repairs
import random

statusList = ["Pending","Finished","NotStarted"]
deviceList = Repairs.Devices.keys()
#deviceRepairs = Repairs.Devices


#___________________________________________________________________________CLASS___________________________________________________________________________#
class Ticket:
    def __init__(self, ticketID, customerName, dropOffDate, pickUpDate, device, repairs, repairTime, status):
        self.ticketID = ticketID
        self.customerName = customerName
        self.dropOffDate = dropOffDate
        self.pickUpDate = pickUpDate
        self.device = device
        self.repairs = repairs
        self.repairTime = repairTime
        self.status = status


#___________________________________________________________________________LOGIC___________________________________________________________________________#
def AddNew():

    customerName = str(input("Name? "))
    dropOffDate = int(input("Drop off date? ")) #format date
    pickUpDate = int(input("Pick up date? ")) #format date
    ticketID = str(int(random.randint(10, 99)))+str(dropOffDate) + str(int(random.randint(10, 99)))

    #pick device
    print(*deviceList) #Shows devices from dictionary
    print("Select Device 0-2")
    chosenDevice = int(input("Device? "))
    items = list(deviceList)    # convert dictionary to templist
    device = items[chosenDevice]
    print(device)# Print chosen from items list

    #pick repairs
    repairList = Repairs.Devices.get(items[chosenDevice])
    print(*repairList.keys()) #Show repair options from selected device dictionary

    repairSel = int(input("Repairs? "))
    repairItems = list(repairList) # convert dictionary to templist
    repairs = repairItems[repairSel]
    selectedRepairs = [repairs]
    print("Selected:",repairs)

    #multi select
    while True:
        choice = input("Add more repair items? (1. Yes 2.No): ")

        if choice == "1":
            repairList = Repairs.Devices.get(items[chosenDevice])
            print(*repairList.keys()) #Show repair options from selected device dictionary

            repairSel = int(input("Repairs? "))
            repairItems = list(repairList) # convert dictionary to templist
            repairs = repairItems[repairSel]
            selectedRepairs.append(repairs)


        elif choice == "2":
            print(*selectedRepairs) #Finished picking
            break
        else:
            print("Invalid choice. Please try again.")


    #calculate Time
    time = 0.0
    for each in selectedRepairs:
        time = time + Repairs.Devices[device][repairs]["estTime"]
    print("Estimated Labour time is: ", time)
    repairTime = time
    repairs = selectedRepairs

    #SHOW STATUS OPTIONS
    count = 0
    for option in statusList:
        print(count,".",option, sep='',end='   ')
        count +=1
    print("\n")

    status = int(input("Status?"))#Gets int and selects status from list
    statusTitle = statusList[status]

    ticket = Ticket(ticketID,customerName,dropOffDate,pickUpDate,device,repairs,repairTime,statusTitle)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\x1b[32m _____________________________________________________\x1b[0m")
    print("\x1b[32m|                                                     |\x1b[0m")
    print("\x1b[32m|                    ","\x1b[37m\x1b[1mNEW TICKET\x1b[0m","\x1b[32m                     |\x1b[0m")
    print("\x1b[32m|_____________________________________________________|\x1b[0m\n\n")
    #PRINT DETAILS and continue
    print("Ticket ID: ")
    print("Name: ", customerName)
    print("Drop Off Date: ", dropOffDate)
    print("Pickup Date: ", pickUpDate)
    print("Device: ", device)
    print("Selected Repairs: ", *repairs)
    print("Estimated Repair Time: ", repairTime)
    print("Ticket Status: ", statusTitle)

    with open('Tickets/'+str(ticket.ticketID), 'w') as f:#Open local folder and write ticket to file
        f.write(str(ticket.ticketID)+"-")
        f.write(ticket.customerName+"-")
        f.write(str(int(ticket.dropOffDate))+"-")
        f.write(str(int(ticket.pickUpDate))+"-")
        f.write(ticket.device+"-")
        f.write(str(ticket.repairs)+"-")#convert list to string
        f.write(str(float(ticket.repairTime))+"-")
        f.write(statusTitle)
        f.close



def ShowAll():#Show all Tickets in folder
    for entry in os.scandir("Tickets"):
        if entry.is_file():
            with open(entry.path, 'r') as file:
                text = file.read()
                cleaned = text.split('-')
                reordered = dict(enumerate(cleaned))

                #Colour code by status
                if reordered.get(7) == 'Pending':
                    print("\x1b[34m ",cleaned," \x1b[0m")

                elif reordered.get(7) == 'Finished':
                    print("\x1b[32m ",cleaned," \x1b[0m")

                elif reordered.get(7) == 'NotStarted':
                    print("\x1b[33m ",cleaned," \x1b[0m")#CORRECT BUT NEED TO REFRESH DATABASE




# def Edit(sel):#-----------------------------------------------------TODO----------------
#     for entry in os.scandir("Tickets"):
#             if entry.is_file():
#                 with open(entry.path, 'r') as file:
#                     text = file.read()
#                     cleaned = text.split('-')
#                     reordered = dict(enumerate(cleaned))
#
#                     my_dict ={}
#                     if reordered.get(0) == sel:
#                         print("{__line__}","\x1b[34m ",reordered," \x1b[0m")
#                         #convert to dict
#                         key, value = line.strip().split('\t', 1)
#                         my_dict[key] = float(value)
#
#
#
#                     choice = input("1: Name 2:Dropoff 3:Date 4:PickupDate 5:Device 6:Repairs 7:Status: ")
#
#                         #break into feilds
#                         #select feild to edit
#                         #save
#                     if choice == "1":
#                             print(my_dict,"\n")
#                             newName = str(input("Name? "))
#                             reordered["customerName"] = newName
#                             ShowAll()
#                             return
#
#                     elif choice == "2":
#                             newDropDate = int(input("Drop off date? ")) #format date
#
#
#
#                     #
#                     #
#
#                              #Finished picking
#                     #


def Delete(selected):
        os.remove('Tickets/'+selected)
        ShowAll()
        return


def Select(sel):
    for entry in os.scandir("Tickets"):
        if entry.is_file():
            with open(entry.path, 'r') as file:
                text = file.read()
                cleaned = text.split('-')
                reordered = dict(enumerate(cleaned))

                if reordered.get(0) == sel:
                    print("\x1b[0m ",reordered," \x1b[0m")
                else:
                    return
                print(input("To continue press enter"))
                ShowAll()

def Export(selected):
    #Change Directories)
    #FEED VALUES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TODO
    os.open('Tickets/'+selected)
    new_file = open(selected+".txt","w")#Open selected Ticket

    new_file.close
    #Output Reciept-----------------------------------TODO-------------------------------------------------------------------------
    return



def Filter(sel):
    for entry in os.scandir("Tickets"):
        if entry.is_file():
            with open(entry.path, 'r') as file:
                text = file.read()
                cleaned = text.split('-')
                reordered = dict(enumerate(cleaned))
                if reordered.get(0) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")
                elif reordered.get(1) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")

                elif reordered.get(2) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")

                elif reordered.get(3) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")

                elif reordered.get(4) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")


                elif reordered.get(5) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")

                elif reordered.get(6) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")

                elif reordered.get(7) == sel:
                    print("\x1b[0m ",cleaned," \x1b[0m")


    print("Press Enter to Continue")
    return




def CalcCost():
    #Calculate total cost, parts+Labour+tax-------------------TODO------------------------------------------------------------------------
    return


#___________________________________________________________________________NOTES___________________________________________________________________________#
#print("\x1b[31mThis is red text\x1b[0m") #ASNI Escape codes for bold text and colour, so f-ing cool! :0
#Had more in mind, ran out of time as i got stuck on the edit fucntion trying to allow fine control over editing, will continue to fix, refactor and expand as a personal tool
