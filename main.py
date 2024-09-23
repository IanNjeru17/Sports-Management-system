# main.py
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
    while True:
        print("\nSports Management System")
        print("1. Schedule Match")
        print("2. View Assignments")
        print("3. Update Existing Match")
        print("4. Add Team")
        print("5. Add Field")
        print("6. Add Referee")
        print("7. Delete Team")  # New option for deleting a team
        print("8. List All Teams")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            schedule_match()
        elif choice == '2':
            view_assignments()
        elif choice == '3':
            update_existing_match()
        elif choice == '4':
            add_team()
        elif choice == '5':
            add_field()
        elif choice == '6':
            add_referee()
        elif choice == '7':
            delete_team()  
        elif choice == '8':
            list_teams()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
