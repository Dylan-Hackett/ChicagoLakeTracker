import subprocess
import os

# Export the database
def export_database():
    db_type = 'postgresql'  # Change this to 'sqlite' if you're using SQLite
    db_name = 'your_database_name'
    backup_file = 'backup.sql'

    if db_type == 'postgresql':
        # Export PostgreSQL database
        export_command = f'pg_dump {db_name} > {backup_file}'
    elif db_type == 'sqlite':
        # Export SQLite database
        export_command = f'sqlite3 {db_name} .dump > {backup_file}'

    subprocess.run(export_command, shell=True)

# Push the backup file to Heroku
def push_to_heroku():
    branch_name = 'database_backup'

    # Add backup file to Git repository
    subprocess.run(f'git add {backup_file}', shell=True)

    # Commit changes
    subprocess.run(f'git commit -m "Database backup"', shell=True)

    # Push branch to Heroku
    subprocess.run(f'git push heroku {branch_name}:main', shell=True)

# Main script
if __name__ == '__main__':
    # Change to the project directory
    os.chdir('/path/to/your/project')

    # Export the database
    export_database()

    # Push the backup file to Heroku
    push_to_heroku()