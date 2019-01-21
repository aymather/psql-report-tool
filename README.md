# Report.py

## Description
This tool is used to make queries to our **News** database. The results of running this tool is a file called 'report.txt' which will include the following:

1. 3 most popular articles (by views)
2. Most popular writers (by total views)
3. Days when 404 errors exceeded 1% of our responses to clients

## Dependencies
- [PostgreSQL](https://www.postgresql.org/download/)
- [psycopg2](http://initd.org/psycopg/download/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Python 3](https://www.python.org/downloads/)

## Usage
**IMPORTANT**: This tool should be used inside a virtual environment, in development we used _VirtualBox_ which we will explain how to set up correctly here...

1. [Download VM setup folder](./FSND-VM.zip) (by default this includes all program dependencies)

2. `cd` into your new FSND-VM/vagrant directory
3. To initialize VirtualBox environment with vagrant use:
`vagrant up`
followed by:
`vagrant ssh`
which should bring you into your virtual environment with proper dependencies.
4. To get to program files use the following command upon entering virtual environment:
`cd /vagrant`
5. Load the data into database with this command:
`psql -d news -f newsdata.sql`
6. To use the tool, use the following command:
`python report.py`
7. Although this zip file already contains the output of the `python report.py` command in a text file named 'report.txt', feel free to update the results as often as necessary.
> Important Note: Using the `python report.py` command will check your directory for the 'report.txt' file. If it exists, it will be destroyed and the program will create a new file with the same name with the **current** statistics.

_This program was written by: [Alec Mather](https://www.github.com/aymather)_
