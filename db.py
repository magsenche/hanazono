import argparse
import os
import pathlib

import requests
from bs4 import BeautifulSoup


def csrf_token(response: requests.Response) -> str:
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
    return token


def login_session(host_url: str) -> tuple[requests.Session, dict]:
    session = requests.Session()

    # Get the login page to fetch the CSRF token
    response = session.get(f"{host_url}/adminlogin/")
    response.raise_for_status()  # Ensure we got a successful response
    login_data = {
        "username": os.environ.get("DJANGO_SUPERUSER_USERNAME"),
        "password": os.environ.get("DJANGO_SUPERUSER_PASSWORD"),
        "csrfmiddlewaretoken": csrf_token(response),
    }
    return session, login_data


def export_db(host_url: str, output_path: pathlib.Path):
    session, login_data = login_session(host_url)
    response = session.post(
        f"{host_url}/adminlogin/?next=/admin/export_data/",
        data=login_data,
        headers={"Referer": f"{host_url}/adminlogin"},
    )
    response.raise_for_status()  # Ensure we got a successful response
    output_path.write_text(response.text)


def import_db(host_url: str, import_path: pathlib.Path):
    session, login_data = login_session(host_url)
    login_response = session.post(
        f"{host_url}/adminlogin/?next=/admin",
        data=login_data,
        headers={"Referer": f"{host_url}/adminlogin"},
    )
    login_response.raise_for_status()
    response = session.post(
        f"{host_url}/admin/import_data/",
        files={"file": (str(import_path), import_path.read_text(), "application/json")},
        data={
            "csrfmiddlewaretoken": csrf_token(login_response),
        },
        headers={"Referer": f"{host_url}/admin"},
    )
    response.raise_for_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["import", "export"])
    parser.add_argument("-f", "--file", type=str, required=True)
    parser.add_argument("-H", "--host", type=str, required=True)
    args = parser.parse_args()
    match args.command:
        case "export":
            output_path = pathlib.Path(args.file).with_suffix(".json")
            export_db(args.host, output_path)
        case "import":
            import_path = pathlib.Path(args.file)
            import_db(args.host, import_path)
