from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=24, null=True, blank=True)
    fax = models.CharField(max_length=24, null=True, blank=True)
    email = models.CharField(max_length=60)

    support_rep = models.ForeignKey(
        "staff.Employee",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        db_column="support_rep_id",
        related_name="customers"
    )

    class Meta:
        db_table = "customer"
        managed = False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    invoice_date = models.DateTimeField()
    billing_address = models.CharField(max_length=70, null=True, blank=True)
    billing_city = models.CharField(max_length=40, null=True, blank=True)
    billing_state = models.CharField(max_length=40, null=True, blank=True)
    billing_country = models.CharField(max_length=40, null=True, blank=True)
    billing_postal_code = models.CharField(max_length=10, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
        related_name="invoices",
        db_column="customer_id"
    )

    class Meta:
        db_table = "invoice"
        managed = False
class InvoiceLine(models.Model):
    invoice_line_id = models.IntegerField(primary_key=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.DO_NOTHING,
        related_name="lines",
        db_column="invoice_id"
    )

    track = models.ForeignKey(
        "music.Track",
        on_delete=models.DO_NOTHING,
        related_name="invoice_lines",
        db_column="track_id"
    )

    class Meta:
        db_table = "invoice_line"
        managed = False