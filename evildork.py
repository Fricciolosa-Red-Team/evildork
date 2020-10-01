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
#   @Repository:  https://github.com/edoardottt/evildork
#
#   @Author:      edoardottt, https://www.edoardoottavianelli.it


# ======= INTRO ========

banner = """             _ _     _            _
   _____   _(_) | __| | ___  _ __| | __
  / _ \ \ / / | |/ _` |/ _ \| '__| |/ /
 |  __/\ V /| | | (_| | (_) | |  |   <
  \___| \_/ |_|_|\__,_|\___/|_|  |_|\_\\
"""

print(banner)

# ======= IMPORT =========

import argparse

# ======= GLOBAL VARS ========

sleep_time = 10
banned = False


# - Login pages -

wp1 = "inurl:wp-admin"
wp2 = "inurl:wp-login"
portal = "inurl:portal"
userportal = "inurl:userportal"
remote = "inurl:remote"
dashboard = "inurl:dashboard"
admin = "inurl:admin"
adminlogin = "inurl:adminlogin"
login = "inurl:login"
loginpanel = "inurl:loginpanel"
memberlogin = "inurl:memberlogin"
cplogin = "inurl:cplogin"
weblogin = "inurl:weblogin"
quicklogin = "inurl:quicklogin"
auth = "inurl:auth"
exc = "inurl:exchange"
fp = "inurl:ForgotPassword"
test = "inurl:test"

loginpages = [
    wp1,
    wp2,
    portal,
    userportal,
    remote,
    dashboard,
    admin,
    adminlogin,
    login,
    loginpanel,
    memberlogin,
    cplogin,
    weblogin,
    quicklogin,
    auth,
    exc,
    fp,
    test,
]

# - Filetypes -

xls = "filetype:xls"  # Filetype XLS (MsExcel 97-2003)
xlsx = "filetype:xlsx"  # Filetype XLSX (MsExcel 2007+)
doc = "filetype:doc"  # Filetype DOC (MsWord 97-2003)
docx = "filetype:docx"  # Filetype DOCX (MsWord 2007+)
ppt = "filetype:ppt"  # Filetype PPT (MsPowerPoint 97-2003)
pptx = "filetype:pptx"  # Filetype PPTX (MsPowerPoint 2007+)
mdb = "filetype:mdb"  # Filetype MDB (Ms Access)
pdf = "filetype:pdf"  # Filetype PDF
sql = "filetype:sql"  # Filetype SQL
rtf = "filetype:rtf"  # Filetype RTF
csv = "filetype:csv"  # Filetype CSV
xml = "filetype:xml"  # Filetype XML
key = "filetype:key"  # Filetype KEY
cert = "filetype:cert"  # Filetype CERT
pem = "filetype:pem"  # Filetype PEM
conf = "filetype:conf"  # Filetype CONF
dat = "filetype:dat"  # Filetype DAT
txt = "filetype:txt"  # Filetype TXT
ini = "filetype:ini"  # Filetype INI
log = "filetype:log"  # Filetype LOG
env = "fietype:env"  # Filetype ENV
idrsa = "index%20of:id_rsa%20id_rsa.pub"  # File ID_RSA


filetypes = [
    xls,
    xlsx,
    doc,
    docx,
    ppt,
    pptx,
    mdb,
    pdf,
    sql,
    rtf,
    csv,
    xml,
    key,
    cert,
    pem,
    conf,
    dat,
    txt,
    ini,
    log,
    env,
    idrsa,
]

# - Directory traversal -
parent = "intitle:%22index%20of%22%20%22parent%20directory%22"  # Common traversal
dcim = "intitle:%22index%20of%22%20%22DCIM%22"  # Photo
ftp = "intitle:%22index%20of%22%20%22ftp%22"  # FTP
backup = "intitle:%22index%20of%22%20%22backup%22"  # BackUp
mail = "intitle:%22index%20of%22%20%22mail%22"  # Mail
password = "intitle:%22index%20of%22%20%22password%22"  # Password
pub = "intitle:%22index%20of%22%20%22pub%22"  # Pub

dirtraversals = [parent, dcim, ftp, backup, mail, password, pub]

# - Webcam -

webcamxp5 = 'intitle:"webcamxp 5"'

webcams = [webcamxp5]


# ======= ARGUMENT ========


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="the domain you want to scrape")
    parser.add_argument("-k", help="the keyword you want to insert in the search")
    args = parser.parse_args()
    return args


# ======== FUNCTIONS =======
