import sys
import subprocess
import os

import terminal

extract_path = "__extract__"
extract_file = "__data__.txt"
java_class_name = "Main"
java_file_name = "Main.java"
java_compiled_name = "Main.class"
delimiter_start = "//ftcemustart"
delimiter_end = "//ftcemuend"
delimiter_start_len = len(delimiter_start)

extracted = False

def extract():
    global extracted
    teamcode_path = sys.argv[1]
    print("Extracting:", teamcode_path)
    os.makedirs(extract_path, exist_ok=True)
    try:
        extract_output = open(f"{extract_path}/{extract_file}", "w")
    except:
        extract_output = open(f"{extract_path}/{extract_output}", "x")
    contents = os.walk(teamcode_path)
    output = ""
    for directory, _, src_files in contents:
        for src_file in src_files:
            src_file_content = open(f"{directory}/{src_file}", "r").readlines()
            capture = False
            for line in src_file_content:
                processed = str_collapse(line)
                if processed[:delimiter_start_len] == delimiter_start:
                    print("Writing:", processed[delimiter_start_len:])
                    capture = True
                if capture:
                    output += line
                if processed == delimiter_end:
                    capture = False
    extract_output.write(output)
    extracted = True
    print("Extract complete.")

def embed(): # Requires heavy refactoring and revision.
    global extracted
    if not extracted:
        print("Must extract before embedding.")
        return
    data_raw = open(f"{extract_path}/{extract_file}", "r").readlines()
    data_reprocessed = {}
    label = ""
    block = []
    for line in data_raw:
        processed = str_collapse(line)
        if processed[:delimiter_start_len] == delimiter_start:
            label = processed[delimiter_start_len:]
            block.clear()
        elif processed == delimiter_end:
            data_reprocessed[label] = block.copy()
        else:
            block.append(line)
    keys = list(data_reprocessed.keys())
    keys_len = len(keys)
    print("Select Blocks:")
    selections = []
    index = 0
    printOptions(keys, index, selections)
    while (selection := terminal.getch()) != '\n':
        match selection:
            case '\x1b':
                a = terminal.getch()
                b = terminal.getch()
                if a == '[' and b == 'A': # Up
                    index = max(0, index - 1)
                if a == '[' and b == 'B': # Down
                    index = min(index + 1, keys_len - 1)
            case ' ':
                key_select = keys[index]
                if key_select not in selections:
                    selections.append(key_select)
                else:
                    selections.remove(key_select)
        printOptions(keys, index, selections)
    print("Embedding:", *(x for x in selections))
    inline = open("./daemon/template/inline.txt").read()
    main_content = ""
    for selection in selections:
        block = data_reprocessed[selection]
        for line in block:
            key_words = [
                "public",
                "private",
                "class",
                "enum"
            ]
            add_debug = True
            for key_word in key_words:
                if line.lstrip()[:len(key_word)] == key_word:
                    add_debug = False
                    break
            if add_debug:
                main_content += inline.replace("`ln`", "\"" + line.rstrip().replace("\"", "\\\"") + "\"") + "; "
            main_content += line.lstrip()
    main_in = open("./daemon/template/Main.java", "r").read()
    main_processed = main_in.replace("// INS", main_content)
    try:
        main_out = open(f"{extract_path}/{java_file_name}", "w")
    except:
        main_out = open(f"{extract_path}/{java_file_name}", "x")
    main_out.write(main_processed)
    copy_paths = [
        "./daemon/template/Terminal.java",
        "./addon/*"
    ]
    for path in copy_paths:
        os.system(f"cp -r {path} {extract_path}")
    print("Embed complete.")

def str_collapse(s: str) -> str:
    return s.replace(" ", "").casefold().rstrip()

def printOptions(options: list[str], index, chosen):
    options_len = len(options)
    for i in range(options_len):
        print(f"{'> ' if i == index else '  '}{'+ ' if options[i] in chosen else '  '}{i}: {options[i]}")
    print()

def run():
    print("Running...")
    print("JAVAC")
    if not os.path.exists(f"{extract_path}/{java_compiled_name}"):
        subprocess.run([
            "javac",
            f"{extract_path}/{java_file_name}"
        ])
    print("JAVA")
    subprocess.run([
        "java",
        "-classpath",
        f":{extract_path}",
        java_class_name,
    ])
