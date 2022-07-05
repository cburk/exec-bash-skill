from mycroft import MycroftSkill, intent_file_handler, intent_handler
from os.path import join
from os import mkdir

class ExecBash(MycroftSkill):
    def __init__(self):
        self.hosts = ["127.0.0.1"] # TODO: Swap with better store
        self.target = "127.0.0.1" # TODO: Load from target file
        self.safety = "on"
        MycroftSkill.__init__(self)
        # hello world

    def initialize(self):
        self.register_entity_file('scantype.entity')
        self.register_entity_file('onoff.entity')
        self.register_entity_file('path.entity')
        # TODO: Make output dir automatically

    @intent_file_handler('set.safety.intent')
    def handle_set_safety(self, message):
        onoff = message.data.get("onoff")
        self.safety = onoff
        self.speak(f"ok, safety is {onoff}")

    @intent_file_handler('check.safety.intent')
    def handle_check_safety(self, message):
        self.speak(f"safety is {self.safety}")

    @intent_file_handler('exec.nmap.intent')
    def handle_exec_nmap(self, message):
        scantype = message.data.get('scantype')
        if scantype is None:
            scantype = "syn"

        # TODO: improve
        target = self.target

        with self.file_system.open("/tmp/a.txt", "w") as myfile:
            myfile.write("Hello world, file io working")


        if self.safety == "off":
            self.speak(f"Ok, running {scantype} scan against {target}")
        else:
            self.speak(f"Ok, preparing to run {scantype} scan against {target}.")
            # Prompt

    @intent_file_handler('bash.exec.intent')
    def handle_bash_exec(self, message):
        self.speak_dialog('bash.exec')

    def shutdown(self):
        self.speak_dialog('shutdown')

def create_skill():
    return ExecBash()

