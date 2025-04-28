from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mamad.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, OBJECTNUMBER
import mysql.connector
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    pagenumber = request.GET.get('page', 1)
    res = []
    with mysql.connector.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM groups"
            cursor.execute(sql)
            for i in cursor:
                res.append({"link":i[1], "title":i[3], "des":i[4]})
                
    p = Paginator(res, OBJECTNUMBER)
    page = p.page(pagenumber)
    context = {'res': page, 'p':p}


    return render(request, "index.html", context=context)


def deleteaction(request):
    dellist = request.POST.getlist('mamad')
    for i in dellist:
        with mysql.connector.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD,
                                     host=DATABASE_HOST) as connection:
            with connection.cursor() as cursor:
                sql = f"DELETE FROM groups WHERE link='{i}'"
                cursor.execute(sql)
                connection.commit()
    return HttpResponseRedirect(reverse('index'))


def index1(request):
    res = []
    with mysql.connector.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD,
                                 host=DATABASE_HOST) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM groups"
            cursor.execute(sql)
            for i in cursor:
                res.append({"link": i[1], "title": i[3], "des": i[4]})
    context = {'res': res}

    return render(request, "index1.html", context=context)