import sys
import subprocess

extract_path = "__extract__"
java_class_name = "Main"
java_file_name = "Main.java"

def extract():
    teamcode_path = sys.argv[1]
    print("Extracting:", teamcode_path)

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
