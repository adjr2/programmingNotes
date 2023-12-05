public class Constructor {
//    static variable
    public static String staticName;
//    declared Instance variables
    public String name;

    public int i;
    public Integer I;
    public Constructor()
    {
//        default constructor
//        initializing instance variable
        this.name = "Dhiraj";
        staticName = "Kumar";
    }
    public static void main(String[] args)
    {
        Constructor name = new Constructor();
        System.out.println("The name is: "+ name.name);
        System.out.println("default value for int is: " + name.i);
        System.out.println("static name is: " + staticName);
    }
}
