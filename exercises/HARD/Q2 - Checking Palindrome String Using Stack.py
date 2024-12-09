class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, element):
        self.data.append(element)

    def peek_top(self):
        if self.size() == 0:
            return "Stack Is Empty"
        return self.data[-1]

    def pop(self):
        if self.size() == 0:
            return "Stack Is Empty"
        return self.data.pop()




def is_palindrome(word):
    s = Stack()
    # Inserting the input word into stack
    for l in word:
        s.push(l)
        
    # Poping each word from stack and comparing it with the word letter by letter
    for l in word:
        last = s.pop()
        if (l != last):
            return False        
    return True

        