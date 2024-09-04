#################
#Personal laptop 
#################

How to manage a fork
######################


--->fork in owner github= create teh fork to your own github repo  --->clone the fork in personal machine -->

----get changes in local from a forked repo into a branch
----------------------------------------------------------

git remote add upstream <URL of the original repository> (step once)

git fetch upstream (fetches all branches to see them -->git branch -r)

git checkout -b <personal branch name e.g f_py4g> (create and locate in branch)

git merge upstream/main (main will be interpreted as the branch)

--sending changes to personal repo from personal laptop
---------------------------------------
git checkout personal-branch-name (if not opened already)
git push origin personal-branch-name


#################
#Company laptop 
#################

How to manage a clone of a personal fork
###########################################

git clone https://github.com/your-username/personal-forked-repo.git
cd personal-clonedforked-repo


git remote add personal https://github.com/personal-username/personal-repo.git

# Step 4: Fetch the latest changes from the personal forked repository

git fetch personal

# Step 5: Check out the branch you want to contribute to
git checkout -b my-local-branch(eg b_py4g) personal/branch-name(eg f_py4g)


# Eg (=> git checkout -b b_py4g personal/f_py4g) -now main will be f_py4g

# Stage your changes
git add .

# Commit your changes
git commit -m "Description of changes"

# Push your changes to the personal remote ---I get prompted to my personal git and then make the merge
git push personal b_py4g


#HOw to bring changes from personal to b_py4g
# Ensure you are on your local branch
git checkout b_py4g

# Merge the changes from the personal remote's f_py4g branch
git merge personal/f_py4g
