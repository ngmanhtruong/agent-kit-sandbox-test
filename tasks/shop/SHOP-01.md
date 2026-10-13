---
id: SHOP-01
type: task
epic: SHOP
status: draft
depends_on: []
requirements: [REQ-01]
priority: 1
holdout: true
design: design/shop
---

# Mục tiêu
Thêm hàm add_item vào giỏ hàng.

# Interface (hợp đồng)
`add_item(cart: dict, sku: str, qty: int) -> int` trong `src/shop/cart.py`:
cộng `qty` vào số lượng hiện có của `sku` (chưa có thì coi là 0), trả về số lượng mới.
`qty <= 0` → raise `ValueError`.

# Acceptance (thang điểm — đo được, có/không)
- [ ] `bash eval/checks.sh` pass
- [ ] add_item(new_cart(), "A", 2) trả về 2; gọi tiếp add_item(cart, "A", 3) trả về 5
- [ ] add_item(cart, "A", 0) raise ValueError
- [ ] Có unittest cho các dòng trên trong tests/

# Ngoài phạm vi
Không thêm hàm nào khác.
