# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
try:
    import otg_pb2 as otg__pb2
except ImportError:
    from snappi import otg_pb2 as otg__pb2


class OpenapiStub(object):
    """Description missing in models

    For all RPCs defined in this service, API Server SHOULD provide JSON
    representation of `Error` message as an error string upon failure, ensuring
    name of enum constants (instead of value) for `kind` property is present
    in the representation
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetConfig = channel.unary_unary(
                '/otg.Openapi/SetConfig',
                request_serializer=otg__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=otg__pb2.SetConfigResponse.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/otg.Openapi/GetConfig',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=otg__pb2.GetConfigResponse.FromString,
                )
        self.UpdateConfig = channel.unary_unary(
                '/otg.Openapi/UpdateConfig',
                request_serializer=otg__pb2.UpdateConfigRequest.SerializeToString,
                response_deserializer=otg__pb2.UpdateConfigResponse.FromString,
                )
        self.SetControlState = channel.unary_unary(
                '/otg.Openapi/SetControlState',
                request_serializer=otg__pb2.SetControlStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetControlStateResponse.FromString,
                )
        self.SetControlAction = channel.unary_unary(
                '/otg.Openapi/SetControlAction',
                request_serializer=otg__pb2.SetControlActionRequest.SerializeToString,
                response_deserializer=otg__pb2.SetControlActionResponse.FromString,
                )
        self.SetTransmitState = channel.unary_unary(
                '/otg.Openapi/SetTransmitState',
                request_serializer=otg__pb2.SetTransmitStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetTransmitStateResponse.FromString,
                )
        self.SetLinkState = channel.unary_unary(
                '/otg.Openapi/SetLinkState',
                request_serializer=otg__pb2.SetLinkStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetLinkStateResponse.FromString,
                )
        self.SetCaptureState = channel.unary_unary(
                '/otg.Openapi/SetCaptureState',
                request_serializer=otg__pb2.SetCaptureStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetCaptureStateResponse.FromString,
                )
        self.UpdateFlows = channel.unary_unary(
                '/otg.Openapi/UpdateFlows',
                request_serializer=otg__pb2.UpdateFlowsRequest.SerializeToString,
                response_deserializer=otg__pb2.UpdateFlowsResponse.FromString,
                )
        self.SetRouteState = channel.unary_unary(
                '/otg.Openapi/SetRouteState',
                request_serializer=otg__pb2.SetRouteStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetRouteStateResponse.FromString,
                )
        self.SendPing = channel.unary_unary(
                '/otg.Openapi/SendPing',
                request_serializer=otg__pb2.SendPingRequest.SerializeToString,
                response_deserializer=otg__pb2.SendPingResponse.FromString,
                )
        self.SetProtocolState = channel.unary_unary(
                '/otg.Openapi/SetProtocolState',
                request_serializer=otg__pb2.SetProtocolStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetProtocolStateResponse.FromString,
                )
        self.SetDeviceState = channel.unary_unary(
                '/otg.Openapi/SetDeviceState',
                request_serializer=otg__pb2.SetDeviceStateRequest.SerializeToString,
                response_deserializer=otg__pb2.SetDeviceStateResponse.FromString,
                )
        self.GetMetrics = channel.unary_unary(
                '/otg.Openapi/GetMetrics',
                request_serializer=otg__pb2.GetMetricsRequest.SerializeToString,
                response_deserializer=otg__pb2.GetMetricsResponse.FromString,
                )
        self.GetStates = channel.unary_unary(
                '/otg.Openapi/GetStates',
                request_serializer=otg__pb2.GetStatesRequest.SerializeToString,
                response_deserializer=otg__pb2.GetStatesResponse.FromString,
                )
        self.GetCapture = channel.unary_unary(
                '/otg.Openapi/GetCapture',
                request_serializer=otg__pb2.GetCaptureRequest.SerializeToString,
                response_deserializer=otg__pb2.GetCaptureResponse.FromString,
                )
        self.GetVersion = channel.unary_unary(
                '/otg.Openapi/GetVersion',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=otg__pb2.GetVersionResponse.FromString,
                )


class OpenapiServicer(object):
    """Description missing in models

    For all RPCs defined in this service, API Server SHOULD provide JSON
    representation of `Error` message as an error string upon failure, ensuring
    name of enum constants (instead of value) for `kind` property is present
    in the representation
    """

    def SetConfig(self, request, context):
        """Sets configuration resources on the traffic generator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfig(self, request, context):
        """Description missing in models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConfig(self, request, context):
        """Updates specific attributes of resources configured on the traffic generator. The
        fetched configuration shall reflect the updates applied successfully.
        The Response.Warnings in the Success response is available for implementers to disclose
        additional information about a state change including any implicit changes that are
        outside the scope of the state change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetControlState(self, request, context):
        """Sets the operational state of configured resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetControlAction(self, request, context):
        """Triggers actions against configured resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTransmitState(self, request, context):
        """Deprecated: Please use `set_control_state` with `traffic.flow_transmit` choice instead

        Deprecated: Please use `set_control_state` with `traffic.flow_transmit` choice instead

        Updates the state of configuration resources on the traffic generator.
        The Response.Warnings in the Success response is available for implementers to disclose
        additional information about a state change including any implicit changes that are
        outside the scope of the state change.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLinkState(self, request, context):
        """Deprecated: Please use `set_control_state` with `port.link` choice instead

        Deprecated: Please use `set_control_state` with `port.link` choice instead

        Updates the state of configuration resources on the traffic generator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCaptureState(self, request, context):
        """Deprecated: Please use `set_control_state` with `port.capture` choice instead

        Deprecated: Please use `set_control_state` with `port.capture` choice instead

        Updates the state of configuration resources on the traffic generator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFlows(self, request, context):
        """Deprecated: Please use `update_config` with `flow` choice instead

        Deprecated: Please use `update_config` with `flow` choice instead

        Updates flow properties without disruption of transmit state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRouteState(self, request, context):
        """Deprecated: Please use `set_control_state` with `protocol.route` choice instead

        Deprecated: Please use `set_control_state` with `protocol.route` choice instead

        Updates the state of configuration resources on the traffic generator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPing(self, request, context):
        """Deprecated: Please use `set_control_action` with `protocol.ipv*.ping` choice instead

        Deprecated: Please use `set_control_action` with `protocol.ipv*.ping` choice instead

        API to send an IPv4 and/or IPv6 ICMP Echo Request(s) between endpoints. For each
        endpoint 1 ping packet will be sent and API shall wait for ping response to either
        be successful or timeout. The API wait timeout for each request is 300ms.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetProtocolState(self, request, context):
        """Deprecated: Please use `set_control_state` with `protocol.all` choice instead

        Deprecated: Please use `set_control_state` with `protocol.all` choice instead

        Sets all configured protocols to `start` or `stop` state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceState(self, request, context):
        """Deprecated: Please use `set_control_state` with `protocol` choice instead

        Deprecated: Please use `set_control_state` with `protocol` choice instead

        Set specific state/actions on device configuration resources on the traffic generator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Description missing in models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStates(self, request, context):
        """Description missing in models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCapture(self, request, context):
        """Description missing in models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Description missing in models
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OpenapiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=otg__pb2.SetConfigRequest.FromString,
                    response_serializer=otg__pb2.SetConfigResponse.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=otg__pb2.GetConfigResponse.SerializeToString,
            ),
            'UpdateConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConfig,
                    request_deserializer=otg__pb2.UpdateConfigRequest.FromString,
                    response_serializer=otg__pb2.UpdateConfigResponse.SerializeToString,
            ),
            'SetControlState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetControlState,
                    request_deserializer=otg__pb2.SetControlStateRequest.FromString,
                    response_serializer=otg__pb2.SetControlStateResponse.SerializeToString,
            ),
            'SetControlAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetControlAction,
                    request_deserializer=otg__pb2.SetControlActionRequest.FromString,
                    response_serializer=otg__pb2.SetControlActionResponse.SerializeToString,
            ),
            'SetTransmitState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTransmitState,
                    request_deserializer=otg__pb2.SetTransmitStateRequest.FromString,
                    response_serializer=otg__pb2.SetTransmitStateResponse.SerializeToString,
            ),
            'SetLinkState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLinkState,
                    request_deserializer=otg__pb2.SetLinkStateRequest.FromString,
                    response_serializer=otg__pb2.SetLinkStateResponse.SerializeToString,
            ),
            'SetCaptureState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCaptureState,
                    request_deserializer=otg__pb2.SetCaptureStateRequest.FromString,
                    response_serializer=otg__pb2.SetCaptureStateResponse.SerializeToString,
            ),
            'UpdateFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFlows,
                    request_deserializer=otg__pb2.UpdateFlowsRequest.FromString,
                    response_serializer=otg__pb2.UpdateFlowsResponse.SerializeToString,
            ),
            'SetRouteState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRouteState,
                    request_deserializer=otg__pb2.SetRouteStateRequest.FromString,
                    response_serializer=otg__pb2.SetRouteStateResponse.SerializeToString,
            ),
            'SendPing': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPing,
                    request_deserializer=otg__pb2.SendPingRequest.FromString,
                    response_serializer=otg__pb2.SendPingResponse.SerializeToString,
            ),
            'SetProtocolState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetProtocolState,
                    request_deserializer=otg__pb2.SetProtocolStateRequest.FromString,
                    response_serializer=otg__pb2.SetProtocolStateResponse.SerializeToString,
            ),
            'SetDeviceState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceState,
                    request_deserializer=otg__pb2.SetDeviceStateRequest.FromString,
                    response_serializer=otg__pb2.SetDeviceStateResponse.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=otg__pb2.GetMetricsRequest.FromString,
                    response_serializer=otg__pb2.GetMetricsResponse.SerializeToString,
            ),
            'GetStates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStates,
                    request_deserializer=otg__pb2.GetStatesRequest.FromString,
                    response_serializer=otg__pb2.GetStatesResponse.SerializeToString,
            ),
            'GetCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCapture,
                    request_deserializer=otg__pb2.GetCaptureRequest.FromString,
                    response_serializer=otg__pb2.GetCaptureResponse.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=otg__pb2.GetVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'otg.Openapi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Openapi(object):
    """Description missing in models

    For all RPCs defined in this service, API Server SHOULD provide JSON
    representation of `Error` message as an error string upon failure, ensuring
    name of enum constants (instead of value) for `kind` property is present
    in the representation
    """

    @staticmethod
    def SetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetConfig',
            otg__pb2.SetConfigRequest.SerializeToString,
            otg__pb2.SetConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/GetConfig',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            otg__pb2.GetConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/UpdateConfig',
            otg__pb2.UpdateConfigRequest.SerializeToString,
            otg__pb2.UpdateConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetControlState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetControlState',
            otg__pb2.SetControlStateRequest.SerializeToString,
            otg__pb2.SetControlStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetControlAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetControlAction',
            otg__pb2.SetControlActionRequest.SerializeToString,
            otg__pb2.SetControlActionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTransmitState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetTransmitState',
            otg__pb2.SetTransmitStateRequest.SerializeToString,
            otg__pb2.SetTransmitStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLinkState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetLinkState',
            otg__pb2.SetLinkStateRequest.SerializeToString,
            otg__pb2.SetLinkStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCaptureState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetCaptureState',
            otg__pb2.SetCaptureStateRequest.SerializeToString,
            otg__pb2.SetCaptureStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/UpdateFlows',
            otg__pb2.UpdateFlowsRequest.SerializeToString,
            otg__pb2.UpdateFlowsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRouteState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetRouteState',
            otg__pb2.SetRouteStateRequest.SerializeToString,
            otg__pb2.SetRouteStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SendPing',
            otg__pb2.SendPingRequest.SerializeToString,
            otg__pb2.SendPingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetProtocolState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetProtocolState',
            otg__pb2.SetProtocolStateRequest.SerializeToString,
            otg__pb2.SetProtocolStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/SetDeviceState',
            otg__pb2.SetDeviceStateRequest.SerializeToString,
            otg__pb2.SetDeviceStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/GetMetrics',
            otg__pb2.GetMetricsRequest.SerializeToString,
            otg__pb2.GetMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/GetStates',
            otg__pb2.GetStatesRequest.SerializeToString,
            otg__pb2.GetStatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/GetCapture',
            otg__pb2.GetCaptureRequest.SerializeToString,
            otg__pb2.GetCaptureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/otg.Openapi/GetVersion',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            otg__pb2.GetVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)