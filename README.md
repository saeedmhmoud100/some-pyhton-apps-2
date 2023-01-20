# some-pyhton-programs-2

### 30. Develop two functions to encrypt and decrypt a given text in Caesar cypher. Given a text to encrypt, alphabetic characters are all shifted by one and spaces are removed. To decrypt the text, the opposite process is followed but spaces are not recovered. Notice that 'z' turns to 'a'. And all encryption is done on small letters version of the message. Sample input: I love Python Programming. My home is 3 Zewail Street, Dokki. Encryption: jmpwfqzuipoqsphbnnjoh. nzipnfjt3afxbjmtusffu,epllj. Decryption: ilovepythonprogramming. myhomeis3zewailstreetdokki. You might want to use the built-in function ord, which converts a character to a numeric code, and chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical order, so for example: >>> ord('c') - ord('a') 2

### 31. Develop a Python function that checks if two lists have the same elements, even if not in order. Do not use built in functions. Sample input: [1, 2, 3, 4, 5, 6, 7, 8] and [8, 7, 6, 5, 4, 3, 2, 1] Output: Lists are equal = True Sample input: [1, 2, 3, 4, 44, 6, 7, 8] and [8, 7, 6, 5, 4, 3, 2, 1] Output: Lists are equal = False

### 32. Repeat the same exercise (37) using built-in functions.

### 33. Write a Python function that checks that a given list is sorted in ascending order, descendant order or not sorted. It should return 1 for ascending and -1 for descending and 0 for not sorted. Sample inputs: [1, 2, 3, 4, 5, 6, 7, 8] [8, 7, 6, 5, 4, 3, 2, 1] [4, 5, 6, 3, 2, 9] Outputs: 1 -1` 0

### 34. ***Number scrabble*** is played with the list of numbers between 1 and 9. Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If out of the number a player has picked so far, three numbers add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15, the game is a draw. Example: (1) 4 (2) 7 (1) 3 (2) 8 (1) 5 (2) 6 (1) 1 (2) 2 => 2 wins ( 7 + 6 + 2 = 15)

### 35. ***Subtract a square.*** This is a two-player mathematical game of strategy. It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins. Example of this game is at: http://delphiforfun.org/Programs/SubtractingSquares.htm Hint: Modify the Nim game written in the lecture and available in course page to do this .

### 36. Write a Python program that takes two file names and copies the first file to the second one.

### 37. Write a Python program that takes a file name, opens the file, reads it and prints its content in reverse order.

### 38. Write a Python program that opens the file and counts the number of words, lines and characters in it.

### 39. Create a dictionary with 10 or more Egyptian cities. City name is the key, while the value to store population. Or it can be the distance from Cairo. Then the program that allows the user to choose from three functions; Listing all cities and their information, query the dictionary for a city or add a new city.

### 40. Write a Python function that loads the most common English words from a file (See https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt) into a dictionary where word is the key and value is the number of letters in the word (length). Then write another functions that allows the user to display all words of certain length, for example can display English words of three letters only, four letters only, etc.
