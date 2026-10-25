# The Dreamer, the Realist and the Critic

A method to get a group thinking, borrowed from the way Walt Disney worked. Three roles,
one after the other: the Dreamer thinks big without asking if it's possible, the Realist
turns the dream into a plan, the Critic looks for what breaks. **Never at the same
time** — if the Critic talks while the Dreamer is dreaming, there's no dream left.

With an AI, there's no group: the AI plays all three roles, one at a time.
[`postures.md`](postures.md) is the kernel file that tells it how.

## Why three and not six

Edward de Bono's *Six Thinking Hats* does the same job with six roles. Sam had a note,
in a file: "compare Disney and de Bono", with a checkbox. It was never checked. Three
roles were enough. Which is, when you think about it, a pretty good comparison.

## What happened in the episode

The topic was Sam's "control room": how to see all his projects at a glance.

**Four rounds of Dreamer.** Sam asked the AI not to close anything down. Along the way, he
said the line that changed the direction: *"This looks more like a CEO's assistant than
anything else."* Some of the dreams were far too big for that week — an assistant that
answers the phone in his voice. They were kept on the side, not killed. That's the
Dreamer's job.

**Then the Critic found a problem.** Sam's kernel had a rule: *don't recite the state of
my projects at the start of a conversation — it clutters things up.* A board that shows
everything seemed to contradict it.

It didn't. The rule forbids **reciting in the conversation**. It doesn't forbid the
information. To see the state of the projects without the AI reciting it, you need a
separate place: a wall. The wall wasn't a nice-to-have; it was the way out of a
contradiction. And the Critic is the one who found it. That wall is in
[`../wall/`](../wall/).

**Two days later, the order became a rule**, the line in `postures.md`: the Realist goes
before the Critic. Always. Because criticizing a dream gets you giving up; criticizing a
plan makes it solid.

## Try it

1. Copy `postures.md` next to your other kernel files and add it to your `CLAUDE.md`.
2. Next time you have an idea you're not sure about, say: "Dreamer, three rounds, don't
   close anything."
3. Then "Realist". Then, and only then, "Critic".

Watch what the Critic finds when it has a plan to attack instead of a dream.
