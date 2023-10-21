from flask import Flask, jsonify, render_template
from config import get_config_by_flask_env
from models.models import FileSystem
from models import db

app = Flask(__name__, static_folder='static', static_url_path="/static")
app.config.from_object(get_config_by_flask_env())
db.init_app(app)


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
