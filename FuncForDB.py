import psycopg2
import config


def sel(cursor, tabl):
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
    for i in array:
        d += f'''<div class="col-md-6 col-lg-4">
                <div class="card text-center card-product">
                  <div class="card-product__img">
                    <img class="card-img" src="static/image/{i}.jpg" alt="">
                    <ul class="card-product__imgOverlay">
                      <li><button><i class="ti-search"></i></button></li>
                      <li><button><i class="ti-shopping-cart"></i></button></li>
                      <li><button><i class="ti-heart"></i></button></li>
                    </ul>
                  </div>
                  <div class="card-body">
                    <p>Accessories</p>
                    <h4 class="card-product__title"><a href="#">Quartz Belt Watch</a></h4>
                    <p class="card-product__price">$150.00</p>
                  </div>
                </div>
              </div>'''
    return array


def upd(conn, cursor, tabl):
    import parser
    for i in range(15):
        up_query = f"""UPDATE {tabl} SET page_name = '{parser.name[i].text}', price = '{parser.price[i].text}', priceDis = '{parser.priceDis[i].text}', mark = '{parser.mark[i].text}' WHERE id = {i+1}"""
        cursor.execute(up_query)
        conn.commit()
