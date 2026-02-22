#Use function method to create a program that as a book suggestion system
#The program would have different functionalites


#using def, define the function name  menu()
#print the menus from number  to the last menu
#Display them differently
#display 6 for exit after all variables have been displayed or printed
#ask user to enter an operation, meaning to select an option from the menu or varible displayed
#declare if the user enters 1 which is the first menu option of Book suggestion
#type book_suggestion(), this is so it takes the user to the book selection function menu which is created in step 2

#step 2
#create another def function with function name title book_suggestion ():
#next line create the function signature eg book = [  insert all book title in the block, as much as hundred
#display all the book title inside the book block using " ", to differenciate the values and closing it at the end with ]
#apply the for loop, for title in books, print title
#ask user to make a chioce by telling the user to enter yes or no, if you want another book suggestion click yes




#   Add books, click 2
# Books can be added by user if it doesnt exist in the book list

#  Remove books
# Click 3 to remove a book


#UPdate books, click 4
#update a book in the book list

#Show all books click 5
#to show all books in th book list


import random



def menu():
      print('Welcome to book suggestion library!')
      print("1. Get Suggestion")
      print("2. Add Book")
      print("3. Remove Book")
      print("4. Update Book")
      print("5. Show Books")
      print("6. Exit")
      enter = input("Enter Operation: ")

      if enter == "1":
          get_suggestion()
        

def get_suggestion():
      book = [
                    "Book Title: The Hobbit\nPage: 1",
                    "Book Title: The Mastery\nPage: 2",
                    "Book Title: Jackie\nPage: 3",
                    "Book Title: Manmaid\nPage: 4",
                    "Book Title: Anonymous\nPage: 5",
                    "Book Title: The Hero\nPage: 6",
                    "Book Title: SLayer\nPage: 7",
                    "Book Title: Tom\nPage: 8",
                    "Book Title: The Heros\nPage: 9",
                    "Book Title: Thief and thaft\nPage: 10",
                    "Book Title: The Killer\nPage: 11",
                    "Book Title: Lost job\nPage: 12",
                    "Book Title: The Accountant\nPage: 13",
                    "Book Title: Magic\nPage: 14",
                    "Book Title: Cast\nPage: 15",
                    "Book Title: Hell\nPage: 16",
                    "Book Title: Semicolon\nPage: 17",
      ]


      for title in book:
            print(random.randint(title))

            select = input("Would you like another suggestion? (yes/no): ").lower()
     
            if select == "no":
              print("stopped")
              menu()
              

            elif select != "yes":
             print("please type yes or no")
             return


     
menu()
get_suggestion()
