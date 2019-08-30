"""
print out a Sheet via caller->sheet
"""
from evennia import default_cmds

class CmdSheet(default_cmds.MuxCommand):
    """
    Print out your Character skill sheet

    Usage:
      sheet <nr>d<sides> [modifier] [success condition]
    """

    key = "sheet"
    aliases = ["skills", "c"]
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.sheet()"""
        self.msg((self.caller.sheet(), {'type':'sheet'}), options=None)

