package striver.basics.javatutorial.exceptions;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;

public class ExceptionsDemo {
    public static void show() {
        sayHello(null);
        String currentDirectory = System.getProperty("user.dir");
        String filePath = currentDirectory + File.separator + "striver" + File.separator + "basics" + File.separator
                + "javatutorial" + File.separator + "exceptions" + File.separator + "test.txt";
        System.out.println(filePath);
        readFile(filePath);
        try {
            withdrawMoney(120);
        } catch (InsufficientFundsException e) {
            System.out.println(e.getMessage());
        }
        
    }

    public static String getCurrentDirectory() {
        try {
            File file = new File(ExceptionsDemo.class.getProtectionDomain().getCodeSource().getLocation().toURI());
            return file.getParent(); // Returns the directory where the .class file is located
        } catch (URISyntaxException e) {
            throw new RuntimeException("Failed to get current directory", e);
        }
    }

    public static void sayHello(String name) {
        try {
            System.out.println("Hello" + name.toUpperCase());
        } catch (NullPointerException e) {
            System.out.println("Null pointer exception happened with the value " + e.getMessage());
        }

    }

    public static void readFile(String fileName) {
        // This is a try block with resources, used to release the resource
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            System.out.println("File found: " + fileName);

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (FileNotFoundException ex) {
            System.out.println("File not found: " + fileName);
        } catch (IOException ex) {
            System.out.println("IO exception happened while reading the file");
        }
    }
    public static void deposit(float value) {
        if(value <= 0) {
            // This is an unchecked exception
            // This is a runtime exception
            throw new IllegalArgumentException("Deposit value must be greater than 0");
        } else {
            System.out.println("Deposited: " + value);
        }
    }
    // This is to show checked exception
    public static void withdraw(float value) throws IOException {
        if(value <= 0)
            throw new IOException();
    }
    public static void withdrawMoney(int value) throws InsufficientFundsException {
        if(value > 100) throw new InsufficientFundsException();
    }

    // chaining exception
    public static void withdrawMoneyChainingException(int value) throws AccountException {
        if(value > 100) throw new AccountException(new InsufficientFundsException());
    }

}
