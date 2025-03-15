import curses
# import process

class select_process:
    
    def __init__(self, process_name : str):
        self.pn = process_name
        pass

    def describe(self):
        print("DESCRIBE")
        pass

    def train(self):
        print("TRAIN")
        pass

    def predict(self):
        print("PREDICT")
        pass

    def data_visualizzation(self):
        print("DATA_VISUALIZZATION")
        pass




def menu(stdscr, options):
    curses.curs_set(0)  # Hide cursor
    current_row = 0

    while True:
        stdscr.clear()
        
        # Print the menu
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx, 0, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, option)

        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Navigate
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_row]


def main ():
    options = ["describe", "predict", "train", "data_visualizzation", "quit"]
    curses.wrapper(lambda stdscr: curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE))
    
    selected = curses.wrapper(menu, options)
    if selected == "quit":
        quit(1)
    else:
        c_process = select_process(selected)
        method = getattr(c_process, selected)
        method()



if __name__ == "__main__":
    main()