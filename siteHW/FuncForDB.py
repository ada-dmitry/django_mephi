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
        d += f'''<div class="col-md-6 col-lg-4">
                <div class="card text-center card-product">
                  <div class="card-product__img">
                    <img class="card-img" src="/static/image/{j}.jpg" width="300" height="600" alt="">
                    <ul class="card-product__imgOverlay">
                      <li><button><i class="ti-search"></i></button></li>
                      <li><button><i class="ti-shopping-cart"></i></button></li>
                      <li><button><i class="ti-heart"></i></button></li>
                    </ul>
                  </div>
                  <div class="card-body">
                    <p>Mark: {i[4]}</p>
                    <h4 class="card-product__title"><a href="#">{i[1]}</a></h4>
                    <p class="card-product__price">{i[2]}</p>
                  </div>
                </div>
              </div>'''
        j += 1
    cursor.close()
    connection.close()
    return d
