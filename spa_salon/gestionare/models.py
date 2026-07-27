from django.db import models

class Pacient(models.Model):
    CodPacient = models.AutoField(primary_key=True)
    NumePacient = models.CharField(max_length=100)
    PrenumePacient = models.CharField(max_length=100)
    Adresa = models.CharField(max_length=255)
    Telefon = models.CharField(max_length=15)
    DataNasterii = models.DateField()

    def __str__(self):
        return f'{self.NumePacient} {self.PrenumePacient}'

class Tratament(models.Model):
    CodTratament = models.AutoField(primary_key=True)
    CodPacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    Diagnoza = models.CharField(max_length=255)
    DataCazarii = models.DateField()
    Durata = models.IntegerField()

    def __str__(self):
        return f'{self.Diagnoza} - {self.CodPacient}'
