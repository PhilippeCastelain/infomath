from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Theme(models.Model):
    PREMIERE = 'P'
    TERMINALE = 'T'
    AUTRE = 'A'
    NIVEAU_CHOICES = [
        (PREMIERE, 'Première'),
        (TERMINALE,'Terminale'),
        (AUTRE, 'Autre'),
    ]
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=10, blank=True)
    niveau = models.CharField(max_length=1, choices=NIVEAU_CHOICES, default=PREMIERE)
    image = models.CharField(max_length=100, blank=True)
    descriptif = models.TextField(blank=True)
    def save(self, *args, **kwargs):
        if self.short_name == "":
            self.short_name = self.name
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('nsi:theme-detail', args=[str(self.id)])


class Cours(models.Model):
    name = models.CharField(max_length=100)
    contenu = models.CharField(max_length=100, blank=True)

    image1 = models.CharField(max_length=100, blank=True)
    text1 = models.TextField(blank=True)
    
    image2 = models.CharField(max_length=100, blank=True)
    text2 = models.TextField(blank=True)
    
    image3 = models.CharField(max_length=100, blank=True)
    text3 = models.TextField(blank=True)
    
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "cours"
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('nsi:cours-detail', args=[str(self.id)])


class Question(models.Model):
    name = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    cours = models.ForeignKey(Cours, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Td(models.Model):
    name = models.CharField(max_length=100)
    contenu = models.CharField(max_length=100, blank=True)
    cours = models.ForeignKey(Cours, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "TD"
        verbose_name_plural = "travaux dirigés"
    
    def __str__(self):
        return self.name

class Qcm(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name