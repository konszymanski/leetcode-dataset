import ast
import tokenize
import io

from base_obfuscator import BaseObfuscator


class VariableRenamer(BaseObfuscator):
    """Lexical: Renames variables and function arguments."""

    def __init__(self, seed=None):
        super().__init__(seed)
        self.mapping = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load, ast.Store)):
            if node.id not in dir(__builtins__):
                if node.id not in self.mapping:
                    self.mapping[node.id] = f"var_{self._random_string(4)}"
                node.id = self.mapping[node.id]
        return node

    def visit_FunctionDef(self, node):
        if node.name not in self.mapping:
            self.mapping[node.name] = f"func_{self._random_string(4)}"
        node.name = self.mapping[node.name]

        for arg in node.args.args:
            if arg.arg not in self.mapping:
                self.mapping[arg.arg] = f"arg_{self._random_string(4)}"
            arg.arg = self.mapping[arg.arg]
        return self.generic_visit(node)


class AugAssignExpander(BaseObfuscator):
    """Lexical: Expands 'x += 1' into 'x = x + 1' to change token counts."""

    def visit_AugAssign(self, node):
        new_node = ast.Assign(
            targets=[node.target],
            value=ast.BinOp(left=node.target, op=node.op, right=node.value),
        )
        return ast.copy_location(new_node, node)


def remove_comments(source_code):
    """Lexical: Entirely strips comments from the source."""
    io_obj = io.StringIO(source_code)
    out, last_lineno, last_col = "", -1, 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        if tok.start[0] > last_lineno:
            last_col = 0
        if tok.start[1] > last_col:
            out += " " * (tok.start[1] - last_col)
        if tok.type != tokenize.COMMENT:
            out += tok.string
        last_col, last_lineno = tok.end[1], tok.end[0]
    return out


def obfuscate_formatting(source_code):
    """Lexical: Adds inconsistent spacing and blank lines."""
    return "\n\n".join(
        [
            l.replace("=", "  =  ").replace("+", " + ")
            for l in source_code.splitlines()
            if l.strip()
        ]
    )
