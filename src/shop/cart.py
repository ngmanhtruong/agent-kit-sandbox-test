"""Giỏ hàng tối giản. Giỏ là dict: sku -> số lượng."""


def new_cart():
    return {}


# [SHOP-01]
def add_item(cart, sku, qty):
    if qty <= 0:
        raise ValueError('qty')
    cart[sku] = cart.get(sku, 0) + qty
    return cart[sku]

# [SHOP-02]

# [FIX-1]
