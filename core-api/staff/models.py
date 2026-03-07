from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    title = models.CharField(max_length=30, null=True, blank=True)

    reports_to = models.ForeignKey(
        "self",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        db_column="reports_to",
        related_name="subordinates",
    )

    birth_date = models.DateTimeField(null=True, blank=True)
    hire_date = models.DateTimeField(null=True, blank=True)

    address = models.CharField(max_length=70, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    phone = models.CharField(max_length=24, null=True, blank=True)
    fax = models.CharField(max_length=24, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = "employee"
        managed = False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"