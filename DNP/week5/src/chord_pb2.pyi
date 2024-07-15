from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaveDataMessage(_message.Message):
    __slots__ = ("key", "text")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    key: str
    text: str
    def __init__(self, key: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class SaveDataResponse(_message.Message):
    __slots__ = ("node_id", "status")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    status: bool
    def __init__(self, node_id: _Optional[int] = ..., status: bool = ...) -> None: ...

class RemoveDataMessage(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class RemoveDataResponse(_message.Message):
    __slots__ = ("node_id", "status")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    status: bool
    def __init__(self, node_id: _Optional[int] = ..., status: bool = ...) -> None: ...

class FindDataMessage(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class FindDataResponse(_message.Message):
    __slots__ = ("data", "node_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    data: str
    node_id: int
    def __init__(self, data: _Optional[str] = ..., node_id: _Optional[int] = ...) -> None: ...

class GetFingerTableMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FingerTableEntry(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class GetFingerTableResponse(_message.Message):
    __slots__ = ("finger_table",)
    FINGER_TABLE_FIELD_NUMBER: _ClassVar[int]
    finger_table: _containers.RepeatedCompositeFieldContainer[FingerTableEntry]
    def __init__(self, finger_table: _Optional[_Iterable[_Union[FingerTableEntry, _Mapping]]] = ...) -> None: ...
