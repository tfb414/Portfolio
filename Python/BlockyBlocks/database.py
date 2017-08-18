def db_return_scores():
    import psycopg2
    conn = psycopg2.connect("dbname=blockyblocks user=timbrady")
    cursor = conn.cursor()

    query = """select * from scores order by score desc limit 10;"""

    db_return = cursor.execute(query)
    db_return = cursor.fetchall()
    scores = []
  
    for s in range(len(db_return)):
        scores.append([db_return[s][0], db_return[s][1]])
    return scores

db_return_scores()
        
