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
def remove_item(cart, sku, qty):
    if sku not in cart:
        raise KeyError(sku)
    left = cart[sku] - qty
    if left <= 0:
        del cart[sku]
        return 0
    cart[sku] = left
    return left

# [FIX-1]
