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
      select = int(input("Would you like another suggestion? (yes/no): ")).lower()
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
      elif enter == "2":
          add_new_books() 
      elif enter == "3":
          remove_book() 
      elif enter == "4":
            update_book() 
      elif enter == "5":
          sho_books() 
      elif enter == "6":
            print(Goodbye)
            exit() 

def get_suggestion():
      books = [
                    "The Hobbit",
                    "The Mastery",
                    "Jackie",
                    "Manmaid",
                    "Anonymous",
                    "The Hero",
                    "Slayer",
                    "Tom",
                    "The Heros",
                    "Thief and thaft",
                    "The Killer",
                    "Lost job",
                    "The Accountant",
                    "Magic",
                    "Cast",
                    "Hell",
                    "Semicolon",
      ]
       
      while True:
            
            book = random.choice(books)
            page = random.randint(1, 100)

            print(f"Book of the Day:\n\tBook Title: {book}\n\tPage: {page}")

            select = int(input("Would you like another suggestion? (yes/no): ")).lower()
     
            if select == "no":
              print("stopped")
              menu()
              

            elif select != "yes":
             print("please type yes or no")
             return

menu()
get_suggestion()


def add__new_books():
          new_book = int(input("Enter a book title: ")).lower()
          print("Book added Successfully")

          
          
          
add_new_books()
menu()
