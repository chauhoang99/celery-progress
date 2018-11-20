import json
from django.http import HttpResponse
from celery_progress.backend import Progress
import logging


def get_progress(request, task_id):
    logger = logging.getLogger(__name__)
    progress = Progress(task_id)
    update_info = progress.get_info()
    try:
        update_info['progress']['percent'] = str(update_info['progress']['percent'])
    except TypeError:
        pass
    return HttpResponse(json.dumps(update_info), content_type='application/json')
