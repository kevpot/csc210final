from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .. import db
from . import main
from ..models import Data, User
from .forms import PlayerForm



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scouts')
def Scouts():
    stats = Data.query.all()
    return render_template("scouts.html", stats=stats)


@main.route('/managers')
def Managers():
    stats = Data.query.all()
    return render_template("managers.html", stats=stats)


#Adds new player
@main.route('/addplayer', methods=['GET', 'POST'])
@login_required
def addplayer():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Data(first_name=form.first_name.data,
                    middle_initial=form.middle_initial.data,
                    last_name=form.last_name.data,
                    date_of_birth=form.date_of_birth.data,
                    age=form.age.data,
                    home_town=form.home_town.data,
                    height=form.height.data,
                    weight=form.weight.data)
        db.session.add(player)
        db.session.commit()
        flash('Player Added.')
        return redirect(url_for('main.Scouts'))
    return render_template('player.html', form=form)

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    deleting_item = Data.query.get_or_404(id)
    try:
    	db.session.delete(deleting_item)
    	db.session.commit()
    	return redirect(url_for('main.Scouts'))

    except:
    	return "couldn't delete that homie"

