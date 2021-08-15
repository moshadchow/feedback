from django.db import models


class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title


class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title

class feature(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='feature/', blank=False)
    
    def __str__(self):
        return self.title

class service(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.title

class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=700, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=700, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)

    def __str__(self):
        return self.name

class category(models.Model):
    cat_nm = models.CharField(max_length=10)

    def __str__(self):
        return self.cat_nm


class product(models.Model):
    p_name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='category/', blank=False)
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
