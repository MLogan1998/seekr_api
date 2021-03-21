# Generated by Django 3.1.7 on 2021-03-21 19:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_seeker', models.BooleanField()),
                ('has_profile', models.BooleanField(default=False)),
                ('has_company', models.BooleanField(default=False)),
                ('has_listing', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_bio', models.TextField()),
                ('company_logo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.TextField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employerProfiles', related_query_name='EmployerProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('salary', models.CharField(max_length=250)),
                ('benefits', models.BooleanField()),
                ('requirements', models.TextField()),
                ('job_title', models.CharField(max_length=250)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.companyprofile')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.employerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('icon', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=350)),
                ('profile_img', models.TextField()),
                ('project_name', models.CharField(max_length=200)),
                ('project_detail', models.TextField(max_length=400)),
                ('project_img', models.TextField()),
                ('project_url', models.CharField(max_length=200)),
                ('github_username', models.CharField(max_length=200)),
                ('tech_ed', models.CharField(max_length=200)),
                ('languages', models.ManyToManyField(related_name='seeker_languages', related_query_name='seeker_language', to='seekrapi.Languages')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', related_query_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeker_response', models.BooleanField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.jobposting')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeker_response', models.BooleanField(null=True)),
                ('employer_response', models.BooleanField(null=True)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seekrapi.employerprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.jobposting')),
                ('seeker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seekrapi.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_response', models.BooleanField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.employerprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.jobposting')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.seekerprofile')),
            ],
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='employer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekrapi.employerprofile'),
        ),
    ]
