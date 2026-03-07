import math_utils as mu
import string_utils as su
import shop_package.billing as billing
import shop_package.discount as discount

print(mu.add(2, 3))
print(mu.subtract(5, 2))
print(mu.square(4))
print(su.capitalize_words("hello world"))
print(su.reverse_string("hello world"))
print(su.word_count("hello world"))
print(discount.apply_discount(100, 20))
print(discount.flat_discount(100, 50))
print(billing.calculate_total([10, 20, 30]))
print(billing.apply_tax(100, 5))

