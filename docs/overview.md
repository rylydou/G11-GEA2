# Assignment Overview: CMP_SC 4050 Group Algorithm Engineering Assignment 2

**Worth:** 100 points · **Group work** · **Due:** November 12, 2026, 11:59 PM

> Note: The PDF says "Wednesday, November 12," but Nov 12, 2026 is a **Thursday**. (It also says "Monday, Nov 1," but Nov 1 is a Sunday.) Check the real due date with the instructor.

## The Big Idea

Start with a slow algorithm that gives the right answer, then build a faster one. Show that the fast one gives the same answers, measure how much faster it is, and explain why.

This happens twice:

1. **Divide and conquer:** counting inversions in an array.
2. **Dynamic programming:** the coin change problem.

## Ground Rules

- Keep everything in one repo: code, experiment scripts, data, and a README.
- Always check a fast algorithm against a simple, separately written slow one on small inputs.
- Make runs repeatable. If you use randomness, record the seeds.
- Time only the algorithm. Don't include plotting, file I/O, or printing in the timing.
- Use Big-O analysis to predict growth, then use experiments to see if the results match.
- Don't say tests *prove* the code is correct. Tests only show it works on the inputs you tried. Proof comes from a correctness argument.
- **AI is allowed**, but you must check everything it produces yourself and write an AI Use Statement. If you used no AI, say so.

---

## Part I: Counting Inversions (35 pts)

An **inversion** is a pair of positions `i < j` where `A[i] > A[j]`. Basically, a pair that is out of order.

### 1A. Build two counters (25 pts)

| What | Points | What it needs |
|---|---|---|
| **Brute force:** check every pair | 5 | Gives the exact count |
| **Divide and conquer:** modified mergesort | 10 | Splits, recurses, counts during merge in O(n), and returns the sorted array |
| Correctness explanation | 5 | Explain left-half, right-half, and cross inversions, and why each one is counted exactly once |
| Complexity analysis | 5 | Brute force is Θ(n²). D&C: write the recurrence and show it is Θ(n log n) |

Key idea to show in the code: when an element from the right half is smaller than the next element from the left half, it forms an inversion with **every remaining element** in the left half.

### 1B. Test and time them (10 pts)

- Write **10+ hand-checked arrays**: sorted, reverse sorted, nearly sorted, and random.
- Run **200+ random small arrays**. Both methods must give the same answer every time.
- Time both methods as `n` grows, until the difference is obvious.
- Repeat each timing and report the **median**.
- Present the results in a table or graph.
- Say roughly at what `n` the fast method starts winning on your machine, and explain why that point depends on your code and hardware.

---

## Part II: Coin Change (55 pts)

You get coin values `D = {d1, ..., dk}` and a target amount `A`. You can use as many of each coin as you want. Find the **fewest coins** that add up to exactly `A`, or report **IMPOSSIBLE**.
Unless an experiment says otherwise, generated coin sets should include a 1-coin so every target can be reached.

### 2A. Build four solvers (25 pts)

All four use the **same interface** and return `(coin_count, chosen_coins)` or `IMPOSSIBLE`.

| Solver | Points | What it needs |
|---|---|---|
| **Greedy:** always take the biggest coin that fits | 4 | Follows the rule and returns a valid coin list. This is a heuristic and not always correct |
| **Naive recursion:** try every possible last coin, no caching | 5 | Exact answer, handles impossible cases. Only for small `A` |
| **Top-down DP (memoization):** same recursion, but cache results | 6 | Uses the cache correctly, gives the exact answer, and rebuilds the coin list |
| **Bottom-up DP:** fill a table for amounts 0 to A | 6 | Fills in the right order, gives the exact answer, and rebuilds the coin list |
| Complexity analysis | 4 | Time and extra space for each solver |

### 2B. Validate and break greedy (15 pts)

- Write **10+ hand-checked cases**, including target 0, impossible cases, and cases with more than one best answer.
- Run **100+ random small cases**. Naive, memoized, and bottom-up must agree on the coin count.
- Separately check that every returned coin list adds up to `A`.
- Write an **automated search** that finds cases where greedy works but uses more coins than the best answer.
- Report **3+ different greedy failures**.
- **Required check:** the search must find `D = {1,3,4}, A = 6`. Greedy gives 4+1+1 (3 coins), but 3+3 (2 coins) is better.
- For at least one failure, explain *why* grabbing the biggest coin first blocks a better overall answer.

### 2C. DP experiments (15 pts)

**Experiment 1: Repeated subproblems**
- Add counters to the naive and memoized solvers to track: total recursive calls, distinct amounts solved, and cache hits.
- Increase `A` until naive becomes too slow. Use a documented safety cutoff.
- Explain why both use the same recursion but do very different amounts of work.

**Experiment 2: Pseudo-polynomial scaling**
- Keep the number of coins `k` small and fixed. Double `A` each step (2⁸, 2⁹, 2¹⁰, ...).
- For each step, record `A`, its bit length (`floor(log2 A) + 1`), the number of DP states, and the runtime.
- Explain why O(kA) work is *linear in A* but *exponential in the number of bits* used to write A.

---

## Part III: Reflection (10 pts)

Compare the two parts in the report. Answer all six questions, using your own results as evidence:

1. What work does divide and conquer skip compared to checking every pair?
2. Why are inversion subproblems independent, while coin change subproblems overlap a lot?
3. What role does sorting play in the D&C speedup?
4. Naive and memoized coin change use the same recursion. Why can their runtimes be so different?
5. How did the slow, exact versions help you check the fast versions?
6. Given a new problem, what clues would make you try divide and conquer first? What clues would point to dynamic programming?

---

## What to Turn In

- [ ] **Source code:** inversion counters, coin change solvers, validators, input generators, greedy failure search, and experiment scripts
- [ ] **README:** language and version, plus exact steps to rerun the main experiments
- [ ] **Report** (about 6–8 pages): methods, correctness and complexity, validation, results, interpretation, and reflection
- [ ] **Raw results** in CSV or JSON behind every main table and plot
- [ ] **Contribution statement:** what each group member did
- [ ] **AI Use Statement:** which tools you used, how they helped, and how you checked their output

## Points at a Glance

| Part | Points |
|---|---|
| 1A: Inversion algorithms | 25 |
| 1B: Inversion validation and runtime | 10 |
| 2A: Coin change solvers | 25 |
| 2B: Validation and greedy counterexamples | 15 |
| 2C: DP experiments | 15 |
| III: Reflection | 10 |
| **Total** | **100** |
