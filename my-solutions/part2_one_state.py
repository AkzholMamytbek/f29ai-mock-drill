"""F29AI Mock Drill, Part 2: One state (2 loops).

My own solutions, written while practising. Each passed the task's tests in the trainer.
The example MDPs EX, STUDY and M3 come from the trainer (see src/build.py).
"""

# ----------------------------------------------------------------------
# num_actions_in(transitions, s)
# Return how many actions state s has.
# ----------------------------------------------------------------------
def num_actions_in(transitions, s):
    result=0
    for a in transitions[s]:
        result+=1
    return result


# ----------------------------------------------------------------------
# reachable_states(transitions, state)
# Return a sorted list (no duplicates) of the states reachable in one step from state, using any action, through outcomes with prob > 0.
# ----------------------------------------------------------------------
def reachable_states(transitions, state):
    result=set()
    for outcomes in transitions[state]:
        for prob,next_state, reward,terminal in outcomes:
            if prob>0:
                result.add(next_state)
    return sorted(result)


# ----------------------------------------------------------------------
# outcomes_in_state(transitions, s)
# Return the total number of outcomes over all actions of state s.
# ----------------------------------------------------------------------
def outcomes_in_state(transitions, s):
    result=0
    for outcomes in transitions[s]:
        for prob,next_state,reward,terminal in outcomes:
            result+=1
    return result


# ----------------------------------------------------------------------
# max_reward_in_state(transitions, s)
# Return the largest reward of any outcome of any action of state s.
# ----------------------------------------------------------------------
def max_reward_in_state(transitions, s):
    best=None
    for outcomes in transitions[s]:
        for prob,next_state,reward,terminal in outcomes:
            if best is None or reward>best:
                best=reward
    return best


# ----------------------------------------------------------------------
# has_self_loop(transitions, s)
# Return True if some outcome (with prob > 0) of some action of s leads back to s itself.
# ----------------------------------------------------------------------
def has_self_loop(transitions, s):
    for outcomes in transitions[s]:
        for prob,next_state, reward,terminal in outcomes:
            if prob>0 and s==next_state:
                return True
    return False


# ----------------------------------------------------------------------
# can_terminate(transitions, s)
# Return True if some action of s has a terminal outcome with prob > 0.
# ----------------------------------------------------------------------
def can_terminate(transitions, s):
    for outcomes in transitions[s]:
        for prob,next_state,reward,terminal in outcomes:
            if prob>0 and terminal:
                return True
    return False


# ----------------------------------------------------------------------
# terminal_actions(transitions, s)
# Return the list of action indices of s that have at least one terminal outcome with prob > 0. Each action at most once.
# ----------------------------------------------------------------------
def terminal_actions(transitions, s):
    lst=[]
    for a,outcomes in enumerate(transitions[s]):
        for prob,next_state,reward,terminal in outcomes:
            if prob>0 and terminal:
                lst.append(a)
                break
    return lst


# ----------------------------------------------------------------------
# best_reward_action(transitions, s)
# Return the index of the action of s with the highest expected immediate reward (Σ prob × reward). Ties → lowest index.
# ----------------------------------------------------------------------
def best_reward_action(transitions, s):
    best_a=0
    best_r=None
    for a in range(len(transitions[s])):
        imreward=0
        for prob,next_state,reward,terminal in transitions[s][a]:
            imreward+=prob*reward
        if best_r is None or imreward>best_r:
            best_a=a
            best_r=imreward
    return best_a


# ----------------------------------------------------------------------
# avg_expected_reward(transitions, s)
# Return the average, over the actions of s, of each action's expected immediate reward.
# ----------------------------------------------------------------------
def avg_expected_reward(transitions, s):
    result=0
    for a in transitions[s]:
        for prob,next_state,reward,terminal in a:
            result+=prob*reward
    return result /len(transitions[s])
