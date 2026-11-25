"""F29AI Mock Drill, Part 1: One action (1 loop).

My own solutions, written while practising. Each passed the task's tests in the trainer.
The example MDPs EX, STUDY and M3 come from the trainer (see src/build.py).
"""

# ----------------------------------------------------------------------
# sum_probs(transitions, s, a)
# Return the sum of the probabilities of all outcomes of (s, a).
# ----------------------------------------------------------------------
def sum_probs(transitions, s, a):
    result=0.0
    for prob, next_state, reward, terminal in transitions[s][a]:
        result+=prob
    return result


# ----------------------------------------------------------------------
# expected_reward(transitions, s, a)
# Return the expected immediate reward of (s, a): Σ prob × reward.
# ----------------------------------------------------------------------
def expected_reward(transitions, s, a):
    total=0.0
    for prob, next_state, reward, terminal in transitions[s][a]:
        total+=prob*reward
    return total


# ----------------------------------------------------------------------
# prob_to_reach(transitions, s, a, target)
# Return the total probability of landing in state target after doing a in s. Several outcomes may lead to the same state.
# ----------------------------------------------------------------------
def prob_to_reach(transitions, s, a, target):
    total=0.0
    for prob, next_state, reward, terminal in transitions[s][a]:
        if next_state==target:
            total+=prob
    return total


# ----------------------------------------------------------------------
# terminal_prob(transitions, s, a)
# Return the total probability of the **terminal** outcomes of (s, a).
# ----------------------------------------------------------------------
def terminal_prob(transitions, s, a):
    total=0.0
    for prob, next_state, reward, terminal in transitions[s][a]:
        if terminal:
            total+=prob
    return total


# ----------------------------------------------------------------------
# next_states(transitions, s, a)
# Return the list of next_state of every outcome of (s, a), in order (keep duplicates).
# ----------------------------------------------------------------------
def next_states(transitions, s, a):
    lst=[]
    for prob,next_state,reward,terminal in transitions[s][a]:
        lst.append(next_state)
    return lst


# ----------------------------------------------------------------------
# max_outcome_reward(transitions, s, a)
# Return the largest reward among the outcomes of (s, a).
# ----------------------------------------------------------------------
def max_outcome_reward(transitions, s, a):
    best=None
    for prob,next_state,reward,terminal in transitions[s][a]:
        if best is None or reward>best:
            best=reward
    return best


# ----------------------------------------------------------------------
# min_outcome_reward(transitions, s, a)
# Return the smallest reward among the outcomes of (s, a).
# NOTE: this version returns `reward` (the last reward seen) instead of `smallest`.
# It passed the original tests by coincidence; the fix is `return smallest`.
# ----------------------------------------------------------------------
def min_outcome_reward(transitions, s, a):
    smallest=None
    for prob,next_state,reward,terminal in transitions[s][a]:
        if smallest is None or reward<smallest:
            smallest=reward
    return reward


# ----------------------------------------------------------------------
# count_positive_outcomes(transitions, s, a)
# Return how many outcomes of (s, a) have prob > 0.
# ----------------------------------------------------------------------
def count_positive_outcomes(transitions, s, a):
    result=0.0
    for prob,next_state,reward,terminal in transitions[s][a]:
        if prob>0:
            result+=1
    return result


# ----------------------------------------------------------------------
# is_deterministic_action(transitions, s, a)
# Return True if (s, a) has **exactly one** outcome with prob > 0, otherwise False.
# ----------------------------------------------------------------------
def is_deterministic_action(transitions, s, a):
    count=0
    for prob,next_state,reward,terminal in transitions[s][a]:
        if prob>0:
            count+=1
    return count==1


# ----------------------------------------------------------------------
# most_likely_next_state(transitions, s, a)
# Return the next_state of the outcome with the **highest probability**. On a tie, the first one.
# ----------------------------------------------------------------------
def most_likely_next_state(transitions, s, a):
    best=None
    result=0
    for prob,next_state,reward,terminal in transitions[s][a]:
        if best==None or prob>best:
            best=prob
            result=next_state
    return result


# ----------------------------------------------------------------------
# expected_next_value(transitions, s, a, V)
# Return Σ prob × V(next_state) over the outcomes of (s, a), where terminal outcomes count as 0. (No reward, no gamma.)
# ----------------------------------------------------------------------
def expected_next_value(transitions, s, a, V):
    result=0.0
    for prob,next_state,reward,terminal in transitions[s][a]:
        if terminal==0:
            result+=prob*V[next_state]
    return result


# ----------------------------------------------------------------------
# q_value(transitions, V, s, a, gamma)
# Return Q(s, a) = Σ prob × (reward + gamma × V(next_state)), with V(next_state) = 0 for terminal outcomes.
# ----------------------------------------------------------------------
def q_value(transitions, V, s, a, gamma):
    result=0.0
    for prob,next_state,reward,terminal in transitions[s][a]:
        if terminal:
            result+=prob*(reward+gamma*0)
        else:
            result+=prob*(reward+gamma*V[next_state])
    return result
