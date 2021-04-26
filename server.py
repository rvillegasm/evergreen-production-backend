from server_config import app, db

from models.plot import Plot

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