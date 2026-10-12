# Git

Git is not my topic and I don't want to deal with it. What I want: `main` up to date,
and nothing leaving my private space unless I decided it. The rest is your job.

Commit messages follow Conventional Commits (`feat:`, `fix:`, `docs:`…).

## Automatic, without asking

- Commit and push in my private repositories, for work I asked for.
- `git pull --rebase` before pushing, silently. I work from more than one machine;
  diverging is normal.
- Add only files you wrote yourself, **by explicit path**. Never `git add -A` or
  `git add .`: a repository always has untracked files that don't belong in it.
- One commit per intention.
- Don't let me end a session with uncommitted work without telling me. What isn't pushed
  doesn't exist for the next session.

## Ask me first

Force-push, rewriting history, deleting files from git, deleting a remote branch, and
anything that changes who can see a repository.

## Stop and tell me

If a rebase hits a conflict — that's a real decision about content, and it's mine.
