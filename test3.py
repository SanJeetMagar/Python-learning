a = [[1, 2], [3, 4]]
b = a.copy()

a[0].append(99)

print(a)
print(b)


# Both print(a) and print(b) output [[1, 2, 99], [3, 4]].
# b got modified even though you copied. Here is why.

# What does .copy() actually copy?
# pythona = [[1, 2], [3, 4]]
# b = a.copy()
# .copy() creates a new outer list. But it does not copy the inner lists. It just copies their addresses.
# a ----→ [  address_101,  address_102  ]  (outer list)
#              ↓                ↓
#           [1, 2]           [3, 4]

# b ----→ [  address_101,  address_102  ]  (new outer list, same inner addresses)
#              ↓                ↓
#           [1, 2]           [3, 4]   ← SAME objects, not copies
# a and b are different outer lists. But their contents — [1,2] and [3,4] — are the same objects in memory.

# Now a[0].append(99) runs:
# It goes to address_101 and modifies [1,2] → [1,2,99] directly.
# b[0] also points to address_101. So b sees the change too.
# a ----→ [ address_101, address_102 ]
# b ----→ [ address_101, address_102 ]
#               ↓
#            [1,2,99]  ← both a[0] and b[0] see this

# This is called a shallow copy.
# .copy() only copies one level deep. The outer list is new. The inner objects are shared.
# To actually copy everything independently you need a deep copy:
# pythonimport copy
# b = copy.deepcopy(a)
# Now every nested object gets copied too. a and b share nothing.

# Real world this hits you on your SaaS project. You pass a nested config dict into a function, do a .copy(), think you're safe, modify a nested key — and you just corrupted the original config silently.