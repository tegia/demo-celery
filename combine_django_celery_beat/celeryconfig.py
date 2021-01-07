from kombu import Queue

timezone = "utc"
accept_content = ["json"]

task_serializer = "json"
result_serializer = "json"

task_time_limit = 5 * 60
task_soft_time_limit = 60

task_default_queue = "b-medium"

task_create_missing_queues = True

#app.conf.task_default_priority = 3

broker_transport_options = {"queue_order_strategy": "sorted"}

# worker_prefetch_multiplier = 1

# task_inherit_parent_priority = True

task_queues = (
    Queue("a-high"),
    Queue("b-medium"),
    Queue("c-low"),
)

task_routes = {
    f'mytasks.add': {
        'queue': 'c-low',
        'routing_key': 'c-low.priority',
    },
    f'mytasks.retry': {
        'queue': 'a-high',
        'routing_key': 'a-high.priority',
    },
    f'mytasks.find_task_fail': {
        'queue': 'a-high',
        'routing_key': 'a-high.priority',
    },
}

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'mytasks.find_task_fail',
        'schedule': 30.0
    },
}

timezone = 'UTC'

result_expires = 10
#app.conf.broker_transport_options = {
#    'priority_steps': list(range(10)),
#}