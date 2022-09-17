# https://leetcode.com/problems/goal-parser-interpretation/
class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        
        while command:
            if command[0] == "G":
                res += "G"
                command = command[1:]
            elif command[:4] == "(al)":
                res += "al"
                command = command[4:]
            elif command[:2] == "()":
                res += "o"
                command = command[2:]
        
        return res
