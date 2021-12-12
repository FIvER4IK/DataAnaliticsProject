from flask import Flask, render_template
import jupyter as jp
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/task1.html')
def task1():
    tables, titles = jp.tables, jp.titles
    oil_stat, gold_stat, snp_stat = jp.oil_stat, jp.gold_stat, jp.snp_stat
    return render_template('task1.html', tables=tables, titles=titles, oil_stat=oil_stat, gold_stat=gold_stat, snp_stat=snp_stat)

@app.route('/task2.html')
def task2():
    return render_template('task2.html')

@app.route('/task2.5.html')
def task2point5():
    return render_template('task2.5.html')

@app.route('/task3.html')
def task3():
    return render_template('task3.html')

if __name__ == "__main__":
    app.run(debug=True)
