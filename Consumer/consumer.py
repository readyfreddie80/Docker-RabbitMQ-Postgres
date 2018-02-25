#!/usr/bin/env python
import pika
import psycopg2
import time

is_connected = False

while not is_connected:
    try:
        pika_conn = pika.BlockingConnection(
		pika.URLParameters("amqp://guest:guest@queue:5672") 
	)
        pstgrs_conn = psycopg2.connect("dbname=my_db user=ninja host=database")
        is_connected = True
    except:
        time.sleep(1)
        is_connected = False

channel = pika_conn.channel()
channel.queue_declare(queue='hello')

sql = """INSERT INTO strings VALUES(%s)"""

def callback(ch, method, properties, body):
    recieved = (body.decode())
    cur = pstgrs_conn.cursor()
    cur.execute(sql, (recieved,))
    pstgrs_conn.commit()
    cur.close()


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
channel.start_consuming()

pstgrs_conn.close()
pika_conn.close()


