
#!/usr/bin/env python

import MySQLdb
import Home_Automation


def insertTemp(temp,curs,db):
    with db:    
        curs.execute ("INSERT INTO temps values(CURRENT_DATE(),CURTIME(),"+str(temp)+")")
	db.commit()
        ##print temp,"committed"

def printData():
    curs=db.cursor()
    curs.execute ("SELECT * FROM temps")
    print "\nDate            Time      Temperature"
    print "======================================="
    num = 0 
    for reading in curs.fetchall():
        print str(reading[0])+"    "+str(reading[1])+"    "+str(reading[2])
        num +=1
    print "Number of enteries printed", num                

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "mtangy", "*password**", "roomTemps")
    curs=db.cursor()
    iter = 0
    while True:
        temp = 0.0;
        temp = Home_Automation.getCurrentTemp()
        insertTemp(temp,curs,db)
	t = open('/usr/local/bin/temp.txt', 'r')
	utemp = int(t.read().strip())
        t.close()
        if utemp > temp:
            Home_Automation.turnACoff()
        time.sleep(1000)
    

