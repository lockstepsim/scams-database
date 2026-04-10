# scams-database
Developed by volunteers from the Economics discord server.

```yaml
# April 10, 2026
# Instructions by Leslie D. @lespam for Economics Server Discord.
# Requires Git and Anaconda.


git clone https://github.com/Dollar-Scholars/scams-database.git

####################################
# create conda environment
####################################
# if you have the file
conda env create -f environment.yml
# else
conda create -n scams python Django

conda activate scams

##############################
# makemigrations and run bot
##############################
# In the folder where manage.py file is
# First time only
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# From now on
git pull

# Everytime the db is updated you will need to run
python manage.py makemigrations
python manage.py migrate

python manage.py run_bot

##############################
# push your results
##############################
git add .
git commit -m 'message'
git push
```
