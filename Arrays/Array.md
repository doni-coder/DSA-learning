### What is an Array?
→ An **array** is a data structure that stores elements of the **same data type** in **contiguous memory locations**.  
→ It allows **fast access** to elements using index positions.

---

### Array in Python
→ In Python, arrays can be created using:
1. **`array` module** (built-in, type-restricted)
2. **`numpy` module** (powerful, supports multi-dimensional arrays)

---

### Array using `array` Module
→ Requires importing the `array` module  
→ Stores elements of **same type only** (defined by typecode)

**Example Typecodes:**
- `'I'` → Unsigned Integer (4 bytes)
- `'f'` → Float
- `'u'` → Unicode Character

→ Supports methods like:
- `append()`
- `insert()`
- `reverse()`

---

### Array using `numpy` Module
→ Requires importing `numpy`  
→ Automatically handles data types  
→ Supports **multi-dimensional arrays**  
→ Faster and widely used in **Data Science & ML**

**Key Points from Code:**
→ `numpy.array([1,2,3])` creates a 1D array  
→ Mixed values convert to a common data type (int → float)  
→ Supports:
- 1D Array
- 2D Array (Matrix)
- 3D Array (Tensor)

---

### Accessing Elements
→ Elements are accessed using **indexing**
→ For multi-dimensional arrays:
`array[row][column][depth]`

**Example:**
→ `three[0][0][0]` accesses the first element of a 3D array
