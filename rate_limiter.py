import time
from threading import Lock

class RateLimiter:
    def __init__(self):
        self.requests = {}
        self.lock = Lock()
        self.max_requests = 5
        self.time_window = 60  # 1 minute

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.requests:
                self.requests[user_id] = []

            # Remove old requests outside of the time window
            self.requests[user_id] = [req_time for req_time in self.requests[user_id] 
                                      if current_time - req_time <= self.time_window]

            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

if __name__ == "__main__":
    rate_limiter = RateLimiter()
    print(rate_limiter.allow_request('user1'))  # Test example
