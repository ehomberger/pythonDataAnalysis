import MySQLdb

def connectTest():
    db = MySQLdb.connect(host='data-sandbox.cknuv1qv6esb.us-east-1.rds.amazonaws.com',
            port=3306, user='Python', passwd='isveryfun', db='main')

    cur = db.cursor();

    
    
    cur.execute('SELECT * FROM helloWorld')

    for row in cur.fetchall():
        print row[0]

    db.close()
