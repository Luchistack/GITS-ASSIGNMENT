
import java.util.Scanner;
public class threeNumbers{
public static void main(String[] args){
Scanner input = new Scanner(System.in);

System.out.print("Enter Number one: ");
double num1 = input.nextDouble();

System.out.print("Enter Number two: ");
double num2 = input.nextDouble();

System.out.print("Enter Number three: ");
double num3 = input.nextDouble();

System.out.println(secondLargestNumber(num1,num2,num3));

}

public static double decreasingOrder( double numberOne, double numberTwo, double numberThree   ){

double largestNumber = numberOne;
if  (numberTwo > largestNumber) {
    largestNumber = numberTwo;  
}
else if (numberThree > largestNumber) {
    largestNumber = numberThree;
}
else {
    largestNumber = numberOne;
}
return largestNumber;

}

public static double secondLargestNumber(double numberTwo, double numberThree, double numberOne ){

double largest = decreasingOrder( numberOne, numberTwo, numberThree);
double secondLargest = numberTwo;
if (numberThree < secondLargest && secondLargest != largest){
    secondLargest = numberThree;
}
else {
    secondLargest = numberTwo;
}
return secondLargest;

}

public static double smallestNumber( double numbertThree, double numberTwo, double numberOne   ){

double smallestNumber = numberThree;
if  (numberThree < secondLargest && smallestNumber != secondLargest) {
    smallestNumber = numberThree;  
}
else {
    smallestNumber = numberThree;
}
return smallestNumber;

}

}
