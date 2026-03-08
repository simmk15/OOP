class reverse:
    def __init__(self,s=""):
        self.__s=s
    def setString(self,word):
        self.__s=word
    def reverseString(self):
        rev=" "
        for i in range(len(self.__s)-1,-1,-1):
            rev+=self.__s[i]
        return rev
word=input("Enter a word: ")
obj=reverse()
obj.setString(word)
print("Reversed string:",obj.reverseString())