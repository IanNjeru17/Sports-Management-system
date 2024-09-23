from models import Team, Field, Referee, Match
from db import SessionLocal
from datetime import datetime

def schedule_match():
    session = SessionLocal()

    # Get all teams
    teams = session.query(Team).all()
    if not teams:
        print("No teams available. Please add teams first.")
        session.close()
        return
    
    # Select home team
    print("\nSelect the Home Team:")
    for index, team in enumerate(teams, start=1):
        print(f"{index}. {team.name}")
    home_team_choice = int(input("Enter home team number: ")) - 1
    home_team = teams[home_team_choice]

    # Select away team (opponent)
    print("\nSelect the Away Team (Opponent):")
    for index, team in enumerate(teams, start=1):
        if team != home_team:  # Prevent selecting the same team
            print(f"{index}. {team.name}")
    away_team_choice = int(input("Enter away team number: ")) - 1
    away_team = teams[away_team_choice]

    # Select field
    fields = session.query(Field).all()
    if not fields:
        print("No fields available. Please add fields first.")
        session.close()
        return
    
    print("\nSelect the Field:")
    for index, field in enumerate(fields, start=1):
        print(f"{index}. {field.name}")
    field_choice = int(input("Enter field number: ")) - 1
    field = fields[field_choice]

    # Select referee
    referees = session.query(Referee).all()
    if not referees:
        print("No referees available. Please add referees first.")
        session.close()
        return
    
    print("\nSelect the Referee:")
    for index, referee in enumerate(referees, start=1):
        print(f"{index}. {referee.name}")
    referee_choice = int(input("Enter referee number: ")) - 1
    referee = referees[referee_choice]

    # Get the time of play
    time_of_play_str = input("Enter time of play (YYYY-MM-DD HH:MM format): ")
    try:
        time_of_play = datetime.strptime(time_of_play_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD HH:MM' format.")
        session.close()
        return

    # Schedule the match
    new_match = Match(
        home_team_id=home_team.id,  
        away_team_id=away_team.id,  
        field_id=field.id,        
        referee_id=referee.id,      
        time_of_play=time_of_play
    )

    session.add(new_match)
    session.commit()
    print(f"Match scheduled: {home_team.name} vs {away_team.name} on {field.name} at {time_of_play}.")
    session.close()

def view_assignments():
    session = SessionLocal()

    matches = session.query(Match).all()
    if matches:
        print("\nCurrent Match Assignments:")
        for match in matches:
            print(f"{match.home_team.name} vs {match.away_team.name} at {match.field.name}, "
                  f"Referee: {match.referee.name}, Time: {match.time_of_play}")
    else:
        print("No matches scheduled.")
    
    session.close()

def add_team():
    session = SessionLocal()
    team_name = input("Enter team name: ")
    new_team = Team(name=team_name)
    session.add(new_team)
    session.commit()
    print(f"Team '{team_name}' added successfully.")
    session.close()

def delete_team():
    session = SessionLocal()
    teams = session.query(Team).all()
    if not teams:
        print("No teams available to delete.")
        session.close()
        return
    
    print("\nSelect the Team to delete:")
    for index, team in enumerate(teams, start=1):
        print(f"{index}. {team.name}")
    team_choice = int(input("Enter team number: ")) - 1
    team_to_delete = teams[team_choice]

    session.delete(team_to_delete)
    session.commit()
    print(f"Team '{team_to_delete.name}' deleted successfully.")
    session.close()

def list_teams():
    session = SessionLocal()
    teams = session.query(Team).all()
    if teams:
        print("\nList of Teams:")
        for team in teams:
            print(f"- {team.name}")
    else:
        print("No teams available.")
    session.close()

def add_field():
    session = SessionLocal()
    field_name = input("Enter field name: ")
    new_field = Field(name=field_name)
    session.add(new_field)
    session.commit()
    print(f"Field '{field_name}' added successfully.")
    session.close()

def add_referee():
    session = SessionLocal()
    referee_name = input("Enter referee name: ")
    new_referee = Referee(name=referee_name)
    session.add(new_referee)
    session.commit()
    print(f"Referee '{referee_name}' added successfully.")
    session.close()

def update_existing_match():
    session = SessionLocal()
    
    matches = session.query(Match).all()
    if not matches:
        print("No matches available to update.")
        session.close()
        return

    print("\nSelect a match to update:")
    for index, match in enumerate(matches, start=1):
        print(f"{index}. {match.home_team.name} vs {match.away_team.name} on {match.time_of_play}")
    match_choice = int(input("Enter match number: ")) - 1
    selected_match = matches[match_choice]

    print(f"Updating match: {selected_match.home_team.name} vs {selected_match.away_team.name}")

    # Option to update time of play
    time_of_play_str = input("Enter new time of play (YYYY-MM-DD HH:MM format) or press enter to keep current: ")
    if time_of_play_str:
        try:
            time_of_play = datetime.strptime(time_of_play_str, '%Y-%m-%d %H:%M')
            selected_match.time_of_play = time_of_play
        except ValueError:
            print("Invalid date format. Keeping the current time.")
    
    # Commit changes
    session.commit()
    print(f"Match updated successfully.")
    session.close()
