from flask import Flask
import os
import datetime
import psutil

app = Flask(__name__)

def get_top_output():
    return os.popen("top -b -n 1").read()

@app.route('/htop')
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = get_top_output()

    return f"""
    <h1>Name - Shashwat Tewari</h1>
    <h2>Username - {username}</h2>
    <h2>Server Time (IST) - {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
