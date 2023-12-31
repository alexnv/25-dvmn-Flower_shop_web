# Generated by Django 4.1 on 2023-08-16 16:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория цены')),
            ],
            options={
                'verbose_name': 'ценовая категория',
                'verbose_name_plural': 'ценовые категории',
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='FlowersBunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30, verbose_name='Название букета')),
                ('price', models.IntegerField(verbose_name='Цена букета')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка букета')),
                ('description', models.TextField(verbose_name='смысл букета')),
                ('composition', models.TextField(verbose_name='цветочный состав букета')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunchs', to='webshop.categoryprice', verbose_name='ценовая категория')),
            ],
            options={
                'verbose_name': 'букет',
                'verbose_name_plural': 'букеты',
                'db_table': 'flower',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название повода')),
            ],
            options={
                'verbose_name': 'повод',
                'verbose_name_plural': 'поводы',
                'db_table': 'reason',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, db_index=True, default='', max_length=50, verbose_name='Фамилия')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region='RU', verbose_name='номер телефона')),
                ('comment', models.TextField(blank=True, default='', verbose_name='комментарий к заказу')),
                ('order_status', models.CharField(choices=[('raw_order', 'Необработанный'), ('done', 'Выполнен')], db_index=True, default='raw_order', max_length=17, verbose_name='статус заказа')),
                ('method_payment', models.CharField(choices=[('right_now', 'Электронно'), ('delivery_pay_cash', 'Наличностью при доставке'), ('check_to_manager', 'Уточнить у менеджера')], db_index=True, default='check_to_manager', max_length=17, verbose_name='способ оплаты')),
                ('called_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='дата звонка')),
                ('delivered_at', models.DateTimeField(db_index=True, verbose_name='дата доставки')),
                ('bunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='webshop.flowersbunch', verbose_name='название букета в заказе')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='flowersbunch',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunchs', to='webshop.reason', verbose_name='повод для букета'),
        ),
    ]
