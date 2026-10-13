---
id: SHOP-02
type: task
epic: SHOP
status: draft
depends_on: []
requirements: [REQ-02]
priority: 2
holdout: false
design: design/shop
---

# Mục tiêu
Thêm hàm remove_item vào giỏ hàng.

# Interface (hợp đồng)
`remove_item(cart: dict, sku: str, qty: int) -> int` trong `src/shop/cart.py`:
trừ `qty` khỏi số lượng của `sku`, trả về số lượng còn lại; còn lại <= 0 thì xoá `sku`
khỏi giỏ và trả về 0. `sku` không có trong giỏ → raise `KeyError`.

# Acceptance (thang điểm — đo được, có/không)
- [ ] `bash eval/checks.sh` pass
- [ ] cart {"A": 5}: remove_item(cart, "A", 2) trả về 3
- [ ] cart {"A": 1}: remove_item(cart, "A", 5) trả về 0 và "A" không còn trong cart
- [ ] remove_item(cart, "Z", 1) raise KeyError
- [ ] Có unittest cho các dòng trên trong tests/

# Ngoài phạm vi
Không sửa add_item.
