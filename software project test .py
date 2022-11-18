x=10
L=()
M= ()
N=[]
a=0

class ticket():
    a += 1
    # to create ticket number
    
    ticket_no = a + 2000
    print(ticket_no)




#to create ticket count
    def __init__():
        ticket_count = int(a)
        print(ticket_count)



class menulist():

    def display_ticket():
        print("Name: ",nm )
        print("Staff ID: ",id)
        print("Description of issue: ",desc)

    def __init__(self,nm,id,des,em):
        self.name=nm
        self.id=id
        self.desc=des
        self.email=em


    def pg(self):
        if "password" in des:
            print("your password is " ,nm[0:3]++id[0:2] )
        else:
            print("Not Yet Provided")

    def __int__(self,re,rs,cl):

         self.reopen=re
         self.resolved=rs
         self.closed=cl

         tot_ticket == int(re)+int(rs)+int(cl)

    def open():

        if ticket_no is True:
            print("ticket is now open")
        else:
            print("that is not a valid ticket number")

    def ticketstats():
        print("Tickets Created : ",tot_created )
        print("Tickets Resolved :", rs)
        print("Tickets to reopen : ",re )

while x!=0:

        print("Welcome to Helpdesk")
        print("Select from the following choices: \n 0:Exit \n 1:Submit Helpdesk ticket \n 2:Show all tickets"
              "\n 3:Respond to ticket by Number \n 4: Re-open resolved ticket \n 5: Display Ticket Stats")
        x=int(input("select options" ))

        if x==1:
            i = input("enter your name ")
            j = input("enter your id ")
            k = input("enter desc  ")
            l = input("enter email  ")
            print("your ticket has been submitted  ")
            print("ticket no is " ,Ticket_no)
        ticket()

        if x==2:
             display_ticket()

        if x==3:
            input("enter ticket no to open")
            open()

        if x==4:
            input("enter ticket number to reopen")
            ticket_open=tot_ticket-1

        if x==0:
            
            break



