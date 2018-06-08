from globals import State
from globals import Token_Type

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

    def get_next_char():
        if (self.line_pos < self.line_size):
            self.line_pos += 1
            return self.line[self.line_pos]
        else:
            #return empty string for eof
            self.eof_flag = True
            return ''

    def unget_char():
        if (not self.eof_flag):
            self.line_pos -= 1

    def getToken(self):
        state = State().START
        self.c = get_next_char()
        self.go_on = True
        while (self.current_state != State().DONE && self.go_on):
            self.state_options[state]()
            





        

    def start(self):
        print("start")
        if self.c == ' ' || self.c == '\n' || self.c == '\t':
            pass
        elif self.c.isdigit():
            self.current_state = State().INNUM
        elif self.c.isalpha():
            self.current_state = State().INID
        elif self.c == ':':
            self.current_state = State().INASSIGN
        elif: self.c == '{':
            self.current_state = State().INCOMMENT
        else:
            self.current_state = State().DONE
            if self.c == '':
                self.current_token_type = Token_Type().ENDFILE
                return
            elif self.c not in self.symbol_map:
                self.current_token_type = Token_Type().ERROR
                return
            else:
                self.current_token_type = self.symbol_map[self.c]
                return


    def innum(self):
        print("innum")
        if not self.c.isdigit():
            
        
    def inid(self):
        print("inid")
        
    def inassign(self):
        print("inassign")
        
    def incomment(self):
        print("incomment")
        
    def done(self):
        print("done")
        


if __name__ == '__main__':
    scanner = Scanner()
    scanner.get_str("This is a sentence")
    scanner.getToken()
