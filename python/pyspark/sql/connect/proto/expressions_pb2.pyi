#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyspark.sql.connect.proto.types_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Expression(google.protobuf.message.Message):
    """Expression used to refer to fields, functions and similar. This can be used everywhere
    expressions in SQL appear.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Window(google.protobuf.message.Message):
        """Expression for the OVER clause or WINDOW clause."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class WindowFrame(google.protobuf.message.Message):
            """The window frame"""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class _FrameType:
                ValueType = typing.NewType("ValueType", builtins.int)
                V: typing_extensions.TypeAlias = ValueType

            class _FrameTypeEnumTypeWrapper(
                google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
                    Expression.Window.WindowFrame._FrameType.ValueType
                ],
                builtins.type,
            ):  # noqa: F821
                DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                FRAME_TYPE_UNDEFINED: Expression.Window.WindowFrame._FrameType.ValueType  # 0
                FRAME_TYPE_ROW: Expression.Window.WindowFrame._FrameType.ValueType  # 1
                """RowFrame treats rows in a partition individually."""
                FRAME_TYPE_RANGE: Expression.Window.WindowFrame._FrameType.ValueType  # 2
                """RangeFrame treats rows in a partition as groups of peers.
                All rows having the same 'ORDER BY' ordering are considered as peers.
                """

            class FrameType(_FrameType, metaclass=_FrameTypeEnumTypeWrapper): ...
            FRAME_TYPE_UNDEFINED: Expression.Window.WindowFrame.FrameType.ValueType  # 0
            FRAME_TYPE_ROW: Expression.Window.WindowFrame.FrameType.ValueType  # 1
            """RowFrame treats rows in a partition individually."""
            FRAME_TYPE_RANGE: Expression.Window.WindowFrame.FrameType.ValueType  # 2
            """RangeFrame treats rows in a partition as groups of peers.
            All rows having the same 'ORDER BY' ordering are considered as peers.
            """

            class FrameBoundary(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                CURRENT_ROW_FIELD_NUMBER: builtins.int
                UNBOUNDED_FIELD_NUMBER: builtins.int
                VALUE_FIELD_NUMBER: builtins.int
                current_row: builtins.bool
                """CURRENT ROW boundary"""
                unbounded: builtins.bool
                """UNBOUNDED boundary.
                For lower bound, it will be converted to 'UnboundedPreceding'.
                for upper bound, it will be converted to 'UnboundedFollowing'.
                """
                @property
                def value(self) -> global___Expression:
                    """This is an expression for future proofing. We are expecting literals on the server side."""
                def __init__(
                    self,
                    *,
                    current_row: builtins.bool = ...,
                    unbounded: builtins.bool = ...,
                    value: global___Expression | None = ...,
                ) -> None: ...
                def HasField(
                    self,
                    field_name: typing_extensions.Literal[
                        "boundary",
                        b"boundary",
                        "current_row",
                        b"current_row",
                        "unbounded",
                        b"unbounded",
                        "value",
                        b"value",
                    ],
                ) -> builtins.bool: ...
                def ClearField(
                    self,
                    field_name: typing_extensions.Literal[
                        "boundary",
                        b"boundary",
                        "current_row",
                        b"current_row",
                        "unbounded",
                        b"unbounded",
                        "value",
                        b"value",
                    ],
                ) -> None: ...
                def WhichOneof(
                    self, oneof_group: typing_extensions.Literal["boundary", b"boundary"]
                ) -> typing_extensions.Literal["current_row", "unbounded", "value"] | None: ...

            FRAME_TYPE_FIELD_NUMBER: builtins.int
            LOWER_FIELD_NUMBER: builtins.int
            UPPER_FIELD_NUMBER: builtins.int
            frame_type: global___Expression.Window.WindowFrame.FrameType.ValueType
            """(Required) The type of the frame."""
            @property
            def lower(self) -> global___Expression.Window.WindowFrame.FrameBoundary:
                """(Required) The lower bound of the frame."""
            @property
            def upper(self) -> global___Expression.Window.WindowFrame.FrameBoundary:
                """(Required) The upper bound of the frame."""
            def __init__(
                self,
                *,
                frame_type: global___Expression.Window.WindowFrame.FrameType.ValueType = ...,
                lower: global___Expression.Window.WindowFrame.FrameBoundary | None = ...,
                upper: global___Expression.Window.WindowFrame.FrameBoundary | None = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["lower", b"lower", "upper", b"upper"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal[
                    "frame_type", b"frame_type", "lower", b"lower", "upper", b"upper"
                ],
            ) -> None: ...

        WINDOW_FUNCTION_FIELD_NUMBER: builtins.int
        PARTITION_SPEC_FIELD_NUMBER: builtins.int
        ORDER_SPEC_FIELD_NUMBER: builtins.int
        FRAME_SPEC_FIELD_NUMBER: builtins.int
        @property
        def window_function(self) -> global___Expression:
            """(Required) The window function."""
        @property
        def partition_spec(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___Expression
        ]:
            """(Optional) The way that input rows are partitioned."""
        @property
        def order_spec(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___Expression.SortOrder
        ]:
            """(Optional) Ordering of rows in a partition."""
        @property
        def frame_spec(self) -> global___Expression.Window.WindowFrame:
            """(Optional) Window frame in a partition.

            If not set, it will be treated as 'UnspecifiedFrame'.
            """
        def __init__(
            self,
            *,
            window_function: global___Expression | None = ...,
            partition_spec: collections.abc.Iterable[global___Expression] | None = ...,
            order_spec: collections.abc.Iterable[global___Expression.SortOrder] | None = ...,
            frame_spec: global___Expression.Window.WindowFrame | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "frame_spec", b"frame_spec", "window_function", b"window_function"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "frame_spec",
                b"frame_spec",
                "order_spec",
                b"order_spec",
                "partition_spec",
                b"partition_spec",
                "window_function",
                b"window_function",
            ],
        ) -> None: ...

    class SortOrder(google.protobuf.message.Message):
        """SortOrder is used to specify the  data ordering, it is normally used in Sort and Window.
        It is an unevaluable expression and cannot be evaluated, so can not be used in Projection.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _SortDirection:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _SortDirectionEnumTypeWrapper(
            google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
                Expression.SortOrder._SortDirection.ValueType
            ],
            builtins.type,
        ):  # noqa: F821
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SORT_DIRECTION_UNSPECIFIED: Expression.SortOrder._SortDirection.ValueType  # 0
            SORT_DIRECTION_ASCENDING: Expression.SortOrder._SortDirection.ValueType  # 1
            SORT_DIRECTION_DESCENDING: Expression.SortOrder._SortDirection.ValueType  # 2

        class SortDirection(_SortDirection, metaclass=_SortDirectionEnumTypeWrapper): ...
        SORT_DIRECTION_UNSPECIFIED: Expression.SortOrder.SortDirection.ValueType  # 0
        SORT_DIRECTION_ASCENDING: Expression.SortOrder.SortDirection.ValueType  # 1
        SORT_DIRECTION_DESCENDING: Expression.SortOrder.SortDirection.ValueType  # 2

        class _NullOrdering:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _NullOrderingEnumTypeWrapper(
            google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
                Expression.SortOrder._NullOrdering.ValueType
            ],
            builtins.type,
        ):  # noqa: F821
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SORT_NULLS_UNSPECIFIED: Expression.SortOrder._NullOrdering.ValueType  # 0
            SORT_NULLS_FIRST: Expression.SortOrder._NullOrdering.ValueType  # 1
            SORT_NULLS_LAST: Expression.SortOrder._NullOrdering.ValueType  # 2

        class NullOrdering(_NullOrdering, metaclass=_NullOrderingEnumTypeWrapper): ...
        SORT_NULLS_UNSPECIFIED: Expression.SortOrder.NullOrdering.ValueType  # 0
        SORT_NULLS_FIRST: Expression.SortOrder.NullOrdering.ValueType  # 1
        SORT_NULLS_LAST: Expression.SortOrder.NullOrdering.ValueType  # 2

        CHILD_FIELD_NUMBER: builtins.int
        DIRECTION_FIELD_NUMBER: builtins.int
        NULL_ORDERING_FIELD_NUMBER: builtins.int
        @property
        def child(self) -> global___Expression:
            """(Required) The expression to be sorted."""
        direction: global___Expression.SortOrder.SortDirection.ValueType
        """(Required) The sort direction, should be ASCENDING or DESCENDING."""
        null_ordering: global___Expression.SortOrder.NullOrdering.ValueType
        """(Required) How to deal with NULLs, should be NULLS_FIRST or NULLS_LAST."""
        def __init__(
            self,
            *,
            child: global___Expression | None = ...,
            direction: global___Expression.SortOrder.SortDirection.ValueType = ...,
            null_ordering: global___Expression.SortOrder.NullOrdering.ValueType = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["child", b"child"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "child", b"child", "direction", b"direction", "null_ordering", b"null_ordering"
            ],
        ) -> None: ...

    class Cast(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EXPR_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        TYPE_STR_FIELD_NUMBER: builtins.int
        @property
        def expr(self) -> global___Expression:
            """(Required) the expression to be casted."""
        @property
        def type(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        type_str: builtins.str
        """If this is set, Server will use Catalyst parser to parse this string to DataType."""
        def __init__(
            self,
            *,
            expr: global___Expression | None = ...,
            type: pyspark.sql.connect.proto.types_pb2.DataType | None = ...,
            type_str: builtins.str = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "cast_to_type",
                b"cast_to_type",
                "expr",
                b"expr",
                "type",
                b"type",
                "type_str",
                b"type_str",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "cast_to_type",
                b"cast_to_type",
                "expr",
                b"expr",
                "type",
                b"type",
                "type_str",
                b"type_str",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["cast_to_type", b"cast_to_type"]
        ) -> typing_extensions.Literal["type", "type_str"] | None: ...

    class Literal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class Decimal(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            VALUE_FIELD_NUMBER: builtins.int
            PRECISION_FIELD_NUMBER: builtins.int
            SCALE_FIELD_NUMBER: builtins.int
            value: builtins.str
            """the string representation."""
            precision: builtins.int
            """The maximum number of digits allowed in the value.
            the maximum precision is 38.
            """
            scale: builtins.int
            """declared scale of decimal literal"""
            def __init__(
                self,
                *,
                value: builtins.str = ...,
                precision: builtins.int | None = ...,
                scale: builtins.int | None = ...,
            ) -> None: ...
            def HasField(
                self,
                field_name: typing_extensions.Literal[
                    "_precision",
                    b"_precision",
                    "_scale",
                    b"_scale",
                    "precision",
                    b"precision",
                    "scale",
                    b"scale",
                ],
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal[
                    "_precision",
                    b"_precision",
                    "_scale",
                    b"_scale",
                    "precision",
                    b"precision",
                    "scale",
                    b"scale",
                    "value",
                    b"value",
                ],
            ) -> None: ...
            @typing.overload
            def WhichOneof(
                self, oneof_group: typing_extensions.Literal["_precision", b"_precision"]
            ) -> typing_extensions.Literal["precision"] | None: ...
            @typing.overload
            def WhichOneof(
                self, oneof_group: typing_extensions.Literal["_scale", b"_scale"]
            ) -> typing_extensions.Literal["scale"] | None: ...

        class CalendarInterval(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            MONTHS_FIELD_NUMBER: builtins.int
            DAYS_FIELD_NUMBER: builtins.int
            MICROSECONDS_FIELD_NUMBER: builtins.int
            months: builtins.int
            days: builtins.int
            microseconds: builtins.int
            def __init__(
                self,
                *,
                months: builtins.int = ...,
                days: builtins.int = ...,
                microseconds: builtins.int = ...,
            ) -> None: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal[
                    "days", b"days", "microseconds", b"microseconds", "months", b"months"
                ],
            ) -> None: ...

        NULL_FIELD_NUMBER: builtins.int
        BINARY_FIELD_NUMBER: builtins.int
        BOOLEAN_FIELD_NUMBER: builtins.int
        BYTE_FIELD_NUMBER: builtins.int
        SHORT_FIELD_NUMBER: builtins.int
        INTEGER_FIELD_NUMBER: builtins.int
        LONG_FIELD_NUMBER: builtins.int
        FLOAT_FIELD_NUMBER: builtins.int
        DOUBLE_FIELD_NUMBER: builtins.int
        DECIMAL_FIELD_NUMBER: builtins.int
        STRING_FIELD_NUMBER: builtins.int
        DATE_FIELD_NUMBER: builtins.int
        TIMESTAMP_FIELD_NUMBER: builtins.int
        TIMESTAMP_NTZ_FIELD_NUMBER: builtins.int
        CALENDAR_INTERVAL_FIELD_NUMBER: builtins.int
        YEAR_MONTH_INTERVAL_FIELD_NUMBER: builtins.int
        DAY_TIME_INTERVAL_FIELD_NUMBER: builtins.int
        @property
        def null(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        binary: builtins.bytes
        boolean: builtins.bool
        byte: builtins.int
        short: builtins.int
        integer: builtins.int
        long: builtins.int
        float: builtins.float
        double: builtins.float
        @property
        def decimal(self) -> global___Expression.Literal.Decimal: ...
        string: builtins.str
        date: builtins.int
        """Date in units of days since the UNIX epoch."""
        timestamp: builtins.int
        """Timestamp in units of microseconds since the UNIX epoch."""
        timestamp_ntz: builtins.int
        """Timestamp in units of microseconds since the UNIX epoch (without timezone information)."""
        @property
        def calendar_interval(self) -> global___Expression.Literal.CalendarInterval: ...
        year_month_interval: builtins.int
        day_time_interval: builtins.int
        def __init__(
            self,
            *,
            null: pyspark.sql.connect.proto.types_pb2.DataType | None = ...,
            binary: builtins.bytes = ...,
            boolean: builtins.bool = ...,
            byte: builtins.int = ...,
            short: builtins.int = ...,
            integer: builtins.int = ...,
            long: builtins.int = ...,
            float: builtins.float = ...,
            double: builtins.float = ...,
            decimal: global___Expression.Literal.Decimal | None = ...,
            string: builtins.str = ...,
            date: builtins.int = ...,
            timestamp: builtins.int = ...,
            timestamp_ntz: builtins.int = ...,
            calendar_interval: global___Expression.Literal.CalendarInterval | None = ...,
            year_month_interval: builtins.int = ...,
            day_time_interval: builtins.int = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "binary",
                b"binary",
                "boolean",
                b"boolean",
                "byte",
                b"byte",
                "calendar_interval",
                b"calendar_interval",
                "date",
                b"date",
                "day_time_interval",
                b"day_time_interval",
                "decimal",
                b"decimal",
                "double",
                b"double",
                "float",
                b"float",
                "integer",
                b"integer",
                "literal_type",
                b"literal_type",
                "long",
                b"long",
                "null",
                b"null",
                "short",
                b"short",
                "string",
                b"string",
                "timestamp",
                b"timestamp",
                "timestamp_ntz",
                b"timestamp_ntz",
                "year_month_interval",
                b"year_month_interval",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "binary",
                b"binary",
                "boolean",
                b"boolean",
                "byte",
                b"byte",
                "calendar_interval",
                b"calendar_interval",
                "date",
                b"date",
                "day_time_interval",
                b"day_time_interval",
                "decimal",
                b"decimal",
                "double",
                b"double",
                "float",
                b"float",
                "integer",
                b"integer",
                "literal_type",
                b"literal_type",
                "long",
                b"long",
                "null",
                b"null",
                "short",
                b"short",
                "string",
                b"string",
                "timestamp",
                b"timestamp",
                "timestamp_ntz",
                b"timestamp_ntz",
                "year_month_interval",
                b"year_month_interval",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["literal_type", b"literal_type"]
        ) -> typing_extensions.Literal[
            "null",
            "binary",
            "boolean",
            "byte",
            "short",
            "integer",
            "long",
            "float",
            "double",
            "decimal",
            "string",
            "date",
            "timestamp",
            "timestamp_ntz",
            "calendar_interval",
            "year_month_interval",
            "day_time_interval",
        ] | None: ...

    class UnresolvedAttribute(google.protobuf.message.Message):
        """An unresolved attribute that is not explicitly bound to a specific column, but the column
        is resolved during analysis by name.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        UNPARSED_IDENTIFIER_FIELD_NUMBER: builtins.int
        unparsed_identifier: builtins.str
        """(Required) An identifier that will be parsed by Catalyst parser. This should follow the
        Spark SQL identifier syntax.
        """
        def __init__(
            self,
            *,
            unparsed_identifier: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["unparsed_identifier", b"unparsed_identifier"],
        ) -> None: ...

    class UnresolvedFunction(google.protobuf.message.Message):
        """An unresolved function is not explicitly bound to one explicit function, but the function
        is resolved during analysis following Sparks name resolution rules.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FUNCTION_NAME_FIELD_NUMBER: builtins.int
        ARGUMENTS_FIELD_NUMBER: builtins.int
        IS_DISTINCT_FIELD_NUMBER: builtins.int
        IS_USER_DEFINED_FUNCTION_FIELD_NUMBER: builtins.int
        function_name: builtins.str
        """(Required) name (or unparsed name for user defined function) for the unresolved function."""
        @property
        def arguments(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___Expression
        ]:
            """(Optional) Function arguments. Empty arguments are allowed."""
        is_distinct: builtins.bool
        """(Required) Indicate if this function should be applied on distinct values."""
        is_user_defined_function: builtins.bool
        """(Required) Indicate if this is a user defined function.

        When it is not a user defined function, Connect will use the function name directly.
        When it is a user defined function, Connect will parse the function name first.
        """
        def __init__(
            self,
            *,
            function_name: builtins.str = ...,
            arguments: collections.abc.Iterable[global___Expression] | None = ...,
            is_distinct: builtins.bool = ...,
            is_user_defined_function: builtins.bool = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "arguments",
                b"arguments",
                "function_name",
                b"function_name",
                "is_distinct",
                b"is_distinct",
                "is_user_defined_function",
                b"is_user_defined_function",
            ],
        ) -> None: ...

    class ExpressionString(google.protobuf.message.Message):
        """Expression as string."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EXPRESSION_FIELD_NUMBER: builtins.int
        expression: builtins.str
        """(Required) A SQL expression that will be parsed by Catalyst parser."""
        def __init__(
            self,
            *,
            expression: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["expression", b"expression"]
        ) -> None: ...

    class UnresolvedStar(google.protobuf.message.Message):
        """UnresolvedStar is used to expand all the fields of a relation or struct."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TARGET_FIELD_NUMBER: builtins.int
        @property
        def target(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Optional) The target of the expansion, either be a table name or struct name, this
            is a list of identifiers that is the path of the expansion.
            """
        def __init__(
            self,
            *,
            target: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["target", b"target"]
        ) -> None: ...

    class UnresolvedRegex(google.protobuf.message.Message):
        """Represents all of the input attributes to a given relational operator, for example in
        "SELECT `(id)?+.+` FROM ...".
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        COL_NAME_FIELD_NUMBER: builtins.int
        col_name: builtins.str
        """(Required) The column name used to extract column with regex."""
        def __init__(
            self,
            *,
            col_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["col_name", b"col_name"]
        ) -> None: ...

    class UnresolvedExtractValue(google.protobuf.message.Message):
        """Extracts a value or values from an Expression"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CHILD_FIELD_NUMBER: builtins.int
        EXTRACTION_FIELD_NUMBER: builtins.int
        @property
        def child(self) -> global___Expression:
            """(Required) The expression to extract value from, can be
            Map, Array, Struct or array of Structs.
            """
        @property
        def extraction(self) -> global___Expression:
            """(Required) The expression to describe the extraction, can be
            key of Map, index of Array, field name of Struct.
            """
        def __init__(
            self,
            *,
            child: global___Expression | None = ...,
            extraction: global___Expression | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal["child", b"child", "extraction", b"extraction"],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["child", b"child", "extraction", b"extraction"],
        ) -> None: ...

    class Alias(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EXPR_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        @property
        def expr(self) -> global___Expression:
            """(Required) The expression that alias will be added on."""
        @property
        def name(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) a list of name parts for the alias.

            Scalar columns only has one name that presents.
            """
        metadata: builtins.str
        """(Optional) Alias metadata expressed as a JSON map."""
        def __init__(
            self,
            *,
            expr: global___Expression | None = ...,
            name: collections.abc.Iterable[builtins.str] | None = ...,
            metadata: builtins.str | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_metadata", b"_metadata", "expr", b"expr", "metadata", b"metadata"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_metadata", b"_metadata", "expr", b"expr", "metadata", b"metadata", "name", b"name"
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["_metadata", b"_metadata"]
        ) -> typing_extensions.Literal["metadata"] | None: ...

    class LambdaFunction(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FUNCTION_FIELD_NUMBER: builtins.int
        ARGUMENTS_FIELD_NUMBER: builtins.int
        @property
        def function(self) -> global___Expression:
            """(Required) The lambda function.

            The function body should use 'UnresolvedAttribute' as arguments, the sever side will
            replace 'UnresolvedAttribute' with 'UnresolvedNamedLambdaVariable'.
            """
        @property
        def arguments(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) Function variable names. Must contains 1 ~ 3 variables."""
        def __init__(
            self,
            *,
            function: global___Expression | None = ...,
            arguments: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["function", b"function"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "arguments", b"arguments", "function", b"function"
            ],
        ) -> None: ...

    LITERAL_FIELD_NUMBER: builtins.int
    UNRESOLVED_ATTRIBUTE_FIELD_NUMBER: builtins.int
    UNRESOLVED_FUNCTION_FIELD_NUMBER: builtins.int
    EXPRESSION_STRING_FIELD_NUMBER: builtins.int
    UNRESOLVED_STAR_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    CAST_FIELD_NUMBER: builtins.int
    UNRESOLVED_REGEX_FIELD_NUMBER: builtins.int
    SORT_ORDER_FIELD_NUMBER: builtins.int
    LAMBDA_FUNCTION_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    UNRESOLVED_EXTRACT_VALUE_FIELD_NUMBER: builtins.int
    @property
    def literal(self) -> global___Expression.Literal: ...
    @property
    def unresolved_attribute(self) -> global___Expression.UnresolvedAttribute: ...
    @property
    def unresolved_function(self) -> global___Expression.UnresolvedFunction: ...
    @property
    def expression_string(self) -> global___Expression.ExpressionString: ...
    @property
    def unresolved_star(self) -> global___Expression.UnresolvedStar: ...
    @property
    def alias(self) -> global___Expression.Alias: ...
    @property
    def cast(self) -> global___Expression.Cast: ...
    @property
    def unresolved_regex(self) -> global___Expression.UnresolvedRegex: ...
    @property
    def sort_order(self) -> global___Expression.SortOrder: ...
    @property
    def lambda_function(self) -> global___Expression.LambdaFunction: ...
    @property
    def window(self) -> global___Expression.Window: ...
    @property
    def unresolved_extract_value(self) -> global___Expression.UnresolvedExtractValue: ...
    def __init__(
        self,
        *,
        literal: global___Expression.Literal | None = ...,
        unresolved_attribute: global___Expression.UnresolvedAttribute | None = ...,
        unresolved_function: global___Expression.UnresolvedFunction | None = ...,
        expression_string: global___Expression.ExpressionString | None = ...,
        unresolved_star: global___Expression.UnresolvedStar | None = ...,
        alias: global___Expression.Alias | None = ...,
        cast: global___Expression.Cast | None = ...,
        unresolved_regex: global___Expression.UnresolvedRegex | None = ...,
        sort_order: global___Expression.SortOrder | None = ...,
        lambda_function: global___Expression.LambdaFunction | None = ...,
        window: global___Expression.Window | None = ...,
        unresolved_extract_value: global___Expression.UnresolvedExtractValue | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "alias",
            b"alias",
            "cast",
            b"cast",
            "expr_type",
            b"expr_type",
            "expression_string",
            b"expression_string",
            "lambda_function",
            b"lambda_function",
            "literal",
            b"literal",
            "sort_order",
            b"sort_order",
            "unresolved_attribute",
            b"unresolved_attribute",
            "unresolved_extract_value",
            b"unresolved_extract_value",
            "unresolved_function",
            b"unresolved_function",
            "unresolved_regex",
            b"unresolved_regex",
            "unresolved_star",
            b"unresolved_star",
            "window",
            b"window",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "alias",
            b"alias",
            "cast",
            b"cast",
            "expr_type",
            b"expr_type",
            "expression_string",
            b"expression_string",
            "lambda_function",
            b"lambda_function",
            "literal",
            b"literal",
            "sort_order",
            b"sort_order",
            "unresolved_attribute",
            b"unresolved_attribute",
            "unresolved_extract_value",
            b"unresolved_extract_value",
            "unresolved_function",
            b"unresolved_function",
            "unresolved_regex",
            b"unresolved_regex",
            "unresolved_star",
            b"unresolved_star",
            "window",
            b"window",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["expr_type", b"expr_type"]
    ) -> typing_extensions.Literal[
        "literal",
        "unresolved_attribute",
        "unresolved_function",
        "expression_string",
        "unresolved_star",
        "alias",
        "cast",
        "unresolved_regex",
        "sort_order",
        "lambda_function",
        "window",
        "unresolved_extract_value",
    ] | None: ...

global___Expression = Expression
