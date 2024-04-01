# Git

## Commit messages

1) put a blank line between header and body
2) use on of the following `type`:

   - `feat`: (new feature for the user, not a new feature for build script)
   - `fix`: (bug fix for the user, not a fix to a build script)
   - `docs`: (changes to the documentation)
   - `style`: (formatting, missing semi colons, etc; no production code change)
   - `refactor`: (refactoring production code, eg. renaming a variable)
   - `test`: (adding missing tests, refactoring tests; no production code change)
   - `chore`: (updating grunt tasks etc; no production code change)

## Configuration

- global config at `~/.gitconfig`
- add a global gitignore `git config --global core.excludesfile ~/.gitignore_global`
- use vscode as default git editor (linux only?) `git config --global core.editor code -w`

## Remote

- add a remote using `git remote add <remote_name>`
- see remotes with `git remote -v`
- see current upstream branch with `git branch -vv`

just do `git push -u <remote_name> <src>:<dst>`  the first time to setup the upstream branch for the current branch


## Resources

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/)
- [Semantic Commit Messages](https://seesparkbox.com/foundry/semantic_commit_messages)
- [Git Commit Msg](http://karma-runner.github.io/1.0/dev/git-commit-msg.html)