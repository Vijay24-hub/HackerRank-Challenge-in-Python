"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line.
The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Output Format

On a new line for each query, print Not found if the name has no corresponding entry in the phone book;
otherwise, print the full  and  in the format name=phoneNumber.
"""

n = int(input())
new_dict = {}
for i in range(n):
    x = input().split()
    new_dict[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in new_dict:
            print(f"{name}={new_dict[name]}")
        else:
            print("Not found")
    except:
        break
