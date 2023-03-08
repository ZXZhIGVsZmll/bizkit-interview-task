from flask import Blueprint,request

from .data.schedule_data import SCHEDULES

bp = Blueprint("schedule", __name__, url_prefix="/schedule")

@bp.route("<int:user_id>", methods=["POST"])
def schedule(user_id):
    return get_schedule(user_id)
 

def get_schedule(user_id):
    req_data = request.get_json()
    start = req_data["start"]
    end = req_data["end"]

    id_list = [SCHEDULES[i]["user_id"] for i in SCHEDULES]

    # Recurring user id
    if user_id in id_list:
        for i in SCHEDULES:
            if SCHEDULES[i]["user_id"] == user_id:
                if f"{start} - {end}" in SCHEDULES[i]["schedules"]:
                    msg = f'Requested time "{start} - {end}" is duplicate for User ID: {user_id}'

                    return f"{msg}\n{SCHEDULES[i]}\n"

                else:
                    msg = f'"{start} - {end}" added to list for User ID: {user_id}'
                    SCHEDULES[i]['schedules'].append(f"{start} - {end}")

                    return f"{msg}\n{SCHEDULES[i]}\n"

    # New user id
    else:
        req = {
            "user_id": user_id,
            "schedules": [
                f"{start} - {end}",
            ]
        }

        msg1 = f"New user found. User ID: {user_id}"
        msg2 = f'"{start} - {end}" added to list for User ID: {user_id}'
        sched_id = len(SCHEDULES)
        SCHEDULES[sched_id] = req

        return f"{msg1}\n{msg2}\n{SCHEDULES[sched_id]}\n"
