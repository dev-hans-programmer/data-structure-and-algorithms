#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
};

class SLL
{
private:
    node *start;
    /* data */
public:
    SLL(/* args */);
    ~SLL();
};

SLL::SLL(/* args */)
{
    start = NULL;
}

SLL::~SLL()
{

    if (start)
    {
        // delete the node
    }
}
