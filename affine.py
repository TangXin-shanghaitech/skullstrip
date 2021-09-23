import ants
import os

path6 = '/public/home/tangx/test/new6'
oldpath12 = '/public/home/tangx/test/old12'
newpath12 = '/public/home/tangx/test/new12'


# 将a12 alabel 配准到a6上 并且存储
def af(a6, a12, alabel, r12, rlabel):
    fix_img = ants.image_read(a6)
    move_img = ants.image_read(a12)
    label_img = ants.image_read(alabel)

    out = ants.registration(fix_img, move_img, type_of_transform='Affine')

    affine_img = out['warpedmovout']
    ants.image_write(affine_img, r12)

    affinelabel_img = ants.apply_transforms(fix_img, label_img, transformlist=out['fwdtransforms'], interpolator='nearestNeighbor')

    ants.image_write(affinelabel_img, rlabel)


# 获取 6, 12 所有子文件夹dirs6, dirs12用于遍历
dirs6 = os.listdir(path6)
dirs12 = os.listdir(oldpath12)
# 遍历6 子文件夹i 并且找到对应12 子文件夹
for i in dirs6:
    for j in dirs12:
        if j.split('_')[2] == i.split('_')[2]:
            # 获取a6路径  affine 6
            a6 = os.path.join(path6, i, 'intensity.nii.gz')
            # 获取a12路径
            a12 = os.path.join(oldpath12, j, 'intensity.nii.gz')
            # 获取a12 label路径 alabel
            alabel = os.path.join(oldpath12, j, 'segment.nii.gz')
            # 首先创建文件夹
            os.makedirs(os.path.join(newpath12, j))
            # 获取r12存储路径 register 12
            r12 = os.path.join(newpath12, j, 'intensity.nii.gz')
            # 获取rlabel 路径
            rlabel = os.path.join(newpath12, j, 'segment.nii.gz')
            # 调用 affine函数 af
            af(a6, a12, alabel, r12, rlabel)




