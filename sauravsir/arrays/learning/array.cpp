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
    bool isEmpty();
    bool isFull();
    void traverse();
};

Array::Array(int cap)
{
    ptr = new int[cap];
    lastIndex = -1;
    capacity = cap;
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
    for (int i = 0; i <= lastIndex; i++)
        cout << ptr[i] << " ";
    cout << "\n";
}

int main()
{
    Array a1(2);
    a1.traverse();
    cout << a1.isEmpty();
    cout << a1.isFull();
}
