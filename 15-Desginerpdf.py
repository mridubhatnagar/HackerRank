"""
When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

Input Format

The first line contains  space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z]. 
The second line contains a single word, consisting of lowercase English alphabetic letters.

Constraints

, where  is an English lowercase letter.
Word contains no more than  letters.
Output Format

Print a single integer denoting the area in  of highlighted rectangle when the given word is selected. Do not print units of measure.

Sample Input 0

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
Sample Output 0

9
Explanation 0

We are highlighting the word abc:

Letter heights are ,  and . The tallest letter, b, is  high. The selection area for this word is .

Note: Recall that the width of each character is .

Sample Input 1

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
Sample Output 1

28
Explanation 1

The tallest letter in  is  at . The selection area for this word is .
"""
import sys

def designerPdfViewer(h, word):
    # Complete this function
    L = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' , 'o', 'p', 'q', 'r', 's', 't' , 'u', 'v', 'w', 'x', 'y','z']
    L2 = []
    for letter in word:
    	if letter in L:
    		int_val = L.index(letter)
    		#print(int_val)
    		letter_height = h[int_val]
    		L2.append(letter_height)
    height = max(L2)
    width = len(word)
    result = height * width

    return result


if __name__ == "__main__":
	
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)


