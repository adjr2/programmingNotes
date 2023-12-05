import java.text.DecimalFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FormattedOutput {
    public static void main(String[] args)
            throws ParseException // have to add this to handle error with .parse
    {
//        FIRST: Using System.out.printf()
//        Note: System.out.format() is equivalent to printf() and can also be used.
        int x = 100;
        System.out.printf("Printing simple integer: x %d\n", x);
        System.out.printf("Formatted with precision: PI = %.2f\n", Math.PI);

        float n = 5.2f;
        //since total number of digits after decimal is less than 4, it will add 0s.
        System.out.printf("Formatted to specific width: n = %.4f\n", n);

        n = 2324242.3f;
        //since total number of digits before decimal is less than 20, it will print blanks.
        System.out.printf("Formatted to right margin: n = %20.4f\n", n);

//        SECOND: using DecimalFormat class
        System.out.println("SECOND TYPE");
        double num = 123.3461;
        DecimalFormat ft = new DecimalFormat("####");
        System.out.println("Without fraction part: num = " + ft.format(num));

        ft = new DecimalFormat("#.##");
        System.out.println("Formatted to give precision: num = " + ft.format(num));

        ft = new DecimalFormat("#.0000000");
        System.out.println("appended zeroes to right: num = " + ft.format(num));

        double income = 232434.3162;
        ft = new DecimalFormat("$###,###.##");
        System.out.println("Your formatted income: " + ft.format(income));

//        THIRD: Formatting dates and parsing using SimpleDateFormat class
        System.out.println("THIRD TYPE");
        SimpleDateFormat ftt = new SimpleDateFormat("dd-MM-yyyy");
        String str = ftt.format(new Date());
        System.out.println("Formatted date: " + str);

        // parsing a given string
        str = "03-09-1995";

        ftt = new SimpleDateFormat("dd-MM-yyyy");
        Date date = ftt.parse(str);

        System.out.println("Parsed Date: " +date);

    }
}
