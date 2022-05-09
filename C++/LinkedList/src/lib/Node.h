#ifndef NODE_H
#define NODE_H
#include <cstddef>

namespace my_class {
	template<typename NodeValueType>
	class Node {
	public:
		NodeValueType data;
		Node<NodeValueType> *next;
		Node(NodeValueType data, Node<NodeValueType> *next = nullptr) {
			this->data = data;
			this->next = next;
		}
	};
}

#endif
