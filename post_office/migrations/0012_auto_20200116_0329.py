# Generated by Django 2.2.9 on 2020-01-16 09:29

from django.db import migrations, models
import post_office.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0011_auto_20200108_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='from_email',
            field=models.CharField(default='admin@robertnclayton.net', help_text='Must have permission to send through the default server!', max_length=254, validators=[post_office.validators.validate_email_with_name], verbose_name='Email From'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='html_content',
            field=models.TextField(blank=True, default='<br /><br /><p style="text-align:center;font-size:small;">Click <a href="https://{{ unsubscribe }}">here</a> to unsubscribe from future emails.</p>', help_text='Email HTML body. Context variables available for personalisation, ex: {{ first_name }} {{ last_name }} returns Joe Smith', validators=[post_office.validators.validate_template_syntax], verbose_name='HTML Content'),
        ),
    ]