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

```
