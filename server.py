from server_config import app, db

from models.plot import Plot
from models.crop import Crop
from flask import jsonify


@app.route('/')
def hello_world():
    test_plot = Plot(
        area=32.2,
        lat=12.0,
        lng=12.0,
        state='Nice',
        available=True,
        num_workers=20
    )

    db.session.add(test_plot)
    db.session.commit()

    return 'hello world!'

@app.route('/plot')
def retrievePlots():
    query = Plot.query.all()
    if (len(query) > 0):
        return jsonify(query)
    else:
        return "No hay datos disponibles"    
    
@app.route('/crop')
def retrieveCrops():
    query = Crop.query.all()
    if (len(query) > 0):
        res = " "
        for row in query:
            res+= "Type:"+str(row.type)+ " Variation:"+str(row.variation) + "\n\n"
        return res    
    else:
        return "No hay datos disponibles"    
    