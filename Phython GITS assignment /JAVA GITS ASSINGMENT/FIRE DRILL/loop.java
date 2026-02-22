
import java.util.Scanner; 


public class loop{

public static void main(String[] args) {


Scanner input = new Scanner(System.in);

int total = 0; 

int number = 1; 

while (number <= 10) { 

System.out.print("Enter score: "); 

int score = input.nextInt();

total = total + score; 

number = number + 1;

}

System.out.printf("%nTotal of all 10 grades is %d%n", total);

}
}


