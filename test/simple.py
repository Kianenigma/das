import sys

import common.user, common.game, common.command
from common.constants import USERS
import emulation.GTAEventsReader

listOfEvents = emulation.GTAEventsReader.LoadEventsFromFile('WoWSession_Node_Player_Fixed_Dynamic.zip')

# Normalize the timeStamps of the Login/Logout events using the time between the the first and last login/logout events
listOfNormalizedEvents = emulation.GTAEventsReader.NormalizeEvents(listOfEvents, 10000)

print("Total number of Login/Logout events: " + str(len(listOfNormalizedEvents)))

g = common.game.Game()


h = common.user.User(USERS.PLAYER)
h1 = common.user.User(USERS.PLAYER)
g.add_user(h, 0, 0)
g.add_user(h1, 2, 0)
d = common.user.User(USERS.DRAGON)
g.add_user(d, 1, 0)


g.commands = [
    common.command.MoveCommand(h.id, 1, 'h'),
    common.command.AttackCommand(h.id, d.id),
    common.command.AttackCommand(d.id, h1.id),
    common.command.MoveCommand(h.id, 1, 'h'),
    common.command.HealCommand(h.id, h1.id)
]
try:
    # g.emulate_all()
    g._simulate(10000)
    g.emulate(3)

except KeyboardInterrupt:
    sys.exit()