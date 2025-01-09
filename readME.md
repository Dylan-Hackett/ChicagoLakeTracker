Chicago Beach E.Coli Predictions

This is a Flask-based web application that fetches beach water data from the city of Chicago's official resources, scrapes data from specific beach URLs, and presents this data in an organized and visually appealing manner. The main goal of this application is to predict E.Coli levels at different beaches, based on the fetched and scraped data.

### Technologies Used
- Flask: Python web framework for building the application
- SQLAlchemy: Python library for database management and interaction with PostgreSQL
- BeautifulSoup: Python library for web scraping and parsing HTML
- PostgreSQL: Relational database used for storing beach data
- HTML/CSS: Markup and styling languages for the web interface
- JavaScript: Used for interactive features and data visualization
- Chart.js: JavaScript library for creating charts and graphs

### Functionality
- Fetches beach water data from the city of Chicago's resources.
- Scrapes additional data from specific beach URLs using BeautifulSoup.
- Processes and saves the fetched and scraped data in a PostgreSQL database using SQLAlchemy.
- Displays the ordered beach data on the web page.
- Predicts E.Coli levels based on the available data.

### Project Structure
- `app.py`: Main application file containing Flask routes and logic.
- `templates/index.html`: HTML template file for displaying the beach data on the web page.
- `static/js/chart.js`: JavaScript file for creating charts using Chart.js library.
