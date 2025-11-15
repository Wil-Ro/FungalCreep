import curses


class InteractiveDisplay:
    def __init__(self, display, input):
        self.disp = display
        self.inp = input
        self.window = display.window

    def basic_input_window(self):
        max_answer_length = 4
        x, y = self.disp.get_window_size()
        x = int(x/2)-max_answer_length
        y = int(x/2)

        answer = ""
        while True:
            self.window.addstr(x, y, answer)
            latest_input = self.inp.wait_on_any_key()
            if latest_input == curses.KEY_ENTER:
                return answer
            if latest_input == curses.KEY_BACKSPACE:
                answer = answer[:-1]
            elif latest_input is not None:
                answer += latest_input
