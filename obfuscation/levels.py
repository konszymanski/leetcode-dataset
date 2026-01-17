import re
import random
import builtins
from pygments import lexers, token
import ast
import os

DATA_SOURCE = "official_solutions/python"
OUTPUT_DIR = "obfuscated_solutions/python"

class StructuralObfuscator(ast.NodeTransformer):
    """
    AST Transformer to perform L2 Structural Obfuscation:
    1. Invert 'if/else' blocks
    2. Expand augmented assignments (+= to = x +)
    """

    def __init__(self):
        # Map of operators to their inverses
        self.op_map = {
            ast.Eq: ast.NotEq,
            ast.NotEq: ast.Eq,
            ast.Lt: ast.GtE,
            ast.LtE: ast.Gt,
            ast.Gt: ast.LtE,
            ast.GtE: ast.Lt,
            ast.Is: ast.IsNot,
            ast.IsNot: ast.Is,
            ast.In: ast.NotIn,
            ast.NotIn: ast.In,
        }

    def visit_If(self, node):
        # We only invert if there is an 'else' block (node.orelse)
        if node.orelse:
            # Check if the test is a simple comparison (e.g., x > y)
            if isinstance(node.test, ast.Compare) and len(node.test.ops) == 1:
                op_type = type(node.test.ops[0])
                
                if op_type in self.op_map:
                    # 1. Invert the operator
                    new_op = self.op_map[op_type]()
                    node.test.ops[0] = new_op
                    
                    # 2. Swap the body and the else block
                    node.body, node.orelse = node.orelse, node.body
        
        # Continue visiting child nodes (in case of nested ifs)
        self.generic_visit(node)
        return node

    def visit_AugAssign(self, node):
        # Expand x += 1 to x = x + 1
        # Create a binary operation: (target) (op) (value)
        bin_op = ast.BinOp(
            left=ast.Name(id=node.target.id, ctx=ast.Load()) if isinstance(node.target, ast.Name) else node.target,
            op=node.op,
            right=node.value
        )
        # Create the explicit assignment
        assign_node = ast.Assign(
            targets=[node.target],
            value=bin_op
        )
        return assign_node

class SemanticObfuscator(ast.NodeTransformer):
    """
    Level 3 Obfuscator: Uses AST to safely inject logic without breaking indentation.
    """
    def __init__(self):
        self.predicates = [
            ast.Compare(left=ast.BinOp(left=ast.Constant(value=1), op=ast.Add(), right=ast.Constant(value=1)),
                        ops=[ast.Eq()], comparators=[ast.Constant(value=2)]), # 1+1==2
            ast.Compare(left=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Constant(value='abc')], keywords=[]),
                        ops=[ast.Eq()], comparators=[ast.Constant(value=3)]) # len('abc')==3
        ]

    def visit_For(self, node):
        # Process child nodes first
        self.generic_visit(node)
        
        # Inject junk code into the loop body
        junk_node = ast.Assign(
            targets=[ast.Name(id=f"v_junk_{random.randint(10,99)}", ctx=ast.Store())],
            value=ast.Constant(value=random.randint(1, 100))
        )
        node.body.insert(0, junk_node)
        return node

    def visit_Assign(self, node):
        """Randomly wrap assignments in an 'if True' opaque predicate."""
        if random.random() < 0.3:
            return ast.If(
                test=random.choice(self.predicates),
                body=[node],
                orelse=[]
            )
        return node

import ast
import re
import random
import builtins
from pygments import lexers, token

