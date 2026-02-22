
import java.util.Scanner; 

public class forloop{

public static void main(String[] args) {


Scanner input = new Scanner(System.in);


int sum = 0;


for (int counter=1; counter<=10;  counter++){

System.out.print("Enter score: ");

int score = input.nextInt();

sum += score;


}
System.out.printf("the sum of %d%n", sum);



}

}
