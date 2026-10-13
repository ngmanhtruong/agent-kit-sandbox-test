---
feature: shop
status: approved
---
# PRD: giỏ hàng

## 1. Product brief
- **Vấn đề:** cần thao tác giỏ hàng cơ bản.

## 3. Yêu cầu chức năng
- **REQ-01** (must) — Thêm sản phẩm vào giỏ. *Kiểm chứng:* add_item cộng dồn số lượng; qty <= 0 báo ValueError.
- **REQ-02** (must) — Bớt sản phẩm khỏi giỏ. *Kiểm chứng:* remove_item trừ số lượng, về 0 thì xoá sku.
