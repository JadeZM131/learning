from torch.utils.tensorboard import SummaryWriter

# 训练日志记录

writer = SummaryWriter()  # 给日志写入的文件目录，可以不写，有默认路径

writer.add_scalar()
writer.add_image()

writer.close()