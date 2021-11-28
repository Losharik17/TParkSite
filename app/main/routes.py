import employee as employee
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from app.main import bp
from app import db
from app.models import Text, Event, Category, ServiceCategory, Service, Employee
from sqlalchemy import create_engine

engine = create_engine("sqlite:///T_Park.db")


@bp.route('/', methods=['GET'])
@bp.route('/TPark', methods=['GET'])
def index():
    main_text = Text.query.filter_by(title="main_text").first().text
    events = Event.query.all()

    return render_template('main/main.html', main_text=main_text, events=events)


@bp.route('/category', methods=['GET'])
def test():
    try:
        category_id = request.args.get('category_id')

        category = Category.query.filter_by(id=category_id).first()
        services = category.services.all()

        return render_template('main/category.html', category=category, category_id=category_id,
                               services=services)
    except:
        return render_template('errors/500.html')


@bp.route('/category/service', methods=['GET'])
def service():
    service_id = request.args.get('service_id')

    service = Service.query.filter_by(id=service_id).first()
    return render_template('main/service.html', service=service)


@bp.route('/O_nas', methods=['GET'])
def O_nas():

    O_nas_text = Text.query.filter_by(title="O_nas").first().text
    employees = Employee.query.all()

    return render_template('main/O_nas.html', O_nas_text=O_nas_text, employees=employees)
