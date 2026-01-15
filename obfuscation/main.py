import ast
import random
import astor
import os

from control_flow_obfuscators import BooleanIdentityInserter, ConditionReverser, WhileLoopFlattener
from lexical_obfuscators import AugAssignExpander, VariableRenamer, obfuscate_formatting, remove_comments
from structural_obfuscators import DeadCodeInserter, LoopTransformer, StatementReorderer, UniversalWrapper

DATA_SOURCE = "official_solutions/python"
OUTPUT_DIR = "obfuscated_solutions/python"

# ==========================================
#      MAIN GENERATOR
# ==========================================

def generate_dataset(source_code, filename_base="solution"):
    # Registry of available techniques
    # (Name, Handler, Type)
    techniques = [
        ("renaming", VariableRenamer, 'ast'),
        ("dead_code", DeadCodeInserter, 'ast'),
        ("aug_expand", AugAssignExpander, 'ast'),
        ("bool_ident", BooleanIdentityInserter, 'ast'),
        ("universal_wrap", UniversalWrapper, 'ast'),
        ("loop_to_while", LoopTransformer, 'ast'),
        ("loop_flatten", WhileLoopFlattener, 'ast'),
        ("logic_flip", ConditionReverser, 'ast'),
        ("reorder", StatementReorderer, 'ast'),
        ("no_comments", remove_comments, 'text'),
        ("formatting", obfuscate_formatting, 'text')
    ]
    
    generated_files = {}

    print(f"Processing: {filename_base}...")

    for name, handler, tech_type in techniques:
        try:
            if tech_type == 'ast':
                # 1. Parse AST
                tree = ast.parse(source_code)
                # 2. Transform
                transformer = handler(seed=42)
                tree = transformer.visit(tree)
                ast.fix_missing_locations(tree)
                # 3. Regenerate
                obfuscated_source = astor.to_source(tree)
                
            elif tech_type == 'text':
                # Direct text manipulation
                random.seed(42) 
                obfuscated_source = handler(source_code)
            
            # Save result
            output_name = f"{filename_base}_{name}.py"
            generated_files[output_name] = obfuscated_source
            print(f"  -> Generated: {output_name}")

        except SyntaxError:
            print(f"Syntax error for {filename_base}")

    return generated_files

if __name__ == "__main__":
    for dir_name in os.listdir(DATA_SOURCE):
        problem_dir = os.path.join(OUTPUT_DIR, dir_name)
        if not os.path.exists(problem_dir):
            os.makedirs(problem_dir)
        
        for solution_name in os.listdir(os.path.join(DATA_SOURCE, dir_name)):
            print(solution_name)
            with open(os.path.join(DATA_SOURCE, dir_name,solution_name)) as f:
                results = generate_dataset(f.read(), solution_name[:-3])
                for obf_file_name, code in results.items():
                    file_path = os.path.join(problem_dir, obf_file_name)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(code)
        

    
    # results = generate_dataset(original_code, "test_file")
    # for key, val in results.items():
    #     print(f"\n--- Preview: {key} ---")
    #     print(val)