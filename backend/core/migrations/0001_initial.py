# Generated by Django 4.2.7 on 2023-11-08 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, null=True, unique=True, verbose_name='Email Address')),
                ('email_is_verified', models.BooleanField(default=False, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/profile-pictures/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('info', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Service Categories',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measurment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('process', 'process'), ('done', 'done'), ('rejected', 'rejected')], max_length=16, null=True)),
                ('time_ordered', models.DateTimeField(blank=True, null=True)),
                ('service_name', models.CharField(blank=True, max_length=64, null=True)),
                ('client_name', models.CharField(blank=True, max_length=64, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.PositiveSmallIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('measurment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricings', to='core.measurment')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('info', models.TextField(null=True)),
                ('price', models.FloatField(null=True)),
                ('since_date', models.DateField(null=True)),
                ('category', models.ManyToManyField(related_name='services', to='core.category')),
                ('pricing', models.ManyToManyField(related_name='services', to='core.pricing')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('contributors', models.ManyToManyField(related_name='contributions', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='VisitPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='images/visits')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('district', models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='core.district')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='images/services')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.service')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='villages',
            field=models.ManyToManyField(related_name='services', to='core.village'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('country', models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='core.service'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=32, null=True)),
                ('longitude', models.CharField(max_length=32, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='core.region'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, null=True)),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, null=True)),
                ('reason', models.TextField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='village',
            field=models.ManyToManyField(blank=True, related_name='users', to='core.village'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email'),
        ),
    ]
