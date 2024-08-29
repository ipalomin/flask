from flask import Blueprint

taskRoute = Blueprint('tasks',__name__,url_prefix='/tasks')

@taskRoute.route('/')
def index():
    return 'Index'

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show'+str(id)

@taskRoute.route('/delete<int:id>')
def delete(id:int):
    return 'Delete'+str(id)

@taskRoute.route('/create', methods=['POST','GET'])
def create():
    return 'Create'

@taskRoute.route('/update<int:id>', methods=['POST','GET'])
def update(id:int):
    return 'Update'+str(id)