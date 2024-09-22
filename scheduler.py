from prompt_toolkit import prompt
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Team, Field, Referee, Match
from datetime import datetime

def schedule_match():
    """Schedule a new match by assigning a team, field, referee, and time of play."""
    session = SessionLocal()

    # Prompt the user for team, field, referee, and time of play
    team_name = prompt('Enter team name: ')
    field_name = prompt('Enter field name: ')
    referee_name = prompt('Enter referee name: ')
    time_of_play_input = prompt('Enter time of play (YYYY-MM-DD HH:MM format): ')

    try:
        # Convert the user input to a datetime object
        time_of_play = datetime.strptime(time_of_play_input, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD HH:MM' format.")
        return

    # Query the database for existing team, field, and referee
    team = session.query(Team).filter_by(name=team_name).first()
    field = session.query(Field).filter_by(name=field_name).first()
    referee = session.query(Referee).filter_by(name=referee_name).first()

    if not team or not field or not referee:
        print("Error: Ensure that the team, field, and referee exist.")
        return

    # Create a new match with the provided details
    new_match = Match(team=team, field=field, referee=referee, time_of_play=time_of_play)
    session.add(new_match)
    session.commit()
    print(f'Match scheduled: {team.name} on {field.name} with referee {referee.name} at {time_of_play}.')

def view_assignments():
    """View all scheduled matches."""
    session = SessionLocal()
    matches = session.query(Match).all()
    
    # Display match details
    for match in matches:
        print(f'Match {match.id}: {match.team.name} on {match.field.name} with {match.referee.name} at {match.time_of_play}')

def update_existing_match():
    """Update an existing match with new field, referee, or time of play."""
    session = SessionLocal()
    match_id = int(prompt('Enter match ID to update: '))

    # Fetch the match by its ID
    match = session.query(Match).get(match_id)

    if not match:
        print(f"Match with ID {match_id} not found.")
        return

    # Prompt for new field, referee, or time of play
    field_name = prompt('Enter new field name (leave empty to keep current): ')
    referee_name = prompt('Enter new referee name (leave empty to keep current): ')
    time_of_play_input = prompt('Enter new time of play (YYYY-MM-DD HH:MM) or leave blank to keep current: ')

    # Update field, referee, and time of play if provided
    if field_name:
        field = session.query(Field).filter_by(name=field_name).first()
        if field:
            match.field = field
        else:
            print(f"Field '{field_name}' not found.")

    if referee_name:
        referee = session.query(Referee).filter_by(name=referee_name).first()
        if referee:
            match.referee = referee
        else:
            print(f"Referee '{referee_name}' not found.")

    if time_of_play_input:
        try:
            time_of_play = datetime.strptime(time_of_play_input, '%Y-%m-%d %H:%M')
            match.time_of_play = time_of_play
        except ValueError:
            print("Invalid date format. Keeping current time of play.")

    session.commit()
    print(f"Match {match.id} updated.")

def add_team():
    """Add a new team."""
    session = SessionLocal()
    team_name = prompt('Enter the new team name: ')

    # Check if the team already exists
    if session.query(Team).filter_by(name=team_name).first():
        print(f"Team '{team_name}' already exists.")
        return

    # Add the new team to the database
    new_team = Team(name=team_name)
    session.add(new_team)
    session.commit()
    print(f"Team '{team_name}' added successfully.")

def add_field():
    """Add a new field."""
    session = SessionLocal()
    field_name = prompt('Enter the new field name: ')

    # Check if the field already exists
    if session.query(Field).filter_by(name=field_name).first():
        print(f"Field '{field_name}' already exists.")
        return

    # Add the new field to the database
    new_field = Field(name=field_name)
    session.add(new_field)
    session.commit()
    print(f"Field '{field_name}' added successfully.")

def add_referee():
    """Add a new referee."""
    session = SessionLocal()
    referee_name = prompt('Enter the new referee name: ')

    # Check if the referee already exists
    if session.query(Referee).filter_by(name=referee_name).first():
        print(f"Referee '{referee_name}' already exists.")
        return

    # Add the new referee to the database
    new_referee = Referee(name=referee_name)
    session.add(new_referee)
    session.commit()
    print(f"Referee '{referee_name}' added successfully.")
