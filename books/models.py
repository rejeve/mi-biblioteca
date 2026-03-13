from django.db import models

class Publisher (models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    city = models.CharField(max_length=60, verbose_name="Ciudad")
    state_province = models.CharField(max_length=30, verbose_name="Estado")
    country = models.CharField(max_length=50, verbose_name="Pais")
    website = models.URLField(verbose_name="Sitio web", blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=60, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Email", blank=True)
    headshot = models.ImageField(verbose_name="Foto", blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    authors = models.ManyToManyField(Author, verbose_name="Autores")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Editorial")
    publication_date = models.DateField()

    def __str__(self):
        return self.title