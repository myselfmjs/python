# coding: utf-8
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():

    def __init__(self,key,iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')
        self.mode = AES.MODE_CBC

    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv)
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

        #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        text = text
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')
       # return plain_text.rstrip('\0')


if __name__ == '__main__':
    text = {'username': '', 'password': '', 'rememberLogin': 'true'}
    param = 'YfuximnhctY9INMO167IwI43Hlsa0pI0MisoQVLEkgJBYuxBsbdX5tkfm5hHSr1Bxtsc27ERKvL6oH6gyHtfYUbRWvhLA+wt0DZpN8oMrxZm+spOghqlHaFhB7l56x/jrWcQLMm8bVD7Mzq20GEakPXo42nj+VgmiUt+BryTAdiS29t4dWGinWF5rDXVc0k+'
    iv = '0102030405060708'
    pc = prpcrypt('0CoJUm6Qyw8W8jud',iv)      #初始化密钥
    # d = pc.decrypt(param)
    # print(d)

    e = pc.encrypt(str(text))
    d = pc.decrypt(e)
    print (e, d)

    # e = pc.encrypt("00000000000000000000000000")
    # d = pc.decrypt(e)
    # print (e, d)