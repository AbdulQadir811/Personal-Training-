
#include <iostream>

using namespace std;
class LinkList
{
    public:
    int data;
    LinkList *next;
    LinkList *head;
    LinkList()
    {
        head = NULL;
    }
    void add_node(int my_data)
    {
        LinkList *ptr = new LinkList;
        LinkList *temp = new LinkList;
        
        ptr = head;
        if(head == NULL)
        {
            head= temp;
            head -> data = my_data;
            head -> next = NULL;
        }
        else
        {
             while(ptr->next != NULL)
            {
                ptr = ptr -> next;
            }
            ptr->next = temp;
            temp->data = my_data;
            temp->next = NULL;
        
           }
           
        
    
    }
    void print_linklist()
    {
        LinkList *ptr ;
        ptr = head;
        bool 
        while(ptr != NULL)
        {
            if()
        cout << ptr->data <<endl;
        ptr = ptr->next;
        }
    }
};
int main()
{
    LinkList obj;
    obj.add_node(1);
    obj.add_node(2);
    obj.add_node(3);
    obj.print_linklist();

    return 0;
}
