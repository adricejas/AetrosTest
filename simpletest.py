import aetros.backend
import time

job = aetros.backend.start_job('stefanopalmieri/simpletest')
x = job.get_parameter('x')
y = job.get_parameter('y')

accuracy_channel = job.create_channel('accuracy', kpi=True, main=True, yaxis={'dtick': 1})

kpi = -(x-0.5)**2-(y-0.5)** 2+3

accuracy_channel.send(1, 98.9)

job.done()

