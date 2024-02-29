from enum import Enum
import numpy as np
from time import sleep
# from brain.brain import act_at

from brain.game.constants import find_card

from brain.game.constants import (DECK_LOCATION, FLOP_LOCATIONS, TURN_LOCATION,
                                  RIVER_LOCATION, FLIP_LOC)

class State(Enum):
        FLOP = 1
        TURN = 2
        RIVER = 3


class CommunityCardsDealer():

    def __init__(self, node):
        self.curr_state = State.FLOP
        self.node = node

    def run(self):
        if self.curr_state == State.FLOP:
            for i in range(3):
                self.node.act_at(DECK_LOCATION, np.pi/2, "GB_CARD")
                self.node.act_at(FLIP_LOC, 0.0, "FLIP")
                loc, theta = find_card(self.node)
                self.node.act_at(loc, theta, "GB_CARD")
                self.node.act_at(FLOP_LOCATIONS[i], 0.0, "DROP")
                sleep(4)
            self.curr_state = State.TURN
            return

        elif self.curr_state == State.TURN:
            self.node.act_at(DECK_LOCATION, np.pi/2, "GB_CARD")
            self.node.act_at(FLIP_LOC, 0.0, "FLIP")
            loc, theta = find_card(self.node)
            self.node.act_at(loc, theta, "GB_CARD")
            self.node.act_at(TURN_LOCATION, 0.0, "DROP")
            self.curr_state = State.RIVER
            return

        elif self.curr_state == State.RIVER:
            self.node.act_at(DECK_LOCATION, np.pi/2, "GB_CARD")
            self.node.act_at(FLIP_LOC, 0.0, "FLIP")
            loc, theta = find_card(self.node)
            self.node.act_at(loc, theta, "GB_CARD")
            self.node.act_at(RIVER_LOCATION, 0.0, "DROP")
            self.curr_state == State.FLOP
            return 
