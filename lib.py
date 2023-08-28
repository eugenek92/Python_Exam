import csv
import os

def read_file():

    try:

        file = open("database.csv", "r")

        csvreader = csv.reader(file)

        return csvreader

        file.close()

    except Exception as error:

        print(f"Error: {error}")



def write_file(database):

    try:

        file = open("database.csv", "w")

        for row in database:

            for item in row:

                if item == row[-1]:

                    file.writelines(f"{item}")

                    break

                file.writelines(f"{item},")

            file.writelines("\n")

        file.close()

    except Exception as error:

        print(f"Error: {error}")


database = []

csvreader = read_file()


def create_database(csvreader, database):

    for item in csvreader:

        database.append(item)


# Function to show all objects in database       

def show_store(database):

    for item in database:

        show_item(item)

 
# Show chosen object

def show_item(item):

    print(f"{item[0]}.Name: {item[1]}\n  Type: {item[2]}\n  Genre: {item[3]}\n  Country: {item[4]}")
    print(f"  Year of production:{item[5]}\n  Seasons: {item[6]}\n  Series: {item[7]}\n  Time: {item[8]}\n  Plot: {item[9]}\n  ID: {item[10]}\n")


# Function for add new object in database (menu 2.3)

def add_item(database):

    i = 0

    id = 0

    for item in database:

        i+=1
        id+=5

    number = str(i+1)

    name = input("Enter object name: ")

    type = input(f"Enter {name} type (Movie, Cartoon, Serial, Cartoon series): ")

    genre = input(f"Enter {name} genre (Action, Adventure, Anime, Comedy, Drama, Documental, Fantasy, Mystery): ")

    country = input(f"Enter {name} country of production: ")

    year = input(f"Enter {name} year of production: ")

    seasons = input(f"Enter {name} number of seasons: ")

    series = input(f"Enter {name} number of series: ")

    time = input(f"Enter {name} duration (in minutes): ")

    plot = input(f"Write {name} plot: ")

    id = str(id+10)

    #special_id(database)

    item = [number, name, type, genre, country, year, seasons, series, time, plot, id]

    database.append(item)


# Function for editiong movie (menu 2.4)

def edit_item(database):

    choice = input("Enter item ID to edit: ")

    for item in database:

        if item[10] == choice:

            print(f"{item}")

            editing = input("1. Name\n2. Type\n3. Genre\n4. Country\n5. Year\n6. Seasos\n7. Series\n8. Time\n9. Plot\n\nEnter an element to edit: ")

            if editing == "1":

                new_name = input("Enter a new name: ")

                item[1] = new_name

            elif editing == "2":

                new_type = input("Enter a new type: ")

                item[2] = new_type

            elif editing == "3":

                new_genre = input("Enter a new genre: ")

                item[3] = new_genre
            
            elif editing == "4":

                new_country = input("Enter a new country of production: ")

                item[4] = new_country
            
            elif editing == "5":

                new_year = input("Enter a new year of production: ")

                item[5] = new_year

            elif editing == "6":

                new_seasons = input("Enter a new number of seasons: ")

                item[6] = new_seasons
            
            elif editing == "7":

                new_series = input("Enter a new number of series: ")

                item[7] = new_series

            elif editing == "8":

                new_time = input("Enter a new duration time: ")

                item[8] = new_time

            elif editing == "9":

                new_plot = input("Enter a new plot: ")

                item[9] = new_plot

# Function for deleting movie

def delete_item(database):

    deleting = input("Enter ID of object to delete: ")

    for item in database:

        if item[10] == deleting:

            database.remove(item)


# Function's for searching object

#search by name

def search_name(database):

    search_name = input("Enter a name for search: ")

    print("\n==================\nRESULT: ")

    for item in database:
        if search_name in item:
            print(f"Name: {item[1]}\nType: {item[2]}\nGenre: {item[3]}\nCountry: {item[4]}")
            print(f"Year of production:{item[5]}\nSeasons: {item[6]}\nSeries: {item[7]}\nTime: {item[8]}\nPlot: {item[9]}\n")
        else:
            print(f"There are no object with name {search_name}")
    os.system('pause')        

# search by genre

def search_genre(database):

    search_genre = input("Enter a genre for search: ")

    print("\n==================\nRESULT: ")

    for item in database:
        if search_genre in item:
            print(f"Name: {item[1]}\nType: {item[2]}\nGenre: {item[3]}\nCountry: {item[4]}")
            print(f"Year of production:{item[5]}\nSeasons: {item[6]}\nSeries: {item[7]}\nTime: {item[8]}\nPlot: {item[9]}\n")
        else:
            print(f"There are no object with genre {search_genre}")
    os.system('pause')       

# search by country

def search_country(database):

    search_country = input("Enter object country of production for search: ")

    print("\n==================\nRESULT: ")

    for item in database:
        if search_country in item:
            print(f"Name: {item[1]}\nType: {item[2]}\nGenre: {item[3]}\nCountry: {item[4]}")
            print(f"Year of production:{item[5]}\nSeasons: {item[6]}\nSeries: {item[7]}\nTime: {item[8]}\nPlot: {item[9]}\n")
        else:
            print(f"There are no object with genre {search_country}")
    os.system('pause') 

# search by year

def search_year(database):

    search_year = input("Enter object year of production for search: ")

    print("\n==================\nRESULT: ")

    for item in database:
        if search_year in item:
            print(f"Name: {item[1]}\nType: {item[2]}\nGenre: {item[3]}\nCountry: {item[4]}")
            print(f"Year of production:{item[5]}\nSeasons: {item[6]}\nSeries: {item[7]}\nTime: {item[8]}\nPlot: {item[9]}\n")
        else:
            print(f"There are no object with genre {search_year}")
    os.system('pause') 

# Function for actual numbering objects    

def numbering(database):
    i=1
    for item in database:
        item[0]=i
        i+=1

# Function for unrepeatability objects ID

def special_id(database):
    for item in database:
        for id in item:
            while(item[10]==id):
                if id==item[10]:
                    print(f"ID\"{id}\" already use! Please, enter another one object ID:")
                    id = input(f"Write ID: ")
                elif id!=item[10]: 
                    item[10]=id


# def special_id(database):
 #   while(item[10]==id):
  #      for item in database:
   #         if item[10]==id:
    #            id=input(f"ID\"{id}\" already use! Please, enter another one object ID:")
     #       else: 
      #          item[10]=id    

        

