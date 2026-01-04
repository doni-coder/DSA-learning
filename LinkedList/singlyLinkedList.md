### What is a Singly Linked List (SLL)?
→ A **Singly Linked List** is a **linear data structure** where elements are stored in **nodes**.  
→ Each node contains:
- **Data (item)**
- **Reference (next)** to the next node in the list  

→ Nodes are **not stored in contiguous memory** like arrays.

---

### Node Structure
→ The `Node` class represents a single element of the linked list.

**Components:**
- `item` → stores the data
- `next` → stores the reference to the next node

→ Every linked list is built by connecting multiple `Node` objects.

---

### Singly Linked List (SLL) Class
→ The `SLL` class manages the entire linked list.

**Key Attribute:**
- `start` → points to the first node (head) of the list

---

### Core Operations in SLL

#### Check if List is Empty
→ `is_empty()` returns `True` if the list has no nodes.

---

#### Insert at Start
→ `insert_at_start(data)`  
→ Creates a new node and makes it the **first node** of the list.

---

#### Insert at Last
→ `insert_at_last(data)`  
→ Traverses the list and inserts the new node at the **end**.

---

#### Search an Element
→ `search(data)`  
→ Traverses the list to find a node with matching data.  
→ Returns the **node reference** if found, otherwise `None`.

---

#### Insert After a Given Node
→ `insert_after(node, data)`  
→ Inserts a new node **after a specific node**.

---

#### Insert Using Node Reference
→ `insert(temp, data)`  
→ Inserts a new node after the given node reference.

---

### Deletion Operations

#### Delete from First
→ `delete_from_first()`  
→ Removes the **head node** of the list.

---

#### Delete from Last
→ `delete_from_last()`  
→ Traverses the list and removes the **last node**.

---

#### Delete a Specific Item
→ `delete_item(data)`  
→ Removes the first occurrence of the given data from the list.

---

### Traversal and Display

#### Print Linked List
→ `print_list()`  
→ Traverses the list and prints each node’s data.

---

### Iterator Support (Looping with `for`)
→ Custom iterator implemented using `SLLIterator` class.  
→ Enables looping directly over the linked list using:

```python
for item in my_list:
    print(item)
