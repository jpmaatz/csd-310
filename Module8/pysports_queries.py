import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    team_cursor = db.cursor()
    team_cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = team_cursor.fetchall()
    print()
    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()

    player_cursor = db.cursor()
    player_cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = player_cursor.fetchall()
    print()
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()

except mysql.connector.Error as err:
    print(err)

finally :
    db.close()