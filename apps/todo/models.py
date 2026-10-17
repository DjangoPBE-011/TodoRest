from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="Category Name")
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  
        
        
    def __str__(self):
        return self.name
    
class Task(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Task Title")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", verbose_name="Category")
    completed = models.BooleanField(default=False, verbose_name="Completed")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks", verbose_name="Assigned To")


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"  
        
        
    def __str__(self):
        return self.title