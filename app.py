import logging
import os
from pathlib import Path
from typing import List, Optional

import requests
import sh
import typer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

cli = typer.Typer()


@cli.command()
def desktop_apod(debug: bool = False, random: bool = False):
    """
    Sets your desktop background to the Astronomy Picture of the day
    If `random` is `True`, use a random astronomy picture instead.
    """
    img_paths = download_apod(count=1 if random else None, debug=debug)
    set_desktop_backgrounds(img_paths[0])


@cli.command()
def download_apod(
    count: Optional[int] = None,
    debug: bool = False,
) -> List[str]:
    """
    Downloads the Astronomy Picture of the Day
    """
    if debug:
        logger.setLevel(logging.DEBUG)
    with open("nasa_api_key.txt", "r") as f:
        api_key = f.read()
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
    }
    if count:
        params["count"] = count
    response = requests.get(
        url=url,
        params=params,
    )
    if response.status_code == 200:
        if count:
            hdurls = [js["hdurl"] for js in response.json()]
        else:
            hdurls = [response.json()["hdurl"]]
        return [wget_url_move_to_apod_images_dir(url) for url in hdurls]
    else:
        raise Exception(f"NASA APOD api failed. Check response for details. {response.content}")


def apod_images_dir():
    # currently only works on Mac OS
    dir = os.path.join(os.getenv("HOME"), "Pictures", "APOD")
    Path(dir).mkdir(exist_ok=True)
    return dir


def wget_url_move_to_apod_images_dir(url: str) -> str:
    image_file = os.path.basename(url)
    img_path = os.path.join(apod_images_dir(), image_file)
    sh.wget(url)
    sh.mv(image_file, img_path)  # wget downloaded it to the current directory
    return img_path


def set_desktop_backgrounds(img_path: str) -> None:
    sh.osascript("-e", f'tell application "System Events" to tell every desktop to set picture to "{img_path}"')
    return


if __name__ == "__main__":
    cli()
