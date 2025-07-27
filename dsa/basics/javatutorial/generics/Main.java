package dsa.basics.javatutorial.generics;

public class Main {
   public static void main(String [] args) {
    var genericList = new GenericList<Integer>();
    genericList.add(1);
    int result = genericList.get(0);
    System.out.println(genericList.get(0));
     // genericList.add(1); // This will cause a compile-time error
    
     var numbers = new GenericClassWithConstraint<Integer>();
     
     // var error = new GenericClassWithConstraint<String>() compile time error
     System.err.println("Max is " +GenericMethods.maxGeneric(1, 2));
    
     GenericMethods.printKey("Name", "Hasan");
     GenericMethods.printKey("Age", 26);
    } 
} 
