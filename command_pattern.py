class TextObject():

    def __init__(self, text):
        self.text = text
        self.clip_board = ""

    def cut(self, start=0, end=0):
        self.clip_board = self.text[start:end]
        self.text = self.text[:start] + self.text[end:]

    def paste(self, offset=0):
        self.text = self.text[:offset] + self.clip_board + self.text[offset:]

    def clear_clipboard(self):
        self.clip_board = ""

    def get_text(self):
        return self.text


class TextCommand():

    def __init__(self, text_object):
        self.text_object = text_object
        self.previus_status = text_object.get_text()

    def execute(self):
        pass

    def undo(self):
        pass


class CutCommand(TextCommand):

    def __init__(self, text_object, star=0, end=0):
        super().__init__(text_object)
        self.start = star
        self.end = end

    def execute(self):
        self.text_object.cut(self.start, self.end)

    def undo(self):
        self.text_object.clear_clipboard()
        self.text_object.text = self.previus_status


class PasteCommand(TextCommand):

    def __init__(self, text_object, offset=0):
        super().__init__(text_object)
        self.offset = offset

    def execute(self):
        self.text_object.paste(self.offset)

    def undo(self):
        self.text_object.clear_clipboard()
        self.text_object.text = self.previus_status


class TextInvoker():

    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


if __name__ == '__main__':

    text = TextObject("Hello World")
    text_invocer = TextInvoker()
    cut = CutCommand(text, star=6, end=11)
    paste = PasteCommand(text)

    print(text.get_text())
    text_invocer.store_and_execute(cut)
    print(text.get_text())
    text_invocer.undo_last()
    print(text.get_text())

