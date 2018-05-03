from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.') # '.'은 현재 디렉터리를 의미

run(host='localhost', port=9999) #웹 서버 실행