#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <cstddef>
#include <iostream>
#include "LinkedListNode.h"

namespace my_class {
	using namespace std;

	template<typename LT>
	class LinkedList {
		int no;
		LinkedListNode<LT> *head;
		LinkedListNode<LT> *current;
	public:
		LinkedList() {
			this->no = 0;
			this->head = nullptr;
			this->current = nullptr;
		}
		int length() {
			return this->no;
		}
		int search(LT data) {
			int cnt = 0;
			LinkedListNode<LT> ptr = this->head;
			while (ptr != nullptr) {
				if (ptr->data == data) {
					this->current = ptr;
					return cnt;
				}
			}
		}
		bool contains(LT data) {
			return this->search(data) >= 0;
		}
		void add_first(LT data) {
			LinkedListNode<LT> *ptr = this->head;
			this->head = this->current = new LinkedListNode<LT> (data, ptr);
			this->no++;
		}
		void add_last(LT data) {
			if (this->head == nullptr) {
				this->add_first(data);
			} else {
				LinkedListNode<LT> *ptr = this->head;
				while (ptr->next != nullptr) {
					ptr = ptr->next;
				}
				this->no++;
				ptr->next = this->current = new LinkedListNode<LT> (data, nullptr);
			}
		}
		void remove_first() {
			if (this->head != nullptr) {
				delete this->head;
				this->head = this->current = this->*head->next;
			}
			this->no--;
		}
		void remove_last() {
			if (this->head != nullptr) {
				if (this->*head->next == nullptr) {
					this->remove_first();
				} else {
					LinkedListNode<LT> *ptr = this->head;
					LinkedListNode<LT> *pre = this->head;

					while (ptr->next != nullptr) {
						pre = ptr;
						ptr = ptr->next;
					}
					delete pre->next;
					this->current = pre;
					this->no--;
				}
			}
		}
		void remove(LinkedListNode<LT> *p) {
			if (this->head != nullptr) {
				if (p == this->head) {
					this->remove_first();
				} else {
					LinkedListNode<LT> *ptr = this->head;
					while (ptr->next != p) {
						ptr = ptr->next;
						if (ptr == nullptr) {
							return;
						}
					}
					ptr->next = *p->next;

				}
			}
		}
		void remove(LT p) {
			if (this->head != nullptr) {
				if (p == this->head) {
					this->remove_first();
				} else {
					LinkedListNode<LT> *ptr = this->head;
					while (ptr->next->data != p) {
						ptr = ptr->next;
						if (ptr == nullptr) {
							return;
						}
					}
					ptr->next = *p->next;

				}
			}
		}
		void remove_current_node() {
			this->remove(this->current);
		}
		void clear() {
			while (this->head != nullptr) {
				this->remove_first();
			}
			this->current = nullptr;
			this->no = 0;
		}
		bool next() {
			if (this->current != nullptr || this->current->next != nullptr) {
				return false;
			} 
			this->current = this->*current->next;
			return true;
		}
		void print_current_node() {
			if (this->current != nullptr) {
				cout << "着目ノードはありません" << endl;
			} else {
				print(this->current->data);
			}
		}
		void print() {
			LinkedListNode<LT> ptr = this->head;
			
			while (ptr != nullptr) {
				cout << ptr->data << endl;
				ptr = ptr->next;
			}
		}
	};
}

#endif