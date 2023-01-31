# Challenge Summary
- Write a function called repeated word that finds the first word to occur more than once in a string
  - Arguments: string
  - Return: string

## Whiteboard Process
![hashtable_repeat_word](python/docs/hashtable_repeated_word/hashtable-repeated-word.png)

## Approach & Efficiency
- Time:  O(n) where n is the number of words in the string - worst case scenario, it will need to loop through each word in the string
- Space: O(n) where n is the number of words in the string - we’re creating a set to hold each word until we find a duplicate. Worst case scenario the set will have to hold every word except the last one

## Link to Code
- [hashtable repeat word](python/code_challenges/hashtable_repeated_word.py)