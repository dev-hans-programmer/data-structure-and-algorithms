#include <iostream>
using namespace std;

int main()
{
    vector<string> names;

    names.push_back("Hasan Ali");
    names.push_back("Rohan Pradev");

    for (vector<string>::iterator itr = names.begin(); itr != names.end(); itr++)
        cout << *itr << endl;
}
