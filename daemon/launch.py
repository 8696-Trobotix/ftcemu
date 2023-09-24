import sys
import subprocess
import os

extract_path = "__extract__"
extract_file = "__data__.txt"
java_class_name = "Main"
java_file_name = "Main.java"
delimiter_start = "//ftcemustart"
delimiter_end = "//ftcemuend"

def extract():
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
                processed = line.replace(" ", "").casefold().rstrip()
                if processed == delimiter_start:
                    capture = True
                if capture:
                    output += line
                if processed == delimiter_end:
                    capture = False
    extract_output.write(output)
    print("Done.")

def run():
    print("Running...")
    print("JAVAC")
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
