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