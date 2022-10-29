class Questions:
    def __init__(self):
        self.question1 = '''Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
                            
                    Example
                
                    x = 1
                    y = 1
                    z = 2
                    n = 3
                    
                    All permutations of [i,j,k] are:
                    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]</br>
                
                    Print an array of the elements that do not sum to n=3.
                    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]</br>
                
                    Input Format
                
                    Four integers x,y,z and n, each on a separate line.
                
                    Constraints
                
                    Print the list in lexicographic increasing order.
                
                    Sample Input 0
                    
                    1
                    1
                    1
                    2
                    Sample Output 0
                    
                    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
                    Explanation 0
                    
                    Each variable  and  will have values of  or . All permutations of lists in the form .
                    Remove all arrays that sum to  to leave only the valid permutations.
                    
                    Sample Input 1
                    
                    2
                    2
                    2
                    2
                    Sample Output 1
                    
                    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]] '''
        
        self.question2 = '''In Python, a string can be split on a delimiter.

                    Example:
                    
                    >>> a = "this is a string"
                    >>> a = a.split(" ") # a is converted to a list of strings.
                    >>> print a
                    ['this', 'is', 'a', 'string']
                    Joining a string is simple:
                    
                    >>> a = "-".join(a)
                    >>> print a
                    this-is-a-string
                    Task
                    You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
                    
                    Function Description
                    
                    Complete the split_and_join function in the editor below.
                    
                    split_and_join has the following parameters:
                    
                    string line: a string of space-separated words
                    Returns
                    
                    string: the resulting string<
                    Input Format
                    The one line contains a string consisting of space separated words.
                    
                    Sample Input
                    
                    this is a string 
                    Sample Output
                    
                    this-is-a-string'''
        
        self.question3 = '''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
                    alison heck = Alison Heck
                    
                    Given a full name, your task is to capitalize the name appropriately.
                    
                    Input Format
                    
                    A single line of input containing the full name, S.
                    
                    Constraints
                    1. length od S must be in between 100 and 1000 (both exclusive).
                    2. The string consists of alphanumeric characters and spaces.
                    Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
                
                    Output Format
                    
                    Print the capitalized string, S.
                    
                    Sample Input
                    
                    chris alan
                    Sample Output
                    
                    Chris Alan'''