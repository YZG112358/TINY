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
    assert scanner.getToken() == Token_Type.READ
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.SEMI
    assert scanner.getToken() == Token_Type.IF
    assert scanner.getToken() == Token_Type.NUM
    assert scanner.getToken() == Token_Type.LT
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.THEN
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.ASSIGN
    assert scanner.getToken() == Token_Type.NUM
    assert scanner.getToken() == Token_Type.SEMI
    assert scanner.getToken() == Token_Type.REPEAT
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.ASSIGN
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.TIMES
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.SEMI
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.ASSIGN
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.MINUS
    assert scanner.getToken() == Token_Type.NUM
    assert scanner.getToken() == Token_Type.UNTIL
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.EQ
    assert scanner.getToken() == Token_Type.NUM
    assert scanner.getToken() == Token_Type.SEMI
    assert scanner.getToken() == Token_Type.WRITE
    assert scanner.getToken() == Token_Type.ID
    assert scanner.getToken() == Token_Type.END
    assert scanner.getToken() == Token_Type.ENDFILE