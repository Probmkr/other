#ifndef LINKEDLISTNODE_H
#define LINKEDLISTNODE_H
#include <cstddef>

namespace my_class {
	template<typename LLVT>
	class LinkedListNode {
	public:
		LLVT data;
		LinkedListNode<LLVT> *next;
		
		LinkedListNode(LLVT data, LinkedListNode<LLVT> *next = nullptr) {
			this->data = data;
			this->next = next;
		}
	};
}

#endif
