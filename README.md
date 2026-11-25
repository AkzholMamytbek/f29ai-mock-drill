# F29AI Mock Drill

**The main idea:** this is another practice resource for my fellow students, like [MDP Code Trainer](https://github.com/AkzholMamytbek/mdp-code-trainer), but focused **only on mock-test style exam tasks**. No long lessons: just many short tasks in the same format as the F29AI CodeRunner class test (MDPs and reinforcement learning), so you can drill until the patterns feel automatic.

> ⚠️ **Mock practice only.** These tasks are written in the *style* of the class test. They are not the real test questions.

## How to use

1. Open `index.html` in any modern browser. Nothing to install: Python runs in the page.
2. Read the task, write the function in the box, press **Check** (or Ctrl / Cmd + Enter).
3. Stuck? Open **Hint 1**, then **Hint 2**. The **Solution** button asks twice so you try first.
4. Progress and your code are saved in your browser.
5. The **Playground** button (bottom right) runs any code you like.

## What's inside

63 tasks, grouped by the pattern you need to write them:

| Part | Pattern | Tasks |
|---|---|---|
| 1. One action | given `s` and `a` → one loop over `transitions[s][a]` | 12 |
| 2. One state | given `s` → loop over the actions of `transitions[s]`, then their outcomes | 9 |
| 3. Whole MDP | only `transitions` → states → actions → outcomes | 13 |
| 4. Lists of states & tables | `enumerate`, flags, `break`, list of lists | 10 |
| 5. Reward lists | discounted return, step numbers, walking backwards | 6 |
| 6. Exam mix | Bellman backup, best action, value iteration, policy evaluation, TD, Q-learning | 11 |

All tasks use the test-style MDP format:

```python
transitions[s][a] = [(prob, next_state, reward, terminal), ...]
```

Three example MDPs (`EX`, `STUDY`, `M3`) are pre-loaded in every task and in the playground, and can be viewed at the top of the page.

Each check shows every test case with the expected and actual value, and explains common mistakes (missing `return`, missing `:`, index out of range, unpacking at the wrong level, infinite loops).

## How it works

- `index.html` is a single self-contained page. Python runs in the browser with [Skulpt](https://skulpt.org), loaded from the jsDelivr CDN, so an internet connection is needed.
- Tasks are written in Python in `src/mock_tasks.py` using a tiny DSL (`src/dsl.py`).
- `src/build.py` runs every model solution with CPython to compute the expected test values, checks that each solution passes and each starter does not, and writes `index.html`.

```bash
python3 src/build.py
```

## Disclaimer

An independent study aid, not official course material. Always follow your course's rules for assessments.

## License

MIT
