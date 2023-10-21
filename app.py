import io
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from config import get_config_by_flask_env
from models.models import FileSystem
from models import db
from flask import Flask, request, send_file
from azure.storage.blob import BlobServiceClient

app = Flask(__name__, static_folder='static', static_url_path="/static")
app.config.from_object(get_config_by_flask_env())
db.init_app(app)

# Replace 'your_connection_string' with your Azure Blob Storage connection string
load_dotenv()
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "rag-hackathon-demo"


@app.route('/download/<file_id>', methods=['GET'])
def download_blob(file_id):
    print(file_id)
    try:
        file_instance = FileSystem.query.filter(FileSystem.id == file_id).first()
        blob_name = file_instance.file_path
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_properties = blob_client.get_blob_properties()

        # Set the appropriate content type for the file
        response_headers = {
            'Content-Type': blob_properties['content_settings']['content_type']
        }

        # Use io.BytesIO to wrap the blob content as a file-like object
        file_data = blob_client.download_blob().readall()
        file_obj = io.BytesIO(file_data)

        # Stream the file to the client
        return send_file(
            file_obj,
            as_attachment=True,
            download_name=blob_name,
            mimetype=response_headers['Content-Type']
        )
    except Exception as e:
        return str(e), 404  # You can handle errors appropriately


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/review')
def review():
    #  get review_page_index.html
    data_list = FileSystem.query.filter(FileSystem.censor_status == 0).all()

    return render_template("review_page_index.html", data=data_list)


@app.route('/get-data', methods=['GET'])
def get_data():
    evaluation_list = FileSystem.query.filter(FileSystem.censor_status == 0).all()
    # turn the evaluation_list into a list of dictionaries
    evaluation_list = [evaluation.to_dict() for evaluation in evaluation_list]
    return jsonify({"data": evaluation_list}), 200


@app.route(f'/change_status_to_success/<file_system_id>', methods=['GET'])
def change_status_to_success(file_system_id):
    print(file_system_id)
    file_instance = FileSystem.query.filter(FileSystem.id == file_system_id).first()
    file_instance.censor_status = 2
    db.session.add(file_instance)
    db.session.commit()
    return jsonify({"data": f"success in {file_system_id}"}), 200


@app.route(f'/change_status_to_failed/<file_system_id>', methods=['GET'])
def change_status_to_failed(file_system_id):
    # print(file_system_id)
    file_instance = FileSystem.query.filter(FileSystem.id == file_system_id).first()
    file_instance.censor_status = 3
    db.session.add(file_instance)
    db.session.commit()
    return jsonify({"data": f"success in {file_system_id}"}), 200


if __name__ == '__main__':
    app.run()
