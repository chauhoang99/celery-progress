import json
from django.http import HttpResponse
from celery_progress.backend import Progress


def get_progress(request, task_id):
    progress = Progress(task_id)
    update_info = progress.get_info()
    update_info['progress']['percent'] = str(update_info['progress']['percent'])
    return HttpResponse(json.dumps(update_info), content_type='application/json')
