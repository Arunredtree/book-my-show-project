from mybookmyshow import MyBookMyShow
row = int(input("How many rows? "))
column = int(input("How many columns? "))

my_movie = MyBookMyShow(row,column)
loop = True
print("\n")
my_movie.print_seats()
while loop:
    user_choice = input("\n1. Print seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked tickets user info\n0. Exit\n")
    if user_choice == "1":
        my_movie.print_seats()
    elif user_choice == "0":
        loop = False
    elif user_choice == "2":
        book_row = int(input("Which Row: "))
        book_column = int(input("Which Column: "))
        my_movie.book_ticket(book_row,book_column)
    elif user_choice == "3":
        ticket_sold = my_movie.statistics()
        percentage = "{:.2f}".format(ticket_sold[1])
        print(f"Tickets Sold: {ticket_sold[0]}")
        print(f"Percentage: {percentage}%")
        print(f"Current income: ${ticket_sold[3]}")
        print(f"Total income: ${ticket_sold[2]}")
        
    elif user_choice == "4":
        row = int(input("Which Row?: "))
        col = int(input("Which Col?: "))
        viewer = my_movie.print_user_details(row,col)
        if viewer[0] and viewer[1]["name"] != "None":
            print("\n========================================================")
            print(f'Name: {viewer[1]["name"]}\nGender: {viewer[1]["gender"]}\nAge: {viewer[1]["age"]}\nTicket Cost: ${viewer[1]["ticketcost"]}\nPhone: {viewer[1]["phone"]}')
            print("========================================================")
        elif viewer[0] and viewer[1]["name"] == "None":\
            print("Not Booked!") 
        else:
            print(viewer[1])
            