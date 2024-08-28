# Generated by Django 5.1 on 2024-08-28 13:22

import django.db.models.deletion
import iam.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0023_requirementassessment_answer_and_more'),
        ('iam', '0005_alter_user_managers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('mission', models.TextField(blank=True)),
                ('reference_link', models.URLField(blank=True, null=True)),
                ('builtin', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(default=iam.models.Folder.get_root_folder, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_folder', to='iam.folder')),
                ('owned_folders', models.ManyToManyField(blank=True, related_name='owner', to='iam.folder', verbose_name='Owned folders')),
            ],
            options={
                'verbose_name': 'Entity',
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='EntityAssessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('eta', models.DateField(blank=True, null=True, verbose_name='ETA')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Due date')),
                ('version', models.CharField(blank=True, default='1.0', help_text='Version of the compliance assessment (eg. 1.0, 2.0, etc.)', max_length=100, null=True, verbose_name='Version')),
                ('status', models.CharField(blank=True, choices=[('planned', 'Planned'), ('in_progress', 'In progress'), ('in_review', 'In review'), ('done', 'Done'), ('deprecated', 'Deprecated')], default='planned', max_length=100, null=True, verbose_name='Status')),
                ('criticality', models.IntegerField(default=0, verbose_name='Criticality')),
                ('penetration', models.IntegerField(default=0, verbose_name='Penetration')),
                ('dependency', models.IntegerField(default=0, verbose_name='Dependency')),
                ('maturity', models.IntegerField(default=0, verbose_name='Maturity')),
                ('trust', models.IntegerField(default=0, verbose_name='Trust')),
                ('authors', models.ManyToManyField(blank=True, related_name='%(class)s_authors', to=settings.AUTH_USER_MODEL, verbose_name='Authors')),
                ('compliance_assessment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.complianceassessment')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tprm.entity')),
                ('evidence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.evidence')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project', verbose_name='Project')),
                ('reviewers', models.ManyToManyField(blank=True, related_name='%(class)s_reviewers', to=settings.AUTH_USER_MODEL, verbose_name='Reviewers')),
            ],
            options={
                'verbose_name': 'Entity assessment',
                'verbose_name_plural': 'Entity assessments',
            },
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representatives', to='tprm.entity', verbose_name='Entity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('ref_id', models.CharField(blank=True, max_length=255)),
                ('criticality', models.IntegerField(default=0, verbose_name='Criticality')),
                ('provider_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_solutions', to='tprm.entity', verbose_name='Provider entity')),
                ('recipient_entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_solutions', to='tprm.entity', verbose_name='Recipient entity')),
            ],
            options={
                'verbose_name': 'Solution',
                'verbose_name_plural': 'Solutions',
            },
        ),
    ]
