Project Title: Chicago Beach E.Coli Predictions
This is a Flask-based web application that fetches beach water data from the city of Chicago's official resources, scrapes data from specific beach URLs, and presents this data in an organized and visually appealing manner. The main goal of this application is to predict E.Coli levels at different beaches, based on the fetched and scraped data.


It uses Flask as a web framework and SQLAlchemy for interacting with the PostgreSQL database.
It fetches beach water data from the city of Chicago's resources.
It scrapes additional data from specific beach URLs.
It processes and saves the fetched and scraped data in a PostgreSQL database.
When a user accesses the web application, it pulls the data from the database, processes it to provide ordered data, and displays this data on the web page.
The database contains a single table BeachData, with columns:
id: An integer that uniquely identifies each record
beach_name: A string that stores the name of the beach
data: A JSON object that stores the record data for each beach
The get_data() function is responsible for fetching the beach data and saving it in the database.
The scrape_beach_data(url) function is responsible for scraping additional data from specific beach URLs.
The order_data(data) function orders the beach data in a specific order before it is displayed on the web page.
The / route displays the ordered beach data.

Contributing
Contributions are welcomed! Please fork this repository and open a Pull Request to add enhancements or fix issues.

