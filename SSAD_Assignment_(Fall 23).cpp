//Polina Pushkareva
//p.pushkareva@innopolis.university
#include <iostream>
#include <vector>
#include <set>
using namespace std;
//class CellInfo containing the char-value of element and how many times it should be added in the multiset
class CellInfo {
public:
    char value;
    int copies;
    //public constructor
    CellInfo(char val, int c) {
        this->value=val;
        this->copies=c;
    }
};
//class Bag
class Bag {
public:
    //declaring vector for storing all objects
    vector<CellInfo> elements;
    //declaring multiset for storing data
    multiset<char> bag;
    //insert function
    void insert (char val, int n) {
        //firstly, we add value to the multiset n times
        for (int i=0; i<n; i++) {
            bag.insert(val);
        }
        //secondly, we add current CellINfo to the vector
        for(auto & element : elements) {
            //changing the number of copies if the vector already contains current value
            if(element.value==val) {
                element.copies+=n;
                return;
            }
        }
        //adding current CellInfo if it wasn't found in the vex=ctor
        elements.emplace_back(CellInfo(val, n));
    }
    //removing as many copies as possible
    void remove (char val, int n) {
        //removing value from multiset n times
        for(int i=0; i<n; i++) {
            bag.extract(val);
        }
        //removing copies from the vector
        for (auto & element : elements) {
            if (element.value==val) {
                //if n greater that the number of copies we assign them to 0
                if(element.copies <= n) {
                    element.copies=0;
                    //otherwise, we subtract needed number of copies
                } else if (element.copies>n){
                    element.copies-=n;
                }
                return;
            }
        }
    }
    //function that find the minimum element in the vector
    char min() {
        char min='{';
        for(auto & element : elements) {
            if(element.value<min && element.copies!=0) {
                min=element.value;
            }
        }
        return min;
    }
    //function that find the maximum element in the vector
    char max() {
        char max='Z';
        for(auto & element : elements) {
            if(element.value>max && element.copies!=0) {
                max=element.value;
            }
        }
        return max;
    }
    //function that checks if two bags are equal
    bool isEqual(const Bag b) {
        if(bag.empty() && b.bag.empty()) {
            return true;
        }
        return bag == b.bag;
    }
};
int main() {
    //declaring 2 empty bags
    Bag bag1, bag2;
    //scanning the number of operations
    int n;
    cin>>n;
    for (int i=0; i<n; i++) {
        char operation, letter;
        int copy, bag;
        //scanning operation, bag's number, letter, and the number of copies
        cin>>operation>>bag>>letter>>copy;
        //performing insertion
        if(operation == 'i') {
            if(bag==1) {
                bag1.insert(letter,copy);
            }
            if(bag==2) {
                bag2.insert(letter,copy);
            }
        }
        //performing removal
        if(operation == 'r') {
            if(bag==1) {
                bag1.remove(letter,copy);
            }
            if(bag==2) {
                bag2.remove(letter,copy);
            }
        }
    }
    //outputting max of the 1 bag
    if(bag1.max()=='Z') {
        cout<< -1<<" ";
    } else {
        cout<<bag1.max()<<" ";
    }
    //outputting min of the 2 bag
    if(bag2.min()=='{') {
        cout<< -1<<" ";
    } else {
        cout<<bag2.min()<<" ";
    }
    //outputting the result of isEqual() function converting it to the number
    if(bag1.isEqual(bag2)) {
        cout<<1;
    } else {
        cout<<0;
    }
    return 0;
}
