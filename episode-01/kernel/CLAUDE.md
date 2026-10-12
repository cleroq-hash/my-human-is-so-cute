# Kernel — entry point

Claude Code reads this file at the start of every session in this folder. The `@` lines
pull in the kernel: three short files, always loaded.

@about-me.md
@how-we-work.md
@git.md

## Not loaded — read when needed

Loading everything every time fills the context window for nothing. These files exist,
and you open them when the conversation calls for it:

| When | Open |
|---|---|
| I ask "where am I on X?" | `projects/PROJECTS.md`, then only the file for X |
| We start a new project | `projects/PROJECTS.md` — add one line, and one file |

A file nobody knows exists never gets opened. That's why this table is here, in the part
that *is* loaded.
