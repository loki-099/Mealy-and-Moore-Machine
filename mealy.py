class MealyState:
    def __init__(self, state):
        self.state = state
        self.transitions = [];
        
    def addTransitions(self, input, nextState, output):
        self.transitions.append((input, nextState, output))

class MealyMachine:
    def __init__(self, initialState):
        self.states = {}
        self.currentState = initialState

    def addState(self, state):
        self.states[state.state] = state

    def reset(self, state):
        self.currentState = state

    def processInput(self, input):
        state = self.states[self.currentState]
        output = ""
        for char in input:
            for transition in state.transitions:
                if char == transition[0]:
                    output += transition[2]
                    self.currentState = transition[1]
                    state = self.states[self.currentState]
                    break
        print(f"Input: {input}")
        print(f"Output: {output}")
    
# Example usage:
if __name__ == "__main__":  
    MealyMachineExample = MealyMachine("A")

    # Create States
    A = MealyState("A")
    B = MealyState("B")
    C = MealyState("C")

    MealyMachineExample.addState(A)
    MealyMachineExample.addState(B)
    MealyMachineExample.addState(C) 

    # Define the transitions with input, next state, and the output
    A.addTransitions("0", "B", "b")
    A.addTransitions("1", "A", "b")
    B.addTransitions("0", "B", "b")
    B.addTransitions("1", "C", "a")
    C.addTransitions("0", "B", "b")
    C.addTransitions("1", "A", "b")

    # Run the tests
    MealyMachineExample.processInput("0110")
    MealyMachineExample.reset("A")
    MealyMachineExample.processInput("1001100")
    MealyMachineExample.reset("A")
    MealyMachineExample.processInput("01010101")
    MealyMachineExample.reset("A")
    MealyMachineExample.processInput("01110101")
    MealyMachineExample.reset("A")
    MealyMachineExample.processInput("100010101")