import java.util.Scanner;
public class StudentGrade{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);




        System.out.print("Enter number of student: ");
        int studentsNumber = input.nextInt();


        System.out.print("How many subject do they offer: ");
        int subjects = input.nextInt();

      
            int [] totals = new[studentNumber];
    
            int [] average = new double[studentNumber];



        int [][] scores = new int [studentsNumber][subjects];

        for(int student = 0; student < studentsNumber; student++){
                System.out.print("Entering scores of student " + (student + 1)+ ":");   
              
                for(int subject = 0; subject < subjects; subject++){

                    int scoresinput;

                    while (true) {

                    System.out.print("Score for subject " + (subject + 1) + ": ");
                    scoresinput = input.nextInt();
            
                    if(scoresinput < 0 || scoresinput > 100){   
                        System.out.print("Invalid entry, Score must not be lesser than 0 or grater than 100");
                   }else{
                        break; 
            }                   
                }
                   scores[student][subject] = scoresinput;

        }
    }
    
        //total and average 
         for(int student = 0; student < studentsNumber; student++){
            int sum = 0;
         for(int subject = 0; subject < students; subject++){
            sum += scores[student][subject];

}
            totals[student] = sum;
            averages[student] = (double) sum / subjects;
}

//computing position based on highest and owest scores (highest = positon 1)
    Integer [] positions = new Integer[studentsNumber];
    for(int index = 0; index < studentsNumber; index ++){


    Arrays.sort(position, (a, b) -> totals[b] - totals[a]); //sort imdex by descending order
    int [] pos = new int[studentsNumber];
    for(int rank = 0; rank < studentsNumber; rank ++){
        pos[position[rank]] = rank + 1; //position starts from 1

}

    System.out.print("\nSTUDENT\n"); //print table Header
    for (int s = 1; s <= studentsNumber; s++){
    System.out.print("SUBJECT" + s + "\t")

}
    System.out.println("TOTAL\tAVERAGE\tPOS");

    //print student data
    for (int tudent = 0; student < studentsNumber; student++){
          System.out.print((student + 1) + "\t");
        for(int subject = 0; subject < subjectsNumber; subject++){
                System.out.print(scores[student][subject] + "\t");

        }

                          
            System.out.printf("%d\t%2.f\t%d\n", total[student], average[student], pos[student]);
        }
    }

}
































