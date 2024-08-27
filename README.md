# postGIS

A learning project focused on integrating PostgreSQL with PostGIS for spatial database management. This repository contains examples and scripts to demonstrate how to set up and interact with a PostgreSQL database, execute SQL queries, and utilize PostGIS extensions for geographic data. It will be built upon as I continue to learn GIS concepts and related development for the USGS.

## Features:

- Basic PostgreSQL setup and connection examples
- Handling spatial data with PostGIS
- Sample data and queries for testing spatial queries
- Python scripts for interacting with the database using `psycopg2` and `SQLAlchemy`

## Workshop Reference

This workshop and project are based on the tutorials available at [PostGIS](https://postgis.net/workshops/postgis-intro/)

## Getting Started:

1. Clone the repository:
   ```bash
   git clone https://github.com/raythurman2386/postGIS.git
   ```
2. Set up your Python environment:
   ```bash
   conda create -n postgis python=3.8
   conda activate postgis
   conda install ipython-sql sqlalchemy psycopg2 pandas -c conda-forge
   ```
3. Configure your PostgreSQL database and PostGIS extension.
4. Run the provided Python scripts to test the setup and interact with the database.

## Contributions:

Feel free to contribute by opening issues or submitting pull requests. This project aims to provide a foundation for learning about spatial databases and geographic information systems (GIS) using PostgreSQL and PostGIS.

### Additional Resources

For further information and resources related to PostgreSQL and PostGIS, you might find the following links useful:

**PostGIS:**

- [PostGIS Official Site](https://postgis.net/)
- [PostGIS Documentation](https://postgis.net/docs/)
- [PostGIS Workshop Slides](https://docs.google.com/presentation/d/1qYXdeCIymLl32uoAHvAPrp1r-hK-_4Z8InG7sHEo6vc/edit#slide=id.gd85280829a_0_248)

**PostgreSQL:**

- [PostgreSQL Official Site](https://www.postgresql.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Downloads](https://www.postgresql.org/download/)

**Drivers:**

- [JDBC Driver](https://jdbc.postgresql.org/)
- [.Net Driver (Npgsql)](https://www.npgsql.org/)
- [Python Driver (PyGreSQL)](http://www.pygresql.org/)
- [C/C++ Driver (libpq)](https://www.postgresql.org/docs/current/static/libpq.html)

**Tools:**

- [PgAdmin](https://www.pgadmin.org/)

**Open Source Desktop Clients:**

- [QGIS](https://qgis.org/)
- [OpenJUMP](http://openjump.org/)
- [uDig](https://udig.github.io/)

Feel free to explore these resources to enhance your understanding and effectively use PostgreSQL and PostGIS.
