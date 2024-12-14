from profile_skill import Profile
import skillmatchDB

def get_profiles_from_db():
    """Fetch profiles from the database and return them as a dictionary by specialty."""
    profiles = {"Music": [], "Arts": [], "Coding": []}

    # Fetch all users from the database
    users = skillmatchDB.get_all_users()

    # Populate the profiles dictionary
    for user in users:
        # Map the user data to a Profile object and add it to the appropriate list based on specialty
        profile = Profile(user[1], user[3], user[4], user[7], user[8])  # Mapping data to Profile constructor
        if user[3] in profiles:
            profiles[user[3]].append(profile)

    return profiles

# Fetch profiles from the database
profiles = get_profiles_from_db()
