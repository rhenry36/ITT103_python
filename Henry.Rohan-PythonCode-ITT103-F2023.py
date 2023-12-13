'''
Author: Rohan Henry
Date Created: December 03, 2023
Course: ITT103
Purpose: Reserve bus seats on three different types of buses
'''

#Global variables for report
fclass_reservation_type = ""
fclass_total_seat_count = 0
fclass_total_seats_reserved = 0

bclass_reservation_type = ""
bclass_total_seat_count = 0
bclass_total_seats_reserved = 0

eclass_reservation_type = ""
eclass_total_seat_count = 0
eclass_total_seats_reserved = 0

#Initialize empty 2D arrays for each bus class
fclass_seat_array = []
bclass_seat_array = []
eclass_seat_array = []

#Declare variables


##Arrays for each bus class##

#Specify row and column numbers to create 27-seat first class bus array
row, column = (7, 4)

for row in range(row):
    #Create empty row
    row = []

    #When row number becomes 6, reduce columns to 3 to get 27 seats on the last row
    if (len(fclass_seat_array)) == 6:
        column = 3

    #Append F to empty rows as place holder for free seats
    for seat in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    fclass_seat_array.append(row)


#Specify row and column number to create 38-seat business class bus array
row, column = (10, 4)

for row in range(row):
    #Create empty row
    row = []

    #When row number becomes 9, reduce columns to 2 to get 38 seats on that last row
    if (len(bclass_seat_array)) == 9:
       column = 2

    #Append F to empty rows as place holder for free seats
    for seat in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    bclass_seat_array.append(row)

#56-seat economy class bus array
row, column = (14, 4)

for row in range(row):
    #Create empty row
    row = []

    #Append F to empty rows as place holder for free seats
    for seat in range(column):
       seat = "F"
       row.append(seat)

    # Append the populated row to the 2D array
    eclass_seat_array.append(row)



##Functions##


#The seats_reserved function reserves seat on a specific bus using its class bus array
def seats_reserved(bus):
    #Initialize reserved seats variable (res_seats)
    count = 0

    # Iterate through the rows
    for row in bus:
        # Iterate through the columns
        for seat in row:
            if seat == "R":
                count += 1
    return count

#The total_seats function gets seat count for a specific bus using its class bus array
def total_seats(bus):
    # Initialize a variable to count elements
    count = 0
    # Iterate through the rows
    for row in bus:
    # Iterate through the columns
        for seat in row:
            count += 1
    return count

#The display_seats function uses on of the class bus array to display seat grid for a specific bus
def display_seats(bus):
   for row in bus:
        print(row)
    print("\n")


#Reserve_seat function uses three arguments to reserve seat
def reserve_seat(bus,row, column):
    if bus[row-1][column-1] == "F":
         bus[row-1][column-1] = "R"
         print(f"Reserving seat: Row {row:02} Column {column:02}")
    else:
        print(f"Seat at Row {row:02}, Column {column:02} is already reserved.")

#First class reservation function
def fclass_reserve():
    #Allow function to update global variables for reservation report
    global fclass_reservation_type
    global fclass_total_seat_count
    global fclass_total_seats_reserved
    #Store reservation type for reservation report
    fclass_reservation_type = "First Class"

    while True:
        print("\n27 seat bus")
        display_seats(fclass_seat_array)
        try:
            #Call the total_seats function to get total seats on a bus
            fclass_total_seat_count = total_seats(fclass_seat_array)
            #Call the seats_reserved function to get total seats reserved on a bus
            fclass_total_seats_reserved = seats_reserved(fclass_seat_array)
            if fclass_total_seats_reserved == 27:
               print("No more seats available!")
               break

            row = int(input("Enter row number in 1-7: "))
            if row <= 0:
                print("Number must be positive or greater than zero!")
                print("\nExiting first class reservation...")
                break

            column = int(input("Enter column number 1-4(Ctrl+C to return to main menu): "))
            seat_type = input("Enter W or A for (window or aisle seat): ")
            
            #Call the reserve_seat function to reserve seat
            if 1 <= row <= 7 and 1 <= column <= 4:
                reserve_seat(fclass_seat_array,row, column)
            else:
                print("Invalid input. Please enter valid row and column numbers.")
        except Exception:
            print("Only seats 1 to 3 are available on row 7")
        except KeyboardInterrupt:
            break
            #print("\nEnter Ctrl+C detected. Exiting gracefully.")
    

