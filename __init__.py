from mycroft import MycroftSkill, intent_file_handler


class ExecBash(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bash.exec.intent')
    def handle_bash_exec(self, message):
        self.speak_dialog('bash.exec')


def create_skill():
    return ExecBash()

