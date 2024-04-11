from bottle import *
website={"Sample":{"html":"<h1>hello!!</h1>","css":"""h1{
  color:#ffffff
}
body{
  background:#000000
}""","js":'console.log("FlyApp!!")'}}
@get('/')
def hello():
    return """<title>fly chat</title>
<form action="/create" method="POST">url
<input name="name" type="text"><br>
html<br>
<textarea name="html"></textarea>
<br>css<br>
<textarea name="css"></textarea>
<br>js<br>
<textarea name="js"></textarea>
<input type="submit" value="作成する">
</form>
"""
@post('/create')
def hello2():
    global website
    print(request)
    try:
        website[request.forms.name]
        return "失敗"
    except:
        website[request.forms.name]={"html":request.forms.html,"css":request.forms.css,"js":request.forms.js}
        return "成功しかした"

@route("/css/site/<name>")
def css(name):
    global website
    return website[name]["css"].replace('\n', '\n')

@route("/js/site/<name>")
def js(name):
    global website
    return website[name]["js"]

@route("/site/<name>")
def site(name):
    global website
    return f"""<script src="/js/site/{name}"></script><link rel="stylesheet" href="/css/site/{name}">
{website[name]["html"]}"""
run(host='0.0.0.0', port="10000",)
