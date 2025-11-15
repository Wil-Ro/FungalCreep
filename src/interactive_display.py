import curses


class InteractiveDisplay:
    def __init__(self, display, input):
        self.disp = display
        self.inp = input
        self.window = display.window

        self.answer = ""

    def basic_input_screen(self, question):
        max_answer_length = 4
        x, y = self.disp.get_window_size()
        y = int(x/2)-max_answer_length
        x = int(y/2)

        answer = ""
        while True:
            self.window.clear()
            self.window.addstr(y-1, x, question)
            self.window.addstr(y, x, answer)
            latest_input = self.inp.wait_on_any_key()
            if latest_input == curses.KEY_ENTER:
                return answer
            if latest_input == curses.KEY_BACKSPACE or latest_input == "KEY_BACKSPACE":
                answer = answer[:-1]
            elif latest_input is not None:
                answer += latest_input

    def input_box(self, x, y, question, max_answer_length = 4):
        self.window.addstr(y-1, x, question)
        self.window.addstr(y, x, self.answer)
        latest_input = self.inp.get_key_now()
        if latest_input == " ":
            ans = self.answer
            self.answer = ""
            return ans
        if latest_input == curses.KEY_BACKSPACE or latest_input == "KEY_BACKSPACE":
            self.answer = self.answer[:-1]
        elif latest_input is not None:
            self.answer += latest_input
        return None
