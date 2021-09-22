# Create a Python virtual enviroment to install python packages.
    pip install virtualenv
    virtualenv <env-name>
    <!-- example: virtualenv web_app  -->
    source <env-name>/bin/activate
    <!-- source web_app/bin/activate  --> To activate the virtual env

# Install python dependencies.
    pip install --no-cache-dir -r requirements.txt

# Install postgresql.
    <!-- install postgress(default install's latest version) -->
    sudo apt-get update && apt-get install postgresql postgresql-contrib

    <!-- login as super user -->
    sudo -u postgres psql

    <!-- Create user and password, ex: CREATE USER sadhguru WITH PASSWORD 'sadhguru@123' -->
    CREATE USER <user> WITH PASSWORD <'password'>;

    <!-- Create database ex: CREATEDB tea_app_db -->
    CREATEDB <database-name>

    For more details, Please check the link below.
    https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

    Note-down the username, password and database and add values in the config/default.py
    example:
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<username>:<password>@127.0.0.1:5432/<database>'

# RUN the project.
    Open two terminals and cd into the repo and run the commands.
    1. source <env->/bin/activate
    2. python run.py db upgrade
    3. python run.py runserver