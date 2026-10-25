# The sealed box — and the sister next door

Sam tested two tools on the same afternoon, with two sessions of the AI, each in its own
window. They don't talk to each other. They don't know the other one exists.

The first session installed a program that runs a small AI model locally and serves it
on a local port. The second one was testing an app store for AI tools — the kind that
installs everything in one click and runs whatever it's handed. So Sam put that one in a
**disposable box**: a container, sealed off from the rest of the machine. If anything goes
wrong, you throw the box away.

Inside the box, the second session looked around, and found an AI server running on the
machine. It wrote, very seriously: *"appears to be already installed — an old install,
probably."*

It was its sister. In the next room. Who had just installed it.

## Two lessons, one funny and one not

**The funny one: two sessions of the same AI are strangers.** Neither knows what the
other did ten minutes ago. Before an AI concludes "this was already there", it should ask
whether another session is running. A kernel line can say it:

```markdown
- Something unexpected is installed or running? Before calling it old or forgotten,
  ask me whether another session is working on this machine right now.
```

**The one that matters: the box wasn't sealed.** The files, yes — the box couldn't see
them. The network, no. If a program inside the box can reach a server running on the
host, it can reach *anything* running on the host: local AI servers, databases,
development servers, admin pages that assume "only I can reach localhost".

Many container setups are built that way on purpose. Docker Desktop, for instance, offers
a special name, `host.docker.internal`, precisely so containers can reach the host. That's
convenient for development, and it means "sealed" is a promise about files, not about
the network.

## Check your own box

[`probe_host.py`](probe_host.py) is meant to be run **inside** the box. It tries to open a
connection to a short list of ports on the addresses a container typically uses to reach
its host, and reports what answers.

```bash
# copy the script into the box, then, inside it:
python3 probe_host.py
python3 probe_host.py --ports 22 80 443 5432    # your own list
```

- **Nothing reachable**: good sign for those ports. Not proof — it only tries what's on
  the list.
- **Something reachable**: the box shares the network with the host. Treat anything
  running there as visible to whatever you run in the box.

Only run it against your own machine. It's a doorbell, not a lock-pick — but it rings
doorbells all the same.

To actually close the network, the usual tools are a container started with no network
at all (`docker run --network none …`), or a virtual machine with its own network, or a
second computer. Which one fits depends on what the tool needs: an app store that
downloads things won't work with no network at all. That trade-off is the real decision.

## The part that didn't need the box

The final verdict on the app store was "no". And about ninety-eight percent of that verdict
could have been reached without installing anything — by reading its documentation, its
permissions and what it runs. Installing it was useful for one thing only: finding the
hole in the box. Which was worth the trip.

The reading part is in episode 1b:
[`../../episode-01b/adapt-dont-import/checklist.md`](../../episode-01b/adapt-dont-import/checklist.md).
