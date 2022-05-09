#include <iostream>
#include <cstddef>
#include "lib/LinkedList.h"
#include "lib/LinkedListNode.h"

using namespace my_class;


int main(){
    LinkedList<int> a;
    a.add_first(12);
    a.add_last(13);
    a.add_last(14);
    a.add_last(15);
    a.add_last(16);
    std::cout << a.length() << std::endl;
}
