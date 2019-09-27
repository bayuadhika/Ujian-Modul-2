from flask import Flask,render_template
from plots import count_type1, dist_total       
from cleaning_data import IndiaClean            
app = Flask(__name__)

# ROUTE
# RENDER TEMPLATE
# RENDER TEMPLATE WITH VARIABLE

@app.route('/')
def index():
    data = IndiaClean()
    return render_template('table_data.html' , dataX = data)


@app.route('/data')
def dataX():
    data = IndiaClean()
    return render_template('table_data.html' , dataX = data)


# @app.route('/plots')
# def plots():
#     plot1 = count_type1()
#     plot2 = dist_total()
#     return render_template('plots.html' , data=[plot1,plot2])


if __name__ == '__main__':
    app.run(debug=True, port=1989)