class APIError(Exception):
    def __init__(
            self, message, http_body=None, http_status=None):
        super().__init__(message)
        self.message = message
        self.http_body = http_body
        self.http_status = http_status
