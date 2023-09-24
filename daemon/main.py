import atexit

import terminal
import launch

@atexit.register
def reset_term_state():
    print("Cleaning up terminal state.")
    terminal.stdin_reset()

def main():
    terminal.stdin_immediate()

    print("""
Daemon started.

0 - Extract and Run
1 - Extract
2 - Run
q - Quit
""")

    while (option := terminal.getch()) != 'q':
        match option:
            case '0':
                launch.run()
            case '1':
                launch.extract()
            case '2':
                launch.extract()
                launch.run()

if __name__ == "__main__":
    main()
