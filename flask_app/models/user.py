import re, requests
from flask_app.config.mysqlconnection import connectToMySQL
from api.python_skynet import siaskynet
from flask import flash, session
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

client = siaskynet.SkynetClient()

class User:
  db = 'demo'  

  def __init__(self,data):
    # self.first_name = data['first_name']
    # self.last_name = data['last_name']
    self.patient_number = data['patnum']
    self.first_name = data['fname']
    self.last_name = data['lname']

  @classmethod
  def get_all(cls):
    patients = []

    # sql query selecting all patients in the database
    query = """
    SELECT * FROM patient;
    """

    # the result of the query on the database. This is a tuple.
    all_users = connectToMySQL(cls.db).query_db(query)

    # we need to break up the tuple into an array and append each instance of the tuple inside the array
    for user in all_users:
      patients.append(cls(user))

    return patients
    # return all_users

  @classmethod
  def get_one_by_id(cls):

    data = { 'patnum' : 7 }

    query = """
    SELECT * FROM patient 
    WHERE patnum = %(patnum)s;
    """

    results = connectToMySQL(cls.db).query_db(query,data)
    
    # print(f"THIS IS THE UNREFINED QUERY RESULTS: {results}")
    # print(f"THIS IS THE REFINED QUERY RESULTS: {results[0]}")

    # this is a test for the skylink upload file method
    skylink = client.upload_file("api/python_skynet/siaskynet/testing.txt")
    print("Upload successful, skylink: " + skylink)

    if len(results) < 1:
      return False

    #  take results and put it into a the upload method for skylink.
    # skylink = client.upload(results[0])
    # print("Upload successful, skylink: " + skylink)

    return results