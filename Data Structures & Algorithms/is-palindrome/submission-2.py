class Solution:
    def isPalindrome(self, s: str) -> bool:
        statement = "";

        for char in s:
            if char.isalnum():
                statement += char;

        statement = statement.lower();
        print(statement);


        for i in range(int(len(statement)/2)):
            if statement[i] != statement[len(statement) - 1 - i]:
                return False;
        return True;


