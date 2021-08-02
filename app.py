from flask import Flask
from flaskext.mysql import MySQL
from flask import request
from config import *
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host
app.config['JSON_AS_ASCII'] = False
mysql.init_app(app)


@app.route('/pzg')
def google():
    arg_project_name = request.args.get('projectname', default='not_defined', type=str)
    arg_date = request.args.get('date', default='not_defined', type=str)
    arg_type_device = request.args.get('type_device', default='not_defined', type=str)
    arg_target_url = request.args.get('target_url', default='not_defined', type=str)
    arg_query = request.args.get('query', default='not_defined', type=str)
    arg_position = request.args.get('position', default='not_defined', type=str)
    arg_get_param = request.args.get('get_param', default='not_defined', type=str)
    arg_record_id = request.args.get('record_id', default='not_defined', type=str)
    arg_profile_id = request.args.get('profile_id', default='not_defined', type=str)

    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "INSERT INTO google_ibot(project_name, date, type_profile, target_url, key_serp, key_position, get_params, " \
          "id_query_record_bd, profile_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,
                   (arg_project_name, arg_date, arg_type_device, arg_target_url, arg_query, arg_position, arg_get_param,
                    arg_record_id, arg_profile_id))
    cursor.close()
    conn.commit()
    return "OK"


@app.route('/pzy')
def yandex():
    arg_project_name = request.args.get('projectname', default='not_defined', type=str)
    arg_date = request.args.get('date', default='not_defined', type=str)
    arg_type_device = request.args.get('type_device', default='not_defined', type=str)
    arg_target_url = request.args.get('target_url', default='not_defined', type=str)
    arg_query = request.args.get('query', default='not_defined', type=str)
    arg_position = request.args.get('position', default='not_defined', type=str)
    arg_get_param = request.args.get('get_param', default='not_defined', type=str)
    arg_record_id = request.args.get('record_id', default='not_defined', type=str)
    arg_profile_id = request.args.get('profile_id', default='not_defined', type=str)

    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "INSERT INTO yandex_ibot(project_name, date, type_profile, target_url, key_serp, key_position, get_params, " \
          "id_query_record_bd, profile_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,
                   (arg_project_name, arg_date, arg_type_device, arg_target_url, arg_query, arg_position, arg_get_param,
                    arg_record_id, arg_profile_id))
    cursor.close()
    conn.commit()
    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
