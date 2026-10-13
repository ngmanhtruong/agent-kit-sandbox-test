"""Giỏ hàng tối giản. Giỏ là dict: sku -> số lượng."""


def new_cart():
    return {}


def remove_item(cart, sku, qty):
    if sku not in cart:
        raise KeyError(sku)
    left = cart[sku] - qty
    if left <= 0:
        del cart[sku]
        return 0
    cart[sku] = left
    return left
