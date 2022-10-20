import practiceClass as p
import csv


shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''



'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode
for rec in shows:
    show_id = shows[rec]['id']
    show_name = shows[rec]['name']
    show_capacity = shows[rec]['capacity']
    show_date = shows[rec]['event_date']


    if show_id == 9587:
        event = p.Play(show_id, show_name, show_capacity, show_date)
#create a csv object from the file object from the step above
infile = open('bookings.csv','r')



# use a for loop to iterate through each record in the bookings file
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)

for record in csvfile:
    if int(record[0]) == 9587:
        if event.get_status():
            x = p.Booking(record[1],record[2])
            event.num_seats_left()
            if event.get_seats()==0:
                event.get_status() 
        else:
            print()
            print('**********Error**********')
            print('Guest Name: ',record[1])
            print(event.get_name(), 'is sold out.')
            print('*************************')
            print()
