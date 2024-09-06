git fetch --all 
git pull origin master 
git checkout master
git checkout -b hotfix/reading

git add .
git commit -m "Fix issue with multiple Monty devices handling"
git pull origin hotfix/reading
git push origin hotfix/reading
git checkout master
git pull origin master
git merge hotfix/reading
git push origin master