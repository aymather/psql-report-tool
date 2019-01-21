#!/usr/bin/python3

# This program should do 3 things

# Return the most popular 3 articles in the database
#   and how many views they have.
# Return the most popular authors and how many views they have.
# Return the number of days where requests had an error rate of over 1%

import psycopg2
import pprint as p
import os

DBNAME = 'news'


def dbquery(QUERY):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(QUERY)
        results = c.fetchall()
        db.close()
        return results
    except Exception as ex:
        print('Something went wrong with your query with exception:')
        print(ex)


def main():

    # Establish psql queries
    getArticles = """select articles.title, count(*) as views
                    from articles, log
                    where substring(log.path,10,100) = articles.slug
                    group by articles.title
                    order by views desc
                    limit 3"""

    getErrors = """select base.date::date, base.percent
                 from (select e.date, e.errors, t.total,
                 round(cast(((e.errors::float / t.total::float) * 100)
                 as numeric),2)
                 as percent
                 from (select date(time) as date,count(*) as errors
                 from log
                 where status != '200 OK'
                 group by date(time))
                 as e,
                 (select date(time), count(*) as total
                 from log
                 group by date(time))
                 as t
                 where e.date = t.date) as base
                 where base.percent > 1;
                 """

    getAuthors = """select authors.name, sum(query.count) as views
                  from authors,(select articles.author as id, count(*) as count
                  from articles, log
                  where substring(log.path,10,100) = articles.slug
                  group by articles.id) as query
                  where authors.id = query.id
                  group by authors.name
                  order by views desc"""

    # Get data
    articles = dbquery(getArticles)
    authors = dbquery(getAuthors)
    errors = dbquery(getErrors)

    # If the report exists, remove it and start from scratch
    if os.path.exists('report.txt'):
        os.remove('report.txt')

    # Open new file for report
    report = open('report.txt', 'w')
    report.write("Most popular articles:\n")
    for i in range(len(articles)):
        report.write(articles[i][0] + " - " + str(articles[i][1]) + " views\n")
    report.write("\nMost popular authors:\n")
    for i in range(len(authors)):
        report.write(authors[i][0] + " - " +
                     str(authors[i][1]) + " total views\n")
    report.write("\nDays when 404 errors exceeded 1%:\n")
    for i in range(len(errors)):
        report.write(str(errors[i][0]) + " - " + str(errors[i][1]) + "%")


if __name__ == '__main__':
    main()
