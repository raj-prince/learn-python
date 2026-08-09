#!/usr/bin/env python3
"""
================================================================================
LESSON 28: EFFICIENT GENERIC LRU CACHE — SOLUTION & EXERCISE TEST
================================================================================
"""

from collections.abc import MutableMapping, Iterator
from typing import Generic, TypeVar, Optional
import threading

K = TypeVar("K")
V = TypeVar("V")


class _Node(Generic[K, V]):
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: Optional[K] = None, val: Optional[V] = None):
        self.key = key
        self.val = val
        self.prev: Optional[_Node[K, V]] = None
        self.next: Optional[_Node[K, V]] = None


class LRUCache(MutableMapping[K, V], Generic[K, V]):
    def __init__(self, capacity: int, thread_safe: bool = False):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._cache: dict[K, _Node[K, V]] = {}
        self._head: _Node[K, V] = _Node()
        self._tail: _Node[K, V] = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._lock = threading.RLock() if thread_safe else None

    def _add_to_head(self, node: _Node[K, V]) -> None:
        node.prev = self._head
        node.next = self._head.next
        assert self._head.next is not None
        self._head.next.prev = node
        self._head.next = node

    def _remove_node(self, node: _Node[K, V]) -> None:
        prev_node, next_node = node.prev, node.next
        if prev_node is not None and next_node is not None:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _move_to_head(self, node: _Node[K, V]) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> _Node[K, V]:
        lru_node = self._tail.prev
        assert lru_node is not None and lru_node is not self._head
        self._remove_node(lru_node)
        return lru_node

    def __getitem__(self, key: K) -> V:
        if self._lock:
            with self._lock:
                return self._get_impl(key)
        return self._get_impl(key)

    def _get_impl(self, key: K) -> V:
        if key not in self._cache:
            raise KeyError(key)
        node = self._cache[key]
        self._move_to_head(node)
        return node.val  # type: ignore[return-value]

    def __setitem__(self, key: K, value: V) -> None:
        if self._lock:
            with self._lock:
                self._set_impl(key, value)
        else:
            self._set_impl(key, value)

    def _set_impl(self, key: K, value: V) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            if len(self._cache) >= self.capacity:
                lru_node = self._pop_tail()
                if lru_node.key is not None:
                    del self._cache[lru_node.key]
            new_node = _Node(key, value)
            self._cache[key] = new_node
            self._add_to_head(new_node)

    def __delitem__(self, key: K) -> None:
        if self._lock:
            with self._lock:
                self._del_impl(key)
        else:
            self._del_impl(key)

    def _del_impl(self, key: K) -> None:
        if key not in self._cache:
            raise KeyError(key)
        node = self._cache.pop(key)
        self._remove_node(node)

    def __iter__(self) -> Iterator[K]:
        curr = self._head.next
        while curr is not None and curr is not self._tail:
            if curr.key is not None:
                yield curr.key
            curr = curr.next

    def __len__(self) -> int:
        return len(self._cache)


def run_solution_verification():
    print("Verifying LRUCache Solution...")
    cache = LRUCache[str, int](capacity=2)
    cache["a"] = 1
    cache["b"] = 2
    assert cache["a"] == 1  # 'a' becomes MRU
    cache["c"] = 3  # Evicts 'b'
    assert "b" not in cache
    assert "a" in cache
    assert "c" in cache
    assert len(cache) == 2
    print("All LRUCache checks passed successfully!")


if __name__ == "__main__":
    run_solution_verification()
