"""Validate every task and build ../index.html.

For each task the model solution is run against its tests to compute the
expected values; the solution must pass all tests and the starter code must not.

Usage (from the repository root):  python3 src/build.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import harness_py as H  # noqa: E402

# A third example MDP used by many tests (4 states, one zero-probability outcome).
H._SETUP = H._SETUP + '''
M3 = [
    [[(0.7, 1, 5.0, False), (0.3, 2, -1.0, False)],
     [(1.0, 3, 10.0, True)],
     [(0.5, 0, 0.0, False), (0.25, 1, 2.0, False), (0.25, 3, -4.0, True)]],
    [[(1.0, 2, 3.0, False)],
     [(0.6, 3, 8.0, True), (0.4, 1, -2.0, False)]],
    [[(1.0, 0, -1.0, False), (0.0, 3, 100.0, True)]],
    [[(1.0, 3, 0.0, True)]],
]
'''

import mock_tasks  # noqa: E402,F401
from dsl import LESSONS  # noqa: E402


def fresh_ns(code=""):
    ns = {}
    exec(H._SETUP, ns)
    if code:
        exec(code, ns)
    return ns


def main():
    problems, ids, n_ex = [], set(), 0
    for L in LESSONS:
        for b in L["blocks"]:
            if b["t"] == "code":
                b["output"] = ""  # pattern snippets, not runnable examples
            elif b["t"] == "ex":
                n_ex += 1
                if b["id"] in ids:
                    problems.append("duplicate id " + b["id"])
                ids.add(b["id"])
                b["tests"] = [{"expr": e, "expected": repr(eval(e, fresh_ns(b["solution"])))} for e in b["tests"]]
                res = json.loads(H._check(b["solution"], json.dumps(b["tests"])))
                if res["error"] or not all(r["pass"] for r in res["results"]):
                    problems.append(f"solution fails {b['id']}: {res}")
                res2 = json.loads(H._check(b["starter"], json.dumps(b["tests"])))
                if not res2["error"] and all(r["pass"] for r in res2["results"]):
                    problems.append(f"starter passes {b['id']}")
    if problems:
        print("\n".join(problems))
        sys.exit(1)

    data = {"lessons": LESSONS, "setup": H._SETUP}
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    with open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8") as f:
        f.write(template.replace("__DATA__", blob))
    print(f"OK: {len(LESSONS)} sections, {n_ex} tasks -> index.html")


if __name__ == "__main__":
    main()
