'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play: 
    def __init__(self, show_id, show_name, show_seats, show_date, show_status = True):
        self.__show_id = show_id
        self.__show_name = show_name
        self.__show_seats = show_seats
        self.__show_date = show_date
        self.__show_status = show_status

    
    def get_name(self):
        return self.__show_name

    def get_seats(self):
        return self.__show_seats

    def get_status(self):
        return self.__show_status

    def num_seats_left(self):
        self.__show_seats -=1

    def set_status(self):
        self.__show_status = False

class Booking: 
    def __init__(self,name,seat_number):
        self.__name = name
        self.__seat_number = seat_number
        
    def get_name(self):
        return self.__name

    def get_seat_number(self):
        return self.__seat_number
    
