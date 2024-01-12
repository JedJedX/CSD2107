import random
from game import Agent
from game import Directions
class DumbAgent(Agent):
    "An agent thay goes West until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        
        print("Location: ",state.getPacmanPosition())
        print("Action availble: ",state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP

class randomAgent(Agent):
    "An agent that picks random legal action"
    
    def getAction(self,state):
        "The agent receives a GameState (defined in pacman.py)"
        print(('Location:'), state.getPacmanPosition())
        listofaction = state.getLegalPacmanActions()[:]
        listofaction.remove(Directions.STOP)
        print (('Actions available:'), listofaction)
        action = random.choice(listofaction)
        print("Going" + action)
        return action
class ReflexAgent(Agent):

    def getAction(self, state):

        print(('Location:'), state.getPacmanPosition())
        listofaction = state.getLegalPacmanActions()[:]
        listofaction.remove(Directions.STOP)
        print(('Actions available:'), listofaction)
        num_food = state.getNumFood()
        for act in listofaction:
            if num_food > state.generatePacmanSuccessor(act).getNumFood():

                return act
        return random.choice(listofaction)