# Generated by Django 5.1 on 2024-09-18 16:33

import cloudinary.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ngay_lap', models.DateTimeField(auto_now_add=True)),
                ('tong_tien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ghi_chu', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('ho_ten', models.CharField(blank=True, max_length=255)),
                ('gioi_tinh', models.CharField(blank=True, max_length=10)),
                ('nam_sinh', models.DateField(blank=True, null=True)),
                ('thanh_vien', models.BooleanField(default=False)),
                ('dia_chi', models.TextField()),
                ('user_role', models.CharField(choices=[('ADMIN', 'Role Admin'), ('USER', 'Role User'), ('CUSTOMER', 'Role Customer')], default='USER', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='KhoHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ten_kho', models.CharField(max_length=255)),
                ('so_luong_sp', models.IntegerField()),
                ('trang_thai', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='khach_hang', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('thanh_vien', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='nhan_vien', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gio_lam', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='NhanVien_QL',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='quan_ly', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phu_cap', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nghi_phep', models.IntegerField()),
                ('chuc_vu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('hinh_anh', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('ten_sp', models.CharField(max_length=255)),
                ('loai', models.CharField(max_length=100)),
                ('don_gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kho_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.khohang')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HoaDon_SP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('so_luong', models.IntegerField()),
                ('hoa_don', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.hoadon')),
                ('san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.sanpham')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.sanpham')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TichDiemVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ngay_lap', models.DateField()),
                ('diem', models.IntegerField()),
                ('tong_tien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ghi_chu', models.TextField(blank=True)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.khachhang')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hoadon',
            name='khach_hang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.khachhang'),
        ),
        migrations.AddField(
            model_name='hoadon',
            name='nhan_vien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.nhanvien'),
        ),
        migrations.CreateModel(
            name='DanhGiaOfKhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ngay_dg', models.DateField()),
                ('noi_dung', models.TextField()),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.khachhang')),
                ('nhan_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyCuaHangSet.nhanvien')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
