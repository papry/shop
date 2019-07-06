# Generated by Django 2.2.3 on 2019-07-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(default='', max_length=250)),
                ('description', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(default='', max_length=250)),
                ('Email', models.CharField(default='', max_length=250)),
                ('Password', models.CharField(default='', max_length=250)),
                ('Phone_no', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Supplier_name', models.CharField(default='', max_length=250)),
                ('Address', models.CharField(default='', max_length=250)),
                ('Phone_no', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(default='', max_length=250)),
                ('Stock', models.IntegerField(default=20000)),
                ('Price', models.IntegerField(default=2000)),
                ('Category_id', models.ForeignKey(on_delete='CASCADE', to='design.category')),
                ('Supplier_id', models.ForeignKey(on_delete='CASCADE', to='design.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_type', models.CharField(default='', max_length=250)),
                ('Payment_date', models.CharField(default='', max_length=250)),
                ('Quantity', models.CharField(default='', max_length=250)),
                ('Amount', models.CharField(default='', max_length=250)),
                ('Customer_id', models.ForeignKey(on_delete='CASCADE', to='design.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Product_id',
            field=models.ForeignKey(on_delete='CASCADE', to='design.Product'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(default='', max_length=250)),
                ('Password', models.CharField(default='', max_length=250)),
                ('Product_id', models.ForeignKey(on_delete='CASCADE', to='design.Product')),
            ],
        ),
    ]