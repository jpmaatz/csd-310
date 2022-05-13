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

    player_cursor = db.cursor()
    player_cursor.execute("""
    SELECT P.player_id, P.first_name, P.last_name, T.team_name 
    FROM player AS P
    INNER JOIN team AS T ON P.team_id = T.team_id
    """)

    players = player_cursor.fetchall()
    print()
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()

except mysql.connector.Error as err:
    print(err)

finally :
    db.close()