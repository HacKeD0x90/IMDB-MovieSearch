#!/usr/bin/python
import sys
import mechanize
import re
from BeautifulSoup import BeautifulSoup
if len(sys.argv)< 2:
	print "Please Enter Movie Name"
	exit()
def MovieSearch():
	movie=sys.argv[1]
	search = "http://www.imdb.com/find?q="
	Link=search + movie
	br = mechanize.Browser()
	r=br.open(Link)
	link = br.find_link(url_regex = re.compile(r'/title/tt.*'))
	res=br.follow_link(link)
	HTMLPage=res.read()
#	print HTMLPage
	begin=HTMLPage.find('<title>')
	end=HTMLPage.find('</title>',begin)
	Year=HTMLPage[begin+len('<title>'):end].strip()
	soup = BeautifulSoup(HTMLPage)
	actors=[]
	actors_soup = soup.findAll('span', itemprop="name")
	#soup2= actors_soup[2].contents
	#print soup2
	Actor_Name=[]
	for i in range(len(actors_soup)):
		actors.append(actors_soup[i].contents)
	for j in actors:
		x=str(j)
		y=x.replace("[u'"," ").replace("']"," ")
		Actor_Name.append(y)
	print ("Movie Name And Year is : "+Year)
	print ("Top 5 Actors Are: ")
	for z in range(1,6):
		print (Actor_Name[z])
	return 

MovieSearch()
