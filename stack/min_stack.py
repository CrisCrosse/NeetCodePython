class MinStack:
    class StackElement:
        def __init__(self, previous_min_element_index: int, val: int):
            self.val = val
            self.previous_min_element_index = previous_min_element_index

    def __init__(self):
        self.my_list_stack = []
        self.current_min_val = 0
        self.current_min_element_index = 0

    def push(self, val: int) -> None:
        print(f"pushing  {val} onto stack")
        if len(self.my_list_stack) == 0:
            self.current_min_val = val
            self.my_list_stack.append(self.StackElement(0, val))
        else:
            index_to_push_onto = len(self.my_list_stack)
            print(
                f"the current min value on the stack is {self.current_min_val} at index {self.current_min_element_index}")
            self.my_list_stack.append(self.StackElement(self.current_min_element_index, val))

            # what should I do where val == current_min_val? do nothing?
            if val < self.current_min_val:
                print(f"the new min value on the stack is {val} at index {index_to_push_onto}")
                self.current_min_val = val
                self.current_min_element_index = index_to_push_onto

    def pop(self) -> None:
        top_stack_element = self.my_list_stack[-1]
        current_stack = [item.val for item in self.my_list_stack]
        print(f"current stack {current_stack}")
        print(
            f"top_stack_element: previous_min_index {top_stack_element.previous_min_element_index}, val: {top_stack_element.val}")
        if top_stack_element.val == self.current_min_val:
            previous_min_index = top_stack_element.previous_min_element_index
            self.current_min_val = self.my_list_stack[previous_min_index].val
            self.current_min_element_index = previous_min_index
            print(
                f"the popped element was the min on stack the new min val is {self.my_list_stack[previous_min_index].val} at index {previous_min_index}")

        self.my_list_stack.pop()

    def top(self) -> int:
        top_stack_element = self.my_list_stack[-1]
        return top_stack_element.val

    def getMin(self) -> int:
        return self.current_min_val

# These should all be O(1) time complexity because we are just assigning indexes or accessing indexes, we never sort or search the list


class TwoStacks:
    class MinStack:
        def __init__(self):
            self.stack = []
            self.minStack = []


        # this is essentially what I did but this is much cleaner
        # we have a stack with the element values
        # and another with the minimum up to that point
        def push(self, val: int) -> None:
            self.stack.append(val)
            # get the minimum between val and the previous minimum unless this is the first element then just add val
            val = min(val, self.minStack[-1] if self.minStack else val)
            # our min Stack records the minimum value we saw up to that point in time
            self.minStack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.minStack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.minStack[-1]


#         I don't quite understand this one but it offers no increase in performance versus the above
class MinStackOneStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min