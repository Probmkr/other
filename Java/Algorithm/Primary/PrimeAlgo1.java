package Java.Algorithm.Primary;

import java.util.Scanner;

import java.util.ArrayList;
import java.util.Arrays;

public class PrimeAlgo1 {
  public static void main(String arg[]) {
    Scanner sc = new Scanner(System.in);
    int upto = -1;
    try {
      upto = Integer.parseInt(arg[0]);
    } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
    }
    System.out.print("Enter the number for the max of the prime numbers: ");
    if (upto < 0) {
      upto = sc.nextInt();
    }
    System.out.println("Calculating...");
    ArrayList<Integer> arr = getPrimariesUpToWithOutPut(upto);
    System.out.println("Prime numbers are...");
    for (int primary : arr) {
      System.out.println(primary);
    }
    sc.close();
  }

  public static ArrayList<Integer> getPrimariesUpToWithOutPut(int upto) {
    ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(2));
    boolean flag = true;
    for (int i = 3; i <= upto; i += 2) {
      flag = true;
      System.out.printf("\n######### %3d #########\n\n", i);
      for (int prime : arr) {
        System.out.printf("%d %% %d = %d\n", i, prime, i % prime);
        if (i % prime == 0) {
          System.out.printf("\n  %d is not prime!!\n", i);
          flag = false;
          break;
        }
      }
      if (flag) {
        System.out.printf("\n  %d is prime!!\n", i);
        arr.add(i);
      }
    }
    System.out.printf("\n#######################\n\n");
    return arr;
  }

  public static ArrayList<Integer> getPrimariesUpTo(int upto) {
    ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(2));
    boolean flag = true;
    for (int i = 3; i <= upto; i += 2) {
      flag = true;
      for (int prime : arr) {
        if (i % prime == 0) {
          flag = false;
          break;
        }
      }
      if (flag) {
        arr.add(i);
      }
    }
    return arr;
  }
}