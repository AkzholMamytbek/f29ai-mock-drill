# My solutions

My own solutions to the F29AI Mock Drill tasks, written while preparing for the class test.

**Progress: 32 / 63 tasks solved.**

| Part | Task | Solved |
|---|---|---|
| 1. One action (1 loop) | `sum_probs(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `expected_reward(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `prob_to_reach(transitions, s, a, target)` | ✅ |
| 1. One action (1 loop) | `terminal_prob(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `next_states(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `max_outcome_reward(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `min_outcome_reward(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `count_positive_outcomes(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `is_deterministic_action(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `most_likely_next_state(transitions, s, a)` | ✅ |
| 1. One action (1 loop) | `expected_next_value(transitions, s, a, V)` | ✅ |
| 1. One action (1 loop) | `q_value(transitions, V, s, a, gamma)` | ✅ |
| 2. One state (2 loops) | `num_actions_in(transitions, s)` | ✅ |
| 2. One state (2 loops) | `reachable_states(transitions, state)` | ✅ |
| 2. One state (2 loops) | `outcomes_in_state(transitions, s)` | ✅ |
| 2. One state (2 loops) | `max_reward_in_state(transitions, s)` | ✅ |
| 2. One state (2 loops) | `has_self_loop(transitions, s)` | ✅ |
| 2. One state (2 loops) | `can_terminate(transitions, s)` | ✅ |
| 2. One state (2 loops) | `terminal_actions(transitions, s)` | ✅ |
| 2. One state (2 loops) | `best_reward_action(transitions, s)` | ✅ |
| 2. One state (2 loops) | `avg_expected_reward(transitions, s)` | ✅ |
| 3. Whole MDP (3 loops) | `count_outcomes(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `count_terminal_outcomes(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `count_zero_prob_outcomes(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `total_actions(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `max_actions(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `max_reward(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `min_reward(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `has_negative_reward(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `unique_rewards(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `terminal_targets(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `valid_mdp(transitions)` | ✅ |
| 3. Whole MDP (3 loops) | `probs_in_range(transitions)` | — |
| 3. Whole MDP (3 loops) | `count_self_loops(transitions)` | — |
| 4. Lists of states & tables | `num_actions(transitions)` | — |
| 4. Lists of states & tables | `states_with_one_action(transitions)` | — |
| 4. Lists of states & tables | `outcomes_per_state(transitions)` | — |
| 4. Lists of states & tables | `states_reaching(transitions, target)` | — |
| 4. Lists of states & tables | `terminating_states(transitions)` | — |
| 4. Lists of states & tables | `stochastic_states(transitions)` | — |
| 4. Lists of states & tables | `deterministic_states(transitions)` | — |
| 4. Lists of states & tables | `always_terminal_states(transitions)` | — |
| 4. Lists of states & tables | `states_with_choice(transitions)` | — |
| 4. Lists of states & tables | `expected_reward_table(transitions)` | — |
| 4. Lists of states & tables | `best_reward_actions(transitions)` | — |
| 4. Lists of states & tables | `terminal_prob_table(transitions)` | — |
| 5. Reward lists | `total_reward(rewards)` | — |
| 5. Reward lists | `discounted_return(rewards, gamma)` | — |
| 5. Reward lists | `discount_weights(gamma, n)` | — |
| 5. Reward lists | `discounted_return_from(rewards, gamma, t)` | — |
| 5. Reward lists | `returns_each_step(rewards, gamma)` | — |
| 5. Reward lists | `first_positive_step(rewards)` | — |
| 6. Exam mix | `bellman_backup(transitions, V, s, gamma)` | — |
| 6. Exam mix | `best_action(transitions, V, s, gamma)` | — |
| 6. Exam mix | `q_table(transitions, V, gamma)` | — |
| 6. Exam mix | `greedy_policy(transitions, V, gamma)` | — |
| 6. Exam mix | `value_iteration(transitions, gamma, k)` | — |
| 6. Exam mix | `policy_evaluation(transitions, policy, gamma, k)` | — |
| 6. Exam mix | `td_update(V, s, r, s2, alpha, gamma, terminal)` | — |
| 6. Exam mix | `q_learning_update(Q, s, a, r, s2, alpha, gamma, terminal)` | — |
| 6. Exam mix | `greedy_action(Q, s)` | — |
| 6. Exam mix | `prob_greedy(epsilon, n_actions)` | — |
| 6. Exam mix | `average_q(Q, s)` | — |

Files: `part1_one_action.py`, `part2_one_state.py`, `part3_whole_mdp.py`.
