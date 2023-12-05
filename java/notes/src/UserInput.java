import java.io.*;
import java.util.Scanner;
public class UserInput {
//    ways to take input

    public static void main(String[] args)
            throws IOException {
//        FIRST: BufferedReader Class
//        BufferedReader bfn = new BufferedReader(new InputStreamReader(System.in));
//
////        String reading internally
//        System.out.println("Enter a string: ");
//        String str = bfn.readLine();
//
////        Integer reading internally
//        System.out.println("Enter an integer: ");
//        int it = Integer.parseInt(bfn.readLine());
//
//        System.out.println("Entered String: "+ str);
//        System.out.println("Entered integer: "+ it);

//      Extra(BufferedReader):
//        FileReader fr = new FileReader("src/file.txt");
//        BufferedReader br = new BufferedReader(fr);
//
//        char[] c = new char[20];
//
//        if (br.markSupported()) {
//            System.out.println("Mark() method is supported.");
////          When you call mark() on a BufferedReader it will begin keeping data you read from that point forwards in its internal buffer.
////          When you call reset() it will jump back to the marked position of the stream, so the next read()s will be satisfied by the in-memory buffer.
////          When you read past the end of that buffer, then it will seamlessly go back to reading fresh data. BufferedInputStream works the same way.
//            br.mark(100);
//        }
//
//        br.skip(8); // skips first 8 characters.
//
//        if (br.ready()) {
//            System.out.println("Readline()");
//            System.out.println(br.readLine());
//
//            br.read(c); //reads characters into a portion of an array.
//
//            for (int i = 0; i < 20; i++) {
//                System.out.println("Char print:");
//                System.out.println(c[i]);
//            }
//
//            System.out.println();
//
//            br.reset(); // this nullified the affect of br.skip.
//
//            for (int i = 0; i < 10; i++) {
//                System.out.println("Char second print:");
//                System.out.print((char) br.read()); // this prints just one charater.
//            }
//        }

//        SECOND: Scanner
//        Scanner scanObj = new Scanner(System.in);
//        String name;
//        int rollno;
//        float marks;
//        System.out.println("Enter your name: ");
//        name= scanObj.nextLine();
//        System.out.println("Enter your rollno: ");
//        rollno=scanObj.nextInt();
//        System.out.println("Enter your marks: ");
//        marks = scanObj.nextFloat();
//
//        System.out.println("Name: "+name);
//        System.out.println("Rollno: "+rollno);
//        System.out.println("Marks: "+marks);

//      Extra (Scanner):
//        check if an int value is available:
//        int sum = 0, count = 0;
//        while (scanObj.hasNextInt()){
//            int num = scanObj.nextInt();
//            sum += num;
//            count++;
//        }

//        character input:
//        System.out.println("Enter gender: ");
//        char gender = scanObj.next().charAt(0); //prints the first character.
//        System.out.println("Gender: "+gender);

//        THIRD: Console class
//        Advantages: reading password without echoing; synchronized; doesn't work in non-interactive environment (such as in IDE)
//        String name = System.console().readLine();
//
//        System.out.println("You entered string: "+ name);

//        FOURTH: Using command line argument
        if (args.length > 0) {
            System.out.println("The command line arguments are: ");

            for (String val: args)
                System.out.println(val);
        }
        else
            System.out.println("No command line arguments found");
    }
}
