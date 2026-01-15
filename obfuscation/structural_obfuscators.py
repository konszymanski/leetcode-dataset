import ast
import random

from base_obfuscator import BaseObfuscator


class UniversalWrapper(BaseObfuscator):
    """Structural: Wraps various blocks in redundant 'if True' or 'while True'."""

    def visit_Assign(self, node):
        if random.random() > 0.6:  # 40% chance to wrap an assignment
            return ast.If(test=ast.Constant(value=True), body=[node], orelse=[])
        return node

    def visit_For(self, node):
        # Wrap the whole loop in a redundant True check
        return ast.If(test=ast.Constant(value=True), body=[node], orelse=[])

    def visit_Return(self, node):
        # Even wrap return statements
        return ast.If(test=ast.Constant(value=True), body=[node], orelse=[])


class LoopTransformer(BaseObfuscator):
    """Structural: Converts 'for' loops to 'while' loops."""

    def visit_For(self, node):
        if (
            isinstance(node.iter, ast.Call)
            and isinstance(node.iter.func, ast.Name)
            and node.iter.func.id == "range"
        ):

            args = node.iter.args
            target_var = node.target
            start_val = args[0] if len(args) > 1 else ast.Constant(value=0)
            stop_val = args[1] if len(args) > 1 else args[0]
            step_val = args[2] if len(args) > 2 else ast.Constant(value=1)

            init_assign = ast.Assign(targets=[target_var], value=start_val)
            condition = ast.Compare(
                left=target_var, ops=[ast.Lt()], comparators=[stop_val]
            )
            increment = ast.AugAssign(target=target_var, op=ast.Add(), value=step_val)

            while_node = ast.While(
                test=condition, body=node.body + [increment], orelse=node.orelse
            )
            return [init_assign, while_node]
        return node


class StatementReorderer(BaseObfuscator):
    """Structural: Shuffles function definitions."""

    def visit_Module(self, node):
        funcs = [n for n in node.body if isinstance(n, ast.FunctionDef)]
        others = [n for n in node.body if not isinstance(n, ast.FunctionDef)]
        random.shuffle(funcs)
        node.body = others + funcs
        return node


class DeadCodeInserter(BaseObfuscator):
    """Structural: Inserts junk math that changes the code's token signature."""

    def visit_FunctionDef(self, node):
        target = self._random_string(5)
        dead_node = ast.Assign(
            targets=[ast.Name(id=target, ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Constant(random.randint(1, 100)),
                op=ast.Mult(),
                right=ast.Constant(2),
            ),
        )
        node.body.insert(random.randint(0, len(node.body)), dead_node)
        return self.generic_visit(node)
