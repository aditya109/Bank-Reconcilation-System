from flask import Flask, request, redirect, send_from_directory
from flask_cors import CORS, cross_origin

from sample.cmd.main import filter_trigger

# Initializing the Flask app
app = Flask(__name__)

# Enabling `Cross-Origin Resource Policy` for app
CORS(app=app, support_credentials=True)
config = None


# Setting upload route
@app.route("/upload", methods=["POST"])
@cross_origin(supports_credentials=True)
def upload_file():
    """
    Upload file to static directory
    """
    
    if request.files:

        # excel = request.files["excel"]
        # print("excel = ", excel)
        # excel.save(config['static'].join(excel.filename))
        # print("excel saved..")
        # if excel.filename == "":
        #     print("No filename")
        # filter_trigger(filename=excel.filename)
        return "200!"
    else:
        return "OK!"


# Setting residue download route
@app.route("/download_residue", methods=["GET"])
@cross_origin(support_credentials=True)
def download_resultant_file():
    """
    Download resultant file from output directory
    """
    return send_from_directory(config['PROJECT_DIRECTORY']["output_directory_path"], "compiled_sheets.xls")


# Setting brs download route
@app.route("/download_brs", methods=["GET"])
@cross_origin(support_credentials=True)
def download_brs_file():
    """
    Download BRS Report from output directory
    """
    return send_from_directory(config['PROJECT_DIRECTORY']["OUTPUT_DIRECTORY"], "brs.xls")


@app.route("/get_chord", methods=["GET"])
@cross_origin(support_credentials=True)
def get_chord_stats():
    """
    Get Statistical Data in Chord Diagrams
    """
    return "Hello"


def trigger(configuration):
    global config
    config = configuration
    app.run(debug=True)
