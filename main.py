import os
import csv
directory = "./"

all_results = []
for path, subdirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".jsx") or filename.endswith(".js"):
            os.system('eslint ' + os.path.join(path, filename) +
                      ' > ./tmp/output.txt')
            a_file = open("./tmp/output.txt")
            lines = a_file. readlines()

            results = {"file_name": filename, "NoOfLines": 0, "depth": [],
                       "id_length": [], "Complexity": [], "nested_callbacks": [],
                       "eqeqeq": 0, "no_extra_parens": 0, "no_console": 0,
                       "no_lone_blocks": 0, "block_scoped_var": 0,
                       "no_empty_function": 0, "no_empty_pattern": 0,
                       "no_useless_return": 0, "no_unused_expressions": 0,
                       "no_alert": 0, "no_loop_func": 0,
                       "no_param_reassign": 0, "no_shadow": 0,
                       "array_bracket_newline": 0, "no_mixed_spaces_and_tabs": 0,
                       "curly": 0, "brace_style": 0, "comma_spacing": 0,
                       "indent": 0, "no_trailing_spaces": 0,
                       "no_whitespace_before_property": 0, "no_multi_spaces": 0
                       }

            for line in lines:
                # line of code
                if line.split(' ')[-1] == "max-lines\n":
                    splitted = line.split(' ')
                    splitted = [x for x in splitted if x != '']
                    line_count = splitted[7][1:-2]
                    results["NoOfLines"] = int(line_count)

                # depth
                if line.split(' ')[-1] == "max-depth\n":
                    splitted = line.split(' ')
                    splitted = [x for x in splitted if x != '']
                    depth = splitted[7][1:-2]
                    results["depth"].append(int(depth))

                # identifier length
                if line.split(' ')[-1] == "id-length\n":
                    splitted = line.split(' ')
                    splitted = [x for x in splitted if x != '']
                    identifier = splitted[4][1:-1]
                    results["id_length"].append(len(identifier))

                # complexity
                if line.split(' ')[-1] == "complexity\n":
                    splitted = line.split(' ')
                    splitted = [x for x in splitted if x !=
                                '' and x != 'Async']
                    if splitted[8] == 'Maximum':
                        complexity = splitted[7][:-1]
                    else:
                        complexity = splitted[8][:-1]
                    results["Complexity"].append(int(complexity))

                # nested callback count
                if line.split(' ')[-1] == "max-nested-callbacks\n":
                    splitted = line.split(' ')
                    splitted = [x for x in splitted if x != '']
                    nested_callbacks = splitted[6][1:-2]
                    results["nested_callbacks"].append(int(nested_callbacks))

                # eqeqeq count
                if line.split(' ')[-1] == "eqeqeq\n":
                    results["eqeqeq"] += 1

                # no_extra_parens count
                if line.split(' ')[-1] == "no-extra-parens\n":
                    results["no_extra_parens"] += 1

                # no-console count
                if line.split(' ')[-1] == "no-console\n":
                    results["no_console"] += 1

                # no-alert count
                if line.split(' ')[-1] == "no-alert\n":
                    results["no_alert"] += 1

                # no-loop-func count
                if line.split(' ')[-1] == "no-loop-func\n":
                    results["no_loop_func"] += 1

                # no-mixed-spaces-and-tabs count
                if line.split(' ')[-1] == "no-mixed-spaces-and-tabs\n":
                    results["no_mixed_spaces_and_tabs"] += 1

                # no_lone_blocks count
                if line.split(' ')[-1] == "no-lone-blocks\n":
                    results["no_lone_blocks"] += 1

                # block-scoped-var
                if line.split(' ')[-1] == "block-scoped-var\n":
                    results["block_scoped_var"] += 1

                # no-empty-function
                if line.split(' ')[-1] == "no-empty-function\n":
                    results["no_empty_function"] += 1

                # no-empty-pattern
                if line.split(' ')[-1] == "no-empty-pattern\n":
                    results["no_empty_pattern"] += 1

                # no-useless-return
                if line.split(' ')[-1] == "no-useless-return\n":
                    results["no_useless_return"] += 1

                # no-param-reassign
                if line.split(' ')[-1] == "no-param-reassign\n":
                    results["no_param_reassign"] += 1

                # no-param-reassign
                if line.split(' ')[-1] == "array-bracket-newline\n":
                    results["array_bracket_newline"] += 1

                # no-shadow
                if line.split(' ')[-1] == "no-shadow\n":
                    results["no_shadow"] += 1

                # no-unused-expressions
                if line.split(' ')[-1] == "no-unused-expressions\n":
                    results["no_unused_expressions"] += 1

                # curly
                if line.split(' ')[-1] == "curly\n":
                    results["curly"] += 1

                # brace-style
                if line.split(' ')[-1] == "brace-style\n":
                    results["brace_style"] += 1

                # comma-spacing
                if line.split(' ')[-1] == "comma-spacing\n":
                    results["comma_spacing"] += 1

                # indent
                if line.split(' ')[-1] == "indent\n":
                    results["indent"] += 1

                # no-multi-spaces
                if line.split(' ')[-1] == "no-multi-spaces\n":
                    results["no_multi_spaces"] += 1

                # no-trailing-spaces
                if line.split(' ')[-1] == "no-trailing-spaces\n":
                    results["no_trailing_spaces"] += 1

                # no-whitespace-before-property
                if line.split(' ')[-1] == "no-whitespace-before-property\n":
                    results["no_whitespace_before_property"] += 1

            # print("Results: ", results)
            # print("Maximum Identifier Length: ", max(results['id_length']))
            # print("Average Identifier Length: ", "{:.2f}".format(sum(
            #     results['id_length'])/len(results['id_length'])))
            # print("Minimum Identifier Length: ", min(results['id_length']))
            all_results.append(results)
print(all_results[0])
csv_file = "output.csv"
csv_columns = [key for key, value in all_results[0].items()]
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in all_results:
            writer.writerow(data)
except IOError:
    print("I/O error")
