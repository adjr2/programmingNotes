import java.io.*;

// Custom wrapper
class Maximum{
    private int maxi = 0;
    private int size = 0;

    public void insert(int x){
        this.size++;
        if (x <= this.maxi)
            return;
        this.maxi = x;
    }
    public int top() {
        return this.maxi;
    }

    public int elementNumber() {return this.size;}
};

public class WrapperClass {
    public static void main(String[] args){
//        The following are example of Autoboxing/wrapping.
//        Autoboxing/Wrapping: automatic conversion of primitive types to the objects of their corresponding
//        wrapper classes.
        byte a = 1;
        Byte byteObj = new Byte(a);
        Byte byteObjNew = Byte.valueOf(a); // new way of wrapping.
        Byte byteObjNew1 = a; // This also works.

        int b =10;
        Integer intObj = new Integer(b);
        Integer intObjNew = Integer.valueOf(b);

        float c = 12.3f;
        Float floatObj = new Float(c);
        Float floatObjNew = Float.valueOf(c);

        char d = 'a';
        Character charObj = new Character(d);
        Character charObjNew = Character.valueOf(d);
        Character charObjNew1 = d;

        System.out.println("Byte: "+a);
        System.out.println("Byte Object: "+byteObj);
        System.out.println("Byte Object New: "+byteObjNew);
        System.out.println("Byte Object New 1: "+byteObjNew1);

//      The following is an example of Unboxing/Unwrapping:
//      Unboxing/Unwrapping is opposite of Autoboxing/Wrapping.
        byte bv = byteObj;
        System.out.println("Byte (unwrapped): "+bv);

//        Custom Wrapper
        Maximum x = new Maximum();
        x.insert(12);
        x.insert(3);
        x.insert(32);

        System.out.println("Maximum element: "+x.top());
        System.out.println("Number of elements inserted: "+x.elementNumber());
    }
}
