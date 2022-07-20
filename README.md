# learning_log

My first web-site.

# Install requirements. 
pip install -r requirement.txt
# Activate env for Linux
source env/bin/activate
# Activate env for Windows
source env/Scripts/activate

# Create db in this project
python manage.py makemigrations

python manage.py migrate 


# Create admin panel 
python manage.py createsuperuser

# Run this project
python manage.py runserver


