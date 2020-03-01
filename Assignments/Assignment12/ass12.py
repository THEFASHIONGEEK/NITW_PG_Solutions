# The model of the maze environment is provided for your reference.

import numpy as np
import sys
import pandas as pd

ACTION_UP    =  0
ACTION_RIGHT =  1
ACTION_DOWN  =  2
ACTION_LEFT  =  3

class GridWorld(object):
    def __init__(self,shape=[5,5]):
        self.shape = shape


        numStates  = shape[0] * shape[1]
        numActions = 4
        self.numStates = numStates
        self.numActions = numActions
        
        xmax = shape[0]
        ymax = shape[1]

        grid = np.arange(numStates).reshape(shape)

        Model = {}

        x_indices = np.arange(xmax)
        y_indices = np.arange(ymax)

        for x in x_indices:
            for y in y_indices:
                state = y + x*(xmax)
                #print(x,y,state)
                Model[state] ={action:[] for action in np.arange(numActions)}

                is_terminal_state = lambda state : state == 0 or state == (numStates-1)
                reward = 0.0 if is_terminal_state(state) else -1.0


                if is_terminal_state(state):
                    Model[state][ACTION_UP] = [(1.0,state,reward,True)]
                    Model[state][ACTION_RIGHT] = [(1.0,state,reward,True)]
                    Model[state][ACTION_DOWN] = [(1.0,state,reward,True)]
                    Model[state][ACTION_LEFT] = [(1.0,state,reward,True)]
                else:
                    next_state = {}
                    next_state[ACTION_UP] = state if x == 0 else state - ymax
                    next_state[ACTION_RIGHT] = state if y == ymax-1 else state +1
                    next_state[ACTION_DOWN] = state if x == xmax-1 else state + ymax
                    next_state[ACTION_LEFT] = state if y == 0 else state -1 
                    Model[state][ACTION_UP] = [(1.0,next_state[ACTION_UP] ,reward,is_terminal_state(next_state[ACTION_UP]))]
                    Model[state][ACTION_RIGHT] = [(1.0,next_state[ACTION_RIGHT],reward,is_terminal_state(next_state[ACTION_RIGHT]))]
                    Model[state][ACTION_DOWN] = [(1.0,next_state[ACTION_DOWN],reward,is_terminal_state(next_state[ACTION_DOWN]))]
                    Model[state][ACTION_LEFT] = [(1.0,next_state[ACTION_LEFT],reward,is_terminal_state(next_state[ACTION_LEFT]))]
        self.model = Model

# Write a function to calculate the value for all the actions in a given state  

def value_iteration(env, theta=0.0001, discount_factor=1.0):
# Helper function to calculate the value for all actions in a given state    
    def compute_value_fn_update(state,value_fn):
        value_fn_update = np.zeros(env.numActions)
        for action in range(env.numActions):
            for prob,next_state,reward,done in env.model[state][action]:
                value_fn_update[action] += prob * (reward + discount_factor * value_fn[next_state])
                
        return value_fn_update 
    
    value_fn = np.zeros(env.numStates)
    while True:
# Stopping Condition        
        delta = 0
# Update each state        
        for state in range(env.numStates):
# Find the best action
            action_values = compute_value_fn_update(state, value_fn)
            best_action_value = np.max(action_values)
# Calculate delta across all states seen so far
            delta = max(delta, np.abs(best_action_value - value_fn[state]))
# Update the value function
            value_fn[state] = best_action_value        
# Check if we can stop       
        if delta < theta:
            break
    
    # Create a deterministic policy by using the optimal value function
    policy = np.zeros([env.numStates, env.numActions])
    for state in range(env.numStates):
    # Find the best action for this state
        A = compute_value_fn_update(state, value_fn)
        best_action = np.argmax(A)
        # Always take the best action
        policy[state, best_action] = 1.0
    
    return policy, value_fn    
# Write the code to create a deterministic policy by using the optimal value function. Print the optimal policy.
env = GridWorld()
policy, value_fn = value_iteration(env)
     # Write your code here
data = np.reshape(np.argmax(policy, axis=1), env.shape)   
# Save the final output as described in the sample format given below 
output = pd.DataFrame(data)
output.columns = ['A','B','C','D','E']
# data= np.array([[1, 2, 3, 4, 5], [0, 0, 4, 1, 2],[3, 4, 1, 0, 2],[2, 1, 3, 4, 5],[2, 1, 3, 4, 5]])
# output=pd.DataFrame(data)
output.to_csv('/code/output/output.csv', index=False)