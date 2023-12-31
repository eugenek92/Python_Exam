from logo import logo
import os
from lib import *

def menu ():
    create_database(csvreader, database)
    exit_program=False
    while exit_program!=True:
        os.system('cls')
        print("======================PyStream======================")
        username=(input("Welcome to PyStream! Please, enter your name:\n"))
        os.system('cls')
        print("======================PyStream======================")
        choice=int(input("Please, select as which you want to enter:\n1.Guest;\n2.Administrator\n0.Close PyStream app\n"))
        if choice==1:
            exit_main_menu=False
            while exit_main_menu!=True:
                os.system('cls')
                print("======================PyStream======================")
                print(f"Hello {username} !\nWelcome to our stream-service \"PyStream\"")
                print(f"{username}, if you use \"PyStream\" first time, please read brief information about our service (section 3)")
                print(f"{username} please, select what you want to do: ")
                choice=int(input("\n1.Show store\n2.Search\n3.Rules of use and information\n0.Exit\n"))
                if choice==1:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      numbering(database)
                      show_store(database)
                      #ShowMovie def
                      select=int(input("\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                elif choice==2:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      choice=int(input("Search by: \n1.Name;\n2.Genre;\n3.Country of production;\n4.Year of production;\n0.Go back\n"))
                      if choice==1:
                         os.system('cls')
                         search_name(database)
                         ##Searchbyname def
                      elif choice==2:
                         os.system('cls')
                         search_genre(database)
                         ##Searchbygenre def
                      elif choice==3:
                         os.system('cls')
                         search_country(database)
                         ##Searchbycountry def
                      elif choice==4:
                         os.system('cls')
                         search_year(database)
                         ##Searchbyyear def
                      elif choice==0:
                        exit_menu=True  
                elif choice==3:
                   exit_menu=False
                   while exit_menu!=True:
                      os.system('cls')
                      print(f"Welcome {username} !\nThank you for reading!\nPyStream is examination project, which was created to meet the needs")
                      print(f"of finding information about movies,\nserials, cartoon's, anime.\n")   
                      print(f"{username}, as a user you can use such functionality:\nShow store - this will allow you to browse our media library;")
                      print(f"Search - this feature allows you to search for a media file by name, genre, country of manufacture or year of release.\n")      
                      print(f"{username}, if you are an administrator and want to make changes to our library\nplease, log in using your password.")
                      print(f"We hope you enjoy using our app PyStream!")
                      select=int(input("\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                elif choice==0:
                    exit_main_menu=True
        elif choice==2:
            os.system('cls')
            password=int(input("If you administrator,please enter your password: "))
            if password==1234:
               exit_main_menu=False
               while exit_main_menu!=True:
                  os.system('cls')
                  print("======================PyStream======================")
                  print(f"Hello administrator {username}!\nAdministrator {username} please, select what you need: ")
                  choice=int(input("\n1.Show store\n2.Search\n3.Add new object\n4.Edit object\n5.Delete object\n0.Exit\n"))
                  if choice==1:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      numbering(database)
                      show_store(database)
                      #ShowMovie def
                      select=int(input("\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                  elif choice==2:
                     exit_menu=False
                     while exit_menu!=True:
                      os.system('cls')
                      choice=int(input("Search by: \n1.Name;\n2.Genre;\n3.Country of production;\n4.Year of production;\n0.Go back\n"))
                      if choice==1:
                         os.system('cls')
                         search_name(database)
                         ##Searchbyname def
                      elif choice==2:
                         os.system('cls')
                         search_genre(database)
                         ##Searchbygenre def
                      elif choice==3:
                         os.system('cls')
                         search_country(database)
                         ##Searchbycountry def
                      elif choice==4:
                         os.system('cls')
                         search_year(database)
                         ##Searchbyyear def
                      elif choice==0:
                        exit_menu=True  
                  elif choice==3:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      add_item(database)
                      select=int(input("Object has been added!\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                  elif choice==4:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      #EditMovie
                      edit_item(database)
                      select=int(input("Editing was successful!\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                  elif choice==5:
                    exit_menu=False
                    while exit_menu!=True:
                      os.system('cls')
                      #DeleteMovie
                      delete_item(database)
                      select=int(input("Deletion was successful!\n0.Go back\n"))
                      if select==0:
                        exit_menu=True
                  elif choice==0:
                    exit_main_menu=True
            else:
               exit_menu=False
               while exit_menu!=True:
                  select=int(input(print("The password is incorrect! Try again!\n0.Exit")))
                  if select==0:
                        exit_menu=True
        elif choice==0:
            exit_program=True
        write_file(database)



