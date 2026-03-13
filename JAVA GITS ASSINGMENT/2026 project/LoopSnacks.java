import java.util.Scanner;
public class LoopSnacks{
    public static void main(String[] args){

    for(int index = 1; index <= 100; index++){
       if(index %2 == 0){
       System.out.println(index); 

//

}
}
System.out.println();



    int count = 50;

    while(count <= 100){

    if(count %3 == 0){
    System.out.print(count);

}

        count++;
}

System.out.println();


for(int num = 100; num > 0; num--){


    System.out.println(num);

}
System.out.println();


for(int square = 1; square <= 21; square++){
    int tot = square * square;
    System.out.print(tot);

}
System.out.println();



for(int threes = 1; threes <= 51; threes+=3){
    System.out.println(threes);



}
System.out.println();


for(int both = 1; both <= 101; both ++){
     if(both %3 == 0 && both %5 == 0){
        System.out.print(both);

}

}
System.out.println();


    for(int index = 1; index <= 100; index++){
       if(index %7 == 0){
       System.out.println(index); 

}
}
System.out.println();


        int total = 0;
    for(int natural = 1; natural <= 50; natural++){
        total += natural;
}
        System.out.println("Sum of 50 natural number = " + total);
System.out.println();


int multiple = 1;
for(int product = 1; product <=10; product++){
    multiple *= product;
}
    System.out.print("Product of 10 natural numbers =" + multiple);
System.out.println();





for(int letters = 97; letters <= 122; letters++){

    System.out.print("\n" + (char)letters);

}
System.out.println();



int tim = 6;
int multi = 0;
for(int table = 1; table <=12; table++){
    multi = tim * table;
    System.out.printf("\n%d X %d = " + multi, tim, table);
}
System.out.println();




String name = "faith";

for(int coun = 0; coun < name.length(); coun++){ 
System.out.println("\n" +name.charAt(coun));
}
System.out.println();


String letter = "impossible";
int many = 0;
for(int times = 0; times < letter.length(); times++){

    if(letter.charAt(times) == 'i'){
    many ++;
}
}
    System.out.print("Number of i in impossible in  = " + many);
System.out.println();


String named = "jerry";
for(int lower = 0; lower < named.length(); lower++){
    System.out.print(Character.toUpperCase(named.charAt(lower)));
}
System.out.println();


String lowerCase = "jerry";
for(int lower = 0; lower < lowerCase.length(); lower++){
    System.out.print(Character.toLowerCase(lowerCase.charAt(lower)));
}
System.out.println();


String word = "angela";
int vowel_string = 0;
for(int words = 0; words < word.length(); words++){
    char ch = word.charAt(words);
    
    if( ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
        vowel_string++;
}
}


System.out.print("Vowel count in string = " + vowel_string);

System.out.println();

//
//
//int all = 2345;
//int to = 0;
//int collect = 0;
//for(int given = 0; given < all.lenght(); given++){
//    collect ++;
//    to += all;
//System.out.print(all);
//
//}








    }


}
