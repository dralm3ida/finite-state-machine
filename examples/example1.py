from enum import Enum, unique
from fsm import State, Transition, FSM

@unique
class StateName(Enum):
   A = "A"
   B = "B"
   C = "C"

STATES = {
   StateName.A.value: State(StateName.A.value),
   StateName.B.value: State(StateName.B.value),
   StateName.C.value: State(StateName.C.value),
}

@unique
class TriggerName(Enum):
   FORWARD = "forward"
   BACKWARD = "backward"

TRANSITIONS = [
   # 1 - A -> forward -> B
   Transition(TriggerName.FORWARD.value, STATES[StateName.A.value], STATES[StateName.B.value]),
   # 2 - B -> forward -> C
   Transition(TriggerName.FORWARD.value, STATES[StateName.B.value], STATES[StateName.C.value]),
   # 3 - C -> forward -> A
   Transition(TriggerName.FORWARD.value, STATES[StateName.C.value], STATES[StateName.A.value]),
   # 4 - A -> backward -> C
   Transition(TriggerName.BACKWARD.value, STATES[StateName.A.value], STATES[StateName.C.value]),
   # 5 - C -> backward -> B
   Transition(TriggerName.BACKWARD.value, STATES[StateName.C.value], STATES[StateName.B.value]),
   # 6 - B -> backward -> A
   Transition(TriggerName.BACKWARD.value, STATES[StateName.B.value], STATES[StateName.A.value]),
]

class EntityModel:
   """Entity model to be passed to FSM"""

   def __init__(self, attr1, attr2):
      self.attr1 = attr1
      self.attr2 = attr2

   stateValue=str
   attr1=int
   attr2=int

   # Entity model state values executions
   def A(self):
      self.stateValue = StateName.A.value

   def B(self):
      self.stateValue = StateName.B.value

   def C(self):
      self.stateValue = StateName.C.value

   # Entity model transition executions
   def forward(self):
      print("forward executed with success!")

   def backward(self, checkAttr1, checkAttr2):
      print("backward executed with success with checkAttr1='{}' and checkAttr2='{}'!".format(checkAttr1, checkAttr2))

def main():
   ''' Example 1 '''

   model = EntityModel(1, 2)
   fsm = FSM(model, STATES, TRANSITIONS, StateName.A.value)

   # A -> B
   fsm.triggerTransition(TriggerName.FORWARD.value)
   fsm.execute()
   # B -> C
   fsm.triggerTransition(TriggerName.FORWARD.value)
   fsm.execute()
   # C -> A
   fsm.triggerTransition(TriggerName.FORWARD.value)
   fsm.execute()
   # A -> C
   fsm.triggerTransition(TriggerName.BACKWARD.value, True, True)
   fsm.execute()
   # C -> B
   fsm.triggerTransition(TriggerName.BACKWARD.value, True, True)
   fsm.execute()
   # B -> A
   fsm.triggerTransition(TriggerName.BACKWARD.value, True, True)
   fsm.execute()

if __name__ == '__main__':
  main()