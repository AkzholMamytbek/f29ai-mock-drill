"""F29AI Mock Drill, Part 3: Whole MDP (3 loops).

My own solutions, written while practising. Each passed the task's tests in the trainer.
The example MDPs EX, STUDY and M3 come from the trainer (see src/build.py).
"""

# ----------------------------------------------------------------------
# count_outcomes(transitions)
# Return the total number of outcomes in the MDP.
# ----------------------------------------------------------------------
def count_outcomes(transitions):
    total=0
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                total+=1
    return total


# ----------------------------------------------------------------------
# count_terminal_outcomes(transitions)
# Return how many outcomes in the MDP have terminal == True.
# ----------------------------------------------------------------------
def count_terminal_outcomes(transitions):
    total=0
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                if terminal:
                    total+=1
    return total


# ----------------------------------------------------------------------
# count_zero_prob_outcomes(transitions)
# Return how many outcomes in the MDP have probability exactly 0.
# ----------------------------------------------------------------------
def count_zero_prob_outcomes(transitions):
    total=0
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                if prob==0:
                    total+=1
    return total


# ----------------------------------------------------------------------
# total_actions(transitions)
# Return the total number of actions in the MDP (summed over all states).
# ----------------------------------------------------------------------
def total_actions(transitions):
    total=0
    for actions in transitions:
        for outcomes in actions:
                total+=1
    return total


# ----------------------------------------------------------------------
# max_actions(transitions)
# Return the largest number of actions that any single state has.
# ----------------------------------------------------------------------
def max_actions(transitions):
    best=None
    for actions in transitions:
        for outcomes in actions:
            if best is None or len(actions) > best:
                best=len(actions)
    return best


# ----------------------------------------------------------------------
# max_reward(transitions)
# Return the largest reward of any outcome in the MDP.
# ----------------------------------------------------------------------
def max_reward(transitions):
    best=None
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                if best is None or reward>best:
                    best=reward
    return best


# ----------------------------------------------------------------------
# min_reward(transitions)
# Return the smallest reward of any outcome in the MDP.
# ----------------------------------------------------------------------
def min_reward(transitions):
    smallest=None
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state, reward,terminal in outcomes:
                if smallest is None or reward<smallest:
                    smallest=reward
    return smallest


# ----------------------------------------------------------------------
# has_negative_reward(transitions)
# Return True if any outcome in the MDP has a negative reward, otherwise False.
# ----------------------------------------------------------------------
def has_negative_reward(transitions):
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                if reward<0:
                    return True
    return False


# ----------------------------------------------------------------------
# unique_rewards(transitions)
# Return a sorted list of all **different** rewards that appear in the MDP.
# ----------------------------------------------------------------------
def unique_rewards(transitions):
    result=set()
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                result.add(reward)
    return sorted(result)


# ----------------------------------------------------------------------
# terminal_targets(transitions)
# Return a sorted list (no duplicates) of the next_states that appear in a terminal outcome anywhere in the MDP.
# ----------------------------------------------------------------------
def terminal_targets(transitions):
    result=set()
    for actions in transitions:
        for outcomes in actions:
            for prob,next_state,reward,terminal in outcomes:
                if terminal:
                    result.add(next_state)
    return sorted(result)


# ----------------------------------------------------------------------
# valid_mdp(transitions)
# Return True if, for every state and action, the outcome probabilities add up to 1 (within 1e-9). Otherwise False.
# ----------------------------------------------------------------------
def valid_mdp(transitions):
    for actions in transitions:
        for outcomes in actions:
            total=0.0
            for prob,next_state,reward,terminal in outcomes:
                total+=prob
            if abs(total-1.0)>1e-9:
                    return False    
    return True
