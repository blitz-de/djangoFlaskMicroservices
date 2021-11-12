import pika

params = pika.URLParameters('amqps://dowzsxzj:UT7_s888elZ3FCRdD1CjiHY9S9aQPI81@cow.rmq2.cloudamqp.com/dowzsxzj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Receieved in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()