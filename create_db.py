#!/usr/bin/env python3
from server_config import db

# load models
from models.crop import Crop
from models.plot import Plot

db.create_all()