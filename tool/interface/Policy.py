from ctypes import (HRESULT, POINTER, Structure, Union, c_float, c_longlong, c_uint32, c_char_p)
from ctypes.wintypes import (BOOL, DWORD, INT, LONG, LPCWSTR, LPWSTR, UINT, ULARGE_INTEGER, VARIANT_BOOL, WORD)
from enum import Enum
import comtypes
import psutil
from comtypes import COMMETHOD, GUID, IUnknown
from comtypes.automation import VARTYPE, VT_BOOL, VT_CLSID, VT_LPWSTR, VT_UI4

POLICY_CONFIG_CLIENT_IID = GUID('{870AF99C-171D-4F9E-AF0D-E63DF40C2BC9}')
IPOLICY_CONFIG_X_IID = GUID('{8F9FB2AA-1C0B-4D54-B6BB-B2F2A10CE03C}')


class ERole(Enum):
    eConsole = 0
    eMultimedia = 1
    eCommunications = 2
    ERole_enum_count = 3


class IPolicyConfigX(IUnknown):
    _iid_ = IPOLICY_CONFIG_X_IID
    _methods_ = (
        # int SetDefaultEndpoint(
        #     [In] [MarshalAs(UnmanagedType.LPWStr)] string pszDeviceName,
        #     [In] [MarshalAs(UnmanagedType.U4)] ERole role);
        COMMETHOD([], HRESULT, 'SetDefaultEndpoint',
                  (['in'], LPWSTR, 'pszDeviceName'),
                  (['in'], c_uint32, 'role')),
    )


class PolicyUtil():

    @staticmethod
    def SetDefaultEndpoint(deviceName, eRole):
        policy = comtypes.CoCreateInstance(POLICY_CONFIG_CLIENT_IID, IPolicyConfigX, comtypes.CLSCTX_INPROC_SERVER)
        # policy.SetDefaultEndpoint(deviceName, eRole)


##### Testing
PolicyUtil.SetDefaultEndpoint("unknown", 0)
