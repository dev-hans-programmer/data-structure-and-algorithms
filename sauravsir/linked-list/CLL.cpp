#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;
};

class CLL
{
private:
    Node *last;

public:
    CLL();
    void insertBegin(int);
    void insertLast(int);
    void insertAfter(Node *, int);
    Node *search(int);
    void deleteFirst();
    void deleteLast();
    void deleteNode(Node *);
    void logListEmpty();

    void traverse();
};

CLL::CLL()
{
    last = NULL;
}

void CLL::logListEmpty()
{
}

void CLL::insertBegin(int data)
{
    Node *n = new Node;
    n->data = data;

    if (last)
    {
        // list is not empty
        n->next = last->next;
        last->next = n;
    }
    else
    {

        n->next = n;
        last = n;
    }
}

void CLL::insertLast(int data)
{
    Node *n = new Node;
    n->data = data;
    if (last)
    {
        n->next = last->next;
        last->next = n;
        last = n;
    }
    else
    {
        n->next = n;
        last = n;
    }
}

Node *CLL::search(int item)
{
    Node *current = last;
    while (current != last->next)
    {
        if (current->data == item)
            return current;
        current = current->next;
    }
    return current->data == item ? current : NULL;
}

void CLL::deleteFirst()
{
    if (last)
    {
        if (last->next != last)
        {
            Node *current = last->next;
            last->next = current->next;
            delete current;
        }
        else
        {
            delete last;
            last = NULL;
        }
    }
    else
    {
        cout << "No node found to delete "
             << " ";
    }
}

void CLL::deleteLast()
{
    if (last)
    {
        if (last->next == last)
            deleteFirst();
        else
        {
            Node *current = last->next;
            Node *lastNode = last;
            while (current->next != lastNode)
                current = current->next;

            current->next = last->next;
            last = current;
            delete lastNode;
        }
    }
    else
    {
        cout << "No node found to delete "
             << " ";
    }
}

void CLL::traverse()
{
    if (last)
    {
        Node *current = last->next;

        do
        {
            cout << current->data << " ";
            current = current->next;
            /* code */
        } while (current != last->next);
    }
}

int main()
{
    CLL c1;
    c1.insertBegin(20);
    c1.insertBegin(5);
    c1.insertLast(40);

    cout << c1.search(20)->data << endl;
}