class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        counter = 0
        howmany = 0
        strsedit = strs
        while counter == 0:
            try:
                tester = strsedit[0][0]
            except IndexError:
                return strs[0]
            for i in range(0, len(strsedit)): 
                try:
                    if strsedit[i][0] != tester:
                        counter += 1
                except IndexError:
                    return strs[0][0:howmany]
            strsedit = [item[1:] for item in strsedit]
            howmany += 1
        if howmany == 0:
            return ""
        else:
            return strs[0][0:howmany-1]
            