class Obfuscator:
    def __init__(self, seed=42):
        random.seed(seed)
        self.base_protected = set(dir(builtins)) | {
            'List', 'Dict', 'Set', 'Tuple', 'Any', 'Optional', 'Union',
            'self', 'cls', '__init__', 'None', 'True', 'False', 'Solution'
        }

    def _find_entry_point(self, tree):
        """Finds the first function name inside the 'Solution' class."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'Solution':
                for item in node.body:
                    if isinstance(node, ast.FunctionDef): # For top-level functions
                        return node.name
                    if isinstance(item, ast.FunctionDef): # For methods in class
                        return item.name
        return None

    def _get_signature_names(self, code):
        """Automatically finds the first method in Solution and protects its signature."""
        protected = set()
        try:
            clean_code = code.replace('\xa0', ' ').replace('\t', '    ')
            tree = ast.parse(clean_code)
            
            entry_name = self._find_entry_point(tree)
            if entry_name:
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == entry_name:
                        protected.add(node.name)
                        # Protect all argument names (nums, target, etc.)
                        for arg in node.args.args:
                            protected.add(arg.arg)
                        break 
        except Exception as e:
            print(f"Signature detection failed: {e}")
        return protected

    def _obfuscate_names_universal(self, code):
        """Tokenizes code and renames only internal variables."""
        lexer = lexers.get_lexer_by_name("python")
        
        # 1. Dynamically find names to protect
        forbidden = set(self.base_protected)
        forbidden.update(self._get_signature_names(code))
        
        name_map = {}
        var_counter = 1
        new_code = []

        # 2. Tokenize and rename
        for ttype, value in lexer.get_tokens(code):
            if (ttype in {token.Name, token.Name.Variable, token.Name.Function} and 
                ttype not in token.Name.Builtin and 
                value not in forbidden):
                
                if value not in name_map:
                    name_map[value] = f"v{var_counter}_{random.randint(100, 999)}"
                    var_counter += 1
                new_code.append(name_map[value])
            else:
                new_code.append(value)
        
        return "".join(new_code)

    

    # =========================================================================
    # LEVEL 0: BASELINE (Noise)
    # Goal: Remove comments, normalize whitespace.
    # =========================================================================
    def apply_l0(self, code):
        """Removes comments and docstrings, normalizes whitespace."""
        # Remove single line comments
        code = re.sub(r"#.*", "", code)
        # Remove docstrings (simple triple-quote matching)
        code = re.sub(r'"""[\s\S]*?"""', "", code)
        code = re.sub(r"'''[\s\S]*?'''", "", code)
        # Remove empty lines
        lines = [line.rstrip() for line in code.splitlines() if line.strip()]
        return "\n".join(lines)

    # =========================================================================
    # LEVEL 1: LEXICAL (Renaming & Shuffling)
    # Goal: Rename variables while keeping builtins; shuffle functions.
    # =========================================================================
    def apply_l1(self, code):
        """Universal L1: Protects the first method found in Solution class."""
        # Step 1: Rename internal identifiers
        code = self._obfuscate_names_universal(code)
        
        # Step 2: Safe spacing (prevents breaking -> or ==)
        def safe_spacing(match):
            op = match.group(0)
            if op in ['->', '==', '!=', '<=', '>=']:
                return f" {op} " 
            return f" {op} " if random.random() > 0.4 else op

        # We use a regex that captures multi-char ops first to keep them together
        code = re.sub(r"(->|==|!=|<=|>=|[=+\-*/<>])", safe_spacing, code)
        return code

    # =========================================================================
    # LEVEL 2: STRUCTURAL (Shape Change)
    # Goal: Expand assignments, invert branches.
    # =========================================================================
    def _expand_assignments(self, code):
        """Expands x += 1 to x = x + 1"""
        pattern = r"([\w\.\[\]]+)\s*([\+\-\*/])=\s*(.+)"
        def expand(m):
            return f"{m.group(1)} = {m.group(1)} {m.group(2)} {m.group(3)}"
        
        lines = [re.sub(pattern, expand, line) for line in code.splitlines()]
        return "\n".join(lines)

    def _invert_if_else(self, code):
        """Inverts if a > b: A else: B  ->  if a <= b: B else: A"""
        # Note: This is a simplified regex approach. 
        # For production use, AST parsing is safer.
        pattern = r"(\s*)if\s+(.+)\s*:\s*\n(\s+)(.+)\n\s*else\s*:\s*\n\s+(.+)"
        op_map = {">": "<=", "<": ">=", "==": "!=", "!=": "==", ">=": "<", "<=": ">"}

        def invert(m):
            indent, cond, inner_indent, if_blk, else_blk = m.groups()
            for op, inv in op_map.items():
                if op in cond:
                    new_cond = cond.replace(op, inv)
                    # We only swap single-line blocks in this regex demo for safety
                    return f"{indent}if {new_cond}:\n{indent}{inner_indent}{else_blk}\n{indent}else:\n{indent}{inner_indent}{if_blk}"
            return m.group(0)

        return re.sub(pattern, invert, code)

    def apply_l2(self, source_code):
        """
        Parses code into AST, applies structural transforms, and unparses.
        Includes sanitization for copy-paste artifacts (NBSP).
        """
        # 1. SANITIZATION: Replace non-breaking spaces with regular spaces
        source_code = source_code.replace('\xa0', ' ')
        
        try:
            tree = ast.parse(source_code)
            transformer = StructuralObfuscator()
            transformed_tree = transformer.visit(tree)
            ast.fix_missing_locations(transformed_tree)
            
            # Check environment for unparse compatibility
            try:
                return ast.unparse(transformed_tree)
            except AttributeError:
                import astunparse
                return astunparse.unparse(transformed_tree)
                
        except SyntaxError as e:
            print(f"L2 Syntax Error in {e.filename or 'string'} line {e.lineno}: {e.msg}")
            print(f"Problematic line: {e.text}")
            return source_code
        except Exception as e:
            print(f"L2 Transformation Error: {e}")
            return source_code
    
    # =========================================================================
    # LEVEL 3: SEMANTIC (Logic Cloaking)
    # Goal: While-True loops, Opaque Predicates, Dead Code.
    # =========================================================================
    def _destructure_loops(self, code):
        """Converts 'while x:' to 'while True: if not x: break'"""
        pattern = r"(\s*)while\s+(.+)\s*:"
        def transform(m):
            indent = m.group(1)
            cond = m.group(2)
            # Add the break check at the start of the loop
            return f"{indent}while True:\n{indent}    if not ({cond}): break"
        return re.sub(pattern, transform, code)

    def _add_opaque_predicates(self, code):
        """Wraps blocks in if (True_Predicate):"""
        predicates = ["(1+1==2)", "(3*3==9)", "('a' in 'abc')"]
        lines = []
        for line in code.splitlines():
            # Randomly wrap assignment lines in a redundant if
            if "=" in line and random.random() < 0.3 and not line.strip().startswith(("def", "class", "if")):
                indent = re.match(r"^\s*", line).group()
                pred = random.choice(predicates)
                lines.append(f"{indent}if {pred}:")
                lines.append(f"    {line}")
            else:
                lines.append(line)
        return "\n".join(lines)
    
    def _get_indent(self, line):
        """Helper to capture the exact leading whitespace of a line."""
        match = re.match(r"^(\s*)", line)
        return match.group(1) if match else ""

    def _insert_dead_code(self, code):
        """Inserts junk logic only where it is safe (inside functions)."""
        dead_snippets = [
            "v_junk = 100 * 2",
            "if 1 > 2: pass",
            "_temp_status = True"
        ]
        lines = code.splitlines()
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            # Only insert dead code if the current line is indented (safe zone)
            # and it's not a return or a loop header
            indent = self._get_indent(line)
            if indent and random.random() < 0.2 and not line.strip().startswith(("return", "break", "continue")):
                new_lines.append(f"{indent}{random.choice(dead_snippets)}")
                
        return "\n".join(new_lines)

    def apply_l3(self, source_code):
        source_code = source_code.replace('\xa0', ' ')
        try:
            transformer = SemanticObfuscator()
            tree = ast.parse(source_code)
            new_tree = transformer.visit(tree)
            ast.fix_missing_locations(new_tree)
            
            return ast.unparse(new_tree)
        except Exception as e:
            print(f"L3 Error: {e}")
            return source_code

    # =========================================================================
    # PIPELINE RUNNER
    # =========================================================================
    def generate_benchmark_suite(self, original_code):
        """Generates all 4 versions of the code."""
        l0 = self.apply_l0(original_code)
        
        # Cumulative Application: L2 includes L1 features? 
        # Usually benchmarks keep them distinct to isolate variables, 
        # OR cumulative to test "Max Obfuscation".
        # Here we return DISTINCT attacks based on the table definitions.
        
        l1 = self.apply_l1(l0) # Lexical
        l2 = self.apply_l2(l0) # Structural (on clean code)
        l1_2 = self.apply_l2(l1) # Structural (on clean code)
        l3 = self.apply_l3(l0) # Semantic (on clean code)
        l2_3 = self.apply_l3(l2) # Semantic (on clean code)
        l1_3 = self.apply_l3(l1) # Semantic (on clean code)
        l1_2_3 = self.apply_l3(self.apply_l2(self.apply_l1(l0)))
        
        return {
            "original": original_code,
            "l0": l0,
            "l0_l1": l1,
            "l0_l2": l2,
            "l0_l1_l2": l1_2,
            "l0_l3": l3,
            "l0_l1_l3": l1_3,
            "l0_l2_l3": l2_3,
            "l0_l1_l2_l3": l1_2_3
        }

if __name__ == "__main__":
    for dir_name in os.listdir(DATA_SOURCE):
        problem_dir = os.path.join(OUTPUT_DIR, dir_name)
        if not os.path.exists(problem_dir):
            os.makedirs(problem_dir)
        
        for solution_name in os.listdir(os.path.join(DATA_SOURCE, dir_name)):
            print(solution_name)
            obf = Obfuscator()
    
            with open(os.path.join(DATA_SOURCE, dir_name,solution_name)) as f:
                results = obf.generate_benchmark_suite(f.read())
                for level, code in results.items():
                    file_path = os.path.join(problem_dir, f"{solution_name[:-3]}_{level}.py")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(code)
        