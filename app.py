from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Mengubah coding di dalam app.py'

if __name__ == '__main__':
    app.run()
