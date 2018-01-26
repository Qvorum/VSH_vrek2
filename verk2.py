from bottle import *
import os

@route("/")
def index():
    return """
    <h2>Verk 2</h2>
    <a href="/a">#1 liður</a>
    <a href="/b">#2 Liður</a>
    """

@route("/a")
def a():
    return """
    <h2>Verkefni 2-A</h2>
    <a href="/page/1">Síða 1</a>
    <a href="/page/2">Síða 2</a>
    <a href="/page/2">Síða 3</a>
    """

@route("/page/<id>")
def page(id):
    if id == '1':
        return "Þetta er síða 1<br><a href='/a'>Til baka</a>"
    if id == '2':
        return "Þetta er síða 2<br><a href='/a'>Til baka</a>"
    if id == '3':
        return "Þetta er síða 3<br><a href='/a'>Til baka</a>"

@route("/b")
def b():
    return """
    <h2>Verkefni 2-B</h2>
    <h3>Veldur Uppáhalds myndina þína!</h3>
    <a href="/page2?img=a"><img src='img/a.jpg'></a>
    <a href="/page2?img=b"><img src='img/b.jpg'></a>
    <a href="/page2?img=c"><img src='img/c.jpg'></a>
    <a href="/page2?img=d"><img src='img/d.jpg'></a>
    """

@route("/page2")
def page():
    l = request.query.img
    if l == 'a':
        return "<h3>Uppáhalds myndin mín er:</h3><img src='img/a.jpg'>"
    if l == 'b':
        return "<h3>Uppáhalds myndin mín er:</h3><img src='img/b.jpg'>"
    if l == 'c':
        return "<h3>Uppáhalds myndin mín er:</h3><img src='img/c.jpg'>"
    if l == 'd':
        return "<h3>Uppáhalds myndin mín er:</h3><img src='img/d.jpg'>"

@error(404)
def villa(error):
    return "<h2>Því miður fann ég ekki myndina en mátti reyna samt!</2>"

@route('/img/<skra>')
def static_skrar(skra):
    return static_file(skra, root='img')
run(host='0.0.0.0', port=os.environ.get('PORT'))
