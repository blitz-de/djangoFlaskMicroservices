import pika, json

params = pika.URLParameters('amqps://dowzsxzj:UT7_s888elZ3FCRdD1CjiHY9S9aQPI81@cow.rmq2.cloudamqp.com/dowzsxzj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

# send events every time a product is updated, created, or deleted.
def publish(method,body):
    properties = pika.BasicProperties(method)
    # convert the object to json before you send it
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),
                        properties=properties)