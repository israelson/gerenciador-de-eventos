from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Event, Registration, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@main.route('/event/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_details.html', event=event)

@main.route('/event/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        # Lógica para criar um evento
        pass
    return render_template('create_event.html')
