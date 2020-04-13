
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/play')
def play():
    inputRoute='landing'
    # return render_template('index.html')
    return render_template('index.html', inputRoute=inputRoute) #Bonus: Implement all routes with one template

@app.route('/play/<int:times>')
def play_times(times):
    inputRoute='times'
    # return render_template('index.html', times=times)
    return render_template('index.html', inputRoute=inputRoute, times=times) #Bonus: Implement all routes with one template


@app.route('/play/<int:times>/<string:color>')
def play_times_color(times, color):
    inputRoute='color'
    # style = f'<div class="square" style="background-color: {color};"></div>'
    # style = f'background-color: {color});'
    # print('*'*10 + style)
    # return render_template('index.html', times=times, color=color)
    return render_template('index.html', inputRoute=inputRoute, times=times, color=color) #Bonus: Implement all routes with one template


if __name__ == '__main__':
    app.run(debug=True)