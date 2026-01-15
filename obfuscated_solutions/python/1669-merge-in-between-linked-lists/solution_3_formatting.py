class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def find_tail(current: ListNode) -> ListNode:

            if current.next is None:

                return current

            return find_tail(current.next)

        def merge(index, start, end):

            # Set start to node a - 1

            if index   =    =   a - 1:

                start   =   end 

            # Base case

            if index   =    =   b:

                # Connect the start node to list2

                start.next   =   list2

                # Set the tail of list2 to end.next

                tail_of_list2   =   find_tail(list2)

                tail_of_list2.next   =   end.next

                end.next   =   None

                return list1

            return merge(index  +  1, start, end.next)

        # Return the merge function with 

        # index   =   0, start   =   none, and end   =   list1

        return merge(0, None, list1)