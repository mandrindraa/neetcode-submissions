class LinkedList {
private:
    struct Node {
        int val = 0;
        Node *next;
        Node(int v) : val(v), next(nullptr) {}
    };
    Node *head;
    Node *tail;


public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    ~LinkedList() {
        Node *cur = head;
        while (cur) {
            Node *next = cur->next;
            delete cur;
            cur = next;
        }
    }

    int get(int index) {
        Node *cur = head;
        for (int i = 0; cur != nullptr && i < index; i++) {
            cur = cur->next;
        }

        return cur ? cur->val : -1;
    }

    void insertHead(int val) {
        Node *node = new Node(val);
        node->next = head;
        head = node;
        if(tail == nullptr) {
            tail = head;
        }
    }
    
    void insertTail(int val) {
        Node *new_tail = new Node(val);
        if(tail==nullptr) {
            head = tail = new_tail;
            return;
        }
        tail->next = new_tail;
        tail = new_tail;
    }

    bool remove(int index) {
        if (head == nullptr) return false;
        if (index == 0) {
            Node *t = head;
            head = head->next;
            if (head == nullptr) {
                tail = nullptr;
            }
            delete t;
            return true;
        }
        Node *current = head;
        for (int i = 0; i < index-1 && current != nullptr; i++) {
            current = current->next;
        }
        if (current == nullptr || current->next == nullptr) {
            return false;
        }

        Node *t = current->next;
        current->next = current->next->next;
        if (t == tail) {
            tail = current;
        }
        delete t;
        return true;
    }

    vector<int> getValues() {
        vector<int> r;
        Node *current = head;
        while(current != nullptr) {
            r.push_back(current->val);
            current = current->next;
        }
        return r;
    }
};
