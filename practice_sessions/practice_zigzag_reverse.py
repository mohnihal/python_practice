"""Program to decode string written in zig zag format in a k rows.
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows)"""

class Solution:
    def convert(self,zzs,numRows):
        encoded_word_list = [0]*len(zzs)
        hop_length = (numRows-1)*2
        start_index = 0
        row_number = 0
        while start_index < len(zzs):
            hop_index = row_number
            while hop_index < len(zzs):
                encoded_word_list[hop_index] = zzs[start_index]
                hop_index+=hop_length
                start_index+=1
            row_number+=1
            if row_number == numRows-1:
                hop_length = (numRows-1)*2
            else:
                hop_length-=2
        return ''.join(encoded_word_list)


sol=Solution()
print (sol.convert("PAHNAPLSIIGYIR",3))