from bottle import *
import datetime
website={"sample":{"page":[{"name":"hello","text":"hello"}],"password":None}}
@get('/')
def hello():
    return """
<form action="/create" method="POST">url
<input name="name" type="text"　maxlength="20"><br>削除パスワード<input name="password" type="text"><br>
<input type="submit" value="作成する">
</form>
"""
@post('/create')
def hello2():
    global website
    try:
        website[request.forms.name]
        print(request.forms.name)
        return "失敗"
    except:
        if not "/" in request.forms.name and not request.forms.name=="" and not " " in request.forms.name:
            website[request.forms.name]={"page":[],"password":request.forms.password}
            return f"""成功しかした <a href="/chat/{request.forms.name}">/chat/{request.forms.name}</a>"""
        else:
            print(request.forms.name)
            return f"失敗"

@route("/css")
def css():
    return """
chat{
  display:block;
  font-size:150%;
  margin:10% 20% 20% 20%;
}
chat>*{
  width: auto;
}
chat>form>textarea{
  font-size:75%;
　width: 50vh;
　height: 30vh;
  resize: none;
}
chat>form{
  width: 100%;
　height: 100%;
}
flex{
  display:flex;
}
flex>button{
  margin-top:8%;
  margin-left:3%;
  height: 30%;
  font-size:20%;
}
  """
@get("/chat/<name>")
def site(name):
    global website
    chat="<ul>"
    new_line = '\n'
    for i in website[name]["page"]:
        chat=chat+f'''<li>{i["name"].replace("<","&lt;").replace(">","&gt;")}:{i["text"].replace("<","&lt;").replace(">","&gt;").replace(new_line,"<br>")}</li>'''
    return f"""<link rel="stylesheet" href="/css"><title>{name.replace("<","&lt;").replace(">","&gt;")}|fly chat</title>
<chat>
<flex><h1>{name.replace("<","&lt;").replace(">","&gt;")}</h1>
<button onclick="download(`{str(website[name]["page"]).replace("`","")}`,'chat_log_fly_{name.replace("<","&lt").replace(">","&gt")}.txt')">ダウンロード</button></flex>
{chat}</ul>
<form action="{name}/form" method="POST">
名前:<input name="name" type="text"><br>
内容:<textarea name="text" rows="5" cols="60"></textarea><br>
<input type="submit" value="投稿する"></form></chat>"""+"""
<script>
function download(x,y) {
  const blob = new Blob([x],{type:"text/plain"});
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = y;
  link.click();
}</script>"""
@post("/chat/<name>/form")
def page2(name):
    global website
    website[name]["page"].append({"name":request.forms.name,"text":request.forms.text,"time":str(datetime.datetime.now())})
    return f"""<meta http-equiv="refresh"content="0;URL=/chat/{name}">"""
run(host='0.0.0.0', port="10000",)
