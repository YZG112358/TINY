from src.scan import Scanner
from src.globals import Token_Type

def test_getToken_id():
    scanner = Scanner()
    scanner.get_str("  abcd  ")
    token = scanner.getToken()
    assert token == Token_Type.ID

def test_getToken_num():
    scanner = Scanner()
    scanner.get_str("  153  ")
    token = scanner.getToken()
    assert token == Token_Type.NUM

def test_getToken_assign():
    scanner = Scanner()
    scanner.get_str("x:=15")
    token1 = scanner.getToken()
    token2 = scanner.getToken()
    token3 = scanner.getToken()
    assert token1 == Token_Type.ID
    assert token2 == Token_Type.ASSIGN
    assert token3 == Token_Type.NUM

def test_getToken_program():
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

    results = []
    res = scanner.getToken()
    while res != Token_Type.ENDFILE:
        results.append(res)
        res = scanner.getToken()

    expected = [Token_Type.READ, Token_Type.ID, Token_Type.SEMI, Token_Type.IF,
    Token_Type.NUM, Token_Type.LT, Token_Type.ID, Token_Type.THEN, Token_Type.ID,
    Token_Type.ASSIGN, Token_Type.NUM, Token_Type.SEMI, Token_Type.REPEAT, Token_Type.ID,
    Token_Type.ASSIGN, Token_Type.ID, Token_Type.TIMES, Token_Type.ID, Token_Type.SEMI,
    Token_Type.ID, Token_Type.ASSIGN, Token_Type.ID, Token_Type.MINUS, Token_Type.NUM,
    Token_Type.UNTIL, Token_Type.ID, Token_Type.EQ, Token_Type.NUM, Token_Type.SEMI,
    Token_Type.WRITE, Token_Type.ID, Token_Type.END]

    assert results == expected