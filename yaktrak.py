import pyak as pk
import MySQLdb as mdb
import ConfigParser

# use configparser to get database info
cp = ConfigParser.ConfigParser()
cp.read("./database.cfg")
host = cp.get("database", "host")
user = cp.get("database", "user")
password = cp.get("database", "password")
db = cp.get("database", "db")

# database connection is set as global and used in most functions
con = mdb.connect(host, user, password, db)
cursor = con.cursor()

def get_yaks_for_location(location_name):
    yakker = get_yakker_for_location(location_name)
    yaklist = yakker.get_yaks()
    return yaklist

def get_yakker_for_location(location_name):
    sql = "SELECT latitude, longitude FROM locations WHERE name = %s"
    cursor.execute(sql, (location_name))
    latitude, longitude = cursor.fetchone()
    # if we've already created an account for this location, we'll just use that
    yakker_id = get_yakker_id_for_location(location_name)
    if yakker_id:
        yakker = pk.Yakker(yakker_id, pk.Location(latitude, longitude))
    # otherwise we can pass in None and pk.Yakker will create one for us...
    else:
        yakker = pk.Yakker(None, pk.Location(latitude, longitude))
        # and we'll cache it for later
        persist_yakker_id(yakker.id, location_name)

    return yakker

def get_yakker_id_for_location(location_name):
    sql = """SELECT yakker_id FROM yakker_ids yi JOIN locations l
            ON yi.location_id = location.id  WHERE name = %s"""
    cursor.execute(sql, (location_name))
    yakker_id = cursor.fetchone()
    return yakker_id[0] # because yakker_id is a 1-tuple, index in & return first result

def get_location_id_from_name(location_name):
    sql = "SELECT id FROM locations WHERE name = %s"
    cursor.execute(sql, (location_name))
    return cursor.fetchone()[0]

def persist_comment(comment, yak_id):
    # first check it doesn't already exist
    sql = "SELECT id FROM comments WHERE message_id = %s"
    cursor.execute(sql, (comment.message_id))
    comment_exists = cursor.fetchone()[0]
    if not comment_exists:
        # and if it doesn't we can store it
        sql = """INSERT INTO comments(message, message_id, time, yak_id)
                VALUES(%s, %s, %s, %s, %s,)"""
        cursor.execute(sql, (comment.message, comment.message_id, comment.time, yak_id))
        conn.commit()

def persist_yak(yak, location_name):
    sql = "SELECT id FROM yaks WHERE message_id = %s"
    cursor.execute(sql, (yak.mesage_id))
    yak_exists = cursor.fetchone()

    if not yak_exists:
        location_id = get_location_id_from_name(location_name)
        sql = """INSERT INTO yaks(message, message_id, time, score, location_id)
        VALUES(%s, %s, %s, %s, %s"""
        cursor.execute(sql, (yak.message, yak.message_id, yak.time, yak.likes, location_id))
    else:
        # we've already stored this before, but we can update its number of likes
        # with the most recent number
        sql = "UPDATE yaks SET score = %s WHERE message_id = %s"
        cursor.execute(sql, (yak.likes, yak.message_id))
        con.commit()
    # return the primary key id of the yak...
    sql = "SELECT id FROM yaks WHERE message_id = %s"
    cursor.execute(sql, (yak.message_id))
    return cursor.fetchone()[0]

def persist_yakker_id(yakker_id, location_name):
    location_id = get_location_id_from_name(location_name)
    sql = "INSERT INTO yakker_ids(yakker_id, location_id) VALUES(%s, %s)"
    cursor.execute(sql, (yakker_id, location_id))
    con.commit()

def main(location_name):
    yaks = get_yaks_for_location(location_name)
    for yak in yaks:
        yak_id = persist_yak(yak, location_name)
        comments = yak.get_comments()
        for comment in comments:
            persist_comment(comment, yak_id)

if __name__ == "__main__":
    main()
