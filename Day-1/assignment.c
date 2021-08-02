#include<stdio.h>
#include<stdlib.h>//for maLLOC
struct node
{
    int data;
    struct node* nxt;
}*head=0,*temp,*newnode,*next;

int count=0,cnt =0;

void Display()
{
    count=0;
    temp=head;
    while(temp!=0)
    {
        printf("%d->",temp->data);
        temp=temp->nxt;
        count++;
    }
    printf("NULL\nTHE LENGTH OF THE LINKED LIST %d",count);
}

void insert_at_front()
{
    newnode=(struct node*)malloc(sizeof(struct node));
//   // newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data==>");
    scanf("%d",&newnode->data);
    newnode->nxt=head;
    head=newnode;
}
void insert_after_specified_position()
{
    int pos,i;
    printf("Enter the position that you want to insert the data after==>");
    scanf("%d",&pos);
    count=0;
    temp=head;
    while(temp!=0)
    {
        temp=temp->nxt;
        count++;
    }
    if(pos>count)
    {
        printf("Please Enter the correct position!!!");
    }
    else if(pos==0)
    {
        insert_at_front();
    }
    else
    {
      temp=head;
       for(i=0;i<pos-1;i++)
       {
           temp=temp->nxt;
       }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data==>");
    scanf("%d",&newnode->data);
    newnode->nxt=0;
    newnode->nxt=temp->nxt;
      temp->nxt=newnode;
    }
}
void insert_at_end()
{
    temp=head;
    while(temp!=0)
    {
        temp=temp->nxt;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter the data==>");
    scanf("%d",&newnode->data);
    temp=newnode;
    newnode->nxt=NULL;
}

void reverse_linked_list()
{
	temp=NULL;
	next=newnode=head;
	while(next!=0)
	{
		next=next->nxt;
		newnode->nxt=temp;
		temp=newnode;
		newnode=next;
	}
	head=temp;
}
void delete_at_front()
{
	head=head->nxt;
}
void delete_at_end()
{
	temp=head;
    while(temp->nxt!=0)
    {
    	next=temp;
        temp=temp->nxt;
    }
    next->nxt=NULL;
}
void delete_after_specified_position()
{
	int pos,i;
    printf("Enter the position that you want to delete the data after==>");
    scanf("%d",&pos);
	if(pos==0)
    {
        delete_at_front();
    }
    else
    {
      temp=head;
       for(i=0;i<pos-1;i++)
       {
           temp=temp->nxt;
       }
       newnode=temp->nxt;
       temp->nxt=newnode->nxt;
	}
}
int check_circular()
{
    int i=0;
    while(i<count)
    {
        temp = temp->nxt;
        i++;
    }
    if(temp->nxt!=head)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

void make_it_circular()
{
    if(check_circular()==0)
    {
        temp =head;
        while(temp->nxt==0)
        {
            temp = temp->nxt;
        }
        temp->nxt=head;
    }
    else{
        printf("\nIt is Already circular!!");
    }
}


int main()
{
   int choice,c=1;
   while(c==1)
   {
       newnode=(struct node*)malloc(sizeof(struct node));
       printf("Enter the data==>");
       scanf("%d",&newnode->data);
       newnode->nxt=NULL;
       if(head==0)
       {
           head=temp=newnode;
           cnt++;
       }
       else
        {
            temp->nxt=newnode;
            temp=newnode;
            cnt++;
        }
        printf("Do you Want to continue press one and Enter =");
        scanf("%d",&c);
   }
   printf("\nChecking wheather the linked list is circular or not :");
   if(check_circular()==0)
   {
       printf("\nNo it is not circular!!");
   }
   c=1;
   while(c==1)
   {
       printf("\nEnter the choice\n1.INSERT AT FRONT,\n2.INSERT AT END,\n3.INSERT AT AFTER SPECIFIED POSITION\n4.DISPLAY\n5.REVERSING\n6.Delete at Front\n7.Delete at End\n8.Delete after specified position\n9.Change it circular if not\n10.check circular\n===>");
       scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                insert_at_front();
                break;
            case 2:
                insert_at_end();
                break;
            case 3:
                insert_after_specified_position();
                break;
            case 4:
                Display();
                break;

            case 5:
                reverse_linked_list();
                break;
            case 6:
            	delete_at_front();
            	break;
            case 7:
            	delete_at_end();
            	break;
            case 8:
            	delete_after_specified_position();
            	break;
            case 9:
                make_it_circular();
                printf("IT Becomes circular so please don't call display any fun other than 10!!\nWarning\n");
                break;
            case 10:
                if(check_circular()==0)
                {
                    printf("\nNot cicular\n");
                }
                if(check_circular()==1)
                {
                    printf("\nYes it is circular\n");
                }
                break;
            default:
                printf("Enter the valid==\n");
        }
        printf("\nEnter 1 and press enter for other operations==");
        scanf("%d",&c);

   }
   return 0;
}
