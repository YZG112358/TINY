from src.globals import Node
from src.globals import Token_Type
from src.globals import Nodekind
from src.globals import StmtKind
from src.globals import ExpKind
from src.globals import ExpType

def new_stmt_node(stmtkind):
    node = Node()
    node.nodekind = Nodekind.StmtK
    node.stmtkind = stmtkind
    
    return node

def new_exp_node(expkind):
    node = Node()
    node.nodekind = Nodekind.ExpK
    node.expkind = expkind
    node.type = ExpType.Void
    
    return node