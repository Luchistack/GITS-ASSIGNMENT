
import java.util.Scanner; 

public class TaskFour{

public static void main(String[] args) {


Scanner input = new Scanner(System.in);



int sum = 0;

double average = 0;


for (int counter=1; counter<=10;  counter++){

System.out.print("Enter score: ");

int score = input.nextInt();

sum += score;

average = sum/10;

if (counter %2 == 0)sum+=sum; count++;

}

System.out.printf("the sum of %d%n", sum);




}

}
