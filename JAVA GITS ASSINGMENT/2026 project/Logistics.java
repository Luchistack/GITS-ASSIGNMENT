import java.util.Scanner;
public class Logistics{
public static void main (String[] args){
Scanner input = new Scanner (System.in);

int basePay = 5000;


boolean running = true;


while (running){

for(int index = 0; index <=48; index++){
System.out.print("=");
}
System.out.println("\n Collection Rate   Amount Per Parcel   Base Pay");

for(int index = 0; index <=48; index++){    
System.out.print("=");
}


System.out.println("\n Less than 50%\t\t160\t\t5000\n 50-59%\t\t\t200\t\t5000\n 60-69%\t\t\t250\t\t5000\n >=70%\t\t\t500\t\t5000");

System.out.println("\nEnter Rider Name: ");
String riderName = input.nextLine();

System.out.println("\nEnter number of delivery: ");
int delivery = input.nextInt();

int expectedResult2 = 0;



if(delivery < 0 || delivery > 100){
System.out.print("Invalid input");


}else if(delivery < 50){
      int amount_per_parcel = 160;
        expectedResult2 = basePay + (delivery * amount_per_parcel);

 
}else if(delivery >= 50 && delivery <= 59){
      int amount_per_parcel = 200;
        expectedResult2 = basePay + (delivery * amount_per_parcel);


}else if(delivery >= 60 && delivery <= 69){
      int amount_per_parcel = 250;
        expectedResult2 = basePay + (delivery * amount_per_parcel);


}else if(delivery >= 70){
      int amount_per_parcel = 500;
        expectedResult2 = basePay + (delivery * amount_per_parcel);


}
input.nextLine();


System.out.printf("\nDear %s,Congratulations! You've Successfully made %d delivery today and your expected wage is %d ", riderName, delivery, expectedResult2 );


System.out.println("\nWill you like to continue, enter yes/no? ");

String enter = input.nextLine().toLowerCase().trim();



if(enter.equals ("no")){
break;

}else if(enter.equals ("yes")){
continue;
}else if(!enter.equals ("no") || !enter.equals ("yes")){
    System.out.println("Invalid entry");
   continue;
}

}
}
}

