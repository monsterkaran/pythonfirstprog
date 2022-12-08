class solution:
    def isvalid(self, s: str) -> bool:
        stack=[]
        dict={
            "}" : "{",
            "]": "[",
            ")": "("
        }

        for char in s :
            if char in dict.value():
                stack.append(char)
            elif char in dict.keys():
                if( stack == [] or dict[char]!=stack.pop())
                    return False
                return stack == []