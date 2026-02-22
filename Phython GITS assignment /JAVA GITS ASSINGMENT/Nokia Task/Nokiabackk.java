import java.util.Scanner;

class Nokia{

public static void main(String[] args){

            Scanner inputCollector = new Scanner(System.in);


        boolean first = true;
        while (first == true){
        String menu = """
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
        Press 14 - Back
        """;
        System.out.print(menu);  
        
        int mainMenuChoice =  inputCollector.nextInt();

	    switch(mainMenuChoice){ 

//END

//START PHONE BOOK

//PHONE BOOK MENU
	
		    case  1 -> {System.out.println("Phone Book Menu"); 
                                                                     first = false;}

	                    String PhoneBookMenu = """
    
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
                        """; 

        System.out.print(PhoneBookMenu);

       int phoneBookMenuChoice = inputCollector.nextInt();

        switch(phoneBookMenuChoice) {

//END OF PHONEBOOK MAIN MENU

case 8 -> {System.out.println("Options Menu");
		
	                   String OptionsMenu = """
    
                                     Press 1 -   Type of view
                                     Press 2 -   Memory status
                                  
                                      """;

        System.out.print(OptionsMenu);

                
}


}

}

}

       int messageMenuChoice = inputCollector.nextInt();

        switch(messageMenuChoice) {                   
            case  2 -> {System.out.println("Message Menu"); 
                                                                  first = false;}

	                    String messageMenu = """
    
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
                        """; 

        System.out.print(messageMenu);



       int settingMessageChoice = inputCollector.nextInt();

        switch(settingMessageChoice) {

        case 7  -> {System.out.println("Message Settings");

	                    String messageSettingsMenu = """
                        Press 1 -   Set 1
                        Press 2 -   Common
                        Press 3 -  Chat
                        """; 

        System.out.print(messageSettingsMenu);

       int setChoice = inputCollector.nextInt();

        switch(setChoice) {

//END OF PHONEBOOK MAIN MENU

                case 1 -> {System.out.println("Set1 Setting");
		
	                   String set1 = """
    
                                     Press 1 -   Message centra number
                                     Press 2 -   Message sent as
                                     Press 3 -   Message validity
                       
                                  
                                      """;

        System.out.print(set1);


                
                         int commonSettingChoice = inputCollector.nextInt();

                        switch(commonSettingChoice) {

                    case 2 -> {System.out.println("Common  Setting");
		
	                   String commonSetting= """
    
                                     Press 1 -   Delivery
                                     Press 2 -   Reply via same centre
                                     Press 3 -   Character support
                                     Press 4 -   Info service
                                     Press 5 -   Voice mailbox number
                                     Press 6 -   Service command editor
                       
                                  
                                      """;

                        System.out.print(commonSetting);

}


}

}

}
 
}

}



}

}


//END OF MESSAGE

       int chatMenuChoice = inputCollector.nextInt();

        switch(chatMenuChoice) {    
               
            case  3 -> {boolean second = true;
                                while (second == true){

                    System.out.println("ChatMenu"); 
                                                    

	                    String chatMenu = """
    
                        Press 1 -  Chat
                       
                        """; 

        System.out.print(chatMenu);



}

}

//END OF CHAT;
        int callRegisterChoice =  inputCollector.nextInt();

	    switch(callRegisterChoice){ 

//END

//START PHONE BOOK

//PHONE BOOK MENU
	            
		    case  4 -> {System.out.println("Call Register"); 
                        System.exit(0);}
	                    String callRegister = """
    
                        Press 1 -   Missed Calls
                        Press 2 -   Recieved Calls 
                        Press 3 -   Dailed Numbers
                        Press 4 -   ERase recent call lists
                        Press 5 -   Show call duration
                        Press 6 -   Show Call Cost 
                        Press 7 -   Call Cost Settings
                        Press 8 -   Prepaid Credit
                       
                        """; 

                  System.out.print(callRegister);

       int callDurationMenu = inputCollector.nextInt();

        switch(callDurationMenu) {

//END OF PHONEBOOK MAIN MENU

case 5-> {System.out.println("Call Duration");
		
	                   String callDuration = """
    
                                     Press 1 -   Last call duration
                                     Press 2 -   All calls duration
                                     Press 3 -   Received calls duration
                                     Press 4 -   Dialled calls duration
                                     Press 5 -   Clear timers

                                      """;

        System.out.print(callDuration);


       int callCostMenu = inputCollector.nextInt();

        switch(callCostMenu) {

//END OF PHONEBOOK MAIN MENU

         case 6 -> {System.out.println("Call Cost");
		
	                   String callCost= """
    
                                     Press 1 -   Last call cost
                                     Press 2 -   All calls cost                                  
                                     Press 3 -   Clear counters

                                      """;

        System.out.print(callCost);



       int showCostMenu = inputCollector.nextInt();

        switch(showCostMenu) {

//END OF PHONEBOOK MAIN MENU

               case 7 -> {System.out.println("Show Cost Settings");
		
	                   String showCost= """
    
                                     Press 1 -   Call cost limit
                                     Press 2 -   Show costs in                                  
                                 
                                      """;

        System.out.print(showCost);


}

}

}

}

               
}


}

}

}


