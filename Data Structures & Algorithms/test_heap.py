import pytest
from heap import binary_heap

@pytest.fixture
def heap():
    h = binary_heap()
    h.insert(5)
    h.insert(10)
    h.insert(3)
    h.insert(1)
    h.insert(4)
    h.insert(6)
    return h


def test_insert_single():
    h = binary_heap()
    h.insert(5)
    assert h.heap[1] == 5

def test_insert_min_bubbles_to_root(heap):
    assert heap.heap[1] == 1

def test_remove_i(heap):
    heap.delete_i(1)
    assert heap.heap == [0, 3, 4, 5, 10, 6]