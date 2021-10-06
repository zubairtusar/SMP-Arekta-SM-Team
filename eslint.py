#!npm install eslint --save-dev
#!eslint test.jsx > "path-to-save-the-output-as-txt"
#!
import os

max_lines = 0
eqeqeq = 0
block_scoped_var = 0
complexity = 0
grouped_accessor_pairs = 0
max_classes_per_file = 0
no_empty_function = 0
no_useless_return = 0
no_unused_expressions = 0
max_depth = 0

directory = "./"

for path, subdirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".jsx") or filename.endswith(".js"):
            os.system('eslint ' + os.path.join(path, filename) +
                      ' > ./tmp/output.txt')
            print("=========================")
            print('eslint ' + os.path.join(path, filename) + ' > ./tmp/output.txt')
            a_file = open("./tmp/output.txt")
            lines = a_file. readlines()
            for line in lines:
                if "eqeqeq" in line:
                    eqeqeq = eqeqeq + 1
                if "block-scoped-var" in line:
                    block_scoped_var = block_scoped_var + 1
                if "complexity" in line:
                    complexity = complexity + 1
                if "grouped-accessor-pairs" in line:
                    grouped_accessor_pairs = grouped_accessor_pairs + 1
                if "max-classes-per-file" in line:
                    max_classes_per_file = max_classes_per_file + 1
                if "no-empty-function" in line:
                    no_empty_function = no_empty_function + 1
                if "no-empty-pattern" in line:
                    no_empty_pattern = no_empty_pattern + 1
                if "no-useless-return" in line:
                    no_useless_return = no_useless_return + 1
                if "no-unused-expressions" in line:
                    no_unused_expressions = no_unused_expressions + 1
                if "max-depth" in line:
                    max_depth = max_depth + 1
                if "max-lines" in line:
                    max_lines = max_lines + 1
            print("eqeqeq", eqeqeq)
            print("block_scoped_var", block_scoped_var)
            print("complexity", complexity)
            print("grouped_accessor_pairs", grouped_accessor_pairs)
            print("max_classes_per_file", max_classes_per_file)
            print("no_empty_function", no_empty_function)
            print("no_useless_return", no_useless_return)
            print("no_unused_expressions", no_unused_expressions)
            print("max_depth", max_depth)
            print("max_lines", max_lines)

            eqeqeq = 0
            block_scoped_var = 0
            complexity = 0
            grouped_accessor_pairs = 0
            max_classes_per_file = 0
            no_empty_function = 0
            no_useless_return = 0
            no_unused_expressions = 0
            max_depth = 0
            max_lines = 0
        else:
            continue
