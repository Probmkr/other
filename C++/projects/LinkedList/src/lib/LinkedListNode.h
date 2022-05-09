#ifndef LINKEDLISTNODE_H
#define LINKEDLISTNODE_H
#include <cstddef>

namespace my_class {
	template<typename LinkedListNodeValueType>
	class LinkedListNode {
	public:
		LinkedListNodeValueType data;
		LinkedListNode<LinkedListNodeValueType> *next;
		LinkedListNode(LinkedListNodeValueType data, LinkedListNode<LinkedListNodeValueType> *next = nullptr) {
			this->data = data;
			this->next = next;
		}
	};
}

#endif