           int tonesMenuChoice =  inputCollector.nextInt();

	    switch(tonesMenuChoice){ 
	
		    case  5  -> {System.out.println("Tones"); 
                            second = false;
                            first = false;}

	                    String tonesMenu = """
    
                        Press 1 -   Ringing tone
                        Press 2 -   Ringing volume
                        Press 3 -   Incoming call alert
                        Press 4 -   Composer
                        Press 5 -   Message alert tone
                        Press 6 -   Keypad tones
                        Press 7 -   Warning and game tones 
                        Press 8 -   Vibrating    
                        Press 9 -   Screen saver
                 
                        """; 

        System.out.print(tonesMenu);

}

}


           int settingsMenuChoice =  inputCollector.nextInt();

	    switch(settingsMenuChoice){ 
	
		    case  6  -> {System.out.println("Settings"); 
                            second = false;
                            first = false;}

	                    String settingsMenu = """
    
                        Press 1 -   Call settiing
                        Press 2 -   Phone settings
                        Press 3 -   Security settings
                        Press 4 -   Restore factory settings
                 
                        """; 

        System.out.print(settingsMenu);


           int callSettingsChoice =  inputCollector.nextInt();
 
	    switch(callSettingsChoice){ 
	
		    case  1  -> {System.out.println("Call Setting"); 

	                    String callSettingsMenu = """
    
                        Press 1 -   Automatic redial
                        Press 2 -   Speed dailing
                        Press 3 -   Call waiting options
                        Press 4 -   Own number sending
                        Press 5 -   Phone line in use
                        Press 6 -   Automate answer

                 
                        """; 

        System.out.print(callSettingsMenu);




        System.out.print(settingsMenu);


           int phoneSettingsChoice =  inputCollector.nextInt();
 
	    switch(phoneSettingsChoice){ 
	
		    case  2  -> {System.out.println("Phone Settings"); 

	                    String phoneSettingsMenu = """
    
                        Press 1 -   Language
                        Press 2 -   Cell info display
                        Press 3 -   Welcome note
                        Press 4 -   Network selection
                        Press 5 -   LIghts 
                        Press 6 -   Confirm SIM service actions

                 
                        """; 

        System.out.print(phoneSettingsMenu);



        System.out.print(settingsMenu);


           int securitySettingsChoice =  inputCollector.nextInt();
 
	    switch(securitySettingsChoice){ 
	
		    case  3  -> {System.out.println("Security Settings"); 

	                    String securitySettingsMenu = """
    
                        Press 1 -   PIN code request
                        Press 2 -   Call barring service
                        Press 3 -   Fixed dialing
                        Press 4 -   Closed user group
                        Press 5 -   Phone security
                        Press 6 -   Change access codes

                 
                        """; 

        System.out.print(securitySettingsMenu);

}

}

}

}


}

}
}

}


           int clockMenuChoice =  inputCollector.nextInt();

	    switch(clockMenuChoice){ 
	
		    case  11  -> {System.out.println("Clock"); 
                            second  = false;
                            

	                    String clockMenu = """
    
                        Press 1 -   Alarm clock
                        Press 2 -   Clock settings
                        Press 3 -   Date setting
                        Press 4 -   Stopwatch
                        Press 5 -   Countdown timer
                        Press 6 -   Auto update of date and time
                 
                        """; 

        System.out.print(clockMenu);


                case 6 -> first = false;

}

}

}

}






