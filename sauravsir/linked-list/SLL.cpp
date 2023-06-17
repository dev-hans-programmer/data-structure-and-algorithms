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
    void insertLast(int);
    Node *search(int);
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

void Sll::insertLast(int item)
{
    Node *n = new Node;
    n->data = item;
    n->next = NULL;

    if (start == NULL)
        start = n;
    else
    {
        Node *temp = start;
        while (temp->next)
            temp = temp->next;

        temp->next = n;
    }
}

Node *Sll::search(int item)
{
    Node *t;
    t = start;
    while (t)
    {
        if (t->data == item)
            return t;
        t = t->next;
    }
    return NULL;
}

void Sll::traverse()
{
    if (start == NULL)
        cout << "No item present in the linked list" << endl;
    else
    {
        Node *t;
        t = start;
        while (t)
        {
            /* code*/
            cout << t->data << " ";
            t = t->next;
        }
    }
}

int main()
{
    // Implement driver code here
    Sll s1;
    s1.insertBegin(10);
    s1.traverse();

    Node *t1 = s1.search(10);
    cout << t1->data;
}