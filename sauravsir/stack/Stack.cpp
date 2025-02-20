#include "ArrayADT.cpp"
#include <iostream>

using namespace std;

class Stack : private Array
{
public:
    Stack(int);
    ~Stack();
    void push(int);
    int peek();
    void pop();
    bool isOverflow();
    bool isUnderflow();
};

Stack::Stack(int cap) : Array(cap)
{
}
Stack::~Stack()
{
}

void Stack::push(int data)
{
    if (isFull())
        cout << "Stack overflow";
    else
        append(data);
}

int Stack::peek()
{
    if (!isEmpty())
        return get(count() - 1);
    return 0;
}

void Stack::pop()
{
    if (!isEmpty())
        deleteAt(count() - 1);
}

bool Stack::isOverflow()
{
    return isFull();
}

bool Stack::isUnderflow()
{
    return isEmpty();
}

int main()
{
    Stack s1(5);
    s1.push(3);
    s1.push(4);
    s1.push(5);

    cout << s1.peek() << " " << s1.peek() << endl;
}
