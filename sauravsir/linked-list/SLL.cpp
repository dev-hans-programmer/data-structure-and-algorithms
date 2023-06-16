#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

class Sll
{
private:
    Node *start;

public:
    Sll();
    void insertBegin(int);
    void traverse();
};

Sll::Sll()
{
    start = NULL;
}

void Sll::insertBegin(int item)
{
    // Create a new node
    Node *temp = new Node;
    temp->data = item;
    temp->next = start;

    start = temp;
}

void Sll::traverse()
{
    if (start == NULL)
        cout << "No item present in the linked list" << endl;
    else
    {
        while (start)
        {
            /* code*/
            cout << start->data << " ";
            start = start->next;
        }
    }
}

int main()
{
    // Implement driver code here
    Sll s1;
    s1.insertBegin(10);
    s1.insertBegin(20);
    s1.insertBegin(30);
    s1.traverse();
}