import os
import json
from GeoIpCore import app
from flask import current_app
from threading import Thread
from GeoIpCore.extensions import db
from GeoIpApi.model import IPV4,IPV6, CountryInfo


#
# b = current_app._get_current_object()

def doo(app, db, fp):
    with app.app_context():
        for each in json.load(fp):
            ip = IPV6()
            ip.StartRange = each["start-range"]
            ip.EndRange = each["end-range"]
            ip.CityName = each["city-name"]
            ip.CountryName = each["country-name"]
            ip.CountryCode = each["country-code"]
            ip.Lat = each["lat"]
            ip.Long = each["long"]
            ip.StateName = each["timezone"]
            ip.TimeZone = each["timezone"]
            ip.ZipCode = each["zip-code"]
            ip.PublicKey = each["public-key"]
            try:
                db.session.add(ip)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            print("Added")
def dooo(app, db, fp):
    with app.app_context():
        for each in json.load(fp):
            ip = CountryInfo()
            CountryInfo.CountryCode =
            CountryInfo.PublicKey =
            CountryInfo.CommonName =
            CountryInfo.OfficialName =
            try:
                db.session.add(ip)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            print("Added")

path = "./GeoIpUpdater/IPV6-database"

# with app.app_context():
#     countries = os.listdir(path)
#     for each in countries:
#         totalpath = path + "/" + each
#         print(totalpath)
#         for file in os.listdir(totalpath):
#             file = totalpath + "/" + file
#             with open(file) as f:
#                 Thread(target=doo, args=(current_app._get_current_object(), db, f)).start()

path = "./GeoIpUpdater/Countries-database"
with app.app_context():
    countries = os.listdir(path)
    for each in countries:
        totalpath = path + "/" + each
        print(totalpath)
        for file in os.listdir(totalpath):
            file = totalpath + "/" + file
            with open(file) as f:
                Thread(target=dooo, args=(current_app._get_current_object(), db, f)).start()

if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True,
    )
