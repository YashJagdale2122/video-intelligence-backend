from enum import Enum

class ProcessingStatus(str,Enum):
    """
    This represents the lifecycle state of a video
    in the processing pipeline.

    These states are used across API responses, services, and persistence
    to avoid inconsistent string status or error handling.
    """

    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    FAILED = "FAILED"
