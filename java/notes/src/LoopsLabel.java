public class LoopsLabel {
    public static void main(String[] args){
        String[] array = {"Ron", "Harry", "Hermoine"};

        // Enhanced For Loop or Java For-Each Loop:
        for (String x: array){
            System.out.println(x);
        }
        boolean t = true;
        first :
        {
            second:
            {
                third:
                {
                System.out.println("Before the break statement");

                if (t)
                    break second;
                System.out.println("This won't execute");
                }

                System.out.println("This won't execute");
            }
            System.out.println("This is after second block");
        }
    }
}
