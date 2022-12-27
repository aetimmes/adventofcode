# 2015 solutions

I completed the 2015 questions between 12/25-27 in 2022, having just finished the 2022 solutions (and stalling out after 19 days in 2021).

Some takeaways:

* Wow, being warmed up from 2022 made the first dozen or so problems a breeze.
* Several 2015 questions had input hard-coded into the actual question text. I appreciate how much less often this happened in 2022 - it was limited to single variables/values rather than the entire RPG item shop.
* The bugs that cost me the most time were _entirely_ due to reading comprehension failures.
  * The place where the "jio" instruction specifications were wrapped on my monitor caused my eyes to skip the crucial bit where it specified jio as jump if **one** and not jump if **odd**.
  * The change in player HP from 100 to 50 between warrior and wizard combat sims also cost me a good hour+.
  * I came to truly appreciate the example inputs in 2022 after trying to work on 2015's problems.
* numpy.array provides powerful array manipulation tools at the cost of slightly more arcane error messages. I need more practice with numpy.
  * I also need to modify my submission skeleton to cast results to `int`s after computing answers in numpy.
  * Wait, why don't I just open a pull request against aocd for that? It's open source. In fact, let me go do that now...
  * Several hours later: woof, that turned into some [Software Engineering](https://github.com/wimglenn/advent-of-code-data/pull/104). In the process I learned a whole bunch about numpy types, so that's cool.
* None of the questions were particularly computationally intensive; my most brute-force solution (24b) ran on the order of minutes.
* No maze traversal questions. Phew.
