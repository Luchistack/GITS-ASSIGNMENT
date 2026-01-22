import java.util.Scanner;
public class inverse{
public static int countLetters(String s){
Scanner input = new Scanner(System.in);

//int number = "6543";
System.out.println("Enter User Number");
int countLetters = input.nextInt();

int reverse = 0;

    while(int count != 0) {
           int number= count %10;
            reverse = reverse * 10 + number;
            count = count /  10;
System.out.println("reversed number = " + reverse);
    }
}

}

