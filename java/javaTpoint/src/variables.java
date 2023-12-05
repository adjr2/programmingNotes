import java.awt.*;

public class variables {
    static int m=100; //static variable
//    static variables have the highest scope
    void method()
    {
        int n = 90; //local variable
//        local variables have scope within the method
    }
    public static void main(String[] args)
    {
        int data=50; //instance variable
//        instance variables have scope within the instance
        System.out.println(m);

//        example: widening
        float f=data;
        System.out.println(f);

//        example: narrowing (typecasting)
        float x=10.5f;
        int a=(int)x;
        System.out.println(a);

//        overflow
        int a1=130;
        byte b=(byte)a1;
        System.out.println(b);

//        adding lower type
        byte a2=10;
        byte b2=10;
        byte c2=(byte)(a2+b2);
        System.out.println(c2);
    }
}
