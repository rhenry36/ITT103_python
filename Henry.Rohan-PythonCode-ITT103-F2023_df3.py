'''
Author: Rohan Henry
Date Created: 
Course: ITT103
Purpose:
'''

#Declare global variables for use in functions
#global_count = None
##global_occurrences = None
reserve_type = None

#Initialize 2D arrays for each bus class
fclass_seat_array = []
bclass_seat_array = []
eclass_seat_array = []

#Declare variables
row = 0
column = 0


##Define arrays##

#27-seat first class bus array
#fbus_rows, fbus_columns = (7, 4)
row, column = (7, 4)
#fclass_seat_array = []

#for i in range(fbus_rows):
for i in range(row):
    #Create empty row
    row = []
    #When size of array becomes 6, reduce columns to 3 to get 27 seats on the last row
    if (len(fclass_seat_array)) == 6:
       #fbus_columns = 3
        column = 3
       #Append F to empty rows as place holder for free seats
    #for j in range(fbus_columns):
    for j in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    fclass_seat_array.append(row)


#38-seat business class bus array
row, column = (10, 4)
#bclass_seat_array = []

for i in range(row):
    #Create empty row
    row = []
    #When size of array becomes 9, reduce columns to 2 to get 38 seats on that last row
    if (len(bclass_seat_array)) == 9:
       column = 2
    #Append F to empty rows as place holder for free seats
    for j in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    bclass_seat_array.append(row)

#56-seat first class bus array
row, column = (14, 4)
#fclass_seat_array = []

for i in range(row):
    #Create empty row
    row = []
    #Append F to empty rows as place holder for free seats
    for j in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    eclass_seat_array.append(row)



##Functions##
#Display main menu
def main_menu():
    print("#########################################################")
    print("################ UCC Signature Expres Ltd ###############")
    print("#########################################################")
    print("Bus Reservation Provisioning System")
    while True:
        print("\n***Reservation Options***\n")
        print("First Class (F/f)")
        print("Business Class (B/b)")
        print("Economy Class (E/e)")
        print("Quit/Cancel (Q/q)")

        #Store selection in a variable named bus_class
        option = input("\nSelect an option: ")
        
        if option in ("F", "f"):
            print("\nYou have selected first class.")
            fclass_reserve()                           #Run the first_class function
        elif option in ("B", "b"):
            print("You have selected business class.")
            bclass_reserve()
            #display_bclass_seats()                         #Display the business class bus seats
        elif option in ("E","e"):
            print("You have selected economy class.")
            eclass_reserve()                          #Run the economy_class function
        elif option in ("Q", "q"):
            print("Reservation Type: ",reserve_type)
            print("Total number of seats: ",count)
            print("Total number of seats reserved: ",count)
            print ("Exiting the program...")
            break
        else:
            print ("Invalid choice. Please enter letter to select a class.")



def seats_reserved(bus):
    # Initialize count variable
    #global global_occurrences
    #global_occurrences = 0
    global count
    count = 0

    # Iterate through the rows
    for row in bus:
        # Iterate through the columns
        for seat in row:
            if seat == "R":
                #global_occurrences += 1
                count += 1


def total_seats(bus):
    # Initialize a variable to count elements
    global count
    count = 0
    # Iterate through the rows
    for row in bus:
    # Iterate through the columns
        for seat in row:
            count += 1
    #print(f"Total number of elements in the 2D array: {total_seats}")
    #return count

def display_seats(bus):
    print("\nBus Seating")
    for row in bus:
        print(row)
    print("\n")
 #   for i, row in enumerate(bus, start=1):
 #       print(f"{i}: {row}")



def reserve_seat(bus,row, column):
    #print(bus.count('F'))
    #print(len([element for element in bus if element == "F"]))
    #print("No more available seats!")
    if bus[row-1][column-1] == "F":
         bus[row-1][column-1] = "R"
         print(f"Reserving seat: Row {row:02} Column {column:02}")
    else:
        print(f"Seat at Row {row:02}, Column {column:02} is already reserved.")

def fclass_reserve():
    while True:
        #display_fclass_seats()
        display_seats(fclass_seat_array)
        try:
            row = int(input("Enter the row number (1-7) or 0 to exit: "))
            if row == 0:
                print("\nExiting first class reservation...")
                global reserve_type
                reserve_type = "First Class"
                total_seats(fclass_seat_array)
                seats_reserved(fclass_seat_array)
                break
            column = int(input("Enter the column number (1-4) or 0 to exit: "))
            if column == 0:
                print("\nExiting first class reservation...")
                reserve_type = "First Class"
                total_seats(fclass_seat_array)
                seats_reserved(fclass_seat_array)
                break
            if 1 <= row <= 7 and 1 <= column <= 4:
                reserve_seat(fclass_seat_array,row, column)
            else:
                print("Invalid input. Please enter valid row and column numbers.")
        except Exception:
            print("Only seats 1 to 3 are available on row 7")

def bclass_reserve():
    while True:
        display_seats(bclass_seat_array)
        try:
            row = int(input("Enter the row number (1-10) or 0 to exit: "))
            if row == 0:
                print("\nExiting business class reservation...")
                global reserve_type
                reserve_type = "Business Class"
                seat_count(bclass_seat_array)
                reserve_count(bclass_seat_array)
                #return reserve_type
                break
            column = int(input("Enter the column number (1-4) or 0 to exit: "))
            if column == 0:
                print("\nExiting business class reservation...")
                reserve_type = "Business Class"
                seat_count(bclass_seat_array)
                reserve_count(bclass_seat_array)
                #return total_seats
                break
            if 1 <= row <= 10 and 1 <= column <= 4:
                reserve_seat(bclass_seat_array,row, column)
                
                
            else:
                print("Invalid input. Please enter valid row and column numbers.")

        except Exception:
            print("Only seats 1 and 2 are available on row 10:")
        #return total_seats

def eclass_reserve():
    while True:
        display_seats(eclass_seat_array)
        try:
            row = int(input("Enter the row number (1-14) or 0 to exit: "))
            if row == 0:
                seat_count(eclass_seat_array)
                print("\nExiting economy class reservation...")
                global reserve_type
                reserve_type = "Economy Class"
                seat_count(eclass_seat_array)
                reserve_count(eclass_seat_array)
                break
            column = int(input("Enter the column number (1-4) or 0 to exit: "))
            if column == 0:
                print("\nExiting economy class reservation...")
                reserve_type = "Economy Class"
                seat_count(eclass_seat_array)
                reserve_count(eclass_seat_array)
                break
            if 1 <= row <= 14 and 1 <= column <= 4:
                reserve_seat(eclass_seat_array,row, column)
            else:
                print("Invalid input. Please enter valid row and column numbers.")

        except Exception:
            print("Only seats 1 to 3 are available on row 7")


main_menu()
