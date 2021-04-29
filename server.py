from server_config import app, db

from models.plot import Plot
from models.crop import Crop
from flask import jsonify, request


@app.route('/plot', methods=['GET', 'POST'])
def retrieve_all_plots():
    if request.method == 'GET':    
        plots = Plot.get_all()
        return jsonify([plot.to_json() for plot in plots])
    
    elif request.method == 'POST':
        # curl request -> curl -X POST -d '{"area":21.0, "lat":12.0, "lng":32.45, "state":"hello", "available":false, "num_workers":12}' --header "Content-Type: application/json" "localhost:5000/plot"
        request_data = request.get_json()
        plot = Plot.insert(
            request_data['area'],
            request_data['lat'],
            request_data['lng'],
            request_data['state'],
            request_data['available'],
            request_data['num_workers']
        )
        return plot.to_json()
    
@app.route('/plot/<int:id>')
def retrieve_plots_by_id(id):
    plot = Plot.get_by_id(id)
    return plot.to_json()

@app.route('/crop', methods=['GET', 'POST'])
def retrieve_all_crops():
    if request.method == 'GET':
        crops = Crop.get_all()
        return jsonify([crop.to_json() for crop in crops])

    elif request.method == 'POST':
        # curl request -> curl -X POST -d '{"type":"Flor", "variation":"girasol", "num_seeds":32, "supervisor":"Luisa", "plot_id":1}' --header "Content-Type: application/json" "localhost:5000/crop"
        request_data = request.get_json()
        crop = Crop.insert(
            request_data['type'],
            request_data['variation'],
            request_data['num_seeds'],
            request_data['supervisor'],
            request_data['plot_id']
        )

        plot = Plot.get_by_id(request_data['plot_id'])
        plot.mark_as_used()

        return crop.to_json()