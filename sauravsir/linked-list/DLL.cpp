#include <iostream>
using namespace std;

struct node
{
    node *prev;
    int data;
    node *next;
};

class Dll
{
private:
    node *start;

public:
    Dll();
    ~Dll();
    bool isEmpty();
    void insertBegin(int);
    void insertLast(int);
    void insertAfter(node *, int);
    void deleteFirst();
    void deleteLast();
    void deleteNode(node *);
    node *search(int);
    void traverse();
};

Dll::Dll()
{
    start = NULL;
}
Dll::~Dll()
{
    while (start)
    {
        deleteFirst();
    }
}
bool Dll::isEmpty()
{
    return start == NULL;
}

void Dll::insertBegin(int item)
{
    // create the node
    node *n = new node;
    n->prev = NULL;
    n->next = start;
    n->data = item;
    if (start)
        start->prev = n;
    start = n;
}
void Dll::insertLast(int item)
{
    // create the node
    node *n = new node;
    n->next = NULL;
    n->data = item;

    if (isEmpty())
    {
        n->prev = start;
        start = n;
    }
    else
    {
        node *t = start;
        while (t->next != NULL)
            t = t->next;
        n->prev = t;
        t->next = n;
    }
}

void Dll::traverse()
{
    if (isEmpty())
        cout << "No node is found to traverse\n";
    else
    {
        node *t = start;
        cout << "The values are:\n";
        while (t)
        {
            cout << t->data << " ";
            t = t->next;
        }
    }
}

void Dll::insertAfter(node *ptr, int item)
{
    node *n = new node;
    n->data = item;

    if (isEmpty())
    {
        n->prev = NULL;
        n->next = NULL;
        start = n;
    }
    else
    {
        if (ptr)
        {
            n->prev = ptr;
            n->next = ptr->next;
            if (ptr->next)
                ptr->next->prev = n;
            ptr->next = n;
        }
    }
}

node *Dll::search(int item)
{
    if (isEmpty())
    {
        cout << "No node is present\n";
        return NULL;
    }

    else
    {
        node *t = start;
        while (t)
        {
            if (t->data == item)
                return t;
            t = t->next;
        }
        return NULL;
    }
}

void Dll::deleteFirst()
{
    if (isEmpty())
        cout << "No node found to delete\n";
    else if (start->next)
    {
        node *t = start;
        start = start->next;
        start->prev = NULL;
        delete t;
    }
    else
    {
        delete start;
        start = NULL;
    }
}

void Dll::deleteLast()
{
    if (isEmpty())
        cout << "No node found to delete\n";
    else if (start->next == NULL)
        deleteFirst();
    else
    {
        node *t = start;
        while (t->next != NULL)
            t = t->next;
        if (t->prev)
            t->prev->next = NULL;
        else
            start = NULL;
        delete t;
    }
}

void Dll::deleteNode(node *ptr)
{
    if (ptr)
    {

        if (start == ptr)
            deleteFirst();
        else if (ptr->next == NULL)
            deleteLast();
        else
        {
            ptr->prev->next = ptr->next;
            ptr->next->prev = ptr->prev;
            ptr->prev = NULL;
            ptr->next = NULL;
            delete ptr;
        }
    }
}

int main()
{
    Dll d1;
    d1.insertBegin(10);
    d1.insertBegin(20);
    d1.insertBegin(30);
    d1.insertLast(5);
    d1.insertLast(1);
    d1.insertBegin(0);
    d1.deleteLast();
    d1.deleteNode(d1.search(20));
    d1.deleteNode(d1.search(0));
    d1.deleteNode(d1.search(5));
    d1.traverse();
}
