from django.db import models
from login.models import User
# Create your models here.

class staff(models.Model):
    '''
    员工表
    '''
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    statuss = (
        (1, '在职'),
        (2, '兼职'),
        (3, '试用'),
        (4, '离职'),
        (5, '返聘'),
        (6, '退休'),
    )

    photo = models.ImageField(verbose_name="照片", upload_to='img', default="img\default.jpg")
    sid = models.AutoField(verbose_name="编号", primary_key = True)
    name = models.CharField(verbose_name="姓名",max_length=128)
    sex = models.CharField(verbose_name="性别",choices=gender, default='男', max_length=8)
    nation = models.CharField(verbose_name="民族",max_length=128)
    birthday = models.DateField(verbose_name="生日")
    politics = models.CharField(verbose_name="政治面貌", max_length=128)
    education = models.CharField(verbose_name="文化程度", max_length=128)
    marriage = models.CharField(verbose_name="婚姻状况", max_length=128)
    hometown = models.CharField(verbose_name="籍贯",max_length=128)
    id_card = models.CharField(verbose_name="身份证",max_length=128)
    phone = models.CharField(verbose_name="电话号码",max_length=12)
    place = models.CharField(verbose_name="档案存放地",max_length=12)
    home_card = models.CharField(verbose_name="户口所在地",max_length=128)
    c_time = models.DateTimeField(auto_now_add=True)
    '''
    工作信息
    '''

    num = models.CharField(verbose_name="工作证号", max_length=128)
    in_time = models.DateField(verbose_name="入职日期")
    pos = models.CharField(verbose_name="工作岗位", max_length=128)
    duty = models.CharField(verbose_name="职务", max_length=128)
    pre_num = models.CharField(verbose_name="上级员工编号",max_length=128)
    status = models.IntegerField(verbose_name="员工状态", choices=statuss, default=1)
    dep = models.ForeignKey("department",
                            to_field='did',
                            verbose_name="所属部门",
                            on_delete=models.CASCADE
                        )
    account = models.OneToOneField(to=User,
                                   on_delete=models.CASCADE,
                                   default='',
                                   verbose_name="账号",
                                   to_field='id'
                                )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '职工'
        verbose_name_plural = verbose_name



class department(models.Model):
    did = models.AutoField(verbose_name="部门编号", primary_key=True)
    name = models.CharField(verbose_name="部门名称", max_length=128)
    work_id = models.CharField(verbose_name="部门职能编号", max_length=128)
    pre_dep_id = models.CharField(verbose_name="上级部门编号", max_length=128)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '部门'
        verbose_name_plural = '部门'