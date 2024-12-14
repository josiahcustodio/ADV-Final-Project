import skillmatchDB
from profile_skill import Profile

def test_database():
    # Create tables if they don't exist
    skillmatchDB.create_tables()

    # Insert profiles into the database for testing
    skillmatchDB.insert_profile("Alice", "Music", "Guitar", "Novice", 0)
    skillmatchDB.insert_profile("Bob", "Music", "Piano", "Intermediate", 10)
    skillmatchDB.insert_profile("Charlie", "Music", "Violin", "Professional", 30)

    # Retrieve all profiles and print them
    profiles = skillmatchDB.get_all_profiles()

    # Print out profiles fetched from the database
    print("Profiles in the database:")
    for profile in profiles:
        print(profile)

if __name__ == "__main__":
    test_database()
