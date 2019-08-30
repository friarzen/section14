"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia.utils import pad


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        self.db.interpersonal = { 
                           'authority': 0,
                           'charm': 0,
                           'coptalk': 0,
                           'detect_bullshit': 0,
                           'flattery': 0,
                           'humint': 0,
                           'impersonate': 0,
                           'inspiration': 0,
                           'interrogation': 0,
                           'intimidation': 0,
                           'negotiation': 0,
                           'reassurance': 0,
                           'respect': 0,
                           'taunt': 0,
            }

        self.db.academic = { 
                           'accounting': 0,
                           'anthropology': 0,
                           'astronomy': 0,
                           'biology': 0,
                           'botany': 0,
                           'geology': 0,
                           'history': 0,
                           'law': 0,
                           'linquistics': 0,
                           'medicine': 0,
                           'military_science': 0,
                           'occult': 0,
                           'psychology': 0,
                           'religion': 0,
                           'research': 0,
                           'trivia': 0,
                           'xenology': 0,
                           'xenobiology': 0,
            }

        self.db.technical = { 
                           'architecture': 0,
                           'aura_reading': 0,
                           'chemistry': 0,
                           'computer_science': 0,
                           'cryptography': 0,
                           'forensics': 0,
                           'forgery': 0,
                           'magic': 0,
                           'notice': 0,
                           'physics': 0,
                           'sigint': 0,
                           'streetwise': 0,
                           'survival': 0,
                           'tradecraft': 0,
                           'traffic_analysis': 0,
            }

        self.db.gskills = {
                           'athletics': 0,
                           'bureaucracy': 0,
                           'conceal': 0,
                           'demolitions': 0,
                           'disguise': 0,
                           'drive': 0,
                           'filch': 0,
                           'firearms': 0,
                           'hacking': 0,
                           'heavyarms': 0,
                           'infiltration': 0,
                           'melee_humanoid': 0,
                           'melee_nonhuman': 0,
                           'medic': 0,
                           'piloting': 0,
                           'preparedness': 0,
                           'psychotherapy': 0,
                           'ride': 0,
                           'schmooze': 0,
                           'sense_trouble': 0,
                           'sorcery': 0,
                           'stealth': 0,
                           'surveillance': 0,
                           'tinkering': 0,
            }

        self.db.gpools = {
                           'athletics': 0,
                           'bureaucracy': 0,
                           'conceal': 0,
                           'demolitions': 0,
                           'disguise': 0,
                           'drive': 0,
                           'filch': 0,
                           'firearms': 0,
                           'hacking': 0,
                           'heavyarms': 0,
                           'infiltration': 0,
                           'melee_humanoid': 0,
                           'melee_nonhuman': 0,
                           'medic': 0,
                           'piloting': 0,
                           'preparedness': 0,
                           'psychotherapy': 0,
                           'ride': 0,
                           'schmooze': 0,
                           'sense_trouble': 0,
                           'sorcery': 0,
                           'stealth': 0,
                           'surveillance': 0,
                           'tinkering': 0,
            }

        self.db.health = 4
        self.db.sanity = 4

        self.db.to_be_hit_melee = 6
        self.db.to_be_hit_ranged = 6
        self.db.armor_melee = 0
        self.db.armor_ballistic = 0


    def sheet(self):
        ipersonal = self.db.interpersonal
        academic  = self.db.academic
        technical = self.db.technical
        gskills   = self.db.gskills
        gpools    = self.db.gpools

        keys_i = list(ipersonal.keys())
        keys_a = list(academic.keys())
        keys_t = list(technical.keys())
        keys_g = list(gskills.keys())
        keys_p = list(gpools.keys())

        m = max([len(keys_i), len(keys_a), len(keys_t), len(keys_g), len(keys_p),])

        text  = f"================================================================================\n"
        text += f"General Skills          Interpersonal       Academic            Technical\n"
        text += f"================================================================================\n"
        for x in range(0,m):
            i = ""
            a = ""
            t = ""
            g = ""
            p = ""

            if x < len(keys_i):
                i = keys_i[x]
                if( ipersonal[i] > 0 ):
                   i = f"|w{keys_i[x]}|n"

            if x < len(keys_a):
                a = keys_a[x]
                if( academic[a] > 0 ):
                    a = f"|w{keys_a[x]}|n"

            if x < len(keys_t):
                t = keys_t[x]
                if( technical[t] > 0 ):
                    t = f"|w{keys_t[x]}|n"

            if x < len(keys_g):
                g = keys_g[x]
                gval = gskills[g]

            if x < len(keys_p):
                p = keys_p[x]
                pval = gpools[p]

            text += f"|w{pad(keys_g[x],width=16,align='l')}|n {pval}/{gval}    "
            text += f"{pad(i, width=20, align='l')}"
            text += f"{pad(a, width=20, align='l')}"
            text += f"{t}\n"
        return text
