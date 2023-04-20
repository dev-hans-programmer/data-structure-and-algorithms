#include <iostream>
using namespace std;

// Search an element in an array
// Time complexity -> O(n) time
int find(int arr[], int size, int element)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == element)
        {
            return i;
        }
    }
    return -1;
}

// insert an element in an array
// In best case, when we want to insert an element at the end of the array -> O(1)
// In worst case, when we want to insert an element at the beginning of the array -> O(n)
int insert(int arr[], int size, int element, int position, int capacity)
{
    if (size == capacity)
        return size;

    int idx = position - 1;

    for (int i = size - 1; i >= idx; i--)
        arr[i + 1] = arr[i];
    arr[idx] = element;
    return size++;
}

int main()
{
    int n[] = {0, 1, 2, 3, 4, 5};
    int size = sizeof(n) / sizeof(int);

    cout << find(n, size, 2) << endl;
    return 0;
}