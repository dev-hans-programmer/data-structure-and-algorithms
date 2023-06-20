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
    ~Sll();
    void insertBegin(int);
    void insertLast(int);
    void insertAfter(Node *, int);
    void deleteFirst();
    void deleteLast();
    void deleteNode(Node *);
    Node *search(int);
    void traverse();
};

Sll::Sll()
{
    start = NULL;
}
Sll::~Sll()
{
    while (start)
    {
        deleteFirst();
    }
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

void Sll::insertAfter(Node *n, int item)
{
    // create the node
    Node *desired = new Node;
    desired->data = item;
    desired->next = NULL;
    if (start == NULL)
        start = desired;
    else
    {
        desired->next = n->next;
        n->next = desired;
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

void Sll::deleteFirst()
{
    if (start)
    {
        Node *temp = start;
        start = start->next;
        delete temp;
    }
}

void Sll::deleteLast()
{
    if (start)
    {

        if (start == NULL)
        {
            cout << "Undeflow";
        }

        else if (start->next == NULL)
        {
            delete start;
            start = NULL;
        }

        else
        {
            Node *temp = start;
            while (temp->next->next != NULL)
                temp = temp->next;
            delete temp->next;

            temp->next = NULL;
        }
    }
}

void Sll::deleteNode(Node *temp)
{
    if (start == NULL)
        cout << "Underflow\n";
    else
    {
        if (temp)
        {
            if (start == temp)
            {
                start = temp->next;
                delete temp;
            }
            else
            {
                Node *t;
                t = start;
                while (t->next != temp)
                    t = t->next;
                t->next = temp->next;
                delete temp;
            }
        }
    }
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

    s1.insertBegin(20);
    s1.insertLast(40);

    // Search the node which contains a value of 10;
    Node *temp = s1.search(10);
    s1.insertAfter(temp, 5);
    s1.deleteNode(s1.search(10));
    s1.deleteNode(s1.search(40));
    s1.deleteLast();
    s1.deleteNode(s1.search(20));
    s1.traverse();
}