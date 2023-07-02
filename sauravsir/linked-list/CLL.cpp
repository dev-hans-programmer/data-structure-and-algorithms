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
    ~CLL();
    void insertBegin(int);
    void insertLast(int);
    void insertAfter(Node *, int);
    Node *search(int);
    void deleteFirst();
    void deleteLast();
    void deleteNode(Node *);

    void traverse();
};

CLL::CLL()
{
    last = NULL;
}
CLL::~CLL()
{
    if (last)
        deleteFirst();
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

void CLL::insertAfter(Node *ptr, int item)
{
    Node *n = new Node;
    if (last)
    {
        n->data = item;
        n->next = ptr->next;
        ptr->next = n;

        if (ptr == last)
            last = n;
    }
}

Node *CLL::search(int item)
{
    Node *current;

    if (last)
    {
        current = last->next;
        do
        {
            if (current->data == item)
                return current;
            current = current->next;
        } while (current != last->next);
    }
    return NULL;
}

void CLL::deleteFirst()
{
    if (last)
    {
        Node *current = last->next;

        if (last->next == last)
            last = NULL;
        else
            last->next = current->next;
        delete current;
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
        Node *current = last;
        while (current->next != last)
            current = current->next;

        if (current == last)
        {
            delete last;
            last = NULL;
        }

        else
        {
            current->next = last->next;
            delete last;
            last = current;
        }
    }
    else
    {
        cout << "No node found to delete "
             << " ";
    }
}

void CLL::deleteNode(Node *ptr)
{
    if (last)
    {
        Node *prevNode = last->next;

        if (prevNode == last)
        {
            delete prevNode;
            last = NULL;
        }
        else
        {
            while (prevNode->next != ptr)
                prevNode = prevNode->next;

            prevNode->next = ptr->next;
            delete ptr;
        }
    }
}

void CLL::traverse()
{
    if (last)
    {
        Node *current = last->next;

        do
        {
            if (current != last)
                cout << current->data << " -> ";
            else
                cout << current->data << "";
            current = current->next;
            /* code */
        } while (current != last->next);
        cout << "\n";
    }
    else
        cout << "No node found to traverse " << endl;
}

int main()
{
    CLL c1;
    c1.insertBegin(20);
    c1.insertBegin(5);
    c1.insertLast(40);

    c1.traverse();
    c1.insertAfter(c1.search(40), 50);
    c1.deleteNode(c1.search(40));
    c1.deleteLast();
    c1.deleteLast();
    c1.deleteLast();
    c1.traverse();
}