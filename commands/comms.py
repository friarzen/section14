"""
Override the default comms permisssions, not EVERYONE should have the ability to randomly create channels.
"""
from evennia.commands.default.comms import CmdChannelCreate, CmdCdestroy

class MyCmdChannelCreate(CmdChannelCreate):
    """
    create a new channel

    Usage:
     ccreate <new channel>[;alias;alias...] = description

    Creates a new channel owned by you.
    """
    key = "ccreate"
    aliases = "channelcreate"
    locks = "cmd: pperm(Builder) and not pperm(channel_banned)"
    help_category = "Comms"

    def func(self):
        super();


class MyCmdCdestroy(CmdCdestroy):
    """
    destroy a channel you created

    Usage:
      cdestroy <channel>

    Destroys a channel that you control.
    """

    key = "cdestroy"
    help_category = "Comms"
    locks = "cmd: pperm(Builder) and not pperm(channel_banned)"

    # this is used by the COMMAND_DEFAULT_CLASS parent
    account_caller = True

    def func(self):
        super();
