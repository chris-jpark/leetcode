class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        # numerals = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        numerals = [[1000, "M"], [500, "D"], [100, "C"], [50, "L"], [10, "X"], [5, "V"], [1, "I"]]

        for letter in range(len(numerals)):

            if num >= numerals[letter][0]:
                if str(num)[0] == '9':
                    roman += numerals[letter+1][1] + numerals[letter-1][1]
                    num = num % (numerals[letter-1][0] - numerals[letter+1][0])
                elif str(num)[0] == '4':
                    roman += numerals[letter][1] + numerals[letter-1][1]
                    num = num % (numerals[letter-1][0] - numerals[letter][0])

                elif num // numerals[letter][0]<= 3 and num // numerals[letter][0] > 0:
                    for i in range(num // numerals[letter][0]):
                        roman += numerals[letter][1]
                    num = num % numerals[letter][0]

            print(num, roman)

        return roman


print(Solution().intToRoman(1))
