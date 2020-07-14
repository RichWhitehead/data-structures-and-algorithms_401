# Code Challenge: Class 13 Multi-Bracket-Validation

# Author: Richard Whitehead

# Challenge
Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : `()`
Square Brackets : `[]`
Curly Brackets : `{}`

# Example

Input	                      Output
`{}	`                       `TRUE`
`{}(){}`	                  `TRUE`
`()[[Extra Characters]]`	  `TRUE`
`(){}[[]]`                  `TRUE`
`{}{Code}[Fellows](())`	    `TRUE`
`[({}]`	                    `FALSE`
`(](`	                      `FALSE`
`{(})`                      `FALSE`


# Approach & Efficiency

Input	Output	Why
`{`	FALSE	error unmatched opening { remaining.
`)`	FALSE	error closing ) arrived without corresponding opening.
`[}	FALSE	error closing }. Doesn’t match opening (

# Solution

[Whiteboard](assets/multi_bracket_validation.png)

# Sources
https://www.cs.auckland.ac.nz/compsci105s1c/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf

https://stackoverflow.com/questions/6701853/parentheses-pairing-issue

https://www.geeksforgeeks.org/stack-data-structure-introduction-program/