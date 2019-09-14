"""
Manage a Character Sheet via caller->sheet caller->spend and caller->exp
"""
from evennia import default_cmds
import re

class CmdSheet(default_cmds.MuxCommand):
    """
    Print out your Character skill sheet

    Usage:
      sheet
    """

    key = "sheet"
    aliases = ["skills", "c"]
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.sheet()"""
        self.msg((self.caller.sheet(), {'type':'sheet'}), options=None)



class CmdRoll(default_cmds.MuxCommand):
    """
    Roll/Use a skill.  Optionally, 'Spend' a number of pips from that
    Skill's Pool to add +1/per-pip to the dice roll.

    Skill Rolls are 2d6 and have a default target number of 6.
    Sometimes, Target Numbers are adjusted up or down by special circumstances.

    Usage:
      roll <skill_name> [#pips]
    """

    key = "roll"
    aliases = ["use"]
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.roll()"""
        arglist = re.split(r'\s+', self.args)

        if( len(arglist) >= 2 and re.match('^[0-9]+$', arglist[1]) ):
            self.msg((self.caller.roll(arglist[0], int(arglist[1])), {'type':'roll'}), options=None)
        else:
            if( len(arglist) == 1 ):
                self.msg((self.caller.roll(arglist[0], 0), {'type':'roll'}), options=None)
            else:
                self.msg(f"Roll what?")



class CmdSpend(default_cmds.MuxCommand):
    """
    Spend EXP to buy/advance a skill, health, sanity, or mana permanently
    on a one-for-one basis.

    Exotic skills (sorcery and heavyarms) cost 8 points for the first pip.
    Exotic skills can only be purchased in chargen with debt.

    You can select 10 Investigative abilties during chargen.
    After chargen, they cost 8 points.

    Usage:
      spend skill_name [#exp]
    """

    key = "spend"
    aliases = ["buy","raise","xp","exp","advance"]
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.spend()"""
        arglist = re.split(r'\s+', self.args)
        if( (len(arglist) >= 2) and (re.match('^[0-9]+$', arglist[1])) ):
            pipsspent = int(arglist[1])
            self.msg((self.caller.spend(arglist[0], pipsspent), {'type':'exp'}), options=None)
        else:
            if( (len(arglist) == 1) ):
                self.msg((self.caller.ispend(arglist[0]), {'type':'exp'}), options=None)
            else:
                self.msg("That doesn't make sense for the spend command.  Usage: 'spend name' or 'spend skillname #pips'");



class CmdRefund(default_cmds.MuxCommand):
    """
    Reset any skill, health, sanity, or mana spends back to their default value.
    Usable only during character generation.

    Usage:
      refund skill_name
    """

    key = "refund"
    aliases = []
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.refund()"""
        arglist = re.split(r'\s+', self.args)
        if( len(arglist) >= 1 ):
            self.msg((self.caller.refund(arglist[0]), {'type':'exp'}), options=None)
        else:
            self.msg("Refund what?")



class CmdDebt(default_cmds.MuxCommand):
    """
    Buy Debt EXP (minimum 8).  Unlocks the exotic skills: sorcery and heavyarms
    Usable only during character generation.

    Usage:
      debt #exp
    """

    key = "debt"
    aliases = []
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.debt()"""
        arglist = re.split(r'\s+', self.args)

        if( len(arglist) >= 1 and re.match('^[0-9]+$', arglist[0]) ):
            self.msg(self.caller.debt( int(arglist[0]) ))
        else:
            self.msg("Debt Usage: debt #exp")



class CmdFinalize(default_cmds.MuxCommand):
    """
    Complete your character generation.

    Usage:
      finalize
    """

    key = "finalize"
    aliases = []
    locks = "cmd:all()"

    def func(self):
        """Mostly just a pass through to typeclasses.character.Character.sheet()"""
        self.msg((self.caller.finalize(), {'type':'sheet'}), options=None)
