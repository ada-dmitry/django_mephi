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
    for i in range(20):
        d += f'''<li>
							<a><img width="270" height="1000" src="/siteHW/polls/static/polls/image/{i}.jpg"></a>
							<div class="product-info">
								<h3>{array[i][1]}</h3>
								<div class="product-desc">
									<h4>{array[i][2]}</h4>
									<p>Mark: {array[i][4]}<br /></p>
									<strong class="price">{array[i][3]}</strong>
								</div>
							</div>
						</li>'''
    cursor.close()
    connection.close()
    return d
