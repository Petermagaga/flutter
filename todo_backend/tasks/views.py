from  rest_framework import viewsets
from .models import Task 
from .serializers import TaskSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task  # Ensure your model is imported

@csrf_exempt  # Only for development; remove in production!
def update_task(request, task_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            print("✅ Received Data:", data)  # Debugging log
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        try:
            task = Task.objects.get(id=task_id)
            task.completed = data.get("completed", task.completed)
            task.save()
            return JsonResponse({"message": "Task updated successfully"})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)
