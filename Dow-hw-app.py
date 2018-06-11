import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DataSets/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)


class otu(db.Model)
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)
    def __repr__(self):
        return '<otu %r>' % (self.otu_id)

class Samples_Metadata(db.Model):
    __tablename__ = 'samples_metadata'

    SAMPLEID = db.Column(db.Integer, primary_key=True)
    AGE = db.Column(db.Integer)
    BBTYPE = db.Column(db.String)
    ETHNICITY = db.Column(db.String)
    GENDER = db.Column(db.String)
    LOCATION = db.Column(db.String)


    def __repr__(self):
        return '<Samples_Metadata %r>' % (self.SAMPLEID)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    """Return the dashboard."""
    return render_template("index.html")

@app.route("/names")
def names_data():
    """Return list of sample names"""

    return db.samples.columns
    limit(10).all()




@app.route("/otu")
def otu_data():
    """Return OTU descriptions"""

    # return OTU descriptions
    results = db.session.query(otu.otu_id, otu.lowest_taxonomic_unit_found)\
    limit(10).all()

    # Select the top 10 query results
    otu_result = [result[0] for result in results]
    taxonomic_result = [(result[1]) for result in results]

    return taxonomic_results

@app.route('/metadata/<sample>')
    """MetaData for a given sample.

    Args: Sample in the format: `BB_940`

    Returns a json dictionary of sample metadata in the format
# 








if __name__ == '__main__':
    app.run(debug=True)
