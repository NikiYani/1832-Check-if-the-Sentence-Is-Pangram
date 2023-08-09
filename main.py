class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_res = set(sentence)
        print(set_res)
        if len(set_res) == 26 :
            return True
        else :
            return False