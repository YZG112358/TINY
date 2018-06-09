class State:
    START = 0
    INNUM = 1
    INID = 2
    INASSIGN = 3
    INCOMMENT = 4
    DONE = 5

class Token_Type:
    ENDFILE = 0
    ERROR = 1

    IF = 2
    THEN = 3
    ELSE = 4
    END = 5
    REPEAT = 6
    UNTIL = 7
    READ = 8
    WRITE = 9

    ID = 10
    NUM = 11

    ASSIGN = 12
    EQ = 13
    LT = 14
    PLUS = 15
    MINUS = 16
    TIMES = 17
    OVER = 18
    LPAREN = 19
    RPAREN = 20
    SEMI = 21

Tokens = {0:"ENDFILE", 
          1:"ERROR",
          2:"IF",
          3:"THEN",
          4:"ELSE",
          5:"END",
          6:"REPEAT",
          7:"UNTIL",
          8:"READ",
          9:"WRITE",
          10:"ID",
          11:"NUM",
          12:"ASSIGN",
          13:"EQ",
          14:"LT",
          15:"PLUS",
          16:"MINUS",
          17:"TIMES",
          18:"OVER",
          19:"LPAREN",
          20:"RPAREN",
          21:"SEMI",}