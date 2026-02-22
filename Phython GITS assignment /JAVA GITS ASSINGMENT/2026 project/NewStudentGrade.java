import java.util.Scanner;
public class NewStudentGrade{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);


        int score = 0;



        System.out.print("Enter number of student: ");
        int studentsNumber = input.nextInt();


        System.out.print("How many subject do they offer: ");
        int subjects = input.nextInt();

        System.out.print("Saving >>>>>>>>>>>>\nSaved successfully\n");



    
        int [] [] studentDetails = new int [studentsNumber][subjects];

        for(int index = 0; index < studentsNumber; index++){
           System.out.printf("\nEntering Score for Student "+ (index + 1)+ ":");

            for(int count = 0; count < subjects; count ++){


            while (true){

            System.out.println("\nEnter score of subject "+(count + 1)+":");
            score = input.nextInt();

          
            if(score <= 0 || score > 100){
            System.out.print("Unable to save >>>>>>>>>>>>\nSaving was unsuccessfull\n");
            System.out.println("Invalid Entry, score must be between 1 - 100");

            }else{
                break;

                }
                }

            }
                           
           System.out.print("Saving >>>>>>>>>>>>\nSaved successfully\n");
        
            
        }


    
//


    }
}
