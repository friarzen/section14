"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia.utils import pad
from random import randint
from typeclasses.objects import Weapon
from evennia.utils.ansi import ANSIString

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
                           'melee': 0,
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
                           'melee': 0,
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
        self.db.mana = 0
        self.db.max_health = 4
        self.db.max_sanity = 4
        self.db.max_mana = 0

        self.db.to_be_hit_melee = 6
        self.db.to_be_hit_ranged = 6
        self.db.to_be_hit_aetheric = 6
        self.db.armor_melee = 0
        self.db.armor_ballistic = 0
        self.db.armor_aetheric = 0

        self.db.exp = 50
        self.db.ixp = 10
        self.db.debt = 0
        self.db.weapon = Weapon()

        self.db.chargen = True


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
                   i = ANSIString( f"|w{keys_i[x]}|n" )

            if x < len(keys_a):
                a = keys_a[x]
                if( academic[a] > 0 ):
                    a = ANSIString( f"|w{keys_a[x]}|n" )

            if x < len(keys_t):
                t = keys_t[x]
                if( technical[t] > 0 ):
                    t = ANSIString( f"|w{keys_t[x]}|n" )

            if x < len(keys_g):
                g = keys_g[x]
                gval = gskills[g]

            if x < len(keys_p):
                p = keys_p[x]
                pval = gpools[p]

            text += f"|w{pad(ANSIString(keys_g[x]), width=17, align='l')}|n"
            text += f"{pad(ANSIString(str(pval)), width=3, align='r')}/{gval}  "
            text += f"{pad(i, width=20, align='l')}"
            text += f"{pad(a, width=20, align='l')}"
            text += f"{t}\n"
        text += f"\n"
        text += f"|whealth|n: {self.db.health}/{self.db.max_health}             "
        text += f"|wsanity|n: {self.db.sanity}/{self.db.max_sanity}         "
        text += f"|wmana|n: {self.db.mana}/{self.db.max_mana}           "
        text += f"|wEXP|n: {self.db.exp}/{self.db.ixp}I"
        if self.db.debt > 0:
            text += f"/{self.db.debt}D"
        text += f"\n"
        text += f"\n"
        text += f"|wTo-Be-Hit|n: {self.db.to_be_hit_melee} Melee / {self.db.to_be_hit_ranged} Ranged / {self.db.to_be_hit_aetheric} Aetheric    "
        text += f"|wWeapon Equipped:    {self.db.weapon.key}|n\n"
        text += f"|wArmor|n:     {self.db.armor_melee} Melee / {self.db.armor_ballistic} Ranged / {self.db.armor_aetheric} Aetheric\n"
        return text


    def refresh(self, skillname, pips):
        skills = self.db.gskills
        pools = self.db.gpools

        if( skillname not in pools ):
            return f"{skillname} is not a refreshable pool."

        if( pools[ skillname ] + pips > skills[ skillname ] ):
            # we are trying to refresh a pool for more than its skill. reset pips.
            pips = skills[ skillname ] - pools[ skillname ]

        pools[ skillname ] += pips
        self.db.gpools = pools

        # TODO: announce to the room?
        return f"{skillname} pool refreshed {pips} pips"


    def roll(self, skillname, pipsspent):
        skills = self.db.gskills
        pools = self.db.gpools

        if( skillname not in pools ):
            return f"{skillname} is not a testable skill."

        if( skills[ skillname ] <= 0 ):
            # we are untrained in the skill and auto fail any test
            self.location.msg_contents( text=f"{self.key} attempts {skillname}... Result: untrained failure." )
            return f"You are not trained in {skillname}, you automatically fail the challenge."

        if( pipsspent > pools[skillname] ):
            return f"You do not have {pipsspent} pips left to spend in the {skillname} pool."

        if( pipsspent > 0 ):
            pools[skillname] -= pipsspent
            self.db.gpools = pools # save the spend back to the db

        die1 = randint(1,6)
        die2 = randint(1,6)

        result = die1+die2+pipsspent

        self.location.msg_contents( text=f"{self.key} attempts {skillname}... Result: {result}" )

        return f"Result: {result}"


    def spend(self, skillname, pipsspent):
        skills = self.db.gskills
        pools = self.db.gpools
        found = False

        if( pipsspent > self.db.exp ):
            return f"You do not have {pipsspent} EXP to spend.  EXP spend cancelled."

        if( skillname in skills ):
            if( ((skillname == "sorcery") or (skillname == "heavyarms")) and (skills[skillname] == 0) ):
                self.msg(f"{skillname} is an exotic skill.  The first pip will cost 8 exp.")
                pipsspent += 7
                if( (self.db.chargen is True) and (self.db.debt <= 0) ):
                    return f"You do not have any chargen debt. To acquire debt, use the 'debt #exp' command.  Spend cancelled."
                if( pipsspent > self.db.exp ):
                    return f"You do not have {pipsspent} EXP to spend.  EXP spend cancelled."
                skills[skillname] += pipsspent - 7
                pools[skillname] += pipsspent - 7
            else:
                skills[skillname] += pipsspent
                pools[skillname] += pipsspent
            self.db.gskills = skills
            self.db.gpools = pools
            self.db.exp -= pipsspent
            found = True
        else:
            if( skillname == "health" ):
                self.db.max_health += pipsspent
                self.db.health += pipsspent
                self.db.exp -= pipsspent
                found = True
            if( skillname == "sanity" ):
                self.db.max_sanity += pipsspent
                self.db.sanity += pipsspent
                self.db.exp -= pipsspent
                found = True
            if( skillname == "mana" ):
                self.db.max_mana += pipsspent
                self.db.mana += pipsspent
                self.db.exp -= pipsspent
                found = True

        if( found is False ):
            return f"{skillname} unknown. Spend XP on what?"

        return self.sheet()


    def ispend(self, skillname):
        if( self.db.chargen is True ):
            if( self.db.ixp <= 0 ):
                return f"You have already allocated your 10 starting ISkills, maybe refund something?"

            if( skillname in self.db.interpersonal and self.db.interpersonal[skillname] == 0 ):
                self.db.interpersonal[skillname] = 1
                self.db.ixp -= 1
            if( skillname in self.db.academic and self.db.academic[skillname] == 0 ):
                self.db.academic[skillname] = 1
                self.db.ixp -= 1
            if( skillname in self.db.technical and self.db.technical[skillname] == 0 ):
                self.db.technical[skillname] = 1
                self.db.ixp -= 1
        else:
            if( self.db.exp < 8 ):
                return f"You do not have 8 EXP to spend to buy a new Investigative Skill."

            self.db.exp -= 8

        return self.sheet()


    def refund(self, skillname):
        # only valid during chargen
        if( self.db.chargen is False ):
            raise Exception('how did we get here? https://xkcd.com/2200/')

        skills = self.db.gskills
        pools = self.db.gpools

        if( skillname in skills ):
            pips = skills[skillname]
            if( skillname == "sorcery" or skillname == "heavyarms" ):
                pips += 7

            skills[skillname] = 0
            pools[skillname] = 0
            self.db.gskills = skills
            self.db.gpools = pools
            self.db.exp += pips
        else:
            if( skillname == "health" ):
                pips = self.db.max_health - 4
                self.db.max_health = 4
                self.db.health = 4
                self.db.exp += pips
            if( skillname == "sanity" ):
                pips = self.db.max_sanity - 4
                self.db.max_sanity = 4
                self.db.sanity = 4
                self.db.exp += pips
            if( skillname == "mana" ):
                pips = self.db.max_mana 
                self.db.max_mana = 0
                self.db.mana = 0
                self.db.exp += pips

            if( skillname in self.db.interpersonal and self.db.interpersonal[skillname] > 0 ):
                self.db.interpersonal[skillname] = 0
                self.db.ixp += 1
            if( skillname in self.db.academic and self.db.academic[skillname] > 0 ):
                self.db.academic[skillname] = 0
                self.db.ixp += 1
            if( skillname in self.db.technical and self.db.technical[skillname] > 0 ):
                self.db.technical[skillname] = 0
                self.db.ixp += 1

        return self.sheet()


    def debt(self, debt):
        # only valid during chargen
        if( self.db.chargen is False ):
            raise Exception('how did we get here? https://xkcd.com/2200/')

        self.db.exp += debt
        self.db.debt += debt

        return self.sheet()


    def finalize(self, debt):
        # only valid during chargen
        if( self.db.chargen is False ):
            raise Exception('how did we get here? https://xkcd.com/2200/')

        self.db.chargen = False

        return "Character Finalized"
