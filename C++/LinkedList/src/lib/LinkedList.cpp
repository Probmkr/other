// #include "LinkedList.h"

// namespace my_class {
// 	using namespace std;

// 	template<typename ListType>
// 	LinkedList<ListType>::LinkedList() {
// 		this->no = 0;
// 		this->head = nullptr;
// 		this->current = nullptr;
// 	}

// 	template<typename ListType>
// 	int LinkedList<ListType>::length() {
// 		return this->no;
// 	}

// 	template<typename ListType>
// 	int LinkedList<ListType>::search(ListType data) {
// 		int cnt = 0;
// 		Node<ListType> *ptr = this->head;
// 		while (ptr != nullptr) {
// 			if (*ptr->data == data) {
// 				this->current = ptr;
// 				return cnt;
// 			}
// 		}
// 	}

// 	template<typename ListType>
// 	bool LinkedList<ListType>::contains(ListType data) {
// 		return this->search(data) >= 0;
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::add_first(ListType data) {
// 		Node<ListType> ptr = this->head;
// 		this->head = this->current = &new Node<ListType> (data, ptr);
// 		this->no++;
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::add_last(ListType data) {
// 		if (this->head == nullptr) {
// 			this->add_first(data);
// 		} else {
// 			Node<ListType> ptr = this->head;
// 			while (*ptr->next != nullptr) {
// 				ptr = *ptr->next;
// 			}
// 			*ptr->next = this->current = &new Node<ListType> (data, nullptr);
// 		}
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::remove_first() {
// 		if (this->head != nullptr) {
// 			delete this->head;
// 			this->head = this->current = this->*head->next;
// 		}
// 		this->no--;
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::remove_last() {
// 		if (this->head != nullptr) {
// 			if (this->*head->next == nullptr) {
// 				this->remove_first();
// 			} else {
// 				Node<ListType> ptr = this->head;
// 				Node<ListType> pre = this->head;

// 				while (*ptr->next != nullptr) {
// 					pre = ptr;
// 					ptr = *ptr->next;
// 				}
// 				delete *pre->next;
// 				this->current = pre;
// 				this->no--;
// 			}
// 		}
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::remove(Node<ListType> *p) {
// 		if (this->head != nullptr) {
// 			if (p == this->head) {
// 				this->remove_first();
// 			} else {
// 				Node<ListType> ptr = this->head;
// 				while (*ptr->next != p) {
// 					ptr = *ptr->next;
// 					if (ptr == nullptr) {
// 						return;
// 					}
// 				}
// 				*ptr->next = *p->next;

// 			}
// 		}
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::remove_current_node() {
// 		this->remove(this->current);
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::clear() {
// 		while (this->head != nullptr) {
// 			this->remove_first();
// 		}
// 		this->current = nullptr;
// 		this->no = 0;
// 	}

// 	template<typename ListType>
// 	bool LinkedList<ListType>::next() {
// 		if (this->current != nullptr || this->current->next != nullptr) {
// 			return false;
// 		} 
// 		this->current = this->*current->next;
// 		return true;
// 	}

// 	template<typename ListType>
// 	void LinkedList<ListType>::print_current_node() {
// 		if (this->current != nullptr) {
// 			cout << "着目ノードはありません" << endl;
// 		} else {
// 			print(this->current->data);
// 		}
// 	}
// }
