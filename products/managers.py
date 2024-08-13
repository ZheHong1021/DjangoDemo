from common.managers import SoftDeleteManager, AlreadySoftDeleteManager

# 只會顯示尚未被軟刪除的數據
class ProductManager(SoftDeleteManager):
    pass

# 只會顯示已經被軟刪除的數據
class DeletedProductManager(AlreadySoftDeleteManager):
    pass