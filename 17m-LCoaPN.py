class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        options = []
        combos = []
        crypto = ''
        joseph = []
        if not digits: 
            return combos
        
        numletter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        for i in range(0, len(digits)):
            options.append(numletter[int(digits[i])-2])
        
        for item in options:
            crypto = crypto + str(len(item)-1)
            joseph.append('0')
        
        
        while int(''.join(joseph)) < int(crypto):
            combi = ''
            for i in range(len(options)):
                combi = combi + str(options[i][int(joseph[i])])

            combos.append(combi)
            
            for i in reversed(range(len(options))):
                if int(joseph[i]) < len(options[i])-1: 
                    joseph[i] = str(int(joseph[i])+1)
                    if i < len(options)-1:
                        for j in reversed(range(i+1,len(options))):
                            if int(joseph[j]) >= len(options[j])-1: 
                                joseph[j] = '0'
                    break
                    
        combi = ''
        for i in range(len(options)):
            combi = combi + str(options[i][int(crypto[i])])

        combos.append(combi) 
        
        return combos
        