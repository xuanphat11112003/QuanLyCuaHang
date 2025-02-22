# myapp/models.py
from cloudinary.models import CloudinaryField
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

# Mô hình người dùng tùy chỉnh
class User(AbstractUser):
    class UserRole(models.TextChoices):
        ROLE_ADMIN = 'ADMIN', 'Role Admin'
        ROLE_USER = 'USER', 'Role User'
        ROLE_CUSTOMER = 'CUSTOMER', 'Role Customer'

    ho_ten = models.CharField(max_length=255, blank=True)
    gioi_tinh = models.CharField(max_length=10, blank=True)
    nam_sinh = models.DateField(null=True, blank=True)
    thanh_vien = models.BooleanField(default=False)
    dia_chi = models.TextField()
    user_role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.ROLE_USER
    )

    def __str__(self):
        return self.username

# Mô hình khách hàng
class KhachHang(models.Model):
    user = models.OneToOneField(User,related_name="khach_hang", on_delete=models.CASCADE,primary_key=True)
    thanh_vien = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# Mô hình nhân viên
class NhanVien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="nhan_vien",primary_key=True)
    gio_lam = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.user.username

# Mô hình nhân viên QL
class NhanVien_QL(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="quan_ly",primary_key=True)
    phu_cap = models.DecimalField(max_digits=10, decimal_places=2)
    nghi_phep = models.IntegerField()
    chuc_vu = models.CharField(max_length=100)

    def __str__(self):
        return f"Nhân viên QL: {self.nhan_vien.user.username}"

# Mô hình phiếu chi đổi thành Tích Điểm Voucher
class TichDiemVoucher(BaseModel):

    ngay_lap = models.DateField()
    diem = models.IntegerField()
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2)
    ghi_chu = models.TextField(blank=True)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)


    def __str__(self):
        return f"Voucher {self.ma_voucher} - {self.ngay_lap}"

# Mô hình hóa đơn
class HoaDon(BaseModel):
    TRANG_THAI_CHOICES = [
        ('prep', 'Đang chuẩn bị'),
        ('deliv', 'Đang giao hàng'),
        ('del', 'Giao thành công'),
    ]

    PHUONG_THUC_THANH_TOAN_CHOICES = [
        ('transfer', 'Chuyển khoản'),
        ('cash', 'Tiền mặt'),
    ]

    ngay_lap = models.DateTimeField(auto_now_add=True)
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2)
    ghi_chu = models.TextField(blank=True)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    nhan_vien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    trang_thai = models.CharField(max_length=10, choices=TRANG_THAI_CHOICES, default='prep')
    phuong_thuc_thanh_toan = models.CharField(max_length=10, choices=PHUONG_THUC_THANH_TOAN_CHOICES, default='cash')

    def __str__(self):
        return f"Hóa đơn {self.id} - {self.ngay_lap}"

# Mô hình sản phẩm
class SanPham(BaseModel):

    hinh_anh = CloudinaryField('image', blank=True, null=True)
    ten_sp = models.CharField(max_length=255)
    loai = models.CharField(max_length=100)
    don_gia = models.DecimalField(max_digits=10, decimal_places=2)
    kho_hang = models.ForeignKey('KhoHang', on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_sp

# Mô hình kho hàng
class KhoHang(BaseModel):

    ten_kho = models.CharField(max_length=255)
    so_luong_sp = models.IntegerField()
    trang_thai = models.CharField(max_length=50)

    def __str__(self):
        return self.ten_kho




# Mô hình đánh giá của khách hàng
class DanhGiaOfKhachHang(BaseModel):
    nhan_vien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ngay_dg = models.DateField()
    noi_dung = models.TextField()

    def __str__(self):
        return f"Đánh giá của {self.khach_hang.user.username} vào ngày {self.ngay_dg}"

# Mô hình chi tiết hóa đơn sản phẩm
class HoaDon_SP(BaseModel):
    hoa_don = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()

    def __str__(self):
        return f"Hóa đơn {self.hoa_don.ma_hd} - Sản phẩm {self.san_pham.ten_sp}"

class Comment(BaseModel):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(SanPham, on_delete=models.CASCADE)


class PaymentForm(forms.Form):

    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)

from django.db import models

# Mô hình địa chỉ giao hàng
class DiaChiGiaoHang(BaseModel):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='dia_chi_giao_hang')
    ho_ten = models.CharField(max_length=255)
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.TextField()
    mac_dinh = models.BooleanField(default=False)  # Địa chỉ mặc định

    def save(self, *args, **kwargs):
        # Nếu địa chỉ này được chọn làm mặc định, phải bỏ mặc định các địa chỉ khác
        if self.mac_dinh:
            DiaChiGiaoHang.objects.filter(khach_hang=self.khach_hang, mac_dinh=True).update(mac_dinh=False)
        super(DiaChiGiaoHang, self).save(*args, **kwargs)

    def __str__(self):
        return f"Địa chỉ giao hàng của {self.khach_hang.user.username}"
