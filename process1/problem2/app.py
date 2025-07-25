#터미널 flask 설치 - 웹서버 기능을 쉽게 해주는 파이썬 도구
#pip install flask


from flask import Flask

# app이 먼저 만들어져 있어야!
app = Flask(__name__)

# 웹브라우저에서 첫 페이지 주소(/)”에 뭐 띄울지 정하는 표시 -  @app.route("/") 데코레이터 사용
# 원래 프로그램에선 함수를 호출해야 실행되지만 저 데코레이터 덕분에 클라이언트나 서버가 함수를 명시적으로 호출하지 않더라도 클라이언트가 해당 url로 접속하면 flask가 대신 호출해서 함수가 실행
@app.route("/")
def hello_world() :
    return "Hello, DevOps!"

@app.route("/test")
def hello_worldtest() :
    return "Hello, DevOpstest!"

# 로컬 서버에서 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)