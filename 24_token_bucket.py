"""Demonstrate a token bucket rate limiter."""
import time

class TokenBucket:
    def __init__(self, capacity: int, refill_per_second: float):
        if capacity <= 0 or refill_per_second < 0:
            raise ValueError("capacity must be positive and refill rate nonnegative")
        self.capacity = capacity
        self.refill_rate = refill_per_second
        self.tokens = float(capacity)
        self.updated_at = time.monotonic()

    def allow(self, cost: float = 1) -> bool:
        if cost <= 0 or cost > self.capacity:
            raise ValueError("cost must be positive and no greater than capacity")
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated_at) * self.refill_rate)
        self.updated_at = now
        if self.tokens < cost:
            return False
        self.tokens -= cost
        return True

if __name__ == "__main__":
    bucket = TokenBucket(capacity=3, refill_per_second=0.5)
    print([bucket.allow() for _ in range(5)])
