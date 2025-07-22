#터미널 flask 설치 - 웹서버 기능을 쉽게 해주는 파이썬 도구
#pip install flask


from flask import Flask

# app이 먼저 만들어져 있어야 한다멍!
app = Flask(__name__)

# 웹브라우저에서 첫 페이지 주소(/)”에 뭐 띄울지 정하는 표시 -  @app.route("/") 데코레이터 사용
@app.route("/")
def hello_world() :
    return "Hello, DevOps!"

# 로컬 서버에서 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)