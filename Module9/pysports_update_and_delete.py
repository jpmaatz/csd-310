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

    player_select_statement = """
    SELECT P.player_id, P.first_name, P.last_name, T.team_name 
    FROM player AS P
    INNER JOIN team AS T ON P.team_id = T.team_id
    """

    player_insert_statement = """
    INSERT INTO player (first_name, last_name, team_id)
    VALUES('Smeagol', 'Shire Folk', 1);
    """

    player_update_statement = """
    UPDATE player
    SET team_id = 2,
        first_name = 'Gollum',
        last_name = 'Ring Stealer'
    WHERE first_name = 'Smeagol';
    """

    player_delete_statement = """
    DELETE FROM player
    WHERE first_name = 'Gollum';
    """

    player_cursor = db.cursor()
    player_cursor.execute(player_insert_statement);
    db.commit()

    player_cursor = db.cursor()
    player_cursor.execute(player_select_statement)

    players = player_cursor.fetchall()
    print()
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()


    player_cursor = db.cursor()
    player_cursor.execute(player_update_statement);
    db.commit()

    player_cursor = db.cursor()
    player_cursor.execute(player_select_statement)

    players = player_cursor.fetchall()
    print()
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()


    player_cursor = db.cursor()
    player_cursor.execute(player_delete_statement);
    db.commit()

    player_cursor = db.cursor()
    player_cursor.execute(player_select_statement)

    players = player_cursor.fetchall()
    print()
    print("-- DISPLAYING PLAYERS AFTER DELETE --")
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