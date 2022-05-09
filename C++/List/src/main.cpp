#include <iostream>
#include <cstddef>
#include "lib/LinkedList.h"
#include "lib/Node.h"

using namespace my_class;


int main(){
	LinkedList<int> a;
	a.add_first(12);
	a.add_last(13);
    std::cout << a.length() << std::endl;
}
