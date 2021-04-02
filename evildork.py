#
# Fricciolosa Red Team presents:
#             _ _     _            _
#   _____   _(_) | __| | ___  _ __| | __
#  / _ \ \ / / | |/ _` |/ _ \| '__| |/ /
# |  __/\ V /| | | (_| | (_) | |  |   <
#  \___| \_/ |_|_|\__,_|\___/|_|  |_|\_\
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
#
#   @Repository:  https://github.com/Fricciolosa-Red-Team/evildork
#
#   @Author:      Fricciolosa Red Team


# ======= IMPORT =========

import argparse
import os
import urllib.parse


# ======= INTRO ========


def banner():

    RED = "\033[91m"
    ENDC = "\033[0m"
    banner = (
        RED
        + """             _ _     _            _
   _____   _(_) | __| | ___  _ __| | __
  / _ \\ \\ / / | |/ _` |/ _ \\| '__| |/ /
 |  __/\\ V /| | | (_| | (_) | |  |   <
  \\___| \\_/ |_|_|\\__,_|\\___/|_|  |_|\\_\\
"""
        + ENDC
    )

    print(banner)


# ======= GLOBAL VARS ========

dorks_file = "dorks.txt"

# ======= ARGUMENT ========


def get_parser():
    """Create and return a parser (argparse.ArgumentParser instance) for main()
    to use"""
    parser = argparse.ArgumentParser(description="Evildork targeting your fiancee")
    parser.add_argument(
        "-d",
        "--domain",
        type=str,
        help="Set the target (a domain)",
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Show the version of evildork"
    )
    return parser


# ======== FUNCTIONS =======


def create_output_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(directory, target):

    create_output_folder(directory)
    filename = directory + "/" + "evildork-" + target + ".html"

    if os.path.exists(filename):
        choice = input(
            "[!] {} already exists. Do you want to overwrite? (y/n):".format(filename)
        )
        if str(choice).lower() != "y":
            exit(1)
        # if choice == y: ====> go forward. The file's content will be flushed and overwritten
    else:
        os.mknod(filename)
    return filename


def add_HTML_banner(filename):

    html_banner = """
    <html>
    <head>
    <title> EVILDORK </title>
    </head>
    <body>
    <h1> EVILDORK </h1>
    <h3>            by Fricciolosa Red Team </h3>
    <ul>

    """

    with open(filename, "w+") as f:
        f.write(html_banner)


def add_HTML_footer(filename):

    html_banner = """
    </ul>
    </body>
    </html>
    """

    with open(filename, "a+") as f:
        f.write(html_banner)


def add_dorks(target, filename):

    with open("dorks.txt", "r") as f:
        text = f.readlines()

    with open(filename, "a") as f:
        for elem in text:
            f.write("<li>" + encode(elem + " inurl:" + target) + "</li>\n")


def encode(search):
    base_url = "https://www.google.com/search?q="
    result = base_url + urllib.parse.quote(search)
    final = "<a href='" + result + "' target='_blank'>" + search + "</a>"
    return final


def start_dorking(target):

    directory = "output-evildork"

    filename = create_output_file(directory, target)
    add_HTML_banner(filename)
    add_dorks(target, filename)
    add_HTML_footer(filename)
    command = "xdg-open " + filename
    os.system(command)


def version():
    print("v0.1")


def main():

    banner()

    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        version()
    elif args.domain:
        start_dorking(args.domain)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
