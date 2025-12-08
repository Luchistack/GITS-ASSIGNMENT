def main_menu():
        while True: 
                print("""

          YOUR NOKIA PHONE - MENU MAP
       
            Press 1 -  Phone book
            press 2 -  Message
            Press 3 -  Chat  
            Press 4 -  Call Register 
            Press 5 -  Tones
            Press 6 -  Settings
            Press 7 -  Call divert
            Press 8 -  Games 
            Press 9 -  Calculator
            Press 10 - Reminders 
            Press 11 - Clock 
            Press 12 - Profiles
            Press 13 - Sim Services
            Press 14 - Exit
     """)    
  
choice = int(input("Select: "))

if choice == 1:
    print("Phonebook menu")
                  
elif choice == 2:
    print("Message menu")
                                 
elif choice == 3:
    print("Chat menu")
                  
elif choice == 4:
                        
    print("Call register")

elif choice == 5:
                        
    print("Tones")

elif choice == 4:
                        
    print("Call register")

elif choice == 6:
                        
    print("Settings")

elif choice == 7:
                        
    print("Call divert")

elif choice == 8:
                        
    print("Games")


elif choice == 9:
                        
    print("Calculator")

elif choice == 10:
                        
    print("Reminder")

elif choice == 11:
                        
    print("Clock")

elif choice == 12:
                        
    print("Profiles")

elif choice == 13:
                        
    print("Sim service")

elif choice == 14:
                        
    print("Exiting...")
    break
else:
                        
    print("Invalid option")

 

#END

  #START PHONE BOOK

  #PHONE BOOK MENU
	    
def phonebook_menu():

    print("Phone Book Menu"); 

    while True:
            print("""
        
                            Press 1 -   Search 
                            Press 2 -   Service Nos 
                            Press 3 -   Add name 
                            Press 4 -   Erase 
                            Press 5 -   Edit 
                            Press 6 -   Assign tone 
                            Press 7 -   Send b'card 
                            Press 8 -   Options     
                            Press 9 -   Speed dials
                            Press 10 - Voice tags
          """)
                            
    print(menu);

choice = int(input("select: "))

if choice == 8:

    print("Options menu")

    print(""" 
        
                         Press 1 -   Type of view
                         Press 2 -   Memory status
                                      
                  """)




def message_menu():

    print ("message_menu")            
    menu = """
        
                            Press 1 -   Write messages
                            Press 2 -   Inbox 
                            Press 3 -   Outbox
                            Press 4 -   Picture messages
                            Press 5 -   Template
                            Press 6 -   Smileys 
                            Press 7 -   Message settings
                            Press 8 -   Info service   
                            Press 9 -   Voice mailbox number
                            Press 10 -  Service command editor
              """
    print(menu)

      
choice=input("select choice")
                        
if choice == 7:
       message_setting()



def message_settings():

    print("message_settings")

    print( """
                            Press 1 -   Set 1
                            Press 2 -   Common
                            Press 3 -  Chat
                            """)


choice = input("Select")

if choice == 1:
    print("Set1 Setting")     
    print("""
        
                                         Press 1 -   Message centra number
                                         Press 2 -   Message sent as
                                         Press 3 -   Message validity
                           
                                      
                """)

elif choice == 2:
                       
    print("common setting")
		   
    print("""
                                         Press 1 -   Delivery
                                         Press 2 -   Reply via same centre
                                         Press 3 -   Character support
                                         Press 4 -   Info service
                                         Press 5 -   Voice mailbox number
                                         Press 6 -   Service command editor
                                                      
                     """)
                              

  #END OF MESSAGE

def chat_menu():
    print("Chat Menu");
    print("Press 1 - Chat")
                            

#END OF CHAT;

def call_register():

    print("Call_Register")
    
    print("""
	    
                            Press 1 -   Missed Calls
                            Press 2 -   Recieved Calls 
                            Press 3 -   Dailed Numbers
                            Press 4 -   ERase recent call lists
                            Press 5 -   Show call duration
                            Press 6 -   Show Call Cost 
                            Press 7 -   Call Cost Settings
                            Press 8 -   Prepaid Credit
                           
                 """)


choice = int(input("select: "))

if choice == 5:
    print("call Duration")
                       
    print ("""
        
                                         Press 1 -   Last call duration
                                         Press 2 -   All calls duration
                                         Press 3 -   Received calls duration
                                         Press 4 -   Dialled calls duration
                                         Press 5 -   Clear timers

                    """)

def call_cost():
    print("Call Cost");
		    
    print("""
        
                                         Press 1 -   Last call cost
                                         Press 2 -   All calls cost                                  
                                         Press 3 -   Clear counters

                """)

def cost_setting():

    print("cost Settings");
		    
    print("""
        
                                         Press 1 -   Call cost limit
                                         Press 2 -   Show costs in                                  
                                     
                                          """)

    #TONES
def tones_menu():
    print("Tones"); 

    print("""
        
                            Press 1 -   Ringing tone
                            Press 2 -   Ringing volume
                            Press 3 -   Incoming call alert
                            Press 4 -   Composer
                            Press 5 -   Message alert tone
                            Press 6 -   Keypad tones
                            Press 7 -   Warning and game tones 
                            Press 8 -   Vibrating    
                            Press 9 -   Screen saver
                     
                            """)
    #CALL SETTING

def settings_menu():

    print("Settings"); 

    print("""
        
                            Press 1 -   Call settiing
                            Press 2 -   Phone settings
                            Press 3 -   Security settings
                            Press 4 -   Restore factory settings
                     
                 """)
            
choice = int(input("Select: "))

if choice == 1:
                        call_setting()
                  
elif choice == 2:
                        phone_setting()
                  
elif choice == 3:
                         security_setting()

elif choice == 4:
                        
    print("restored factory setting")
                  
                               

def call_settings():

    print("Call Setting")

    print ("""
        
                            Press 1 -   Automatic redial
                            Press 2 -   Speed dailing
                            Press 3 -   Call waiting options
                            Press 4 -   Own number sending
                            Press 5 -   Phone line in use
                            Press 6 -   Automate answer

                     
                            """)

      
def phone_setting():		    
                 
    print("Phone Settings") 
    print("""
        
                            Press 1 -   Language
                            Press 2 -   Cell info display
                            Press 3 -   Welcome note
                            Press 4 -   Network selection
                            Press 5 -   LIghts 
                            Press 6 -   Confirm SIM service actions

                     
                  """)

def security_setting():
    print("Security Settings")
    print("""
        
                            Press 1 -   PIN code request
                            Press 2 -   Call barring service
                            Press 3 -   Fixed dialing
                            Press 4 -   Closed user group
                            Press 5 -   Phone security
                            Press 6 -   Change access codes

                     
                            """)


def clock_menu():
    print("Clock")
                            
    print("""
        
                            Press 1 -   Alarm clock
                            Press 2 -   Clock settings
                            Press 3 -   Date setting
                            Press 4 -   Stopwatch
                            Press 5 -   Countdown timer
                            Press 6 -   Auto update of date and time
                     
                 """)


def run():
                    choice = main_menu()

match choice:
                        case 1:
                               phonebook_menu()


match choice:
                        case 2:
                               message_menu()


match choice:
                        case 3:
                               chat_menu()


match choice:
                        case 4:
                               call_register()


match choice:
                        case 5:
                              tones_menu()


match choice:
                        case 6:
                               settings_menu()

match choice:
                        case 7:
                               clock_menu()

                        case _:
                             print("Invalid Selection")

run()

