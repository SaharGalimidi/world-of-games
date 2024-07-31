from flask import Flask, render_template, request, redirect, url_for, session, current_app as app, flash
from app.games import guess_game, memory_game, currency_roulette_game
from app.score import add_score, get_score
import json

@app.route('/')
def index() -> str:
    app.logger.debug('Rendering index page')
    return render_template('index.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome_route() -> str:
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Name is required!')
            return redirect(url_for('index'))
        session['username'] = name
        message = f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."
        app.logger.debug(f'User {name} logged in')
        return render_template('welcome.html', message=message)
    app.logger.debug('Rendering welcome page')
    return render_template('index.html')

@app.route('/game_selection', methods=['GET', 'POST'])
def game_selection() -> str:
    difficulty = request.args.get('difficulty', 1, type=int)
    if request.method == 'POST':
        try:
            game_choice = int(request.form['game_choice'])
            difficulty = int(request.form['difficulty'])
            app.logger.debug(f'Game choice: {game_choice}, Difficulty: {difficulty}')
            
            if game_choice not in [1, 2, 3]:
                raise ValueError("Invalid game choice or difficulty")
            if game_choice == 1:
                return redirect(url_for('play_memory', difficulty=difficulty))
            elif game_choice == 2:
                return redirect(url_for('play_guess', difficulty=difficulty))
            elif game_choice == 3:
                return redirect(url_for('play_currency', difficulty=difficulty))
            
        except ValueError as e:
            app.logger.error(f'Error in game selection: {e}')
            flash(str(e))
            return render_template('game_selection.html', error=str(e), difficulty=difficulty)
        
    app.logger.debug('Rendering game selection page')
    return render_template('game_selection.html', difficulty=difficulty)

@app.route('/play_memory/<int:difficulty>', methods=['GET', 'POST'])
def play_memory(difficulty: int) -> str:
    if request.method == 'POST':
        try:
            user_sequence = request.form.getlist('sequence')[0].split(' ')
            user_sequence = [int(num) for num in user_sequence]
            original_sequence = json.loads(session.get('sequence', '[]'))
            result = memory_game.is_list_equal(original_sequence, user_sequence)
            if result:
                add_score(difficulty)
            app.logger.debug(f'Memory game result: {result}')
            return render_template('result.html', result=result, score=get_score(), difficulty=difficulty)
        except ValueError:
            app.logger.error('Invalid input in memory game')
            flash('Invalid input')
            return render_template('play_memory.html', error="Invalid input", sequence=[])
    sequence = memory_game.generate_sequence(difficulty)
    session['sequence'] = json.dumps(sequence)  # Store the sequence in session
    app.logger.debug(f'Generated sequence for memory game: {sequence}')
    return render_template('play_memory.html', sequence=sequence, difficulty=difficulty)

@app.route('/play_guess/<int:difficulty>', methods=['GET', 'POST'])
def play_guess(difficulty: int) -> str:
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            original_number = session.get('number')
            result = guess_game.compare_results(original_number, guess)
            if result:
                add_score(difficulty)
            app.logger.debug(f'Guess game result: {result}')
            return render_template('result.html', result=result, score=get_score(), difficulty=difficulty)
        except ValueError:
            app.logger.error('Invalid input in guess game')
            flash('Invalid input')
            return render_template('play_guess.html', error="Invalid input", difficulty=difficulty)
    number = guess_game.generate_number(difficulty)
    session['number'] = number  # Store the number in session
    app.logger.debug(f'Generated number for guess game: {number}')
    return render_template('play_guess.html', difficulty=difficulty)

@app.route('/play_currency/<int:difficulty>', methods=['GET', 'POST'])
def play_currency(difficulty: int) -> str:
    if request.method == 'POST':
        try:
            guess = float(request.form['guess'])
            lower, upper = json.loads(session.get('interval', '[0, 0]'))
            result = lower <= guess <= upper
            if result:
                add_score(difficulty)
            app.logger.debug(f'Currency roulette game result: {result}')
            return render_template('result.html', result=result, score=get_score(), difficulty=difficulty)
        except ValueError:
            app.logger.error('Invalid input in currency roulette game')
            flash('Invalid input')
            return render_template('play_currency.html', error="Invalid input", interval=[])
    interval = currency_roulette_game.get_money_interval(difficulty)
    session['interval'] = json.dumps(interval)  # Store the interval in session
    app.logger.debug(f'Generated interval for currency roulette game: {interval}')
    return render_template('play_currency.html', interval=interval)

@app.route('/score')
def score_route() -> str:
    score = get_score()
    app.logger.debug(f'Current score: {score}')
    return render_template('score.html', score=score)
