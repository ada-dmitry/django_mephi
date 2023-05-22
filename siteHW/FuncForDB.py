import psycopg2
import config


def sel():
    connection = psycopg2.connect(
        host=config.hostname, dbname=config.databname, user=config.username, password=config.passw)
    cursor = connection.cursor()

    try:
        query = """SELECT * FROM public.parser"""
        cursor.execute(query)
    except psycopg2.errors.UndefinedTable:
        connection.rollback()
        import tableCreator
    finally:
        array = list(cursor.fetchall())
    d = ''
    j = 0
    for i in array:
        d += f'''<li>
							<a><img width="135" height="500" src="siteHW/polls/static/polls/image/{j}.jpg"/></a>
							<div class="product-info">
								<h3>{i[1]}</h3>
								<div class="product-desc">
									<h4>{i[2]}</h4>
									<p>Mark: {i[4]}<br /></p>
									<strong class="price">{i[3]}</strong>
								</div>
							</div>
						</li>'''
        j += 1
    cursor.close()
    connection.close()
    return d
