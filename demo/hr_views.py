from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def list_jobs(request):
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs order by minsal desc")
    jobs = cur.fetchall()
    print(jobs)
    con.close()
    return render(request,'list_jobs.html',{'jobs' : jobs})
