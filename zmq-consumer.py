import time
import zmq
import random

def consumer():
	consumer_id = random.randrange(1,100005)
	print "I'm consumer #%s" % (consumer_id)
	context = zmq.Context()
	#look for work you lazy bum!
	consumer_receiver = context.socket(zmq.PULL)
	#each consumer looks for work from the main producer in this example
	consumer_receiver.connect("tcp://127.0.0.1:5557")

	#did the work, send it off!
	consumer_sender = context.socket(zmq.PUSH)
	consumer_sender.connect("tcp://127.0.0.1:5558")


	while True:
		#loop and loook for work if you do it send it off
		
		#receiver found some work
		work = consumer_receiver.recv_json()
		print 'received work : ', work
		#make the work our own
		data = work['num']

		#result is a faux respresentation of owrk where we just add
		#consumer's id to the data. 
		result = {'consumer' : consumer_id, 'num' :data}
		if data%2 == 0:
			print 'sending work to result collector : ', result
			consumer_sender.send_json(result)

consumer()