#Business class reservation function
def bclass_reserve():
    #Allow function to update global variables for reservation report
    global bclass_reservation_type
    global bclass_total_seat_count
    global bclass_total_seats_reserved
    #Store reservation type for reservation report
    bclass_reservation_type = "Business Class"


    while True:
        print("\n38 seat bus")
        display_seats(bclass_seat_array)
        try:
            #Call the total_seats function to get total seats on a bus
            bclass_total_seat_count = total_seats(bclass_seat_array)
            #Call the seats_reserved function to get total seats reserved on a bus
            bclass_total_seats_reserved = seats_reserved(bclass_seat_array)
            if bclass_total_seats_reserved == 38:
               print("No more seats available!")
               break

            row = int(input("Enter row number in 1-10: "))
            if row <= 0:
                print("Number must be positive or greater than zero!")
                print("\nExiting business class reservation...")
                break
            
            column = int(input("Enter column number in 1-4 (Ctrl+C to return to main menu): "))
            seat_type = input("Enter W or A for (window or aisle seat): ")

            if 1 <= row <= 10 and 1 <= column <= 4:
                reserve_seat(bclass_seat_array,row, column)
                                
            else:
                print("Invalid input. Please enter valid row and column numbers.")

        except Exception:
            print("Only seats 1 and 2 are available on row 10:")
        except KeyboardInterrupt:
            break


#Economy class reservation function
def eclass_reserve():
    #Allow function to update global variables for reservation report
    global eclass_reservation_type
    global eclass_total_seat_count
    global eclass_total_seats_reserved
    #Store reservation type for reservation report
    eclass_reservation_type = "Economy Class"

    while True:
        print("\n56 seat bus")
        display_seats(eclass_seat_array)
        try:
            #Call the total_seats function to get total seats on a bus
            eclass_total_seat_count = total_seats(eclass_seat_array)
            #Call the seats_reserved function to get total seats reserved on a bus
            eclass_total_seats_reserved = seats_reserved(eclass_seat_array)
            if eclass_total_seats_reserved == 56:
               print("No more seats available!")
               break

            row = int(input("Enter row number in 1-14: "))
            if row <= 0:
                print("Number must be positive or greater than zero!")
                print("\nExiting economy class reservation...")
                break
            
            column = int(input("Enter column number in 1-4(Ctrl+C to return to main menu): "))
            seat_type = input("Enter W or A for (window or aisle seat): ")

            if 1 <= row <= 14 and 1 <= column <= 4:
                reserve_seat(eclass_seat_array,row, column)
            else:
                print("Invalid input. Please enter valid row and column numbers.")

        except Exception:
            print("Only seats 1 to 3 are available on row 7")
        except KeyboardInterrupt:
            break


#Main menu function
def main_menu():
    print("#################################################")
    print("######       UCC Signature Expres Ltd      ######")
    print("######      Ride in comfort and style      ######")
    print("\nBus Reservation Provisioning System")
    while True:                 #Create infinite loop for menu until quit
        print("\n***Select Reservation Option***\n")
        print("First Class (F/f)")
        print("Business Class (B/b)")
        print("Economy Class (E/e)")
        print("Quit/Cancel (Q/q)")

        #Store choice in option variabl
        option = input("\nSelect an option: ")
        
        if option in ("F", "f"):
            print("\nYou have selected first class.")
            fclass_reserve()                           #Call the fclass_reserve function
        elif option in ("B", "b"):
            print("You have selected business class.")
            bclass_reserve()                          #Call the bclass_reserve function
        elif option in ("E","e"):
            print("You have selected economy class.")
            eclass_reserve()                          #Call the eclass_reserve function
        elif option in ("Q", "q"):
            print("\n**** Reservation Report ****\n")
            print("Reservation Type: ",fclass_reservation_type)
            print("Total number of seats: ",fclass_total_seat_count)
            print("Total number of seats reserved: ",fclass_total_seats_reserved)
            print ("\n")
            print("Reservation Type: ",bclass_reservation_type)
            print("Total number of seats: ",bclass_total_seat_count)
            print("Total number of seats reserved: ",bclass_total_seats_reserved)
            print ("\n")
            print("Reservation Type: ",eclass_reservation_type)
            print("Total number of seats: ",eclass_total_seat_count)
            print("Total number of seats reserved: ",eclass_total_seats_reserved)
            print ("Exiting the program...")
            break
        else:
            print ("Invalid choice!")


main_menu()
