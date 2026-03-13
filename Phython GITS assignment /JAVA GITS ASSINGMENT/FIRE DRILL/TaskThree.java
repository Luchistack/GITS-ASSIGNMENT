
import java.util.Scanner; 

public class TaskTwo{

public static void main(String[] args) {


Scanner input = new Scanner(System.in);


int sum = 0;

double average = 0;


for (int counter=1; counter<=10;  counter++){

System.out.print("Enter score: ");

int score = input.nextInt();

sum += score;

average = sum/10;

}

System.out.printf("the sum of %d%n", sum);

System.out.printf("the average  is %.2f%n" , average);


}

}
