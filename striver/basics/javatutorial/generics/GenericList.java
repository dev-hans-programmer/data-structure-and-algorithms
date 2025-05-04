package striver.basics.javatutorial.generics;

public class GenericList<T> {
    private Object[] items = new Object[10];
    private int count;

    public void add(T item) {
        items[count++] = item;
    }
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T) items[index];
    }

}
