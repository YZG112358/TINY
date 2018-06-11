from src.scan import Scanner


class Parser:
"""
This class uses Recursive-Descent Parser for
the EBNF style grammar as follows:

program -> stmt-sequence
stmt-sequence -> if-stmt { ; statement }
statement -> if-stmt | repeat-stmt | assign-stmt | read-stmt | write-stmt
if-stmt -> if exp then stmt-sequence [ else stmt-sequence ]
repeat-stmt -> repeat stmt-sequence until exp
assign-stmt -> identifier := exp
read-stmt -> read identifier
write-stmt -> write exp
exp -> simple-exp [ comparison-op simple-exp ]
comparison-op -> < | =
simple-exp -> term { add term }
addop -> + | -
term -> factor { mulop factor }
mulop -> * | /
factor -> ( exp ) | number | identifier

Ideally A LL(1) parser should be implemented 
with the LL parsing table. This requires LR 
reduction and LR factoring to solve the Left
Recursion problem. Thus it's much easier to
do it just in Recursive-Descent way.
"""
	def __init__(self):
		pass


	def match(self):
		pass






























