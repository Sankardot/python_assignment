# Create a python project which will enable to make a simple movie booking system
#  we will restrict ourselves to just booking the ticket and show ticket.
"""
    Functionalities: movie selection, add movie, 
    buy ticket(
        row and seat number, language, location, discount
        ), show movie timing,
    snack purchase, register user, login user, show ticket history
    Agenda:
    1) register
    2) login
    3) add show/movie
    4) book ticket
    5) show booked ticket history
    6) show all the movies
"""
import json
from json import JSONDecodeError
def register(user_json, user_id, name, password, age, email, phone): # user_json
    """
    returns True if registration is successful
    returns False if registration is unsuccessful
    
    {
    "user_id": <id>,
    "name": <name>,
    "password": <password>,
    "email": <email>,
    "phone": <phn>,
    "age": <age>,
    "booked shows": ["id1", "id2", "id3"]  # it will contain the history of the shows user booked
    }
    """
    d = {
        "user_id": user_id,
        "name": name,
        "password": password,
        "email": email,
        "phone": phone,
        "age": age,
        "booked shows": []
    }
    f = open(user_json, "r+")
    try:
        content = json.load(f) # it is a list
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    except JSONDecodeError:
        l = []
        l.append(d)
        json.dump(l, f)
        f.close()
        return True
    f.close()
    return False

def login(user_json, email_id, password):
    """
    return True if login is success
    return false if login is Failed
    """
    f=open(user_json, "r+")
    try:
        content = json.load(f)
    except JSONDecodeError:
        return False
    f.close()
    d=0
    for i in range(len(content)):
        if content[i]["email"] == email_id and content[i]["password"] == password:
            d=1
            break
    if d==1:
        return True
    return False

def add_movie(movie_json, movie_id, movie_name, duration, price):
    """
    add_movie function adds the new movie
    
    return:
        True if movie was successfully added
        False if movie addition failed
    """
    d = {
        "movie_id": movie_id,
        "name": movie_name,
        "seating": 25,
        "price": price,
        "booked_seats": []
    }
    f=open(movie_json, "r+")
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
        else:
            print("Booking for this movie has already started")
            f.close()
            return False
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l, f)
    f.close()
    return True

def book_ticket(movie_json, user_json, email, tkt_id, no_of_booking, prefered_seat=[]):
    """
    book_ticket function reservs a seat for the user corresponding to the no of seats they want
    return:
        True if booking was successful
        False if booking was unsuccessful
    """
    # open the movie_json
    f = open(movie_json, "r+")
    content = json.load(f)
    count = 0
    for i in range(len(content)):
        if content[i]["movie_id"]==tkt_id:
            movie_show=content[i]
            seat_booked=len(movie_show["booked_seats"])
            number_of_seat = 25-seat_booked
            count+=1
            break
    if count==0:
        return False
    
    # open the user_json
    f1=open(user_json, "r+")
    content1=json.load(f1)
    count=0
    for i in range(len(content)):
        if content1[i]["email"] == email:
            user=content1[i]
            count+=1
            break
    if count==0:
        return False

    # Seating Arrengement
    #   A  B  C  D  E
    # 1 A1 B1 C1 D1 E1
    # 2 A2 B2 C2 D2 E2
    # 3 A3 B3 C3 D3 E3
    # 4 A4 B4 C4 D4 E4
    # 5 A5 B5 C5 D5 E5

    # Recollect the available seats
    seats=[]
    for row in range(1,6):
        for col in range(ord("A"), ord("E")+1):
            if chr(col)+str(row) not in movie_show["booked_seats"]:
                seats.append(chr(col)+str(row))
    # Booking Process
    if number_of_seat >= no_of_booking:
        for i in prefered_seat:
            if i not in seats:
                return False
        
        if prefered_seat:
            movie_show["booked_seats"].extend(prefered_seat)
            user["booked shows"].append(tkt_id)
        else:
            movie_show["booked_seats"].extend(seats[:no_of_booking])
            user["booked shows"].append(tkt_id)
    else:
        return False
    # closing file for user_json
    for i in range(len(content1)):
        if content1[i]["email"] == email:
            content1[i]["booked shows"]=user["booked shows"]
            f1.seek(0)
            f1.truncate()
            json.dump(content1, f1)
            f1.close()

    # closing file for movie_json
    for i in range(len(content)):
        if content[i]["movie_id"]==tkt_id:
            content[i]["booked_seats"]=movie_show["booked_seats"]
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
    return True

def show_booked_ticket_history(user_json, movie_json, email):
    f=open(user_json, "r+")
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["email"] == email:
            history=content[i]["booked shows"]
    f.close()
    f=open(movie_json, "r+")
    content=json.load(f)
    for i in history[::-1]:
        for j in range(len(content)):
            if content[j]["movie_id"] == i:
                print("{} | {}".format(content[j]["movie_id"],content[j]["name"]))

def show_movies(movie_json):
    f=open(movie_json, "r+")
    content=json.load(f)
    for i in range(len(content)):
        availble_seat = content[i]["seating"]-len(content[i]["booked_seats"])
        print(content[i]["movie_id"],content[i]["name"],content[i]["seating"],content[i]["price"], availble_seat)
    f.close()

# print(register.__doc__)
# register("user.json","5479", "Sanvi", "password", "20", "anvi07@gmail.com", "8745897965")