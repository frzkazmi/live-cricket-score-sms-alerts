import way2test as s
from cricmain import *
from time import sleep
msg=""
msg2=""
msg3=""
userid=""
passw=""
dest=""
match_status=""
t1, t2, m = get_team_divs(get_bsoup_object(open_url(url)))
#print t1
#print t2
teams=['India','Pakistan','West Indies','Australia','South Africa','Sri Lanka','New Zealand']
#print m

for i in range(2):
	if t1[i][0] in teams:
		msg+=t1[i][0]+" "+"".join(t1[i][1])+" vs "+" "+t2[i][0]+" "+"".join(t2[i][1])+" "+"\n"
#print msg

for j in range(2,4):
	if t1[j][0] in teams:
		msg2+=t1[j][0]+" "+"".join(t1[j][1])+" vs "+" "+t2[j][0]+" "+"".join(t2[j][1])+" "+"\n"
print msg2	

for n in range(3):
	match_status+="".join(m[n])+"\n"
#print match_status	
def send(msg):
	
	s.login(userid,passw)
	s.send_sms(dest,msg)
#print msg+msg2	
send(msg+msg2)



