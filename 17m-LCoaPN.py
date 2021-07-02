class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        options = []
        combos = []
        temp = ''
        candidate = []
        if not digits: 
            return combos
        
        numletter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        for i in range(0, len(digits)):
            options.append(numletter[int(digits[i])-2])
        
        for item in options:
            tmep = temp + str(len(item)-1)
            candidate.append('0')
        
        
        while int(''.join(candidate)) < int(temp):
            combi = ''
            for i in range(len(options)):
                combi = combi + str(options[i][int(candidate[i])])

            combos.append(combi)
            
            for i in reversed(range(len(options))):
                if int(candidate[i]) < len(options[i])-1: 
                    candidate[i] = str(int(candidate[i])+1)
                    if i < len(options)-1:
                        for j in reversed(range(i+1,len(options))):
                            if int(candidate[j]) >= len(options[j])-1: 
                                candidate[j] = '0'
                    break
                    
        combi = ''
        for i in range(len(options)):
            combi = combi + str(options[i][int(temp[i])])

        combos.append(combi) 
        
        return combos
        