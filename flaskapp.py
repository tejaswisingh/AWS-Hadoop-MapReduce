from flask import Flask,render_template,request
from commands import *
import os,time

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hadoop')
def hadoop():
    #Taking input from users for height range and zip code
    #and also the number of Mapper and Reducer tasks..
    hfrom = request.args.get('from')
    hto = request.args.get('to')
    zzip = request.args.get('zip')
    map=request.args.get('map')
    reducer=request.args.get('reduce')

    start=time.time()
    cmd1="/home/ubuntu/hadoop-2.7.1/bin/hadoop jar /home/ubuntu/hadoop-2.7.1/share/hadoop/mapreduce/hadoop-streaming-2.7.1.jar -D mapred.map.tasks="+map+" -D mapred.reduce.tasks="+reducer+" -input /tejaswi/data.csv -output /tejaswi/test -mapper '/home/ubuntu/newmapper.py "+hfrom+" "+hto+" "+zzip+"' -reducer /home/ubuntu/newreducer.py"
    os.system(cmd1)
    end=time.time()
    total=end-start

    cmd2='/home/ubuntu/hadoop-2.7.1/bin/hadoop fs -getmerge /tejaswi/test /home/ubuntu/output.txt'
    os.system(cmd2)

    l=[]
    path='/home/ubuntu/output.txt'
    with open(path) as f:
        l.append(str(f.readlines()))

    return render_template('display.html',data=l, time=total)


if __name__ == '__main__':
	app.run(debug=True)