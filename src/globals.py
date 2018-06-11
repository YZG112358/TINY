from enum import Enum

class Token_Type(Enum):
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

Tokens = {Token_Type.ENDFILE:"ENDFILE", 
          Token_Type.ERROR:"ERROR",
          Token_Type.IF:"IF",
          Token_Type.THEN:"THEN",
          Token_Type.ELSE:"ELSE",
          Token_Type.END:"END",
          Token_Type.REPEAT:"REPEAT",
          Token_Type.UNTIL:"UNTIL",
          Token_Type.READ:"READ",
          Token_Type.WRITE:"WRITE",
          Token_Type.ID:"ID",
          Token_Type.NUM:"NUM",
          Token_Type.ASSIGN:"ASSIGN",
          Token_Type.EQ:"EQ",
          Token_Type.LT:"LT",
          Token_Type.PLUS:"PLUS",
          Token_Type.MINUS:"MINUS",
          Token_Type.TIMES:"TIMES",
          Token_Type.OVER:"OVER",
          Token_Type.LPAREN:"LPAREN",
          Token_Type.RPAREN:"RPAREN",
          Token_Type.SEMI:"SEMI",}

class Nodekind(Enum):
    StmtK = 0
    ExpK = 1

class StmtKind(Enum):
    IfK = 0
    RepeatK = 1
    AssignK = 2
    ReadK = 3
    WriteK = 4

class ExpKind(Enum):
    OpK = 0
    ConstK = 1
    IdK = 2

class ExpType(Enum):
    Void = 0
    Integer = 1
    Boolean = 2

class State(Enum):
    START = 0
    INNUM = 1
    INID = 2
    INASSIGN = 3
    INCOMMENT = 4
    DONE = 5

#TODO 
#add property for each member to enforce enum
class Node:
    def __init__(self):
        self._children = []
        self.sibling = None
        self.lineno = 0
        self.nodekind = None
        self.stmtkind = None
        self.expkind = None
        self.tokentype = None
        self.name = None
        self.value = None
        self.type = None
    
    def add_child(self, node):
        self._children.append(node)

    @property
    def child(self):
        return self._children