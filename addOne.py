#add one to linked list 
#e.x 4->5->6 +1 becomes 4->5->7
class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        if not head:
            return Node(1)
        
        head=self.reverse(head)
        
        #9->9 +1 0->0->1
        curr= head
        carry =0 
        curr.data+=1
        prev=None
        while curr:
            currSum = carry+ curr.data
            digit =currSum %10 
            carry = currSum//10
            curr.data= digit
            prev=curr
            curr=curr.next
        if carry==1:
            prev.next=Node(carry)
            
        head =self.reverse(head)
        
        return head
    
    def reverse(self,head): 
        prev=None
        curr=head
        while curr:
            nextN =curr.next 
            curr.next=prev
            prev,curr=curr,nextN
        return prev
        
            
