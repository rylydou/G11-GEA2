# From Brute Force to Better Algorithms: Divide and Conquer + Dynamic Programming

**CMP_SC 4050: Group Algorithm Engineering Assignment 2** · Fall 2026
**Team:** _________, _________, _________, _________ · **Submitted:** _________

<!--
HOW TO USE THIS SKELETON
- Each "> TODO(P#)" block says who writes that section, what to cover, and how long to make it.
  Replace the block with your text, and delete all TODO blocks before submitting.
- Find what's left with:  grep -n "TODO(" REPORT.md
- PAGE LIMIT: the assignment asks for about 6-8 pages. Treat 8 pages as the hard cap.
  Budget: about 2,600 words + 3 figures + 5 small tables, which comes to about 7 pages.
  Stay within your section's word target. Check the page count in the final PDF.
- Use only numbers from our own results/*.csv files. Never estimate or make up a result.
- Testing doesn't prove correctness. Say tests "agreed on all N tested inputs", and use the
  correctness arguments for the general claim.
- The Contribution Statement (end of this file) and AI_USE.md are separate deliverables,
  so they don't count toward the page limit.
-->

## 1. Introduction

> **TODO(P4) · ~120 words.** Explain the theme: two correct but slow baselines, each improved by a
> different paradigm. Divide and conquer takes inversion counting from Θ(n²) to Θ(n log n).
> Dynamic programming removes repeated work in coin change. Briefly list what we did:
> implement, validate against baselines, benchmark, explain. Give the language and version,
> and point to the README for how to reproduce the results.

---

## 2. Part I: Counting Inversions

### 2.1 Algorithms

> **TODO(P1) · ~150 words.** Define an inversion. Describe the brute-force pair check and the
> sort-and-count mergesort in a few sentences each. Explain the key merge step: when the next
> right-half element is smaller, it forms an inversion with every remaining left-half element.
> A short pseudocode block for `merge_and_count` is fine if it fits.

### 2.2 Correctness

> **TODO(P1) · ~200 words.** Every inversion (i, j) is one of three kinds: both indices in the left
> half, both in the right half, or split across the halves. Explain why the recursion counts the
> first two kinds, and why the merge counts each cross inversion exactly once. Say why sorting the
> halves doesn't change the cross count. Use induction on n.

### 2.3 Complexity

> **TODO(P1) · ~150 words.** Brute force: count the comparisons and conclude Θ(n²).
> Divide and conquer: write the recurrence T(n), solve it (recursion tree or Master Theorem),
> and state the result. Mention the extra space used by merging.

### 2.4 Validation

> **TODO(P1) · ~120 words + Table 1.** Brute force is the oracle. Describe the 10+ hand-checked
> arrays (Table 1) and the 200+ seeded random arrays, including the sizes and the seed.
> State the outcome: the methods agreed on every tested array. Don't claim this proves correctness.

**Table 1.** Hand-checked arrays (from `src/test_inversions.py`).

| Array | Type | Expected inversions | Brute force | Divide and conquer |
|---|---|---|---|---|
| `[]` | empty | 0 | _ | _ |
| `[42]` | single | 0 | _ | _ |
| `[1, 2, 3, 4, 5]` | sorted | 0 | _ | _ |
| `[5, 4, 3, 2, 1]` | reverse sorted | 10 | _ | _ |
| `[1, 2, 4, 3, 5]` | nearly sorted | 1 | _ | _ |
| `[2, 4, 1, 3, 5]` | random | 3 | _ | _ |
| `[3, 1, 4, 5, 2]` | random | 4 | _ | _ |
| _add 3+ more_ | | | | |

### 2.5 Runtime Scaling

> **TODO(P3) · ~250 words + Figure 1.** Methodology: the sizes n, the number of repeats, using the
> median, how inputs were generated outside the timed region, the brute-force cutoff, and the
> machine. Results: describe Figure 1. Does the log-log slope look like n² versus n log n?
> Crossover: give the approximate n where divide and conquer becomes faster on our machine, and
> explain why that point depends on the implementation and hardware (constant factors, Python
> overhead, recursion and list copying, cache).

![Figure 1: Median runtime vs n, brute force vs divide and conquer (log-log)](results/benchmark_inversions.png)

**Figure 1.** _caption: sizes, repeats, machine._ Data: `results/benchmark_inversions.csv`.

---

## 3. Part II: Coin Change

### 3.1 Solvers

**Greedy** sorts D from largest to smallest and takes as many copies of each coin as fit. It is
fast but only a heuristic. On D = {1, 3, 4}, A = 6 it returns 4+1+1 instead of 3+3. On D = {3, 5},
A = 9 it takes 5+3, gets stuck with 1 left, and returns IMPOSSIBLE, even though 3+3+3 works.

**Naive recursion** uses best(0) = 0 and best(a) = 1 + min over coins d ≤ a of best(a − d). Any
optimal answer for a has some last coin d, and the other coins must be an optimal answer for a − d,
so trying every d finds the optimum. If no coin fits, or every sub-amount is impossible, a is
IMPOSSIBLE. Each call returns its coin list with the count. Nothing is cached, so the same amounts
are solved again and again.

**Top-down memo** runs the same recursion, but the first time it solves an amount it stores the
best count and the last coin used in a dictionary. Later calls for that amount return the stored
value. To rebuild one optimal coin list, it starts at A, takes the stored coin d, moves to A − d,
and repeats until it reaches 0.

> **TODO(P3) · ~70 words.** Bottom-up DP: the table, the order it's filled, and how one optimal coin
> list is rebuilt from the stored choices.

### 3.2 Complexity

Let k = |D|, A be the target, and d_min the smallest coin. **Greedy** sorts in O(k log k), then
makes one pass over the coins. Writing out the coin list adds O(A/d_min). **Naive** branches up to
k ways per call, and the recursion is up to A/d_min deep, so it makes O(k^(A/d_min)) calls. On
D = {1, 3, 4} the call count grew about 2.6× for every +2 in A (Section 3.5). Each stack frame can
hold a coin list of up to A coins, so the extra space is O(A²) in the worst case. **Memo** solves
at most A + 1 distinct amounts, and each one loops over k coins once, so it takes O(kA) time. The
cache and the stack are both O(A). The depth can reach A, so memo raises Python's recursion limit.

> **TODO(P3) · ~30 words.** Explain the bottom-up row.

**Table 2.** Time and auxiliary-space complexity.

| Solver | Time | Auxiliary space | Notes |
|---|---|---|---|
| Greedy | O(k log k + A/d_min) | O(k) | Sorted copy of D. Not always optimal |
| Naive recursion | O(k^(A/d_min)) calls (exponential) | O(A²) worst case | Depth up to A/d_min; each frame holds a coin list |
| Top-down memo | O(kA) | O(A) | Cache of A + 1 entries; depth up to A/d_min |
| Bottom-up DP | _ | _ | _ |

### 3.3 Exact-Solver Validation

> **TODO(P4) · ~150 words + Table 3.** Describe the 10+ hand cases (target 0, impossible, multiple
> optimal solutions), the 100+ seeded random instances where naive, memo, and bottom-up must agree,
> and the independent `is_valid` check (coins sum to A, count matches, coins come from D).
> State the outcome.

**Table 3.** Hand-checked coin cases (from `src/coin_cases.py`).

| D | A | Expected | Naive | Memo | Bottom-up | Why it's included |
|---|---|---|---|---|---|---|
| {1, 2, 5} | 0 | 0 | _ | _ | _ | target 0 |
| {2} | 3 | IMPOSSIBLE | _ | _ | _ | impossible |
| {1, 2, 3} | 4 | 2 | _ | _ | _ | multiple optimal (1+3, 2+2) |
| {1, 3, 4} | 6 | 2 | _ | _ | _ | greedy counterexample |
| _add the rest (10+ total)_ | | | | | | |

### 3.4 Greedy Counterexamples

> **TODO(P4) · ~200 words + Table 4.** Explain how the automated search works (which coin systems,
> which targets, compared against bottom-up DP) and how many cases it found. Show 3+ distinct
> counterexamples. For at least one, explain the structure: why taking the largest coin first
> blocks a better overall combination.

**Table 4.** Greedy counterexamples (from `results/counterexamples.csv`).

| D | A | Greedy coins (count) | Optimal coins (count) |
|---|---|---|---|
| {1, 3, 4} | 6 | 4+1+1 (3) | 3+3 (2) |
| _ | _ | _ | _ |
| _ | _ | _ | _ |

### 3.5 Experiment 1: Repeated Subproblems

**Setup.** We used D = {1, 3, 4} (k = 3). It includes 1, so every A can be reached, and A ran
over 0, 2, …, 60. For each A, we ran each solver once with counters on, then timed it separately
(median of 3 runs, counters off). For safety, we stopped running naive after the first run that
passed 10^7 calls.

**Results.** Naive passed the cutoff at A = 34. It made 17,480,760 calls but reached only 35
distinct amounts, so on average it solved each amount about 500,000 times. Its call count grew about
2.6× for every +2 in A (Figure 2). At the same A, memo made 98 calls: 35 distinct states plus 63
cache hits. In every run, memo made exactly 3A − 4 calls for A ≥ 4 and solved A + 1 distinct
states, so its work grows linearly. At A = 34, naive took 1.70 s and memo took 9.7 µs.

**Interpretation.** Both solvers use the same recurrence and reach the same amounts. Naive solves
an amount again every time a different sequence of coins leads to it, and the number of such
sequences grows exponentially with A. Memo solves each amount once, and every later visit is an O(1)
cache hit. These overlapping subproblems are what dynamic programming takes advantage of.

![Figure 2: Recursive calls vs A, naive vs memo (log y)](results/exp1_repeated_subproblems.png)

**Figure 2.** Recursive calls vs A for D = {1, 3, 4} (log y, one counted run per point). Naive
stopped after it passed the 10^7-call cutoff at A = 34. Data: `results/exp1_repeated_subproblems.csv`.

**Table 5.** Representative rows from Experiment 1 (D = {1, 3, 4}).

| A | Naive calls | Memo calls | Distinct states | Memo cache hits |
|---|---|---|---|---|
| 10 | 168 | 26 | 11 | 15 |
| 20 | 20,736 | 56 | 21 | 35 |
| 30 | 2,550,408 | 86 | 31 | 55 |
| 34 | 17,480,760 | 98 | 35 | 63 |
| 60 | not run (cutoff) | 176 | 61 | 115 |

### 3.6 Experiment 2: Pseudo-Polynomial Scaling

> **TODO(P3) · ~200 words + Figure 3 + Table 6.** Setup: the fixed coin system (k), and A = 2^8, 2^9, ….
> Report A, its bit length, the DP states processed, and the runtime. Interpretation: the work grows
> linearly in A, but exponentially in the number of bits needed to write A. Explain why that makes
> O(kA) pseudo-polynomial.

![Figure 3: Bottom-up runtime vs bit length of A (log y)](results/exp2_pseudo_polynomial.png)

**Figure 3.** _caption._ Data: `results/exp2_pseudo_polynomial.csv`.

**Table 6.** Pseudo-polynomial scaling.

| A | Bit length | States processed | Median time (s) |
|---|---|---|---|
| 256 | 9 | _ | _ |
| _ | _ | _ | _ |

---

## 4. Cross-Paradigm Reflection

> **~500 words total, about 80 per question.** Answer every question with specific evidence from
> our results (numbers, counterexamples, figures). Sections 2 and 3 already cover the detail, so
> refer back to them instead of repeating it.

**Q1. What work does divide and conquer avoid compared with checking every pair?**
> TODO(P1) · ~80 words.

**Q2. Why are inversion subproblems independent before the merge, while coin-change subproblems overlap heavily?**
> TODO(P3) · ~80 words.

**Q3. What role does sorting play in the divide-and-conquer improvement?**
> TODO(P1) · ~80 words.

**Q4. Naive and memoized coin change use essentially the same recurrence. Why can their runtimes be so different?**
Memo doesn't change the recurrence. It only skips repeated work. At A = 34, both solvers reached the
same 35 amounts, but naive made 17,480,760 calls while memo made 98 (35 solves plus 63 cache hits).
Naive's work follows the number of paths through the recursion tree, which grows exponentially in A.
Memo's work follows the number of distinct states times k, which is O(kA). That gap is why naive
took 1.70 s and memo took 9.7 µs (Section 3.5).

**Q5. How did the baseline and exact implementations help validate the faster algorithms in both halves?**
> TODO(P4) · ~80 words.

**Q6. For a new optimization problem, what evidence would make you try divide and conquer first? What would make you try dynamic programming?**
> TODO(everyone drafts 1–2 sentences; P4 merges) · ~100 words. Contrast independent subproblems
> with overlapping ones.
>
> **P2 draft:** Try divide and conquer first when the problem splits into parts that can be solved
> on their own and combined cheaply, like the two halves in inversion counting, which share nothing
> until the merge. Try dynamic programming when a natural recursion keeps reaching the same
> subproblems, like coin change: at A = 34, naive recursion made 17,480,760 calls but reached only 35
> distinct amounts (Section 3.5).

---

## Contribution Statement

_Separate deliverable; doesn't count toward the page limit._

| Member | Role | Primary contributions |
|---|---|---|
| _________ | P1: Inversions | _ |
| Ryly Dou | P2: Recursive coin solvers | `greedy`, `naive`, and `memo` solvers with call counters; Experiment 1 (script, CSV, Figure 2); Report 3.1, 3.2 (greedy, naive, memo), 3.5, and Q4 |
| _________ | P3: Bottom-up DP + timing | _ |
| _________ | P4: Coin checker + integrator | _ |

## AI Use Statement

See [`AI_USE.md`](AI_USE.md). _Paste the final version here, or submit it alongside the report, whichever the course expects._
