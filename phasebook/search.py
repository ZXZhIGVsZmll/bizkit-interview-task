from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    # Return all users if query is empty
    if args == {}:
        return USERS

    # Search with bonus sort
    results = []
    for key,value in args.items():
        for entry in USERS:
            if key == "id":
                if entry[key] == value:
                    results.append(entry)

            elif key == "name":
                if value.lower() in entry[key].lower():
                    results.append(entry)

            elif key == "age":
                if abs(int(entry[key]) - int(value)) < 2:
                    results.append(entry)

            elif key == "occupation":
                if value.lower() in entry[key].lower():
                    results.append(entry)

    # Remove duplicates
    unique_results = []
    for user in results:
        if user not in unique_results:
            unique_results.append(user)

    return unique_results
