import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))