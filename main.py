#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="roedeer-01.rmq.cloudamqp.com",
                              virtual_host="tkfdwjro",
                              credentials=pika.credentials.PlainCredentials(
                                  "tkfdwjro", "calbiuNFyl_9kOwHQH6eBS5omW5Wb_zV")
                              ))
channel = connection.channel()

channel.queue_declare(queue='barcode_queue')
for i in range(5):
    channel.basic_publish(exchange='', routing_key='barcode_queue', body='Buna from Rasberry' + str(i))
connection.close()
