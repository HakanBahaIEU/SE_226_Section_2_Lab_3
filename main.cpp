#include <iostream>
#include <new>

using namespace std;

class Node 
{
    public:
    int data;
    Node *next;
    Node(int x, Node *n) {data = x; next = n;}
};

class queue{
    Node * head;
    Node * p;

    int enqueue(Node* head,int data)
    {
        Node *newNode = new Node(data,nullptr);
        newNode->next = head;
        return 0;
    }

    int top(){
        int ctrl = 0;
        p=head;
        for(p=head; p!=nullptr; p=p->next){
            if(p->data > ctrl) ctrl = p->data;
        }
        cout << ctrl;
        return 0;
    }

    int dequeue(){
        Node * pp;
        for(p=head; p!=nullptr; p=p->next){
            pp = p->next;
            if(pp -> next == nullptr){
                p -> next = nullptr;
            }
        }
        delete pp;
        return 0;
    }

    
    bool isEmpty(){
        if(head != nullptr){return true;}
        return false;
    }

    int size(){
        int count = 0;
        if(isEmpty == false){return count;}
        for(p=head; p!=nullptr; p=p->next){
            count++;
        }
        return count;
    }
};
