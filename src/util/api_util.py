async def get_data(multipart):
    result = {}
    field = await multipart.next()
    while field is not None:
        if field.filename:
            # store file in temp file
            chunk = await field.read_chunk()
            value = bytearray()
            while chunk:
                chunk = field.decode(chunk)
                value += chunk
                chunk = await field.read_chunk()
            result[field.name] = value
        else:
            value = await field.read(decode=True)
            charset = field.get_charset(default='utf-8')
            value = value.decode(charset)
            result[field.name] = value
        field = await multipart.next()
    return result
