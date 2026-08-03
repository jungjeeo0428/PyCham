from flask import Flask, render_template, request
from db_test import get_member

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    return ("hello")
@app.route('/main')
def main():
    nm = "nick"
    return render_template("main.html", nm=nm)

@app.route("/list")
def list():
    members = get_member()
    return render_template("list.html", members=members)
@app.route("/test", methods=['post'])
def test():
    mem_id = request.form.get('memId')
    return f"hello {mem_id}"
if __name__ == "__main__":(
    app.run(debug=True, port=5500, host="0.0.0.0"))