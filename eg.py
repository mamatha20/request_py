import requests
import json
from requests.api import options, request
result=requests.get('https://saral.navgurukul.org/api/courses')
data=result.json()
# print(data)
def opt(slect,var2,slug,data2):
    while True:
        x=var2
        options=input("enter your option up next exit back ")
        if options=="up":
            print(x)
            x-=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(slect)+"/exercise/getBySlug?slug="+str(slug[x]))
            r=req.json()
            print("content",r["content"])
            print(x)
        elif options=="next":
            x+=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(slect)+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1["content"])
            print(x)
        elif options=="back":
            c=1
            for dic1 in data2["data"]:
                print(c,dic1["name"])
                c+=1
                for i in dic1["childExercises"]:
                    print("    ",c,i["name"])
                    c+=1
        else:
            break
def course():
    index=0
    for i in data["availableCourses"]:
        print(index+1,i["name"],i["id"])
        index+=1
    count=0

    for courses in data["availableCourses"]:
        course=int(input("select your course="))
        slect=data["availableCourses"][course-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(slect)+"/exercises")
        data2=var.json()
        slug=[]
        count3=1
        for dic_data2 in data2["data"]:
            print(count3,dic_data2["name"])
            slug.append(dic_data2["slug"])
            count3+=1
            for child in dic_data2["childExercises"]:
                print("       ",count3,child["name"])
                slug.append(child["slug"])
                count3+=1
        var2=int(input("show content slug"))
        var3=requests.get("https://saral.navgurukul.org/api/courses/"+str(slect)+"/exercise/getBySlug?slug="+str(slug[var2-1]))
        data3=var3.json()
        print(data3["content"])
        opt(slect,var2,slug,data2)
course()