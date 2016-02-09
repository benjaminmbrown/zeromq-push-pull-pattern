# zeromq-push-pull-pattern
Push/Pull pattern in zeromq &amp; python

<br/>
This consists of one producer, many consumers, and a resultscollector. Each of these can be scaled. Producers create work and use zmq.PUSH to send work to any available consumer. Consumers pick up the work (it is distributed evenly from producer), process the work, and PUSH the results of their work to results collector.<br/>

