# **Scrabble Calculator**
The following project is my solution to the [Programming Challanges Guild](https://habitica.com/groups/guild/649e9002-73e9-4023-a169-47e203fc953d) October Challenge 2019. The program is written in Python and runs in the terminal.

The program not only calculates the points of a word, but also checks if the word actually exists using the [Yandex Dictionary API](https://tech.yandex.com/dictionary/). I have hidden my own API-key, but if you want to try it out you can follow the provided link to get your own key for free.

There is also an option to save calculated words locally to a json-file. This file, if it exists, will automatically load at the start of the program. If the user tries to look up a word already in the dictionary, the value of that key within the dictionary will be given again instead of re-computing the points. An option to print all the words with its corresponding value in the dictionary is present as well.
