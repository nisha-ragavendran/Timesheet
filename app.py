import os

from flask import Flask, render_template, request

import savedb

app = Flask(__name__, template_folder="Templates", static_folder="static")


def _build_timesheet_document(formdata):
    user_name = formdata.get("User", "").strip()
    date = formdata.get("Date", "").strip()
    counter_raw = formdata.get("counter", "0")

    if not user_name or not date:
        raise ValueError("User and Date are required.")

    try:
        counter_int = int(counter_raw)
    except ValueError as exc:
        raise ValueError("Invalid task counter value.") from exc

    if counter_int < 1:
        raise ValueError("At least one task row is required.")

    task_dict = {}
    task_index = 0
    for i in range(counter_int):
        project = formdata.get(f"text_{i}_P", "").strip()
        task = formdata.get(f"text_{i}_T", "").strip()
        hours = formdata.get(f"text_{i}_H", "").strip()

        has_any_value = any([project, task, hours])
        has_all_values = all([project, task, hours])
        if has_any_value and not has_all_values:
            raise ValueError("Each task row must include project, task, and hours.")
        if has_all_values:
            task_dict[f"Task_{task_index}"] = [project, task, hours]
            task_index += 1

    if not task_dict:
        raise ValueError("At least one completed task row is required.")

    return {"User": user_name, "Date": date, "Task_dts": task_dict}

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/insertdata", methods = ['POST'])
def insertdata():
    formdata = request.form.to_dict()
    try:
        create_row = _build_timesheet_document(formdata)
    except ValueError as exc:
        return (
            render_template("submit.html", success=False, message=str(exc)),
            400,
        )

    response = savedb.insert_row(create_row)
    if not response.get("ok"):
        return (
            render_template(
                "submit.html",
                success=False,
                message=f"Failed to save timesheet: {response.get('error', 'unknown error')}",
            ),
            502,
        )

    return render_template("submit.html", success=True, message="Timesheet has been updated!")

@app.route("/find", methods = ['GET'])
def find():
    user_name = request.args.get("User", "").strip()
    date = request.args.get("Date", "").strip()
    if not user_name or not date:
        return (
            render_template(
                "find.html",
                found=False,
                message="User and Date are required to search.",
            ),
            400,
        )

    response = savedb.find_data(user_name, date)
    if not response.get("ok"):
        return (
            render_template(
                "find.html",
                found=False,
                message=f"Search failed: {response.get('error', 'unknown error')}",
            ),
            502,
        )

    if not response.get("document"):
        return render_template(
            "find.html",
            found=False,
            message=f"No timesheet found for user '{user_name}' on date '{date}'.",
        )

    return render_template("find.html", found=True, data=response)

@app.route("/delete", methods = ['POST'])
def delete():
    formdata = request.form.to_dict()
    user_name = formdata.get("User", "").strip()
    date = formdata.get("Date", "").strip()
    if not user_name or not date:
        return (
            render_template(
                "display.html",
                success=False,
                message="User and Date are required to delete a timesheet.",
            ),
            400,
        )

    response = savedb.delete_data(user_name, date)
    if not response.get("ok"):
        return (
            render_template(
                "display.html",
                success=False,
                message=f"Delete failed: {response.get('error', 'unknown error')}",
            ),
            502,
        )

    deleted_count = response.get("deletedCount", 0)
    if deleted_count < 1:
        return render_template(
            "display.html",
            success=False,
            message="No matching timesheet found to delete.",
        )

    return render_template(
        "display.html",
        success=True,
        message="Timesheet entry deleted successfully.",
    )

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, port=5001)
