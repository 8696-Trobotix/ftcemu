import atexit

import terminal
import launch

@atexit.register
def reset_term_state():
    print("Cleaning up terminal state.")
    terminal.stdin_reset()

def main():
    terminal.stdin_immediate()
    while (test := terminal.getch()) != b'q':
        print("Character:", test)

if __name__ == "__main__":
    main()
