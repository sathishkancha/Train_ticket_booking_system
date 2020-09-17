from view_ticket import *
from ticket_class import *
def main():
    lst=[]
    def Booking_tickets():
        name=str(input('Enter your name:'))
        source=str(input('Enter your source:'))
        destination=str(input('Enter your destination:'))
        train=input('Enter your train name:')
        print("AVALIBLE PREFERENCES\nL:lowerberth\nM:medialberth\nU:upperberth\nSL:sidelower\nSU:sideupper")
        p=input("Enter your peference berth:")
        preference=p.upper()

        
        obj=ticket(name,source,destination,train,preference)
        lst.append(obj)
    def Cancel_tickets():
        nm=input('Enter your name for cancellation your ticket:')
        for j in range(len(lst)):
            if nm==lst[j].name:
                del lst[j]
                break

        
    def  View_tickets():
        if len(lst)<1:
            print("You don't have any ticket")
        
        countL=0
        countM=0
        countU=0
        countSL=0
        countSU=0
        for i in range(len(lst)):
            print("your name is:",lst[i].name,'\n'"your source is:",lst[i].source,'\n'"your destination is:",lst[i].destination,'\n'"your train name is :",lst[i].train,'\n'"your prefrence is:",lst[i].preference)
            if "L"==lst[i].preference:
                countL+=1
                excution(1,countL)
            
            elif "M"==lst[i].preference:
                countM+=1
                excution(2,countM)
            elif "U"==lst[i].preference:
                countU+=1
                excution(3,countU)
            elif "SL"==lst[i].preference:
                countSL+=1
                excution(7,countSL)
            elif"SU"==lst[i].preference:
                countSU+=1
                excution(8,countSU)
            else:
                print("You have enterd wrong  preference\nPlease check once")

    while True:
        
        print("1:Booking_tickets\n2:Cancel_tickets\n3:View_tickets\n4:Exit")
        choice=int(input('Select your option:'))
        if choice==1:
            Booking_tickets()
        elif choice==2:
            Cancel_tickets()
        elif choice==3:
            View_tickets()
        elif choice==4: 
            break

main()