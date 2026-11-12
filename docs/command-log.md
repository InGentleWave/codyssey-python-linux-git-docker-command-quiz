# Command Log

## Git 기초 명령어 7종

### git init

```bash
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-commands-quiz$ git init
Initialized empty Git repository in /home/<USER>/<FOLDER>/codyssey-python-linux-commands-quiz/.git/
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-commands-quiz$ git branch --show-current
main
```

### git add

```bash
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git add README.md 
```

### git commit

```bash
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git commit -m "Docs: README 목차 생성"
[main 8a56519] Docs: README 목차 생성
 1 file changed, 12 insertions(+), 1 deletion(-)

```

### git push

```bash
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 513 bytes | 513.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/InGentleWave/codyssey-python-linux-git-docker-command-quiz.git
   482bd94..8a56519  main -> main
```

### git pull

```bash
<USER>@<HOST>:<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git pull origin main
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 8), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (12/12), 3.25 KiB | 277.00 KiB/s, done.
From https://github.com/InGentleWave/codyssey-python-linux-git-docker-command-quiz
 * branch            main       -> FETCH_HEAD
   0bb9930..a95ea7a  main       -> origin/main
Updating 0bb9930..a95ea7a
Fast-forward
 README.md | 16 ++++++++--------
 1 file changed, 8 insertions(+), 8 deletions(-)
```

### git checkout

```bash
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git checkout -b playQuiz
Switched to a new branch 'playQuiz'
<USER>@<HOST>:~/<FOLDER>/codyssey-python-linux-git-docker-commands-quiz$ git status
On branch playQuiz
nothing to commit, working tree clean
```

### git clone

```bash
<USER>@<HOST>:<FOLDER>/cloneTest$ git clone https://github.com/InGentleWave/codyssey-python-linux-git-docker-command-quiz.git
Cloning into 'codyssey-python-linux-git-docker-command-quiz'...
remote: Enumerating objects: 75, done.
remote: Counting objects: 100% (75/75), done.
remote: Compressing objects: 100% (48/48), done.
remote: Total 75 (delta 37), reused 51 (delta 23), pack-reused 0 (from 0)
Receiving objects: 100% (75/75), 27.82 KiB | 1.46 MiB/s, done.
Resolving deltas: 100% (37/37), done.

<USER>@<HOST>:<FOLDER>/cloneTest$ ls
codyssey-python-linux-git-docker-command-quiz

<USER>@<HOST>:<FOLDER>/cloneTest$ cd codyssey-python-linux-git-docker-command-quiz/

<USER>@<HOST>:<FOLDER>/cloneTest/codyssey-python-linux-git-docker-command-quiz$ ls
README.md  default_quizzes.json  default_quizzes.py  docs  input_utils.py  main.py  quiz.py  quiz_game.py  state.json  storage.py
```
