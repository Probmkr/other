#ifndef DOUBLELINKEDLISTNODE_H
#define DOUBLELINKEDLISTNODE_H

namespace my_class {
    template<typename DLLVT>
    class DoubleLinkedListNode {
    public:
        DLLVT data;
        DoubleLinkedListNode<DLLVT> *pref;
        DoubleLinkedListNode<DLLVT> *next;

        DoubleLinkedListNode(DLLVT data, DoubleLinkedListNode<DLLVT> *prev = nullptr, DoubleLinkedListNode<DLLVT> *next = nullptr) {
            this->data = data;
            this->prev = prev ? prev : this;
            this->next = next ? next : this;
        }
    }
}

#endif
