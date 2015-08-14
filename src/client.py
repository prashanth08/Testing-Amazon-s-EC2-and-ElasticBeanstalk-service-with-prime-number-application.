import requests,time
import sys,os

username = sys.argv[1]
netid = sys.argv[2]
password = sys.argv[3]
start = sys.argv[4]
end = sys.argv[5]
start_num=int(start)
end_num=int(end)
tot_lat = 0
latency = []
#http://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    if len(lst) %2 == 0:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

if(start_num%2==0):
	start_num = start_num+1
for i in range(start_num,end_num,2):
	st = (time.time())
	r = requests.get("http://cs5412pb476-env.elasticbeanstalk.com/prime?n="+ str(i))
	en = (time.time() - st)
	latency.append(en)
	
	tot_lat=tot_lat + en

	#print r.text #prints weather prime or not
	#print en
latency.sort()	
med = median(latency)
min_lat = min(latency)
max_lat = max(latency)
mean = float(sum(latency))/len(latency) if len(latency) > 0 else float('nan')
with open('test.txt', 'w') as f:
	print "Number of queries fired:",    len(latency)
	print "Latency Min:",  min_lat   
	print "Latency Max:",  max_lat
	print "Latency Mean:", 	mean
	print "Latency Median", med
	f.write(username + ' '+ netid + ' ' + password + ' ' + '\n' + "Minimum = %s\n" % str(min_lat))
	f.write("Maximum = %s\n" % str(max_lat))
	f.write("Mean = %s\n" % str(mean))
	f.write("Median = %s\n" % str(med))

	