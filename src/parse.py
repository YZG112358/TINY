from src.scan import Scanner
from src.globals import Node
from src.globals import Nodekind
from src.globals import Token_Type
from src.util import new_stmt_node
from src.util import new_exp_node

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

    def __init__(self, scanner):
        self.scanner = scanner
        self.token = self.scanner.getToken()
        self.Error = False
        if self.token == Token_Type.ENDFILE:
            print("Empty Program")

    def get_next_token(self):
        return self.scanner.getToken()

    def match(self, expected):
        if self.token == expected:
            self.token = self.get_next_token()
        else:
            print("unexpected token -> {}".format(self.token))
            self.Error = True

    def stmt_sequence(self):
        pass





    def statement(self):
        retval = None

        if self.token == Token_Type.IF:
            pass
        elif self.token == Token_Type.REPEAT:
            pass
        elif self.token == Token_Type.ID:
            pass
        elif self.token == Token_Type.READ:
            pass
        elif self.token == Token_Type.WRITE:
            pass
        else:
            print("unexpected token -> {}".format(self.token))
            self.token = self.get_next_token()


    def if_stmt(self):
        t = new_stmt_node(StmtKind.IfK)
        self.match(Token_Type.IF)
        t.add_child(self.exp())
        self.match(Token_Type.THEN)
        t.add_child(self.stmt_sequence())

        if self.token == Token_Type.ELSE:
            self.match(Token_Type.ELSE)
            t.add_child(self.stmt_sequence())

        self.match(Token_Type.END)

        return t


    def repeat_stmt(self):
        t = new_stmt_node(StmtKind.RepeatK)
        self.match(Token_Type.REPEAT)
        t.add_child(self.stmt_sequence())
        self.match(Token_Type.UNTIL)
        t.add_child(self.exp())

        return t


    def assign_stmt(self):
        t = new_stmt_node(StmtKind.AssignK)
        self.match(Token_Type.REPEAT)
        if self.token == Token_Type.ID:
            pass # need to copy token_name to node.name
        self.match(Token_Type.ID)
        self.match(Token_Type.ASSIGN)
        t.add_child(self.exp())

        return t


    def read_stmt(self):
        t = new_stmt_node(StmtKind.ReadK)
        self.match(Token_Type.READ)
        if self.token == Token_Type.ID:
            pass # need to copy token_name to node.name
        self.match(Token_Type.ID)

        return t


    def write_stmt(self):
        t = new_stmt_node(StmtKind.WriteK)
        self.match(Token_Type.WRITE)
        t.add_child(self.exp())

        return t


    def exp(self):
        t = self.simple_exp()
        if self.token == Token_Type.LT or self.token == Token_Type.EQ:
            p = new_exp_node(ExpKind.OpK)
            p.add_child(t)
            p.tokentype = self.token
            t = p
            self.match(self.token)
            t.add_child(self.simple_exp())

        return t


    def simple_exp(self):
        t = self.term()
        while self.token == Token_Type.PLUS or self.token == Token_Type.MINUS:
            p = new_exp_node(ExpKind.OpK)
            p.add_child(t)
            p.tokentype = self.token
            t = p
            self.match(self.token)
            t.add_child(self.term())

        return t


    def term(self):
        t = self.factor()
        while self.token == Token_Type.TIMES or self.token == Token_Type.OVER:
            p = new_exp_node(ExpKind.OpK)
            p.add_child(t)
            p.tokentype = self.token
            t = p
            self.match(self.token)
            t.add_child(self.factor())

        return t


    def factor(self):
        t = None
        if self.token == Token_Type.NUM:
            t = new_exp_node(ExpKind.ConstK)
            #TODO add value to node.value

            self.match(Token_Type.NUM)
        elif self.token == Token_Type.ID:
            t = new_exp_node(ExpKind.IdK)
            #TODO add name to node.name

            self.match(Token_Type.ID)
        elif self.token == Token_Type.LPAREN:
            self.match(Token_Type.LPAREN)
            t = self.exp()
            self.match(Token_Type.RPAREN)
        else:
            print("unexpected token -> {}".format(self.token))
            self.token = self.get_next_token()

        return t


if __name__ == '__main__':
    scanner = Scanner()
    scanner.get_str("")
    parser = Parser(scanner)
    node = Node()
    node.add_child("123")




