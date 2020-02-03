from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 191)
    last_name = models.CharField(max_length = 191)
    sirname = models.CharField(max_length = 191)
    profile_photo = models.ImageField(upload_to='Student_profile')
    adm_number = models.CharField(max_length = 191)
    accademic_year = models.CharField(max_length = 191)
    school = models.CharField(max_length = 191)
    study_method = models.CharField(max_length = 191)
    year_of_study = models.CharField(max_length = 191)
    programme = models.CharField(max_length = 191)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.sirname}: {self.adm_number}'
class Unit(models.Model):
    """Model definition for Unit."""
    unit_name = models.CharField(max_length=191)
    unit_code = models.CharField(max_length=191)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Unit."""

        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        return f'{self.unit_name}'


class StudentUnit(models.Model):
    """Model definition for StudentUnit."""

    # TODO: Define fields here
    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    student_unit = models.CharField(max_length=191)

    class Meta:
        """Meta definition for StudentUnit."""

        verbose_name = 'StudentUnit'
        verbose_name_plural = 'StudentUnits'

    def __str__(self):
        """Unicode representation of StudentUnit."""
        return f'{self.profile}: {self.unit}'
class Fee(models.Model):
    """Model definition for Fee."""

    # TODO: Define fields here
    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default = False,null=True)

    class Meta:
        """Meta definition for Fee."""

        verbose_name = 'Fee'
        verbose_name_plural = 'Fees'

    def __str__(self):
        """Unicode representation of Fee."""
        return f'{self.profile}'

class Log(models.Model):
    """Model definition for Log."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    timstamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Log."""

        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        """Unicode representation of Log."""
        return f'{self.user}: Logs For {self.profile}'
class Report(models.Model):
    """Model definition for Report."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.TextField()
    message = models.TextField()

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        """Unicode representation of Report."""
        return f'{self.user} {self.student} {self.message}'
