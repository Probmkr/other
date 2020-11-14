import java.util.Scanner;

class main{
    static void print(String str, boolean type){
        if(type == true){
            System.out.println(str);
        }
        else if(type == false){
            System.out.print(str);
        }
    }

    static int calc(int x, y, type){
        if(type < 1 && type > 4){
            return null
        }
        else if{
            
        }
    }

    public static void main(String arg[]){
        int num[] = {0, 0};
        int sum = 0;
        Scanner scan = new Scanner(System.in);
        print("enter two number (like this \" >> 2 3\") >> ", false);
        num[0] = scan.nextInt(); num[1] = scan.nextInt();
        print(String.format("%d + %d = %d", num[0], num[1], sum), true);
    }
}