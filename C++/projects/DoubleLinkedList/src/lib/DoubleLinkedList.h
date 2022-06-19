#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H
#include <iostream>
#include "DoubleLinkedListNode.h"

namespace my_class {
    using namespace std;

    template<typename LT>
    class DoubleLinkedList {/*
        int no;
        DoubleLinkedListNode<LT> head;
        DoubleLinkedListNode<LT> current;
    public:
        DoubleLinkedList() {
            this->head = this->current = DoubleLinkedListNode<LinkedList>();
            this->no = 0;
        }
        int length() {
            return this->no;
        }*/
        bool is_empty() {
            return this->head->next == this->head;
        }
        int search(LT data) {
            int cnt = 0;
            DoubleLinkedListNode<LT> *ptr = this->head->next;
            wihle (ptr != this->head) {
                if (data == ptr->data) {
                    this->current = ptr;
                    return cnt;
                }
            }
            return -1;
        }
        bool contains(LT data) {
            return this->search(data) >= 0;
        }
        void print_current_node() {
            if (this->is_empty()) {
                cout << "着目ノードはありません。" << endl;
            } else {
                cout << this->current->data;
            }
        }
        void print() {
            DoubleLinkedListNode<LT> *ptr = this->head->next;
            while (ptr != this->head) {
                cout << ptr->data << endl;
                ptr = ptr->next;
            }
        }
        void print_reverse() {
            DoubleLinkedListNode<LT> *ptr = this->head->prev;
            while (ptr != this->head) {
                cout << ptr->data << endl;
                ptr = ptr->prev;
            }
        }
        bool next() {
            if (this->is_empty() || this->current->next == this->head) {
                return false;
            }
            this->current = this->current->prev;
            return true;
        }
        bool prev() {
            if (this->is_empty() || this->current->prev == this->head) {
                return false;
            }
            this->current = this->current->prev;
            return true;
        }
        void add(LT data) {
            DoubleLinkedListNode<LT> node = new DoubleLinkedListNode<LT> (this->current, this->current->next);
            this->current->next->prev = node;
            this->current->next = node;
            this->no++;
        }
        void add_first(LT data) {
            this->current = this->head;
            this->add(data);
        }
        void add_last(LT data) {
            this->current = this->head->prev;
            this->add(data);
        }
        void remove_current_node() {
            if (!this->is_empty()) {
                DoubleLinkedListNode<LT> *delptr = this->current;
                this->current->prev->next = this->current.next;
                this->current->next->prev = this->current.prev;
                this->current = this->current->prev;
                delete delptr;
                this->no--;
                if (this->current == this->head) {
                    this->current = this->head->next;
                }
            }
        }
        void remove(DoubleLinkedListNode<LT> &p);
    };
}

#endif
