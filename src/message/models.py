""" Module gérant les class concernant les données des messages
    NOTE : Instance de Message et Fiche n'ont pas de field id. Genant ???
"""
from django.db import models
from django.utils import timezone


class TypeDemande(models.Model):
    """ Paramètres du champ du type de demande """
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Service(models.Model):
    """ Paramètres du champ du libellé d'un service """
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return str(self.libelle)


class Ordinateur(models.Model):
    """ Paramètres du champ concerant le matériel """
    reference = models.CharField(max_length=100)

    def __str__(self):
        return str(self.reference)


class Telephone(models.Model):
    """ Paramètres du champ téléphone...Désolé les gens mais fallait un docstring pour pylint -_-"""
    reference = models.CharField(max_length=100)

    def __str__(self):
        return str(self.reference)


class Acces(models.Model):
    """ Paramètres du champ concernant l'accès des références dans un service"""
    reference = models.CharField(max_length=100)

    def __str__(self):
        return str(self.reference)


class Employee(models.Model):
    """ Paramètres des champs concernant les employés"""
    reference = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50, default=None)
    service = models.ForeignKey(Service,on_delete=models.PROTECT, blank=True, null=True)
    password = models.CharField(max_length=100)
    dateStart = models.DateTimeField(default=timezone.now)
    workplace = models.CharField(max_length=50, default=None)
    job = models.CharField(max_length=50, default=None)
    refAcces = models.CharField(max_length=50, null=True, blank=True)
    refOrdi = models.CharField(max_length=50, null=True, blank=True)
    refPhone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.firstName


class Message(models.Model):
    """ Paramètres des champs des messages retournés"""
    typeDemande = models.ForeignKey(TypeDemande, on_delete=models.PROTECT)
    ordinateur  = models.CharField(max_length=100, blank=True, null=True)
    telephone  = models.CharField(max_length=100, blank=True, null=True)
    acces  = models.CharField(max_length=100, blank=True, null=True)
    description  = models.TextField(blank=True, null=True)
    employe = models.ForeignKey(Employee,on_delete=models.PROTECT)
    sendBy = models.CharField(max_length=10)
    receiver = models.ForeignKey(Service,on_delete=models.PROTECT)
    dateReceiver = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)
    file  = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __int__(self):
        return str(self.id)


class Fiche(models.Model):
    """ Paramètres des champs de la Fiche à afficher pour un employé"""
    typeDemande = models.ForeignKey(TypeDemande, on_delete=models.PROTECT)
    ordinateur = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    acces = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employe = models.ForeignKey(Employee, on_delete=models.PROTECT)
    sendBy = models.CharField(max_length=10)
    receiver = models.ForeignKey(Service, on_delete=models.PROTECT)
    dateReceiver = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)
    file = models.CharField(max_length=100, blank=True, null=True)

    def __int__(self):
        return str(self.id)
