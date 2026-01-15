import ast
from base_obfuscator import BaseObfuscator

class BooleanIdentityInserter(BaseObfuscator):
    """Control Flow: Wraps logic in 'opaque predicates' (mathematically always true)."""
    def visit_If(self, node):
        # Wrap the condition: if (old_cond and (1+1==2)):
        identity = ast.Compare(left=ast.BinOp(left=ast.Constant(1), op=ast.Add(), right=ast.Constant(1)), 
                               ops=[ast.Eq()], comparators=[ast.Constant(2)])
        node.test = ast.BoolOp(op=ast.And(), values=[node.test, identity])
        return self.generic_visit(node)

class ConditionReverser(BaseObfuscator):
    """Control Flow: Swaps if/else logic and inverts the comparison operator."""
    def visit_If(self, node):
        if node.orelse and isinstance(node.test, ast.Compare) and len(node.test.ops) == 1:
            op = node.test.ops[0]
            inv = {ast.Gt: ast.LtE, ast.Lt: ast.GtE, ast.GtE: ast.Lt, ast.LtE: ast.Gt, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
            for original, inverse in inv.items():
                if isinstance(op, original):
                    node.test.ops[0] = inverse()
                    node.body, node.orelse = node.orelse, node.body
                    break
        return self.generic_visit(node)

class WhileLoopFlattener(BaseObfuscator):
    """
    Control Flow: Converts 'while cond:' into 'while True: if not cond: break'.
    This hides the loop exit criteria inside the body.
    """
    def visit_While(self, node):
        # 1. If the loop is already 'while True:', skip it
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            return self.generic_visit(node)

        # 2. Create the inverse condition: 'if not cond: break'
        # We wrap the original condition in a 'UnaryOp(Not())'
        break_condition = ast.If(
            test=ast.UnaryOp(op=ast.Not(), operand=node.test),
            body=[ast.Break()],
            orelse=[]
        )

        # 3. Create the new While True loop
        new_while = ast.While(
            test=ast.Constant(value=True),
            body=[break_condition] + node.body,
            orelse=node.orelse
        )

        return ast.copy_location(new_while, node)