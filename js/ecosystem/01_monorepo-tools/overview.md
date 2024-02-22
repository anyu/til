# Overview of monorepo tools

https://monorepo.tools/#what-is-a-monorepo

Not a monolith, not code colocation (repo w/ multiple unrelated projects)

A monorepo is a single repo containing multiple distinct projects or entrypoints, with well-defined relationships.

Characteristics of monorepos:

- Multiple projects in the same repo.
- Projects in the repo can depend on each other / share code.
- When a change is made, only the projects affected by the change need to be rebuilt/retested (allows independent parallel work)

## Pros
- Everything at current commit works together
- More deployment flexibility
- Facilitates splitting code into composable modules
- One toolchain setup

## Challenges
- Trunk-based development is more important
- Needs more advanced CI setup
- Needs devs to think about large-scale changes
- Not for every situation

## Monorepo Tools
- pnpm
- npm workspaces
- turborepo (pretty new, TBD)
- yarn
- Nx (has a lot of features, but anecdotally painful?)