#include "Array.cpp"

// Define a function to find greatest element in the array
int find_greatest(Array a1)
{
    int greatest = a1.get(0);

    for (int i = 1; i < a1.count(); i++)
        if (a1.get(i) > greatest)
            greatest = a1.get(i);

    return greatest;
}

int find_smallest(Array a1)
{
    int smallest = a1.get(0);

    for (int i = 1; i < a1.count(); i++)
        if (a1.get(i) < smallest)
            smallest = a1.get(i);

    return smallest;
}

int main()
{
    Array marks(4), nums(2);
    for (int i = 0; i < 4; i++)
        marks.append((i + 1) * 30);

    nums.append(70);
    nums.append(100);
    marks.traverse();
    cout << "Smallest " << find_smallest(marks);
    cout << "\n";
    // marks.traverse();
    cout << "Greatest " << find_greatest(nums);
}