Run the program with  "python manage.py runserver" in the folder "park_displays"
Index at http://127.0.0.1:8000/park_displays_app/
Navigation through pages example: http://127.0.0.1:8000/park_displays_app/sportrec

python: 3.7.3
django version: (2, 2, 1, 'final', 0)

Get Changes from Master into branch:
-git checkout your_branch_name
-git merge origin/master

To merge branch into master:
-push your branch: git push origin your_branch_name
-switch to master branch on your local repository: git checkout master.
-update local master with remote master using: pull origin master.
-merge your branch into local master: git merge your_branch_name. This may give you conflicts which need to be resolved and changes committed before moving further.
-Once merge of your branch to master on local is committed, push local master to remote master: git push origin master
