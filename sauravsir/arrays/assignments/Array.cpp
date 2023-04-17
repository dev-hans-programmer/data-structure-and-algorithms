#include <iostream>
using namespace std;

class Array
{
private:
    int capacity;
    int *ptr;
    int lastIndex;

public:
    Array(int);
    ~Array();
    bool isEmpty();
    bool isFull();
    void traverse();
    void append(int);
    void edit(int, int);
    void deleteAt(int);
    int get(int);
    int findOne(int);
    int count();
    void insert(int, int);
};

Array::Array(int cap)
{
    ptr = new int[cap];
    lastIndex = -1;
    capacity = cap;
}

Array::~Array()
{
    delete[] ptr;
}

bool Array::isEmpty()
{
    return lastIndex == -1;
}

bool Array::isFull()
{
    return lastIndex == capacity - 1;
}

void Array::traverse()
{

    if (isEmpty())
        cout << "No items found to iterate\n";
    else
        for (int i = 0; i <= lastIndex; i++)
            cout << ptr[i] << " ";
    cout << "\n";
}

void Array::append(int item)
{
    if (!isFull())
    {
        lastIndex++;
        ptr[lastIndex] = item;
    }
}

void Array::edit(int pos, int item)
{
    if (!isEmpty() && pos <= lastIndex)
    {
        ptr[pos] = item;
    }
}

void Array::deleteAt(int pos)
{
    if (pos < 0 || pos > lastIndex)
        __throw_bad_exception();
    else
    {
        for (int i = pos; i < lastIndex; i++)
            ptr[i] = ptr[i + 1];
        lastIndex--;
    }
}

int Array::get(int pos)
{
    if (pos < 0 || pos > lastIndex)
        return 0;
    else
        return ptr[pos];
}

int Array::findOne(int item)
{
    for (int i = 0; i <= lastIndex; i++)
        if (ptr[i] == item)
            return i;
    return -1;
}
int Array::count()
{
    return lastIndex + 1;
}

void Array::insert(int pos, int item)
{
    if (isFull())
        cout << "Array is full \n";
    else if (pos < 0 || pos > lastIndex + 1)
        cout << "Invalid index\n";
    else
    {
        for (int i = lastIndex; i >= pos; i--)
            ptr[i + 1] = ptr[i];
        ptr[pos] = item;
        lastIndex++;
        cout << "Item inserted\n";
    }
}
