import logging
from typing import Dict, List

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

class State:
   def __init__(self, stateKey: str):
      self.key = stateKey

   def execute(self, model):
      log.info("State: Setting '{}' state value.".format(self.key))
      mDict = model.__class__.__dict__
      if self.key not in mDict:
         raise NameError("State value '{}' not present in model!".format(self.key))
      setValue = mDict[self.key]
      setValue(model)

class Transition:
   def __init__(self, triggerKey: str, fromState: State, toState: State):
      self.key = triggerKey
      self.fromState = fromState
      self.toState = toState

   def execute(self, model, data: List):
      log.info("Transition: 'Executing '{}' transition with data='{}' -> from '{}' to '{}' state.".format(self.key, data, self.fromState.key, self.toState.key))
      mDict = model.__class__.__dict__
      if self.key not in mDict:
         raise NameError("Event '{}' not present in model!".format(self.key))
      event = mDict[self.key]
      if data:
         event(model, *data)
      else:
         event(model)

class FSM:
   def __init__(self, model, states: Dict, transitions: List, currentStateValue: str):
      self.model = model
      self.states = states
      self.transitions = transitions
      self.currentState = states[currentStateValue]
      self.currentTransition = None
      self.transitionData = []

   def triggerTransition(self, triggerKey: str, *args):
      log.info("FSM: Triggering '{}' transition with passing data='{}'.".format(triggerKey, args))
      
      for transition in self.transitions:
         if triggerKey == transition.key:
            if self.currentState.key == transition.fromState.key:
               self.currentTransition = transition
               if args is not None:
                  self.transitionData = args

   def execute(self):
      log.info("FSM: Executing Finite State Machine with self.currentTransition='{}'!".format(self.currentTransition))
      if (self.currentTransition):
         self.currentTransition.execute(self.model, self.transitionData)
         self.__setCurrentState(self.currentTransition.toState.key)
         self.currentTransition = None
      self.currentState.execute(self.model)

   def __setCurrentState(self, stateKey: str):
      self.currentState = self.states[stateKey]

