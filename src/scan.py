from src.globals import State
from src.globals import Token_Type
from src.globals import Tokens

DEBUG = False

class Scanner:
    def __init__(self):
        self.state = State()
        self.token_type = Token_Type()
        self.line_pos = 0
        self.current_state = 0
        self.current_token_type = 0
        self.eof_flag = False
        self.state_options = {
            State().START: self.start,
            State().INNUM: self.innum,
            State().INID: self.inid,
            State().INASSIGN: self.inassign,
            State().INCOMMENT: self.incomment,
            State().DONE: self.done,
        }
        self.symbol_map = {
            '=': Token_Type().EQ,
            '<': Token_Type().LT,
            '+': Token_Type().PLUS,
            '-': Token_Type().MINUS,
            '*': Token_Type().TIMES,
            '/': Token_Type().OVER,
            '(': Token_Type().LPAREN,
            ')': Token_Type().RPAREN,
            ';': Token_Type().SEMI,
        }

    def get_str(self, input_string):
        self.line = input_string
        self.line_size = len(input_string)

    def get_next_char(self):
        if (self.line_pos < self.line_size):
            self.line_pos += 1
            return self.line[self.line_pos-1]
        else:
            #return empty string for eof
            self.eof_flag = True
            return ''

    def unget_char(self):
        if (not self.eof_flag):
            self.line_pos -= 1

    def lookupReserved(self, word):
        if DEBUG:
            print(word)
        if word.upper() == "IF":
            self.current_token_type = Token_Type().IF
        elif word.upper() == "THEN":
            self.current_token_type = Token_Type().THEN
        elif word.upper() == "ELSE":
            self.current_token_type = Token_Type().ELSE
        elif word.upper() == "END":
            self.current_token_type = Token_Type().END
        elif word.upper() == "REPEAT":
            self.current_token_type = Token_Type().REPEAT
        elif word.upper() == "UNTIL":
            self.current_token_type = Token_Type().UNTIL
        elif word.upper() == "READ":
            self.current_token_type = Token_Type().READ
        elif word.upper() == "WRITE":
            self.current_token_type = Token_Type().WRITE


    def getToken(self):
        self.current_state = State().START
        tokenString = ""
        while (self.current_state != State().DONE):
            self.c = self.get_next_char()
            # Save the character in default
            self.save = True
            self.state_options[self.current_state ]()
            
            if (self.save):
                tokenString += self.c
            if (self.current_state == State().DONE and self.current_token_type == Token_Type().ID):
                self.lookupReserved(tokenString)

            if DEBUG:
                print("char: " + self.c)
                print("state: " + str(self.current_state))
                print("token_type: " + Tokens[self.current_token_type])
                print("line_pos: " + str(self.line_pos))
                input("")

            

        print("tokenString: {}, tokenType: {}".format(tokenString, Tokens[self.current_token_type]))

        return self.current_token_type
        
    def start(self):
        if DEBUG:
            print("start")
        if self.c == ' ' or self.c == '\n' or self.c == '\t':
            self.save = False
        elif self.c.isdigit():
            self.current_state = State().INNUM
        elif self.c.isalpha():
            self.current_state = State().INID
        elif self.c == ':':
            self.current_state = State().INASSIGN
        elif self.c == '{':
            self.current_state = State().INCOMMENT
            self.save = False
        else:
            self.current_state = State().DONE
            if self.c == '':
                self.current_token_type = Token_Type().ENDFILE
                self.save = False
                return
            elif self.c not in self.symbol_map:
                self.current_token_type = Token_Type().ERROR
                return
            else:
                self.current_token_type = self.symbol_map[self.c]
                return


    def innum(self):
        if DEBUG:
            print("innum")
        if not self.c.isdigit():
            self.current_state = State().DONE
            self.save = False
            self.current_token_type = Token_Type().NUM
            self.unget_char()

        
    def inid(self):
        if DEBUG:
            print("inid")
        if not self.c.isalpha():
            self.current_state = State().DONE
            self.save = False
            self.current_token_type = Token_Type().ID
            self.unget_char()

        
    def inassign(self):
        if DEBUG:
            print("inassign")
        self.current_state = State().DONE
        if self.c == '=':
            self.current_token_type = Token_Type().ASSIGN
        else:
            self.save = False
            self.current_token_type = Token_Type().ERROR
            self.unget_char()
        

    def incomment(self):
        if DEBUG:
            print("incomment")
        self.save = False
        if self.eof_flag:
            self.current_state = State().DONE
            self.current_token_type = Token_Type().ENDFILE
        elif self.c == '}':
            self.current_state = State().START

        
    def done(self):
        print("done")
        


if __name__ == '__main__':
    if __debug__:
        DEBUG = True
        print('Debug ON')
    else:
        print('Debug OFF')
    scanner = Scanner()
    program = "read x; {input an integer }\n"
    program += "if 0 < x then { don't compute if x <= 0 }\n"
    program += "\tfact := 1;\n"
    program += "\trepeat\n"
    program += "\t\tfact := fact * x;\n"
    program += "\t\tx := x - 1\n"
    program += "\tuntil x = 0;\n"
    program += "\t write fact { output factorial of x }\n"
    program += "end"
    scanner.get_str(program)
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()
    scanner.getToken()