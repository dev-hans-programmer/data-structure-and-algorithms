package striver.basics.javatutorial.exceptions;

// checked -> Exception
// unchecked -> RuntimeException
public class InsufficientFundsException extends Exception{

    public InsufficientFundsException() {
        super("Insufficient funds in the account");
    }

    public InsufficientFundsException(String message) {
        super(message);
    }
}
