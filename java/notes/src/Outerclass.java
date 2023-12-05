public class Outerclass {

    private static String msg = "tesing";
    private String msg2 = "Testing";
    public static class NestedStaticClass {
        public void printMessage() {
            System.out.println("Message from nested static class: " + msg);
//            The line below throws an error as static classes can only access static variables from outer class
//            System.out.println("Message from nested static class msg2: " + msg2);
        }
    }

    public class InnerClass {
        public void display() {
            System.out.println("Message from non-static nested class msg: "+ msg);
            System.out.println("Message from non-static nested class msg2: "+ msg2);
        }
    }
}

class GFG {
    public static void main(String[] args)
    {
        Outerclass.NestedStaticClass printer = new Outerclass.NestedStaticClass();
        printer.printMessage();

        Outerclass outer = new Outerclass();
        Outerclass.InnerClass inner = outer.new InnerClass();
        inner.display();

//        we can combine the above two steps into one step
        Outerclass.InnerClass innerObject = new Outerclass().new InnerClass();
        innerObject.display();

    }
}
