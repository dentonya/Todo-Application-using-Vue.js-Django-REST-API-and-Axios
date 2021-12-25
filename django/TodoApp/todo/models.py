from django.db import models


# Create your models here.
class WorkTodo(models.Model):  # Our database model is called WorkTodo
    WORKTODO = 'worktodo'
    WORKDONE = 'workdone'

    STATUS_CHOICES = (  # We create a tuple of status choices
        (WORKTODO, 'Work To do'),
        (WORKDONE, 'Work Done')
    )

    work_description = models.CharField(max_length=255)  # The worktodo description is limited to 255 characters
    work_status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default=WORKTODO)  # The work status, default status = WORKTODO
