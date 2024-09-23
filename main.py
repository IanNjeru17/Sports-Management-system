from db import initialize_db, SessionLocal
from scheduler import (
    schedule_match,
    view_assignments,
    update_existing_match,
    add_team,
    add_field,
    add_referee,
    delete_team,
    list_teams
)

def main():
    # Initialize the db
    initialize_db()
    
    while True:
        print("\nSports Management System")
        print("1. Add Team")
        print("2. Add Field")
        print("3. Add Referee")
        print("4. List All Teams")
        print("5. Schedule Match")
        print("6. View Assignments")
        print("7. Delete Team")
        print("8. Update Existing Match")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '5':
            schedule_match()
        elif choice == '6':
            view_assignments()
        elif choice == '8':
            update_existing_match()
        elif choice == '1':
            add_team()
        elif choice == '2':
            add_field()
        elif choice == '3':
            add_referee()
        elif choice == '7':
            delete_team()
        elif choice == '4':
            list_teams()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
