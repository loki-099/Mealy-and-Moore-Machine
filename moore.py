class MooreState:
    def __init__(self, state, output):
        self.state = state
        self.output = output  # output depends only on state
        self.transitions = []

    def addTransition(self, input, nextState):
        self.transitions.append((input, nextState))


class MooreMachine:
    def __init__(self, initialState):
        self.states = {}
        self.currentState = initialState

    def addState(self, state):
        self.states[state.state] = state

    def reset(self, state):
        self.currentState = state

    def processInput(self, input):
        state = self.states[self.currentState]
        output = state.output  # initial state's output is part of the result
        for char in input:
            for transition in state.transitions:
                if char == transition[0]:
                    self.currentState = transition[1]
                    state = self.states[self.currentState]
                    output += state.output
                    break
        print(f"Input: {input}")
        print(f"Output: {output}")


# Example usage:
if __name__ == "__main__":
    MooreMachineExample = MooreMachine("A")

    # Create states with outputs
    A = MooreState("A", "b")
    B = MooreState("B", "b")
    C = MooreState("C", "a")

    MooreMachineExample.addState(A)
    MooreMachineExample.addState(B)
    MooreMachineExample.addState(C)

    # Define transitions
    A.addTransition("0", "B")
    A.addTransition("1", "A")
    B.addTransition("0", "B")
    B.addTransition("1", "C")
    C.addTransition("0", "B")
    C.addTransition("1", "A")

    # Test runs
    MooreMachineExample.processInput("0110")
    MooreMachineExample.reset("A")
    MooreMachineExample.processInput("1001100")
    MooreMachineExample.reset("A")
    MooreMachineExample.processInput("01010101")
    MooreMachineExample.reset("A")
    MooreMachineExample.processInput("01110101")
    MooreMachineExample.reset("A")
    MooreMachineExample.processInput("100010101")
