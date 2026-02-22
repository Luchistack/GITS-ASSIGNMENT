public class FastingWeekend{
    public static void main(String[] args){

//1
String name = "Rosemary";
String reverse = "";
for(int index = name.length() -1; index >= 0; index--){
reverse += name.charAt(index);
}
System.out.println("reversed of Rosemary: " + reverse);
System.out.println();


//2
String nums = "1222211";
String rev = " ";
for(int in = nums.length() -1; in >= 0; in--){
rev += nums.charAt(in);
}
System.out.println("reversed of Rosemary: " + rev);
System.out.println();



//3
String upper = "Faith";
int counter = 0;
for(int low = 0; low < upper.length(); low++){
       char cased = upper.charAt(low);
    if(Character.isUpperCase(cased)){
        counter ++;

    }
}
        System.out.println("Number of uppercase = " + counter);
System.out.println();
    


//4
String lower = "Faith";
int count = 0;
for(int low = 0; low < lower.length(); low++){
       char cases = lower.charAt(low);
    if(Character.isLowerCase(cases)){
        count ++;

    }
}
        System.out.println("Number of lowercase = " + count);
System.out.println();
    


//6
String named = "rosemary";
for(int index = 0; index < named.length(); index++){
System.out.println((int) named.charAt(index));

}
System.out.println();



//7
double sum = 0;
for(double num = 1; num <=100; num ++){
sum += num; 
}
double average = sum / 100;
System.out.println("Average of 1 - 100 =" + average);

System.out.println();




//8
int divisor_number = 12;
for(int con = 1; con < 13; con++){
    if(divisor_number % con == 0){

        System.out.print("Numbers divisible by 12 =" + con);
System.out.println();

}
}


//9
int divi_number = 12;
int total = 0;
for(int cont = 1; cont < 13; cont++){
    if(divi_number % cont == 0){
    total += cont;
}
}
        System.out.print("Total divisors = " + total);
System.out.println();




//10

//11





//14

int totalSum = 0;
for(int even = 1; even <= 100; even ++){
    if(even % 2 == 0){
     totalSum += even;
}
}
System.out.print("Sum of even digits from 1-100 = " + totalSum);
System.out.println();


//15

int totals = 0;
for(int odd = 1; odd <= 100; odd ++){
    if(odd % 3 == 0){
     totals += odd;
}
}
System.out.print("Sum of odd digits from 1-100 = " + totals);
System.out.println();
















    }




}
