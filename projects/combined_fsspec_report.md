# Master FSSPEC Usage Report Across 8 Major Python Ecosystem Repositories

- **Repositories Crawled:** `8`
- **Total Files Scanned:** `3613`
- **Files with FSSPEC Usages:** `153`
- **Total FSSPEC Usages Detected:** `986`
- **Time Elapsed:** `112.52 seconds`

---

## 📊 Repository Summary Table

| Project Name | Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dask** | [dask/dask](https://github.com/dask/dask) | `365` | `22` | `152` | `NOT_EXPLICIT:150, parts:2` |
| **Intake** | [intake/intake](https://github.com/intake/intake) | `108` | `19` | `97` | `NOT_EXPLICIT:97` |
| **pandas** | [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `1510` | `7` | `13` | `NOT_EXPLICIT:13` |
| **xarray** | [pydata/xarray](https://github.com/pydata/xarray) | `239` | `2` | `12` | `NOT_EXPLICIT:12` |
| **zarr** | [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `379` | `4` | `38` | `NOT_EXPLICIT:38` |
| **DVC** | [iterative/dvc](https://github.com/iterative/dvc) | `554` | `71` | `547` | `NOT_EXPLICIT:547` |
| **Kedro** | [kedro-org/kedro](https://github.com/kedro-org/kedro) | `224` | `3` | `9` | `NOT_EXPLICIT:9` |
| **Hugging Face Datasets** | [huggingface/datasets](https://github.com/huggingface/datasets) | `234` | `25` | `118` | `NOT_EXPLICIT:118` |

---

## 📈 Global Cache_Type Breakdown

| Cache_Type Option | Total Occurrences | Description |
| :--- | :--- | :--- |
| `NOT_EXPLICIT` | `984` | cache_type keyword omitted (uses default fsspec strategy) |
| `parts` | `2` | Custom cache strategy |

---

## 🔍 Detailed Usage Breakdown by Repository

### Dask ([dask/dask](https://github.com/dask/dask))
- **Usages Found:** `152` in `22` files.

#### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L67) (Line 67)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `open_head`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
    """Open a file just to read its head and size"""
    with OpenFile(fs, path, compression=compression) as f:
        head = read_header(f)
```

#### 2. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L69) (Line 69)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `open_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        head = read_header(f)
    size = fs.info(path)["size"]
    return head, size
```

#### 3. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L104) (Line 104)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_avro`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
    if blocksize is not None:
        fs, fs_token, paths = get_fs_token_paths(
            urlpath, mode="rb", storage_options=storage_options
        )
        dhead = delayed(open_head)
```

#### 4. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L123) (Line 123)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_avro`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
            delimiter = head["sync"]
            f = OpenFile(fs, path, compression=compression)
            token = fs_tokenize(
```

#### 5. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L124) (Line 124)
- **Target Call:** `fs_tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_avro`
- **Arguments:** `fs_token, delimiter, path, fs.ukey(path), compression, offset`
- **Keywords:** `{}`

```python
            f = OpenFile(fs, path, compression=compression)
            token = fs_tokenize(
                fs_token, delimiter, path, fs.ukey(path), compression, offset
            )
            keys = [f"read-avro-{o}-{token}" for o in offset]
```

#### 6. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L125) (Line 125)
- **Target Call:** `fs.ukey` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_avro`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            token = fs_tokenize(
                fs_token, delimiter, path, fs.ukey(path), compression, offset
            )
```

#### 7. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L136) (Line 136)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_avro`
- **Arguments:** `urlpath`
- **Keywords:** `{'compression': 'compression'}`

```python
    else:
        files = open_files(urlpath, compression=compression, **storage_options)
        dread = delayed(read_file)
```

#### 8. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L152) (Line 152)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_chunk`
- **Arguments:** `f, off, l, head['sync']`
- **Keywords:** `{}`

```python
    with fobj as f:
        chunk = read_block(f, off, l, head["sync"])
    head_bytes = head["head_bytes"]
```

#### 9. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L256) (Line 256)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_avro`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{'name_function': 'name_function', 'num': 'b.npartitions'}`

```python
    storage_options = storage_options or {}
    files = open_files(
        filename,
        "wb",
        name_function=name_function,
        num=b.npartitions,
        **storage_options,
    )
    name = f"to-avro-{uuid.uuid4().hex}"
```

#### 10. [dask/bag/core.py](https://github.com/dask/dask/blob/main/dask/bag/core.py#L259) (Line 259)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_textfiles`
- **Arguments:** `path`
- **Keywords:** `{'compression': 'compression', 'mode': 'mode', 'encoding': 'encoding', 'name_function': 'name_function', 'num': 'b.npartitions'}`

```python
    mode = "wb" if encoding is None else "wt"
    files = open_files(
        path,
        compression=compression,
        mode=mode,
        encoding=encoding,
        name_function=name_function,
        num=b.npartitions,
        **(storage_options or {}),
    )

```

#### 11. [dask/bag/text.py](https://github.com/dask/dask/blob/main/dask/bag/text.py#L100) (Line 100)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_text`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rt'", 'encoding': 'encoding', 'errors': 'errors', 'compression': 'compression', 'newline': 'newline'}`

```python
            newline = ""
        files = open_files(
            urlpath,
            mode="rt",
            encoding=encoding,
            errors=errors,
            compression=compression,
            newline=newline,
            **(storage_options or {}),
        )
        if files_per_partition is None:
```

#### 12. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L83) (Line 83)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'kwargs'}`

```python

    fs, fs_token, paths = get_fs_token_paths(urlpath, mode="rb", storage_options=kwargs)

```

#### 13. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L103) (Line 103)
- **Target Call:** `infer_compression` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if compression == "infer":
                comp = infer_compression(path)
            else:
```

#### 14. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L111) (Line 111)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                )
            size = fs.info(path)["size"]
            if size is None:
```

#### 15. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L149) (Line 149)
- **Target Call:** `fs.ukey` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    for path, offset, length in zip(paths, offsets, lengths):
        token = tokenize(fs_token, delimiter, path, fs.ukey(path), compression, offset)
        keys = [f"read-block-{o}-{token}" for o in offset]
```

#### 16. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L153) (Line 153)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
            delayed_read(
                OpenFile(fs, path, compression=compression),
                o,
```

#### 17. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L168) (Line 168)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_bytes`
- **Arguments:** `fs, paths[0]`
- **Keywords:** `{'compression': 'compression'}`

```python
            sample = parse_bytes(sample)
        with OpenFile(fs, paths[0], compression=compression) as f:
            # read block without seek (because we start at zero)
```

#### 18. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L194) (Line 194)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_block_from_file`
- **Arguments:** `f, off, bs, delimiter`
- **Keywords:** `{}`

```python
            return f.read()
        return read_block(f, off, bs, delimiter)
```

#### 19. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L21) (Line 21)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 1, 2`
- **Keywords:** `{}`

```python

    assert read_block(f, 1, 2) == b"23"
    assert read_block(f, 0, 1, delimiter=b"\n") == b"123\n"
```

#### 20. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L22) (Line 22)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 1`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 1, 2) == b"23"
    assert read_block(f, 0, 1, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 2, delimiter=b"\n") == b"123\n"
```

#### 21. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L23) (Line 23)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 2`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 1, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 2, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 3, delimiter=b"\n") == b"123\n"
```

#### 22. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L24) (Line 24)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 3`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 2, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 3, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 5, delimiter=b"\n") == b"123\n456\n"
```

#### 23. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L25) (Line 25)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 5`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 3, delimiter=b"\n") == b"123\n"
    assert read_block(f, 0, 5, delimiter=b"\n") == b"123\n456\n"
    assert read_block(f, 0, 8, delimiter=b"\n") == b"123\n456\n789"
```

#### 24. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L26) (Line 26)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 8`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 5, delimiter=b"\n") == b"123\n456\n"
    assert read_block(f, 0, 8, delimiter=b"\n") == b"123\n456\n789"
    assert read_block(f, 0, 100, delimiter=b"\n") == b"123\n456\n789"
```

#### 25. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L27) (Line 27)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 0, 100`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 8, delimiter=b"\n") == b"123\n456\n789"
    assert read_block(f, 0, 100, delimiter=b"\n") == b"123\n456\n789"
    assert read_block(f, 1, 1, delimiter=b"\n") == b""
```

#### 26. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L28) (Line 28)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 1, 1`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 0, 100, delimiter=b"\n") == b"123\n456\n789"
    assert read_block(f, 1, 1, delimiter=b"\n") == b""
    assert read_block(f, 1, 5, delimiter=b"\n") == b"456\n"
```

#### 27. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L29) (Line 29)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 1, 5`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 1, 1, delimiter=b"\n") == b""
    assert read_block(f, 1, 5, delimiter=b"\n") == b"456\n"
    assert read_block(f, 1, 8, delimiter=b"\n") == b"456\n789"
```

#### 28. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L30) (Line 30)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, 1, 8`
- **Keywords:** `{'delimiter': "b'\\n'"}`

```python
    assert read_block(f, 1, 5, delimiter=b"\n") == b"456\n"
    assert read_block(f, 1, 8, delimiter=b"\n") == b"456\n789"

```

#### 29. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L33) (Line 33)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_read_block`
- **Arguments:** `f, o, l, b'\n'`
- **Keywords:** `{}`

```python
    for ols in [[(0, 3), (3, 3), (6, 3), (9, 2)], [(0, 4), (4, 4), (8, 4)]]:
        out = [read_block(f, o, l, b"\n") for o, l in ols]
        assert b"".join(filter(None, out)) == data
```

#### 30. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L41) (Line 41)
- **Target Call:** `seek_delimiter` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_seek_delimiter_endline`
- **Arguments:** `f, b'\n', 5`
- **Keywords:** `{}`

```python
    # if at zero, stay at zero
    seek_delimiter(f, b"\n", 5)
    assert f.tell() == 0
```

#### 31. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L47) (Line 47)
- **Target Call:** `seek_delimiter` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_seek_delimiter_endline`
- **Arguments:** `f, b'\n'`
- **Keywords:** `{'blocksize': 'bs'}`

```python
        f.seek(1)
        seek_delimiter(f, b"\n", blocksize=bs)
        assert f.tell() == 4
```

#### 32. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L54) (Line 54)
- **Target Call:** `seek_delimiter` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_seek_delimiter_endline`
- **Arguments:** `f, b'abc'`
- **Keywords:** `{'blocksize': 'bs'}`

```python
        f.seek(1)
        seek_delimiter(f, b"abc", blocksize=bs)
        assert f.tell() == 6
```

#### 33. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L60) (Line 60)
- **Target Call:** `seek_delimiter` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_seek_delimiter_endline`
- **Arguments:** `f, b'\n', 5`
- **Keywords:** `{}`

```python
    f.seek(5)
    seek_delimiter(f, b"\n", 5)
    assert f.tell() == 7
```

#### 34. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L65) (Line 65)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'/mnt/datasets/test.csv'`
- **Keywords:** `{}`

```python
def test_infer_storage_options():
    so = infer_storage_options("/mnt/datasets/test.csv")
    assert so.pop("protocol") == "file"
```

#### 35. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L70) (Line 70)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'./test.csv'`
- **Keywords:** `{}`

```python

    assert infer_storage_options("./test.csv")["path"] == "./test.csv"
    assert infer_storage_options("../test.csv")["path"] == "../test.csv"
```

#### 36. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L71) (Line 71)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'../test.csv'`
- **Keywords:** `{}`

```python
    assert infer_storage_options("./test.csv")["path"] == "./test.csv"
    assert infer_storage_options("../test.csv")["path"] == "../test.csv"

```

#### 37. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L73) (Line 73)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'C:\\test.csv'`
- **Keywords:** `{}`

```python

    so = infer_storage_options("C:\\test.csv")
    assert so.pop("protocol") == "file"
```

#### 38. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L78) (Line 78)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'d:\\test.csv'`
- **Keywords:** `{}`

```python

    assert infer_storage_options("d:\\test.csv")["path"] == "d:\\test.csv"
    assert infer_storage_options("\\test.csv")["path"] == "\\test.csv"
```

#### 39. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L79) (Line 79)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'\\test.csv'`
- **Keywords:** `{}`

```python
    assert infer_storage_options("d:\\test.csv")["path"] == "d:\\test.csv"
    assert infer_storage_options("\\test.csv")["path"] == "\\test.csv"
    assert infer_storage_options(".\\test.csv")["path"] == ".\\test.csv"
```

#### 40. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L80) (Line 80)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'.\\test.csv'`
- **Keywords:** `{}`

```python
    assert infer_storage_options("\\test.csv")["path"] == "\\test.csv"
    assert infer_storage_options(".\\test.csv")["path"] == ".\\test.csv"
    assert infer_storage_options("test.csv")["path"] == "test.csv"
```

#### 41. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L81) (Line 81)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'test.csv'`
- **Keywords:** `{}`

```python
    assert infer_storage_options(".\\test.csv")["path"] == ".\\test.csv"
    assert infer_storage_options("test.csv")["path"] == "test.csv"

```

#### 42. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L83) (Line 83)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'hdfs://username:pwd@Node:123/mnt/datasets/test.csv?q=1#fragm'`
- **Keywords:** `{'inherit_storage_options': "{'extra': 'value'}"}`

```python

    so = infer_storage_options(
        "hdfs://username:pwd@Node:123/mnt/datasets/test.csv?q=1#fragm",
        inherit_storage_options={"extra": "value"},
    )
    assert so.pop("protocol") == "hdfs"
```

#### 43. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L98) (Line 98)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'hdfs://User-name@Node-name.com/mnt/datasets/test.csv'`
- **Keywords:** `{}`

```python

    so = infer_storage_options("hdfs://User-name@Node-name.com/mnt/datasets/test.csv")
    assert so.pop("username") == "User-name"
```

#### 44. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L103) (Line 103)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
    u = "http://127.0.0.1:8080/test.csv"
    assert infer_storage_options(u) == {"protocol": "http", "path": u}

```

#### 45. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L110) (Line 110)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `f'{protocol}://Bucket-name.com/test.csv'`
- **Keywords:** `{}`

```python
    for protocol in ["s3", "gcs", "gs"]:
        options = infer_storage_options(f"{protocol}://Bucket-name.com/test.csv")
        assert options["path"] == "Bucket-name.com/test.csv"
```

#### 46. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L114) (Line 114)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'file:///bucket/file.csv', {'path': 'collide'}`
- **Keywords:** `{}`

```python
    with pytest.raises(KeyError):
        infer_storage_options("file:///bucket/file.csv", {"path": "collide"})
    with pytest.raises(KeyError):
```

#### 47. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L116) (Line 116)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options`
- **Arguments:** `'hdfs:///bucket/file.csv', {'protocol': 'collide'}`
- **Keywords:** `{}`

```python
    with pytest.raises(KeyError):
        infer_storage_options("hdfs:///bucket/file.csv", {"protocol": "collide"})

```

#### 48. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L131) (Line 131)
- **Target Call:** `infer_storage_options` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_infer_storage_options_c`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
def test_infer_storage_options_c(urlpath, expected_path):
    so = infer_storage_options(urlpath)
    assert so["protocol"] == "file"
```

#### 49. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L141) (Line 141)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_stringify_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = pathlib.Path(test_filepath)
    assert stringify_path(path) == test_filepath

```

#### 50. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L154) (Line 154)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_stringify_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = CustomFSPath(test_filepath)
    assert stringify_path(path) == test_filepath

```

#### 51. [dask/bytes/tests/test_bytes_utils.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_bytes_utils.py#L158) (Line 158)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_stringify_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = (1, 2, 3)
    assert stringify_path(path) is path
```

#### 52. [dask/bytes/tests/test_compression.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_compression.py#L11) (Line 11)
- **Target Call:** `compr.items` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_files`
- **Arguments:** ``
- **Keywords:** `{}`

```python

@pytest.mark.parametrize("fmt,File", compr.items())
def test_files(fmt, File):
```

#### 53. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L58) (Line 58)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_simple`
- **Arguments:** `root + fn`
- **Keywords:** `{}`

```python
    fn = files[0]
    f = open_files(root + fn)[0]
    with f as f:
```

#### 54. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L68) (Line 68)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_loc`
- **Arguments:** `root + fn`
- **Keywords:** `{}`

```python
    fn = files[0]
    f = open_files(root + fn)[0]
    with open(os.path.join(dir_server, fn), "rb") as expected:
```

#### 55. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L87) (Line 87)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fetch_range_with_headers`
- **Arguments:** `root + fn`
- **Keywords:** `{'headers': 'headers'}`

```python
    headers = {"Date": "Wed, 21 Oct 2015 07:28:00 GMT"}
    f = open_files(root + fn, headers=headers)[0]
    with f as f:
```

#### 56. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L98) (Line 98)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ops`
- **Arguments:** `root + fn`
- **Keywords:** `{}`

```python
    fn = files[0]
    f = open_files(root + fn)[0]
    with open(os.path.join(dir_server, fn), "rb") as expected:
```

#### 57. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L114) (Line 114)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ops_blocksize`
- **Arguments:** `root + fn`
- **Keywords:** `{'block_size': '2'}`

```python
    fn = files[0]
    f = open_files(root + fn, block_size=2)[0]
    with open(os.path.join(dir_server, fn), "rb") as expected:
```

#### 58. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L126) (Line 126)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ops_blocksize`
- **Arguments:** `root + fn`
- **Keywords:** `{'block_size': '2'}`

```python
        fn = files[1]
        f = open_files(root + fn, block_size=2)[0]
        with f as f:
```

#### 59. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L138) (Line 138)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_errors`
- **Arguments:** `'http://localhost:8999/doesnotexist'`
- **Keywords:** `{}`

```python
def test_errors(dir_server):
    f = open_files("http://localhost:8999/doesnotexist")[0]
    with pytest.raises(errs):
```

#### 60. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L142) (Line 142)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_errors`
- **Arguments:** `'http://nohost/'`
- **Keywords:** `{}`

```python
            f.read()
    f = open_files("http://nohost/")[0]

```

#### 61. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L151) (Line 151)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_errors`
- **Arguments:** `root + fn`
- **Keywords:** `{'mode': "'wb'"}`

```python
    fn = files[0]
    f = open_files(root + fn, mode="wb")[0]
    with pytest.raises(NotImplementedError):
```

#### 62. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L155) (Line 155)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_errors`
- **Arguments:** `root + fn`
- **Keywords:** `{}`

```python
            pass
    f = open_files(root + fn)[0]
    with f as f:
```

#### 63. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L163) (Line 163)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_files`
- **Arguments:** `[f'{root}{f}' for f in files]`
- **Keywords:** `{}`

```python
    root = "http://localhost:8999/"
    fs = open_files([f"{root}{f}" for f in files])
    for f, f2 in zip(fs, files):
```

#### 64. [dask/bytes/tests/test_http.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_http.py#L172) (Line 172)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_glob`
- **Arguments:** `f'{root}*'`
- **Keywords:** `{}`

```python
    root = "http://localhost:8999/"
    fs = open_files(f"{root}*")
    assert fs[0].path == f"{root}a"
```

#### 65. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L225) (Line 225)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files`
- **Arguments:** `'.test.accounts.*'`
- **Keywords:** `{}`

```python
    with filetexts(files, mode="b"):
        myfiles = open_files(".test.accounts.*")
        assert len(myfiles) == len(files)
```

#### 66. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L236) (Line 236)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files_text_mode`
- **Arguments:** `'.test.accounts.*'`
- **Keywords:** `{'mode': "'rt'", 'encoding': 'encoding'}`

```python
    with filetexts(files, mode="b"):
        myfiles = open_files(".test.accounts.*", mode="rt", encoding=encoding)
        assert len(myfiles) == len(files)
```

#### 67. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L252) (Line 252)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files_compression`
- **Arguments:** `'.test.accounts.*'`
- **Keywords:** `{'mode': 'mode', 'compression': 'fmt'}`

```python
    with filetexts(files2, mode="b"):
        myfiles = open_files(".test.accounts.*", mode=mode, compression=fmt)
        data = []
```

#### 68. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L300) (Line 300)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files_write`
- **Arguments:** `tmpdir`
- **Keywords:** `{'num': '2', 'mode': "'wb'", 'compression': 'compression'}`

```python
    tmpdir = str(tmpdir)
    files = open_files(tmpdir, num=2, mode="wb", compression=compression)
    assert len(files) == 2
```

#### 69. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L318) (Line 318)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pickability_of_lazy_files`
- **Arguments:** `'.test.accounts.*'`
- **Keywords:** `{}`

```python
    with filetexts(files, mode="b"):
        myfiles = open_files(".test.accounts.*")
        myfiles2 = cloudpickle.loads(cloudpickle.dumps(myfiles))
```

#### 70. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L333) (Line 333)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_py2_local_bytes`
- **Arguments:** `fn`
- **Keywords:** `{'compression': "'gzip'", 'mode': "'rt'"}`

```python

    files = open_files(fn, compression="gzip", mode="rt")

```

#### 71. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L345) (Line 345)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_abs_paths`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        f.write("hi")
    out = LocalFileSystem().glob("*")
    assert len(out) == 1
```

#### 72. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L350) (Line 350)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_abs_paths`
- **Arguments:** ``
- **Keywords:** `{}`

```python

    fs = LocalFileSystem()
    os.chdir(here)
```

#### 73. [dask/bytes/tests/test_local.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_local.py#L352) (Line 352)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_abs_paths`
- **Arguments:** `out[0], 'r'`
- **Keywords:** `{}`

```python
    os.chdir(here)
    with fs.open(out[0], "r") as f:
        res = f.read()
```

#### 74. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L135) (Line 135)
- **Target Call:** `fs.invalidate_cache` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `s3_context`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    s3fs.S3FileSystem.clear_instance_cache()
    fs.invalidate_cache()
    try:
```

#### 75. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L139) (Line 139)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `s3_context`
- **Arguments:** `bucket`
- **Keywords:** `{'recursive': 'True'}`

```python
    finally:
        fs.rm(bucket, recursive=True)

```

#### 76. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L247) (Line 247)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files_write`
- **Arguments:** `paths`
- **Keywords:** `{'mode': "'wb'"}`

```python
    paths = [f"s3://{test_bucket_name}/more/{f}" for f in files]
    fils = open_files(paths, mode="wb", **s3so)
    for fil, data in zip(fils, files.values()):
```

#### 77. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L415) (Line 415)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_files`
- **Arguments:** `f's3://{test_bucket_name}/test/accounts.*'`
- **Keywords:** `{'mode': 'mode'}`

```python
def test_open_files(s3, mode, s3so):
    myfiles = open_files(f"s3://{test_bucket_name}/test/accounts.*", mode=mode, **s3so)
    assert len(myfiles) == len(files)
```

#### 78. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L511) (Line 511)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_parquet`
- **Arguments:** `url`
- **Keywords:** `{'storage_options': 's3so'}`

```python
    # Check "open_file_func"
    fs = get_fs_token_paths(url, storage_options=s3so)[0]

```

#### 79. [dask/bytes/tests/test_s3.py](https://github.com/dask/dask/blob/main/dask/bytes/tests/test_s3.py#L515) (Line 515)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_open`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
        assert check
        return fs.open(*args, **kwargs)

```

#### 80. [dask/dataframe/dask_expr/_collection.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5359) (Line 5359)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if not isinstance(path, str):
        path = stringify_path(path)

```

#### 81. [dask/dataframe/dask_expr/_collection.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5374) (Line 5374)
- **Target Call:** `filesystem.lower` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_parquet`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        or isinstance(filesystem, str)
        and filesystem.lower() in ("arrow", "pyarrow")
    ):
```

#### 82. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L140) (Line 140)
- **Target Call:** `fs.equals` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FragmentWrapper.pack`
- **Arguments:** `self._fragment.filesystem`
- **Keywords:** `{}`

```python
            fs = self._filesystem or self._fragment.filesystem
            assert fs.equals(self._fragment.filesystem)
            if self._filesystem_pickle_cache[0] != id(fs):
```

#### 83. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L489) (Line 489)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if hasattr(path, "name"):
        path = stringify_path(path)

```

#### 84. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if fs.exists(path) and fs.isdir(path):
            # Check for any previous parquet ops reading from a file in the
```

#### 85. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if fs.exists(path) and fs.isdir(path):
            # Check for any previous parquet ops reading from a file in the
```

#### 86. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L520) (Line 520)
- **Target Call:** `fs.expand_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `'.'`
- **Keywords:** `{}`

```python
            if _is_local_fs(fs):
                working_dir = fs.expand_path(".")[0]
                if path.rstrip("/") == working_dir.rstrip("/"):
```

#### 87. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L527) (Line 527)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
            # It's safe to clear the output directory
            fs.rm(path, recursive=True)

```

#### 88. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L666) (Line 666)
- **Target Call:** `fs.invalidate_cache` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # that reading files that were just written succeeds.
    fs.invalidate_cache(path)

```

#### 89. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1023) (Line 1023)
- **Target Call:** `self.fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ReadParquetPyarrowFS._dataset_info`
- **Arguments:** `dataset_selector`
- **Keywords:** `{}`

```python
                        finfo
                        for finfo in self.fs.get_file_info(dataset_selector)
                        if finfo.type == pa.fs.FileType.File
```

#### 90. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1028) (Line 1028)
- **Target Call:** `self.fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ReadParquetPyarrowFS._dataset_info`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        except (NotADirectoryError, FileNotFoundError):
            all_files = [self.fs.get_file_info(path) for path in path_normalized]
        # TODO: At this point we could verify if we're dealing with a very
```

#### 91. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1394) (Line 1394)
- **Target Call:** `fs.checksum` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ReadParquetFSSpec._dataset_info`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            # _collect_dataset_info
            checksum.append(fs.checksum(file))
        dataset_info["checksum"] = tokenize(checksum)
```

#### 92. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1781) (Line 1781)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_read_partition_stats`
- **Arguments:** `path`
- **Keywords:** `{'default_cache': "'none'"}`

```python
            row_groups = None if piece[1] == [None] else piece[1]
            with fs.open(path, default_cache="none") as f:
                md = pq.ParquetFile(f).metadata
```

#### 93. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L115) (Line 115)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_pyarrow_filesystem(parquet_file):
    filesystem = fs.LocalFileSystem()

```

#### 94. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L126) (Line 126)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem_dtype_backend`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_pyarrow_filesystem_dtype_backend(parquet_file, dtype_backend):
    filesystem = fs.LocalFileSystem()

```

#### 95. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L139) (Line 139)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem_types_mapper`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    # anywhere
    filesystem = fs.LocalFileSystem()

```

#### 96. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L151) (Line 151)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem_serialize`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_pyarrow_filesystem_serialize(parquet_file):
    filesystem = fs.LocalFileSystem()

```

#### 97. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L167) (Line 167)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem_filters`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_pyarrow_filesystem_filters(parquet_file):
    filesystem = fs.LocalFileSystem()

```

#### 98. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L182) (Line 182)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_pyarrow_filesystem_list_of_files`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_pyarrow_filesystem_list_of_files(parquet_file, second_parquet_file):
    filesystem = fs.LocalFileSystem()

```

#### 99. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L191) (Line 191)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_partition_pruning`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    with dask.config.set({"dataframe.parquet.minimum-partition-size": 1}):
        filesystem = fs.LocalFileSystem()
        df = from_pandas(
```

#### 100. [dask/dataframe/dask_expr/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/tests/test_parquet.py#L309) (Line 309)
- **Target Call:** `fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_aggregate_rg_stats_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def test_aggregate_rg_stats_to_file(tmpdir):
    filesystem = fs.LocalFileSystem()
    fn = str(tmpdir)
```

#### 101. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L488) (Line 488)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_pandas`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        # Translate the input urlpath to a simple path list
        paths = get_fs_token_paths(urlpath, mode="rb", storage_options=storage_options)[
            2
```

#### 102. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L497) (Line 497)
- **Target Call:** `infer_compression` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_pandas`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        # Infer compression from first path
        compression = infer_compression(paths[0])

```

#### 103. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L911) (Line 911)
- **Target Call:** `open_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'mode'}`

```python
    if single_file:
        first_file = open_file(filename, mode=mode, **file_options)
        value = to_csv_chunk(dfs[0], first_file, **kwargs)
```

#### 104. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L915) (Line 915)
- **Target Call:** `open_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'append_mode'}`

```python
        append_mode = append_mode.replace("w", "").replace("x", "")
        append_file = open_file(filename, mode=append_mode, **file_options)
        kwargs["header"] = False
```

#### 105. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L922) (Line 922)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'mode', 'name_function': 'name_function', 'num': 'df.npartitions'}`

```python
    else:
        files = open_files(
            filename,
            mode=mode,
            name_function=name_function,
            num=df.npartitions,
            **file_options,
        )
        values = [to_csv_chunk(dfs[0], files[0], **kwargs)]
```

#### 106. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L147) (Line 147)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_hdf`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

    path = stringify_path(path)

```

#### 107. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L176) (Line 176)
- **Target Call:** `build_name_function` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_hdf`
- **Arguments:** `df.npartitions - 1`
- **Keywords:** `{}`

```python
    if name_function is None:
        name_function = build_name_function(df.npartitions - 1)

```

#### 108. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L381) (Line 381)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_hdf`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    # Convert path-like objects to a string
    pattern = stringify_path(pattern)

```

#### 109. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L78) (Line 78)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_json`
- **Arguments:** `url_path, 'wt'`
- **Keywords:** `{'encoding': 'encoding', 'errors': 'errors', 'name_function': 'name_function', 'num': 'df.npartitions', 'compression': 'compression'}`

```python
    kwargs["lines"] = lines and orient == "records"
    outfiles = open_files(
        url_path,
        "wt",
        encoding=encoding,
        errors=errors,
        name_function=name_function,
        num=df.npartitions,
        compression=compression,
        **(storage_options or {}),
    )
    parts = [
```

#### 110. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L268) (Line 268)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_json`
- **Arguments:** `url_path, 'rt'`
- **Keywords:** `{'encoding': 'encoding', 'errors': 'errors', 'compression': 'compression'}`

```python
    else:
        files = open_files(
            url_path,
            "rt",
            encoding=encoding,
            errors=errors,
            compression=compression,
            **storage_options,
        )
        path_dtype = pd.CategoricalDtype(path_converter(f.path) for f in files)
```

#### 111. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L23) (Line 23)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        # TODO: Handle hive-partitioned data
        if len(paths) == 1 and not fs.isfile(paths[0]):
            paths = fs.find(paths[0])
```

#### 112. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L24) (Line 24)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        if len(paths) == 1 and not fs.isfile(paths[0]):
            paths = fs.find(paths[0])

```

#### 113. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L39) (Line 39)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
            for path in paths:
                with fs.open(path, "rb") as f:
                    o = orc.ORCFile(f)
```

#### 114. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L60) (Line 60)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0], 'rb'`
- **Keywords:** `{}`

```python
                if schema is None:
                    with fs.open(paths[0], "rb") as f:
                        o = orc.ORCFile(f)
```

#### 115. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L111) (Line 111)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowORCEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
        table = pa.Table.from_pandas(df)
        with fs.open(fs.sep.join([path, filename]), "wb") as f:
            orc.write_table(table, f)
```

#### 116. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L122) (Line 122)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_read_orc_stripes`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    batches = []
    with fs.open(path, "rb") as f:
        o = orc.ORCFile(f)
```

#### 117. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L81) (Line 81)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `read_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
    storage_options = storage_options or {}
    fs, fs_token, paths = get_fs_token_paths(
        path, mode="rb", storage_options=storage_options
    )

```

#### 118. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L174) (Line 174)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if hasattr(path, "name"):
        path = stringify_path(path)
    fs, _, _ = get_fs_token_paths(path, mode="wb", storage_options=storage_options)
```

#### 119. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L175) (Line 175)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wb'", 'storage_options': 'storage_options'}`

```python
        path = stringify_path(path)
    fs, _, _ = get_fs_token_paths(path, mode="wb", storage_options=storage_options)
    # Trim any protocol information from the path before forwarding
```

#### 120. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L177) (Line 177)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # Trim any protocol information from the path before forwarding
    path = fs._strip_protocol(path)

```

#### 121. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L184) (Line 184)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    # Use df.npartitions to define file-name list
    fs.mkdirs(path, exist_ok=True)
    filenames = [f"part.{i}.orc" for i in range(df.npartitions)]
```

#### 122. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L112) (Line 112)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_write_partitioned`
- **Arguments:** `root_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    """
    fs.mkdirs(root_path, exist_ok=True)

```

#### 123. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L148) (Line 148)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_write_partitioned`
- **Arguments:** `prefix`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        prefix = fs.sep.join([root_path, subdir])
        fs.mkdirs(prefix, exist_ok=True)
        full_path = fs.sep.join([prefix, filename])
```

#### 124. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L150) (Line 150)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_write_partitioned`
- **Arguments:** `full_path, 'wb'`
- **Keywords:** `{}`

```python
        full_path = fs.sep.join([prefix, filename])
        with fs.open(full_path, "wb") as f:
            pq.write_table(
```

#### 125. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L470) (Line 470)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                    raise ValueError("empty urlpath sequence")
                urlpath = [stringify_path(u) for u in urlpath]
            else:
```

#### 126. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L472) (Line 472)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
            else:
                urlpath = [stringify_path(urlpath)]

```

#### 127. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L483) (Line 483)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `fs`
- **Keywords:** `{}`

```python

            fsspec_fs = ArrowFSWrapper(fs)
            if urlpath[0].startswith("C:") and isinstance(fs, pa_fs.LocalFileSystem):
```

#### 128. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L489) (Line 489)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python

                fs_strip = LocalFileSystem()
            else:
```

#### 129. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L492) (Line 492)
- **Target Call:** `expand_paths_if_needed` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fsspec_fs, None`
- **Keywords:** `{}`

```python
                fs_strip = fsspec_fs
            paths = expand_paths_if_needed(urlpath, "rb", 1, fsspec_fs, None)
            return (
```

#### 130. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L670) (Line 670)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        # Check that target directory exists
        fs.mkdirs(path, exist_ok=True)
        if append and division_info is None:
```

#### 131. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L684) (Line 684)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `fs.sep.join([path, '_metadata'])`
- **Keywords:** `{'mode': "'rb'"}`

```python
                try:
                    with fs.open(fs.sep.join([path, "_metadata"]), mode="rb") as fil:
                        full_metadata = pq.read_metadata(fil)
```

#### 132. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L690) (Line 690)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `sorted(ds.files, key=natural_sort_key)[-1]`
- **Keywords:** `{'mode': "'rb'"}`

```python
                    try:
                        with fs.open(
                            sorted(ds.files, key=natural_sort_key)[-1], mode="rb"
                        ) as fil:
                            tail_metadata = pq.read_metadata(fil)
```

#### 133. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L851) (Line 851)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
            md_list = []
            with fs.open(fs.sep.join([path, filename]), "wb") as fil:
                pq.write_table(
```

#### 134. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L882) (Line 882)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `common_metadata_path, 'wb'`
- **Keywords:** `{}`

```python
                kwargs_meta = {k: v for k, v in kwargs.items() if k in keywords}
                with fs.open(common_metadata_path, "wb") as fil:
                    pq.write_metadata(schema, fil, **kwargs_meta)
```

#### 135. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L895) (Line 895)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
                _append_row_groups(_meta, parts[i][0]["meta"])
            with fs.open(metadata_path, "wb") as fil:
                _meta.write_metadata_file(fil)
```

#### 136. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L940) (Line 940)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        has_metadata_file = False
        if len(paths) == 1 and fs.isdir(paths[0]):
            # Use _analyze_paths to avoid relative-path
```

#### 137. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L947) (Line 947)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `meta_path`
- **Keywords:** `{}`

```python
            meta_path = fs.sep.join([paths, "_metadata"])
            if not ignore_metadata_file and fs.exists(meta_path):
                # Use _metadata file
```

#### 138. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L961) (Line 961)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths`
- **Keywords:** `{}`

```python
                    path
                    for path in fs.find(paths)
                    if path.endswith(parquet_file_extension)
```

#### 139. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1820) (Line 1820)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.collect_file_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    def collect_file_metadata(cls, path, fs, file_path):
        with fs.open(path, "rb") as f:
            meta = pq.ParquetFile(f).metadata
```

#### 140. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1836) (Line 1836)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowDatasetEngine.aggregate_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
            metadata_path = fs.sep.join([out_path, "_metadata"])
            with fs.open(metadata_path, "wb") as fil:
                if not meta:
```

#### 141. [dask/dataframe/io/parquet/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/core.py#L289) (Line 289)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `create_metadata_file`
- **Arguments:** `paths`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        # already defined. The prefixes may already be stripped.
        fs, _, paths = get_fs_token_paths(
            paths, mode="rb", storage_options=storage_options
        )
    ap_kwargs = {"root": root_dir} if root_dir else {}
```

#### 142. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L72) (Line 72)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
            # Use fsspec to infer a filesystem by default
            fs, _, paths = get_fs_token_paths(
                urlpath, mode="rb", storage_options=storage_options
            )
            return fs, paths, dataset_options, open_file_options
```

#### 143. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L95) (Line 95)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                    raise ValueError("empty urlpath sequence")
                urlpath = [stringify_path(u) for u in urlpath]
            else:
```

#### 144. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L97) (Line 97)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
            else:
                urlpath = [stringify_path(urlpath)]

```

#### 145. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L99) (Line 99)
- **Target Call:** `expand_paths_if_needed` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fs, None`
- **Keywords:** `{}`

```python

            paths = expand_paths_if_needed(urlpath, "rb", 1, fs, None)
            return (
```

#### 146. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L102) (Line 102)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                fs,
                [fs._strip_protocol(u) for u in paths],
                dataset_options,
```

#### 147. [dask/dataframe/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/tests/test_parquet.py#L1584) (Line 1584)
- **Target Call:** `LocalFileSystem._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_to_parquet_calls_invalidate_cache`
- **Arguments:** `str(tmpdir)`
- **Keywords:** `{}`

```python
    ddf.to_parquet(tmpdir, compute=compute)
    path = LocalFileSystem._strip_protocol(str(tmpdir))
    assert invalidate_cache.called
```

#### 148. [dask/dataframe/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/tests/test_parquet.py#L3770) (Line 3770)
- **Target Call:** `get_filesystem_class` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_to_parquet_filesystem_option`
- **Arguments:** `'memory'`
- **Keywords:** `{}`

```python
    df = pd.DataFrame({"a": range(10)})
    fs = get_filesystem_class("memory")(use_instance_cache=False)
    df.to_parquet(key1, filesystem=fs)
```

#### 149. [dask/dataframe/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/tests/test_parquet.py#L3782) (Line 3782)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_to_parquet_filesystem_option`
- **Arguments:** `key2`
- **Keywords:** `{'detail': 'False'}`

```python
    # make sure we wrote a key to memory fs
    assert len(fs.ls(key2, detail=False)) == 1

```

#### 150. [dask/dataframe/io/tests/test_parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/tests/test_parquet.py#L3786) (Line 3786)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_to_parquet_filesystem_option`
- **Arguments:** `key2`
- **Keywords:** `{'detail': 'False'}`

```python
    ddf.to_parquet(key2, append=True, filesystem=fs)
    assert len(fs.ls(key2, detail=False)) == 2, "should have two parts"

```

#### 151. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L210) (Line 210)
- **Target Call:** `fsspec_parquet.open_parquet_file` | **Cache_Type:** `parts`
- **Context:** `_open_input_files`
- **Arguments:** `path`
- **Keywords:** `{'fs': 'fs', 'row_groups': 'rgs'}`

```python
            _set_context(
                fsspec_parquet.open_parquet_file(
                    path,
                    fs=fs,
                    row_groups=rgs,
                    **kwargs,
                ),
                context_stack,
```

#### 152. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L221) (Line 221)
- **Target Call:** `fs.open` | **Cache_Type:** `parts`
- **Context:** `_open_input_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    elif fs is not None:
        return [_set_context(fs.open(path, **kwargs), context_stack) for path in paths]
    return [_set_context(open(path, **kwargs), context_stack) for path in paths]
```

### Intake ([intake/intake](https://github.com/intake/intake))
- **Usages Found:** `97` in `19` files.

#### 1. [intake/catalog/base.py](https://github.com/intake/intake/blob/master/intake/catalog/base.py#L341) (Line 341)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Catalog.save`
- **Arguments:** `[url]`
- **Keywords:** `{'mode': "'wt'"}`

```python

        with open_files([url], **(storage_options or {}), mode="wt")[0] as f:
            f.write(self.serialize())
```

#### 2. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L575) (Line 575)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if "://" in path:
        protocol, _ = split_protocol(path)
        out = get_filesystem_class(protocol)._parent(path)
```

#### 3. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L576) (Line 576)
- **Target Call:** `get_filesystem_class` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get_dir`
- **Arguments:** `protocol`
- **Keywords:** `{}`

```python
        protocol, _ = split_protocol(path)
        out = get_filesystem_class(protocol)._parent(path)
        if "://" not in out:
```

#### 4. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L639) (Line 639)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
            elif self.filesystem is None:
                file_open = open_files(self.path, mode="rb", **options)
                assert len(file_open) == 1
```

#### 5. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L644) (Line 644)
- **Target Call:** `self.filesystem.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
            else:
                file_open = self.filesystem.open(self.path, mode="rb")
            self._dir = get_dir(self.path)
```

#### 6. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L690) (Line 690)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[self.path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            options = self.storage_options or {}
            file_open = open_files([self.path], mode="wt", **options)
        else:
```

#### 7. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L693) (Line 693)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            options = storage_options or {}
            file_open = open_files([path], mode="wt", **options)
        assert len(file_open) == 1
```

#### 8. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L805) (Line 805)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `p`
- **Keywords:** `{'mode': "'rb'"}`

```python
        if isinstance(self.path, (list, tuple)):
            files = sum([open_files(p, mode="rb", **options) for p in self.path], [])
            self.name = self.name or "%i files" % len(files)
```

#### 9. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L812) (Line 812)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
                self.path = self.path + "/*"
            files = open_files(self.path, mode="rb", **options)
            self.path = make_path_posix(self.path)
```

#### 10. [intake/catalog/tests/test_local.py](https://github.com/intake/intake/blob/master/intake/catalog/tests/test_local.py#L26) (Line 26)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `abspath`
- **Arguments:** `os.path.join(os.path.dirname(__file__), filename)`
- **Keywords:** `{}`

```python
def abspath(filename):
    return make_path_posix(os.path.join(os.path.dirname(__file__), filename))

```

#### 11. [intake/catalog/tests/test_local.py](https://github.com/intake/intake/blob/master/intake/catalog/tests/test_local.py#L783) (Line 783)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_integration`
- **Arguments:** `'memory'`
- **Keywords:** `{}`

```python

    mem = fsspec.filesystem("memory")
    with mem.open("cat.yaml", "wt") as f:
```

#### 12. [intake/catalog/tests/test_local.py](https://github.com/intake/intake/blob/master/intake/catalog/tests/test_local.py#L784) (Line 784)
- **Target Call:** `mem.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_integration`
- **Arguments:** `'cat.yaml', 'wt'`
- **Keywords:** `{}`

```python
    mem = fsspec.filesystem("memory")
    with mem.open("cat.yaml", "wt") as f:
        f.write(
```

#### 13. [intake/catalog/tests/test_local.py](https://github.com/intake/intake/blob/master/intake/catalog/tests/test_local.py#L805) (Line 805)
- **Target Call:** `mem.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_integration`
- **Arguments:** `'/file.csv', 'wt'`
- **Keywords:** `{}`

```python
        )
    with mem.open("/file.csv", "wt") as f:
        f.write("a,b\n0,1")
```

#### 14. [intake/catalog/zarr.py](https://github.com/intake/intake/blob/master/intake/catalog/zarr.py#L63) (Line 63)
- **Target Call:** `get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ZarrGroupCatalog._load`
- **Arguments:** `self._urlpath`
- **Keywords:** `{}`

```python

                    store = get_mapper(self._urlpath, **self._storage_options)
                else:
```

#### 15. [intake/config.py](https://github.com/intake/intake/blob/master/intake/config.py#L26) (Line 26)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `global`
- **Arguments:** `os.getenv('INTAKE_CONF_DIR', os.path.join(expanduser('~'), '.intake'))`
- **Keywords:** `{}`

```python

confdir = make_path_posix(os.getenv("INTAKE_CONF_DIR", os.path.join(expanduser("~"), ".intake")))

```

#### 16. [intake/config.py](https://github.com/intake/intake/blob/master/intake/config.py#L44) (Line 44)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `cfile`
- **Arguments:** `os.getenv('INTAKE_CONF_FILE', posixpath.join(confdir, 'conf.yaml'))`
- **Keywords:** `{}`

```python
def cfile():
    return make_path_posix(os.getenv("INTAKE_CONF_FILE", posixpath.join(confdir, "conf.yaml")))

```

#### 17. [intake/conftest.py](https://github.com/intake/intake/blob/master/intake/conftest.py#L42) (Line 42)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `tmp_config_path`
- **Arguments:** `os.path.join(tmp_path, 'test_config.yml')`
- **Keywords:** `{}`

```python
    original = os.getenv(key)
    temp_config_path = make_path_posix(os.path.join(tmp_path, "test_config.yml"))
    os.environ[key] = temp_config_path
```

#### 18. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L55) (Line 55)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileSelector.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self.done_callback = done_callback
        self.fs = fsspec.filesystem("file")
        super().__init__(**kwargs)
```

#### 19. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L94) (Line 94)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileSelector.go_clicked`
- **Arguments:** `self.protocol.value`
- **Keywords:** `{}`

```python
    def go_clicked(self, *_):
        self.fs = fsspec.filesystem(
            self.protocol.value, **ast.literal_eval(self.storage_options.value)
        )
        self.make_options()
```

#### 20. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L109) (Line 109)
- **Target Call:** `self.fs._parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileSelector.move_up`
- **Arguments:** `self.path_text.value`
- **Keywords:** `{}`

```python
    def move_up(self, arg=None):
        self.path_text.value = self.fs._parent(self.path_text.value)
        self.make_options()
```

#### 21. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L121) (Line 121)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileSelector.make_options`
- **Arguments:** `self.path, True`
- **Keywords:** `{}`

```python
        try:
            for f in self.fs.ls(self.path, True):
                bn = os.path.basename(f["name"].rstrip("/"))
```

#### 22. [intake/readers/catalogs.py](https://github.com/intake/intake/blob/master/intake/readers/catalogs.py#L376) (Line 376)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `STACIndex._read`
- **Arguments:** `'https://stacindex.org/api/catalogs'`
- **Keywords:** `{}`

```python
    def _read(self, *args, **kwargs):
        with fsspec.open("https://stacindex.org/api/catalogs") as f:
            data = json.load(f)
```

#### 23. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1927) (Line 1927)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `recommend`
- **Arguments:** `url2`
- **Keywords:** `{'refresh': 'True'}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
            mime = mime or fs.info(url2, refresh=True).get("ContentType", None)
        except (IOError, TypeError, AttributeError, ValueError):
```

#### 24. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1932) (Line 1932)
- **Target Call:** `fs.cat_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `recommend`
- **Arguments:** `url2[0] if isinstance(url2, list) else url2`
- **Keywords:** `{'end': '2 ** 20'}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
            head = fs.cat_file(url2[0] if isinstance(url2, list) else url2, end=2**20)
        except (IOError, IndexError, ValueError):
```

#### 25. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1989) (Line 1989)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    if url:
        if fs is not None and fs.isdir(url):
            try:
```

#### 26. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1991) (Line 1991)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{'detail': 'False'}`

```python
            try:
                allfiles = fs.ls(url, detail=False)
            except IOError:
```

#### 27. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L420) (Line 420)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Catalog.to_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wt'"}`

```python
        # TODO: remove ['CATALOG_DIR', 'CATALOG_PATH', 'STORAGE_OPTIONS'] UPs?
        with fsspec.open(path, mode="wt", **storage_options) as stream:
            yaml.safe_dump(self.to_dict(), stream)
```

#### 28. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L432) (Line 432)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        storage_options = kwargs.pop("storage_options", kwargs)
        of = fsspec.open(path, **storage_options)
        with of as stream:
```

#### 29. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L436) (Line 436)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `of.fs._parent(path)`
- **Keywords:** `{}`

```python
        cat.user_parameters["CATALOG_PATH"] = path
        cat.user_parameters["CATALOG_DIR"] = of.fs.unstrip_protocol(of.fs._parent(path))
        cat.user_parameters["STORAGE_OPTIONS"] = storage_options
```

#### 30. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L436) (Line 436)
- **Target Call:** `self.fs._parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        cat.user_parameters["CATALOG_PATH"] = path
        cat.user_parameters["CATALOG_DIR"] = of.fs.unstrip_protocol(of.fs._parent(path))
        cat.user_parameters["STORAGE_OPTIONS"] = storage_options
```

#### 31. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L681) (Line 681)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if any(c in path for c in ("*", "?", "[")):
                expanded = fs.glob(path)
                if not expanded:
```

#### 32. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L684) (Line 684)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_to_files`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
                    return []
                return [fs.info(p) for p in expanded]

```

#### 33. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L688) (Line 688)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            try:
                entry = fs.info(path)
            except FileNotFoundError:
```

#### 34. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L699) (Line 699)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_to_files`
- **Arguments:** `path.rstrip('/')`
- **Keywords:** `{'detail': 'True'}`

```python
                # List only immediate children that are files
                children = fs.ls(path.rstrip("/"), detail=True)
                files = [
```

#### 35. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L125) (Line 125)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NumpyToNumpyFile.run`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if storage_options or "://" in path or "::" in path:
            with fsspec.open(path, **storage_options) as f:
                self._func(x, f)
```

#### 36. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L158) (Line 158)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MatplotlibToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, metadata=None, storage_options=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.savefig(f, format="png", **kwargs)
```

#### 37. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L293) (Line 293)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NumpyToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        img = Image.fromarray(x)
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            img.save(f, format="PNG", **kwargs)
```

#### 38. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L320) (Line 320)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NumpyToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        if storage_options or "://" in url or "::" in url:
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
                tifffile.imwrite(f, x, **kwargs)
```

#### 39. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L337) (Line 337)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PILImageToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="PNG", **kwargs)
```

#### 40. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L353) (Line 353)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PILImageToJPEG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, quality=85, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="JPEG", quality=quality, **kwargs)
```

#### 41. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L368) (Line 368)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PILImageToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="TIFF", **kwargs)
```

#### 42. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L402) (Line 402)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NumpyToWAV.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        if storage_options or "://" in url or "::" in url:
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
                sf.write(f, x, samplerate, **kwargs)
```

#### 43. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L682) (Line 682)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python

        protocol, _ = split_protocol(data.url)
        if protocol is None:
```

#### 44. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L695) (Line 695)
- **Target Call:** `fs._check_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        cached_fn = fs._check_file(path)
        if cached_fn:
```

#### 45. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L699) (Line 699)
- **Target Call:** `fs._mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        sha = fs._mapper(path)
        cached_fn = os.path.join(fs.storage[-1], sha)
```

#### 46. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L702) (Line 702)
- **Target Call:** `self.fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path, cached_fn`
- **Keywords:** `{'callback': 'callback'}`

```python

        fs.fs.get_file(path, cached_fn, callback=callback)
        return cached_fn
```

#### 47. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L736) (Line 736)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `LlamaServerReader._read`
- **Arguments:** `f'simplecache::{v}'`
- **Keywords:** `{}`

```python
            if k == "--system-prompt-file":
                path = fsspec.open_local(f"simplecache::{v}")
                cmd.extend([str(k), path])
```

#### 48. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L923) (Line 923)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `SKLearnModelReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f)
```

#### 49. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L993) (Line 993)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
    def _extract(cls, meta, base):
        h = fsspec.filesystem("http")
        if "URL_ORIGINAL_DATA" in meta:
```

#### 50. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1000) (Line 1000)
- **Target Call:** `h.cat` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `[f"{base}/{u.lstrip('hdl:/')}" for u in ids]`
- **Keywords:** `{}`

```python
            ids = meta["HAS_PARTS"]["value"].split(";")
            rr = h.cat([f"{base}/{u.lstrip('hdl:/')}" for u in ids])
            rr2 = [{i["type"]: i["data"] for i in json.loads(r)["values"]} for r in rr.values()]
```

#### 51. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1006) (Line 1006)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
    def _read(self, data, base="https://hdl.handle.net/api/handles", **kwargs):
        h = fsspec.filesystem("http")
        r = h.cat(f"{base}/{data.url.lstrip('hdl:/')}")
```

#### 52. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1007) (Line 1007)
- **Target Call:** `h.cat` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `f"{base}/{data.url.lstrip('hdl:/')}"`
- **Keywords:** `{}`

```python
        h = fsspec.filesystem("http")
        r = h.cat(f"{base}/{data.url.lstrip('hdl:/')}")
        j = json.loads(r)
```

#### 53. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1044) (Line 1044)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PandasHDF5._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        if data.storage_options:  # or fsspec-like
            with fsspec.open(data.url, "rb", **data.storage_options) as f:
                self._func(f, data.path, **kw)
```

#### 54. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1286) (Line 1286)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PythonModule._read`
- **Arguments:** `data.url, 'rt'`
- **Keywords:** `{}`

```python
            module_name = data.url.rsplit("/", 1)[-1].split(".", 1)[0]
        with fsspec.open(data.url, "rt", **(data.storage_options or {})) as f:
            mod = ModuleType(module_name)
```

#### 55. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1318) (Line 1318)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NumpyText._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if data.storage_options or "://" in data.url or "::" in data.url:
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
                return self._func(f, **kw)
```

#### 56. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1415) (Line 1415)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            elif open_local:
                ofs = fsspec.open_local(data.url, **(data.storage_options or {}))
            elif (isinstance(data.url, str) and is_fsspec_url(data.url)) or is_fsspec_url(
```

#### 57. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1419) (Line 1419)
- **Target Call:** `fsspec.open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            ):
                ofs0 = fsspec.open_files(data.url, **(data.storage_options or {}))
                ofs = [_.open() for _ in ofs0]
```

#### 58. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1433) (Line 1433)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                if open_local:
                    f = fsspec.open_local(data.url, **(data.storage_options or {}))
                    return open_dataset(f, **kw)
```

#### 59. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436) (Line 1436)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                else:
                    f = fsspec.open(data.url, **(data.storage_options or {})).open()
                    return open_dataset(f, **kw)
```

#### 60. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1480) (Line 1480)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `XArrayPatternReader._read`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            url = pattern_to_glob(data.url)
            fs, _, paths = fsspec.get_fs_token_paths(url, **(data.storage_options or {}))
            val_dict = reverse_formats(data.url, paths)
```

#### 61. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1513) (Line 1513)
- **Target Call:** `fsspec.open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `RasterIOXarrayReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python

        ofs = fsspec.open_files(data.url, **(data.storage_options or {}))
        opened = [open_rasterio(of.open(), **kwargs) for of in ofs]
```

#### 62. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1578) (Line 1578)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GeoPandasReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if with_fsspec:
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
                return geopandas.read_file(f, **kwargs)
```

#### 63. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1600) (Line 1600)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ScipyMatrixMarketReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **data.storage_options) as f:
            return self._func(f)
```

#### 64. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1612) (Line 1612)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `NibabelNiftiReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f, **kw)
```

#### 65. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639) (Line 1639)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ASDFReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            # want the file to stay open, since array access is lazy by default
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
            return self._func(f, **kw)
```

#### 66. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1653) (Line 1653)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DicomReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f, **kw)
```

#### 67. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683) (Line 1683)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PMTileReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if "://" in data.url or "::" in data.url:
            f = fsspec.open(data.url, **(data.storage_options or {})).open()

```

#### 68. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889) (Line 1889)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GeoPandasTabular._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if "://" in data.url or "::" in data.url:
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
        else:
```

#### 69. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1971) (Line 1971)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MessagePackReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return msgpack.unpack(f, **kwargs)
```

#### 70. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1998) (Line 1998)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MarkdownReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            return f.read()
```

#### 71. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2005) (Line 2005)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MarkdownReader.discover`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        data = self.kwargs.get("data") or (self.kwargs.get("args") or [None])[0]
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            raw = f.read(head_bytes)
```

#### 72. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2036) (Line 2036)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TOMLReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return tomllib.load(f)
```

#### 73. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2081) (Line 2081)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `INIReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python
        cfg = configparser.ConfigParser(**kwargs)
        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            cfg.read_file(f)
```

#### 74. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2113) (Line 2113)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PDFTextReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return extract_text(f, **kwargs)
```

#### 75. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2251) (Line 2251)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PILImageReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            img = Image.open(f)
```

#### 76. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2468) (Line 2468)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `BioPythonFASTAReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            return list(SeqIO.parse(f, fmt))
```

#### 77. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2664) (Line 2664)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        MAGIC = b"GGUF"
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            header = f.read(24)
```

#### 78. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2751) (Line 2751)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `PMTilesMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        MAGIC = b"PMTiles"
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            raw = f.read(127)
```

#### 79. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2847) (Line 2847)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            # BlobHeader: 4-byte big-endian length, then protobuf BlobHeader
```

#### 80. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2980) (Line 2980)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `SKLearnModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            model = pickle.load(f)
```

#### 81. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3073) (Line 3073)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TorchModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        result: dict = {}
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as raw_f:
            with zipfile.ZipFile(raw_f) as zf:
```

#### 82. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3135) (Line 3135)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JoblibMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            obj = joblib.load(f)
```

#### 83. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3513) (Line 3513)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_as_local`
- **Arguments:** `f'simplecache::{url}'`
- **Keywords:** `{}`

```python
    if data.storage_options or "://" in url or "::" in url:
        return fsspec.open_local(
            f"simplecache::{url}", **{"simplecache": {}, **(data.storage_options or {})}
        )
    return url
```

#### 84. [intake/readers/search.py](https://github.com/intake/intake/blob/master/intake/readers/search.py#L126) (Line 126)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `EnvironmentSatisfied._is_consistent`
- **Arguments:** `env, 'rt'`
- **Keywords:** `{}`

```python
            if "dependencies:" not in env:
                with fsspec.open(env, "rt") as f:
                    env = f.read()
```

#### 85. [intake/readers/tests/test_workflows.py](https://github.com/intake/intake/blob/master/intake/readers/tests/test_workflows.py#L15) (Line 15)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `dataframe_file`
- **Arguments:** `'memory'`
- **Keywords:** `{}`

```python
def dataframe_file():
    m = fsspec.filesystem("memory")
    m.pipe("/data", bindata)
```

#### 86. [intake/readers/tests/test_workflows.py](https://github.com/intake/intake/blob/master/intake/readers/tests/test_workflows.py#L16) (Line 16)
- **Target Call:** `m.pipe` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `dataframe_file`
- **Arguments:** `'/data', bindata`
- **Keywords:** `{}`

```python
    m = fsspec.filesystem("memory")
    m.pipe("/data", bindata)
    return "memory://data"
```

#### 87. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L52) (Line 52)
- **Target Call:** `compressions.values` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JSONFileSource.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        VALID_COMPRESSIONS = list(compressions.values()) + ["infer"]

```

#### 88. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L74) (Line 74)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JSONFileSource.read`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': 'self.mode', 'encoding': 'self.encoding', 'compression': 'self.compression'}`

```python
        urlpath = self._get_cache(self._urlpath)[0]
        with fsspec.open(
            urlpath,
            mode=self.mode,
            encoding=self.encoding,
            compression=self.compression,
            **self._storage_options,
        ) as f:
            return json.load(f)
```

#### 89. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L132) (Line 132)
- **Target Call:** `compressions.values` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JSONLinesFileSource.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        VALID_COMPRESSIONS = list(compressions.values()) + ["infer"]

```

#### 90. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L157) (Line 157)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JSONLinesFileSource._open`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': 'self.mode', 'encoding': 'self.encoding', 'compression': 'self.compression'}`

```python
        urlpath = self._get_cache(self._urlpath)[0]
        with fsspec.open(
            urlpath,
            mode=self.mode,
            encoding=self.encoding,
            compression=self.compression,
            **self._storage_options,
        ) as f:
            yield f
```

#### 91. [intake/source/tests/test_json.py](https://github.com/intake/intake/blob/master/intake/source/tests/test_json.py#L19) (Line 19)
- **Target Call:** `compressions.items` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `global`
- **Arguments:** ``
- **Keywords:** `{}`

```python

EXTENSIONS = {compression: f".{extension}" for extension, compression in compressions.items()}

```

#### 92. [intake/source/tests/test_json.py](https://github.com/intake/intake/blob/master/intake/source/tests/test_json.py#L27) (Line 27)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `json_file`
- **Arguments:** `[file_path]`
- **Keywords:** `{'mode': "'wt'", 'compression': 'request.param'}`

```python
    file_path += EXTENSIONS.get(request.param, "")
    with open_files([file_path], mode="wt", compression=request.param)[0] as f:
        f.write(json.dumps(data))
```

#### 93. [intake/source/tests/test_json.py](https://github.com/intake/intake/blob/master/intake/source/tests/test_json.py#L37) (Line 37)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `jsonl_file`
- **Arguments:** `[file_path]`
- **Keywords:** `{'mode': "'wt'", 'compression': 'request.param'}`

```python
    file_path += EXTENSIONS.get(request.param, "")
    with open_files([file_path], mode="wt", compression=request.param)[0] as f:
        f.write("\n".join(json.dumps(row) for row in data))
```

#### 94. [intake/source/tests/test_text.py](https://github.com/intake/intake/blob/master/intake/source/tests/test_text.py#L40) (Line 40)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_complex_text`
- **Arguments:** `[fn]`
- **Keywords:** `{'mode': "'wt'", 'compression': 'comp'}`

```python
        fn = os.path.join(tempdir, f)
        with open_files([fn], mode="wt", compression=comp)[0] as fo:
            if read:
```

#### 95. [intake/source/tests/test_text.py](https://github.com/intake/intake/blob/master/intake/source/tests/test_text.py#L74) (Line 74)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_complex_bytes`
- **Arguments:** `[fn]`
- **Keywords:** `{'mode': "'wb'", 'compression': 'comp'}`

```python
        fn = os.path.join(tempdir, f)
        with open_files([fn], mode="wb", compression=comp)[0] as fo:
            if read:
```

#### 96. [intake/source/utils.py](https://github.com/intake/intake/blob/master/intake/source/utils.py#L119) (Line 119)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `reverse_format`
- **Arguments:** `format_string`
- **Keywords:** `{}`

```python
    # ensure that format_string is in posix format
    format_string = make_path_posix(format_string)

```

#### 97. [intake/source/utils.py](https://github.com/intake/intake/blob/master/intake/source/utils.py#L131) (Line 131)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `reverse_format`
- **Arguments:** `resolved_string`
- **Keywords:** `{}`

```python
    # ensure that resolved string is in posix format
    resolved_string = make_path_posix(resolved_string)

```

### pandas ([pandas-dev/pandas](https://github.com/pandas-dev/pandas))
- **Usages Found:** `13` in `7` files.

#### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L452) (Line 452)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_filepath_or_buffer`
- **Arguments:** `filepath_or_buffer`
- **Keywords:** `{'mode': 'fsspec_mode'}`

```python
        try:
            open_file = fsspec.open(
                filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
            )
            file_obj = open_file.open()
```

#### 2. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L464) (Line 464)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_filepath_or_buffer`
- **Arguments:** `filepath_or_buffer`
- **Keywords:** `{'mode': 'fsspec_mode'}`

```python
                storage_options["anon"] = True
            open_file = fsspec.open(
                filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
            )
            file_obj = open_file.open()
```

#### 3. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L347) (Line 347)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FastParquetImpl.write`
- **Arguments:** `path, 'wb'`
- **Keywords:** `{}`

```python
            # if filesystem is provided by fsspec, file must be opened in 'wb' mode.
            kwargs["open_with"] = lambda path, _: fsspec.open(
                path, "wb", **(storage_options or {})
            ).open()
        elif storage_options:
```

#### 4. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L397) (Line 397)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FastParquetImpl.read`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python

            parquet_kwargs["fs"] = fsspec.open(path, "rb", **(storage_options or {})).fs
        elif isinstance(path, str) and not os.path.isdir(path):
```

#### 5. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L91) (Line 91)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestCommonIOCapabilities.test_stringify_file_and_path_like`
- **Arguments:** `f'file://{temp_file}'`
- **Keywords:** `{'mode': "'wb'"}`

```python
        fsspec = pytest.importorskip("fsspec")
        with fsspec.open(f"file://{temp_file}", mode="wb") as fsspec_obj:
            assert fsspec_obj == icom.stringify_path(fsspec_obj)
```

#### 6. [pandas/tests/io/test_fsspec.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_fsspec.py#L47) (Line 47)
- **Target Call:** `register_implementation` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspectest`
- **Arguments:** `'testmem', TestMemoryFS`
- **Keywords:** `{'clobber': 'True'}`

```python

    register_implementation("testmem", TestMemoryFS, clobber=True)
    yield TestMemoryFS()
```

#### 7. [pandas/tests/io/test_fsspec.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_fsspec.py#L49) (Line 49)
- **Target Call:** `registry.pop` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspectest`
- **Arguments:** `'testmem', None`
- **Keywords:** `{}`

```python
    yield TestMemoryFS()
    registry.pop("testmem", None)
    TestMemoryFS.test[0] = None
```

#### 8. [pandas/tests/io/test_fsspec.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_fsspec.py#L70) (Line 70)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `cleared_fs`
- **Arguments:** `'memory'`
- **Keywords:** `{}`

```python

    memfs = fsspec.filesystem("memory")
    yield memfs
```

#### 9. [pandas/tests/io/test_fsspec.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_fsspec.py#L133) (Line 133)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_to_csv_fsspec_object`
- **Arguments:** `path`
- **Keywords:** `{'mode': 'mode'}`

```python
    mode = "wb" if binary_mode else "w"
    with fsspec.open(path, mode=mode).open() as fsspec_object:
        df1.to_csv(fsspec_object, index=True)
```

#### 10. [pandas/tests/io/test_fsspec.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_fsspec.py#L138) (Line 138)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_to_csv_fsspec_object`
- **Arguments:** `path`
- **Keywords:** `{'mode': 'mode'}`

```python
    mode = mode.replace("w", "r")
    with fsspec.open(path, mode=mode) as fsspec_object:
        df2 = read_csv(
```

#### 11. [pandas/tests/io/test_gcs.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_gcs.py#L50) (Line 50)
- **Target Call:** `fsspec.register_implementation` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `gcs_buffer`
- **Arguments:** `'gs', MockGCSFileSystem`
- **Keywords:** `{'clobber': 'True'}`

```python
    # Overwrites the default implementation from gcsfs to our mock class
    fsspec.register_implementation("gs", MockGCSFileSystem, clobber=True)

```

#### 12. [pandas/tests/io/test_http_headers.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_http_headers.py#L76) (Line 76)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `parquetfastparquet_responder`
- **Arguments:** `'memory://fastparquet_user_agent.parquet', 'rb'`
- **Keywords:** `{}`

```python
    )
    with fsspec.open("memory://fastparquet_user_agent.parquet", "rb") as f:
        return f.read()
```

#### 13. [pandas/tests/io/xml/test_to_xml.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/xml/test_to_xml.py#L1353) (Line 1353)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_s3_permission_output`
- **Arguments:** `s3_bucket_public.name`
- **Keywords:** `{}`

```python
        fs = s3fs.S3FileSystem(anon=True)
        fs.ls(s3_bucket_public.name)

```

### xarray ([pydata/xarray](https://github.com/pydata/xarray))
- **Usages Found:** `12` in `2` files.

#### 1. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174) (Line 174)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_find_absolute_paths`
- **Arguments:** `fs._strip_protocol(paths)`
- **Keywords:** `{}`

```python
            )
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
```

#### 2. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174) (Line 174)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_find_absolute_paths`
- **Arguments:** `paths`
- **Keywords:** `{}`

```python
            )
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
```

#### 3. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L175) (Line 175)
- **Target Call:** `fs.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_find_absolute_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
        elif is_remote_uri(paths):
```

#### 4. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L221) (Line 221)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_open_remote_file`
- **Arguments:** `file`
- **Keywords:** `{'mode': 'mode', 'storage_options': 'storage_options'}`

```python

    fs, _, paths = fsspec.get_fs_token_paths(
        file, mode=mode, storage_options=storage_options
    )

```

#### 5. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L227) (Line 227)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_open_remote_file`
- **Arguments:** `paths[0]`
- **Keywords:** `{'mode': 'mode'}`

```python

    return fs.open(paths[0], mode=mode, **open_kwargs)

```

#### 6. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L5114) (Line 5114)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestH5NetCDFFileObject.test_fsspec`
- **Arguments:** `tmp_file, 'rb'`
- **Keywords:** `{}`

```python

            with fsspec.open(tmp_file, "rb") as f:
                with open_dataset(f, engine="h5netcdf") as actual:
```

#### 7. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L6866) (Line 6866)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_source_encoding_always_present_with_fsspec`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python

        fs = fsspec.filesystem("file")
        with fs.open(tmp) as f, open_dataset(f) as ds:
```

#### 8. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L6867) (Line 6867)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_source_encoding_always_present_with_fsspec`
- **Arguments:** `tmp`
- **Keywords:** `{}`

```python
        fs = fsspec.filesystem("file")
        with fs.open(tmp) as f, open_dataset(f) as ds:
            assert ds.encoding["source"] == tmp
```

#### 9. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L6869) (Line 6869)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_source_encoding_always_present_with_fsspec`
- **Arguments:** `tmp`
- **Keywords:** `{}`

```python
            assert ds.encoding["source"] == tmp
        with fs.open(tmp) as f, open_mfdataset([f]) as ds:
            assert "foo" in ds
```

#### 10. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L7146) (Line 7146)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsspec`
- **Arguments:** `'memory'`
- **Keywords:** `{}`

```python

    m = fsspec.filesystem("memory")
    mm = m.get_mapper("out1.zarr")
```

#### 11. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L7147) (Line 7147)
- **Target Call:** `m.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsspec`
- **Arguments:** `'out1.zarr'`
- **Keywords:** `{}`

```python
    m = fsspec.filesystem("memory")
    mm = m.get_mapper("out1.zarr")
    ds.to_zarr(mm)  # old interface
```

#### 12. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L7153) (Line 7153)
- **Target Call:** `m.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsspec`
- **Arguments:** `'out2.zarr'`
- **Keywords:** `{}`

```python
    ds0["time"] = ds.time + np.timedelta64(1, "D")
    mm = m.get_mapper("out2.zarr")
    ds0.to_zarr(mm)  # old interface
```

### zarr ([zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python))
- **Usages Found:** `38` in `4` files.

#### 1. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L55) (Line 55)
- **Target Call:** `fs.to_json` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_make_async`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        # Convert sync instance of an async fs to an async instance
        fs_dict = json.loads(fs.to_json())
        fs_dict["asynchronous"] = True
```

#### 2. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L67) (Line 67)
- **Target Call:** `AsyncFileSystemWrapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_make_async`
- **Arguments:** `fs`
- **Keywords:** `{'asynchronous': 'True'}`

```python

    return AsyncFileSystemWrapper(fs, asynchronous=True)

```

#### 3. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L250) (Line 250)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.from_url`
- **Arguments:** `url`
- **Keywords:** `{}`

```python

        fs, path = url_to_fs(url, **opts)
        if not fs.async_impl:
```

#### 4. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L268) (Line 268)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.clear`
- **Arguments:** `self.path`
- **Keywords:** `{'withdirs': 'True'}`

```python
        try:
            for subpath in await self.fs._find(self.path, withdirs=True):
                if subpath != self.path:
```

#### 5. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L270) (Line 270)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.clear`
- **Arguments:** `subpath`
- **Keywords:** `{'recursive': 'True'}`

```python
                if subpath != self.path:
                    await self.fs._rm(subpath, recursive=True)
        except FileNotFoundError:
```

#### 6. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L298) (Line 298)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if byte_range is None:
                value = prototype.buffer.from_bytes(await self.fs._cat_file(path))
            elif isinstance(byte_range, RangeByteRequest):
```

#### 7. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L301) (Line 301)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{'start': 'byte_range.start', 'end': 'byte_range.end'}`

```python
                value = prototype.buffer.from_bytes(
                    await self.fs._cat_file(
                        path,
                        start=byte_range.start,
                        end=byte_range.end,
                    )
                )
```

#### 8. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L309) (Line 309)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{'start': 'byte_range.offset', 'end': 'None'}`

```python
                value = prototype.buffer.from_bytes(
                    await self.fs._cat_file(path, start=byte_range.offset, end=None)
                )
```

#### 9. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L313) (Line 313)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{'start': '-byte_range.suffix', 'end': 'None'}`

```python
                value = prototype.buffer.from_bytes(
                    await self.fs._cat_file(path, start=-byte_range.suffix, end=None)
                )
```

#### 10. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L345) (Line 345)
- **Target Call:** `self.fs._pipe_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.set`
- **Arguments:** `path, value.to_bytes()`
- **Keywords:** `{}`

```python
            raise NotImplementedError
        await self.fs._pipe_file(path, value.to_bytes())

```

#### 11. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L352) (Line 352)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.delete`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        try:
            await self.fs._rm(path)
        except FileNotFoundError:
```

#### 12. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L369) (Line 369)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.delete_dir`
- **Arguments:** `path_to_delete`
- **Keywords:** `{'recursive': 'True'}`

```python
        with suppress(*self.allowed_exceptions):
            await self.fs._rm(path_to_delete, recursive=True)

```

#### 13. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L374) (Line 374)
- **Target Call:** `self.fs._exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.exists`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = _dereference_path(self.path, key)
        exists: bool = await self.fs._exists(path)
        return exists
```

#### 14. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L409) (Line 409)
- **Target Call:** `self.fs._cat_ranges` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.get_partial_values`
- **Arguments:** `paths, starts, stops`
- **Keywords:** `{'on_error': "'return'"}`

```python
        # TODO: expectations for exceptions or missing keys?
        res = await self.fs._cat_ranges(paths, starts, stops, on_error="return")
        # the following is an s3-specific condition we probably don't want to leak
```

#### 15. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L420) (Line 420)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.list`
- **Arguments:** `self.path`
- **Keywords:** `{'detail': 'False', 'withdirs': 'False'}`

```python
        # docstring inherited
        allfiles = await self.fs._find(self.path, detail=False, withdirs=False)
        for onefile in (a.removeprefix(f"{self.path}/") for a in allfiles):
```

#### 16. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L428) (Line 428)
- **Target Call:** `self.fs._ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.list_dir`
- **Arguments:** `prefix`
- **Keywords:** `{'detail': 'False'}`

```python
        try:
            allfiles = await self.fs._ls(prefix, detail=False)
        except FileNotFoundError:
```

#### 17. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L436) (Line 436)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.list_prefix`
- **Arguments:** `f'{self.path}/{prefix}'`
- **Keywords:** `{'detail': 'False', 'maxdepth': 'None', 'withdirs': 'False'}`

```python
        # docstring inherited
        for onefile in await self.fs._find(
            f"{self.path}/{prefix}", detail=False, maxdepth=None, withdirs=False
        ):
            yield onefile.removeprefix(f"{self.path}/")
```

#### 18. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L443) (Line 443)
- **Target Call:** `self.fs._info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FsspecStore.getsize`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = _dereference_path(self.path, key)
        info = await self.fs._info(path)

```

#### 19. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L154) (Line 154)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.store_kwargs`
- **Arguments:** `f's3://{test_bucket_name}'`
- **Keywords:** `{'endpoint_url': 'endpoint_url', 'anon': 'False', 'asynchronous': 'True'}`

```python
            from fsspec.core import url_to_fs
        fs, path = url_to_fs(
            f"s3://{test_bucket_name}", endpoint_url=endpoint_url, anon=False, asynchronous=True
        )
        return {"fs": fs, "path": path}
```

#### 20. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L165) (Line 165)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.get`
- **Arguments:** `'s3'`
- **Keywords:** `{'endpoint_url': 'store.fs.endpoint_url', 'anon': 'store.fs.anon', 'asynchronous': 'False'}`

```python
        #  make a new, synchronous instance of the filesystem because this test is run in sync code
        new_fs = fsspec.filesystem(
            "s3", endpoint_url=store.fs.endpoint_url, anon=store.fs.anon, asynchronous=False
        )
        return self.buffer_cls.from_bytes(new_fs.cat(f"{store.path}/{key}"))
```

#### 21. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L168) (Line 168)
- **Target Call:** `new_fs.cat` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.get`
- **Arguments:** `f'{store.path}/{key}'`
- **Keywords:** `{}`

```python
        )
        return self.buffer_cls.from_bytes(new_fs.cat(f"{store.path}/{key}"))

```

#### 22. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L172) (Line 172)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.set`
- **Arguments:** `'s3'`
- **Keywords:** `{'endpoint_url': 'store.fs.endpoint_url', 'anon': 'store.fs.anon', 'asynchronous': 'False'}`

```python
        #  make a new, synchronous instance of the filesystem because this test is run in sync code
        new_fs = fsspec.filesystem(
            "s3", endpoint_url=store.fs.endpoint_url, anon=store.fs.anon, asynchronous=False
        )
        new_fs.write_bytes(f"{store.path}/{key}", value.to_bytes())
```

#### 23. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L175) (Line 175)
- **Target Call:** `new_fs.write_bytes` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.set`
- **Arguments:** `f'{store.path}/{key}', value.to_bytes()`
- **Keywords:** `{}`

```python
        )
        new_fs.write_bytes(f"{store.path}/{key}", value.to_bytes())

```

#### 24. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L258) (Line 258)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestFsspecStoreS3.test_init_warns_if_fs_asynchronous_is_false`
- **Arguments:** `f's3://{test_bucket_name}'`
- **Keywords:** `{'endpoint_url': 'endpoint_url', 'anon': 'False', 'asynchronous': 'False'}`

```python
            from fsspec.core import url_to_fs
        fs, path = url_to_fs(
            f"s3://{test_bucket_name}", endpoint_url=endpoint_url, anon=False, asynchronous=False
        )
        store_kwargs = {"fs": fs, "path": path}
```

#### 25. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L361) (Line 361)
- **Target Call:** `ReferenceFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_store_open_group_via_reference_filesystem`
- **Arguments:** ``
- **Keywords:** `{'fo': "{'version': 1, 'refs': {'zarr.json': group_json}}", 'asynchronous': 'True'}`

```python
    group_json = json.dumps({"zarr_format": 3, "node_type": "group", "attributes": {}})
    fs = ReferenceFileSystem(
        fo={"version": 1, "refs": {"zarr.json": group_json}},
        asynchronous=True,
    )
    store = FsspecStore(fs=fs, path="/", read_only=True)
```

#### 26. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L410) (Line 410)
- **Target Call:** `ReferenceFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsspec_store_read_array_chunk_via_reference_filesystem`
- **Arguments:** ``
- **Keywords:** `{'fo': "{'version': 1, 'refs': refs}", 'asynchronous': 'True'}`

```python

    fs = ReferenceFileSystem(
        fo={"version": 1, "refs": refs},
        asynchronous=True,
    )
    store = FsspecStore(fs=fs, path="/", read_only=True)
```

#### 27. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L470) (Line 470)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsmap_file`
- **Arguments:** `'file'`
- **Keywords:** `{'auto_mkdir': 'True'}`

```python

    fs = fsspec.filesystem("file", auto_mkdir=True)
    mapper = fs.get_mapper(tmp_path)
```

#### 28. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L471) (Line 471)
- **Target Call:** `fs.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsmap_file`
- **Arguments:** `tmp_path`
- **Keywords:** `{}`

```python
    fs = fsspec.filesystem("file", auto_mkdir=True)
    mapper = fs.get_mapper(tmp_path)

```

#### 29. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L491) (Line 491)
- **Target Call:** `fsspec.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsmap_file_raises`
- **Arguments:** ``
- **Keywords:** `{'auto_mkdir': 'False'}`

```python
    fsspec = pytest.importorskip("fsspec.implementations.local")
    fs = fsspec.LocalFileSystem(auto_mkdir=False)
    mapper = fs.get_mapper(tmp_path)
```

#### 30. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L492) (Line 492)
- **Target Call:** `fs.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_fsmap_file_raises`
- **Arguments:** `tmp_path`
- **Keywords:** `{}`

```python
    fs = fsspec.LocalFileSystem(auto_mkdir=False)
    mapper = fs.get_mapper(tmp_path)
    with pytest.raises(FileNotFoundError, match="No such file or directory: .*"):
```

#### 31. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L533) (Line 533)
- **Target Call:** `self.fs.set_session` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_close_does_not_close_filesystem_session`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    store = FsspecStore.from_url("http://example.com/a")
    session = await store.fs.set_session()

```

#### 32. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L550) (Line 550)
- **Target Call:** `self.fs.set_session` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_close_does_not_break_a_sibling_store`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    s2 = FsspecStore.from_url("http://example.com/b")
    session = await s2.fs.set_session()

```

#### 33. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L566) (Line 566)
- **Target Call:** `_fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_from_mapper_wraps_sync_filesystem`
- **Arguments:** `'file'`
- **Keywords:** `{'auto_mkdir': 'True'}`

```python

    fs = _fsspec.filesystem("file", auto_mkdir=True)
    mapper = fs.get_mapper(str(tmp_path))
```

#### 34. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L567) (Line 567)
- **Target Call:** `fs.get_mapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_from_mapper_wraps_sync_filesystem`
- **Arguments:** `str(tmp_path)`
- **Keywords:** `{}`

```python
    fs = _fsspec.filesystem("file", auto_mkdir=True)
    mapper = fs.get_mapper(str(tmp_path))
    store = FsspecStore.from_mapper(mapper)
```

#### 35. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L604) (Line 604)
- **Target Call:** `AsyncFileSystemWrapper` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_delete_dir_wrapped_filesystem`
- **Arguments:** `LocalFileSystem(auto_mkdir=True)`
- **Keywords:** `{}`

```python

    wrapped_fs = AsyncFileSystemWrapper(LocalFileSystem(auto_mkdir=True))
    store = FsspecStore(wrapped_fs, read_only=False, path=f"{tmp_path}/test/path")
```

#### 36. [tests/test_store/test_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec.py#L604) (Line 604)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_delete_dir_wrapped_filesystem`
- **Arguments:** ``
- **Keywords:** `{'auto_mkdir': 'True'}`

```python

    wrapped_fs = AsyncFileSystemWrapper(LocalFileSystem(auto_mkdir=True))
    store = FsspecStore(wrapped_fs, read_only=False, path=f"{tmp_path}/test/path")
```

#### 37. [tests/test_store/test_fsspec_get_ranges.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_fsspec_get_ranges.py#L35) (Line 35)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `memory_store`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    # so clear state explicitly.
    fs: MemoryFileSystem = MemoryFileSystem()
    fs.store.clear()
```

#### 38. [tests/test_store/test_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/tests/test_store/test_zip.py#L271) (Line 271)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestZipStoreFileObj.test_fsspec_file`
- **Arguments:** `f'local://{path}', 'rb'`
- **Keywords:** `{}`

```python
        path.write_bytes(zip_bytes)
        with fsspec.open(f"local://{path}", "rb") as fileobj:
            store = ZipStore(fileobj, mode="r")
```

### DVC ([iterative/dvc](https://github.com/iterative/dvc))
- **Usages Found:** `547` in `71` files.

#### 1. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L53) (Line 53)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `artifacts_show`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            root = _repo.fs.root_marker
            _dirname = _repo.fs.join(root, dirname) if dirname else root
            with Repo(_dirname, fs=_repo.fs, scm=_repo.scm) as r:
```

#### 2. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L56) (Line 56)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `artifacts_show`
- **Arguments:** `_repo.fs.root_marker, as_posix(path)`
- **Keywords:** `{}`

```python
                path = r.artifacts.get_path(name)
                path = _repo.fs.join(_repo.fs.root_marker, as_posix(path))
                parts = _repo.fs.relparts(path, _repo.root_dir)
```

#### 3. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L57) (Line 57)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `artifacts_show`
- **Arguments:** `path, _repo.root_dir`
- **Keywords:** `{}`

```python
                path = _repo.fs.join(_repo.fs.root_marker, as_posix(path))
                parts = _repo.fs.relparts(path, _repo.root_dir)
                return {"rev": rev, "path": os.path.join(*parts)}
```

#### 4. [dvc/api/data.py](https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L294) (Line 294)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_open`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                fs = DVCFileSystem(repo=_repo, subrepos=True)
                fs_path = fs.from_os_path(path)

```

#### 5. [dvc/api/data.py](https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L297) (Line 297)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode', 'encoding': 'encoding'}`

```python
            try:
                with fs.open(fs_path, mode=mode, encoding=encoding) as fobj:
                    yield fobj
```

#### 6. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L30) (Line 30)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_odb`
- **Arguments:** `fs_path, *prefix`
- **Keywords:** `{}`

```python
    if prefix:
        fs_path = fs.join(fs_path, *prefix)
    if hash_name:
```

#### 7. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L89) (Line 89)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `CacheManager.fs_cache`
- **Arguments:** `self.local_cache_dir, self.FS_DIR`
- **Keywords:** `{}`

```python
            fs=self.local.fs,
            path=self.local.fs.join(self.local_cache_dir, self.FS_DIR),
        )
```

#### 8. [dvc/commands/dag.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dag.py#L89) (Line 89)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_targets`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        for out in outs_trie.itervalues(prefix=repo.fs.parts(path)):
            targets.extend(str(out))
```

#### 9. [dvc/commands/dataset.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dataset.py#L66) (Line 66)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `CmdDatasetAdd.run`
- **Arguments:** `existing.manifest_path`
- **Keywords:** `{}`

```python
            if not self.args.force and existing:
                path = self.repo.fs.relpath(existing.manifest_path)
                raise DvcException(
```

#### 10. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L99) (Line 99)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Config.__init__`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
        if dvc_dir:
            self.dvc_dir = self.fs.abspath(dvc_dir)

```

#### 11. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L140) (Line 140)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Config.files`
- **Arguments:** `self.dvc_dir, self.CONFIG`
- **Keywords:** `{}`

```python
        if self.dvc_dir is not None:
            files["repo"] = self.fs.join(self.dvc_dir, self.CONFIG)

```

#### 12. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L211) (Line 211)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Config.load_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        with fs.open(path) as fobj:
            try:
```

#### 13. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L238) (Line 238)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Config._save_config`
- **Arguments:** `os.path.dirname(filename)`
- **Keywords:** `{}`

```python

        fs.makedirs(os.path.dirname(filename))

```

#### 14. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L241) (Line 241)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Config._save_config`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        config = ConfigObj(_pack_named(conf_dict))
        with fs.open(filename, "wb") as fobj:
            config.write(fobj)
```

#### 15. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L39) (Line 39)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Remote.odb`
- **Arguments:** `path, '.dvc', CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
        if self.worktree:
            path = self.fs.join(path, ".dvc", CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
        else:
```

#### 16. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L41) (Line 41)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Remote.odb`
- **Arguments:** `path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
        else:
            path = self.fs.join(path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
        return get_odb(self.fs, path, hash_name=DEFAULT_ALGORITHM, **self.config)
```

#### 17. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L214) (Line 214)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataCloud._push`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Pushing to {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 18. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L275) (Line 275)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataCloud._pull`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Fetching from {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 19. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L355) (Line 355)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataCloud.get_url_for`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = odb.oid_to_path(checksum)
        return odb.fs.unstrip_protocol(path)
```

#### 20. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L34) (Line 34)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dependency.workspace_status`
- **Arguments:** `self.fs_path, None`
- **Keywords:** `{}`

```python
            try:
                self.fs_path = self.fs.version_path(self.fs_path, None)
                if self.changed_meta():
```

#### 21. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L43) (Line 43)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dependency.update`
- **Arguments:** `self.fs_path, rev`
- **Keywords:** `{}`

```python
        if self.fs.version_aware:
            self.fs_path = self.fs.version_path(self.fs_path, rev)
            self.meta = self.get_meta()
```

#### 22. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L45) (Line 45)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dependency.update`
- **Arguments:** `self.fs_path, self.meta.version_id`
- **Keywords:** `{}`

```python
            self.meta = self.get_meta()
            self.fs_path = self.fs.version_path(self.fs_path, self.meta.version_id)

```

#### 23. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L53) (Line 53)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dependency.save`
- **Arguments:** `self.fs_path, self.meta.version_id`
- **Keywords:** `{}`

```python
        if self.fs.version_aware:
            self.fs_path = self.fs.version_path(self.fs_path, self.meta.version_id)

```

#### 24. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L40) (Line 40)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `RepoDependency.__init__`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python
        self.fs = self._make_fs()
        self.fs_path = as_posix(self.fs.normpath(self.def_path))

```

#### 25. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L106) (Line 106)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `RepoDependency.download`
- **Arguments:** `src_path`
- **Keywords:** `{}`

```python
            try:
                info = maybe_info or self.fs.info(src_path)
                hash_info = info["dvc_info"]["entry"].hash_info
```

#### 26. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L108) (Line 108)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `RepoDependency.download`
- **Arguments:** `dest_path`
- **Keywords:** `{}`

```python
                hash_info = info["dvc_info"]["entry"].hash_info
                dest_info = to.fs.info(dest_path)
            except (KeyError, AttributeError):
```

#### 27. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L108) (Line 108)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileMixin.exists`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        is_ignored = self.repo.dvcignore.is_ignored_file(self.path)
        return self.repo.fs.exists(self.path) and not is_ignored

```

#### 28. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L136) (Line 136)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FileMixin._load`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        self._verify_filename()
        if not self.repo.fs.isfile(self.path):
            raise StageFileIsNotDvcFileError(self.path)
```

#### 29. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L333) (Line 333)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ProjectFile.resolver`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python

        wdir = self.repo.fs.parent(self.path)
        return DataResolver(self.repo, wdir, self.contents)
```

#### 30. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L56) (Line 56)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    with TqdmCallback(desc=f"Downloading {fs.name(fs_path)}", unit="files") as cb:
        if isinstance(fs, DVCFileSystem):
```

#### 31. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L62) (Line 62)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                    f"{fs.normpath(glob.escape(fs_path))}/**"
                    if fs.isdir(fs_path)
                    else glob.escape(fs_path)
```

#### 32. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L61) (Line 61)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `glob.escape(fs_path)`
- **Keywords:** `{}`

```python
                [
                    f"{fs.normpath(glob.escape(fs_path))}/**"
                    if fs.isdir(fs_path)
```

#### 33. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L67) (Line 67)
- **Target Call:** `fs._get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `fs_path, to`
- **Keywords:** `{'batch_size': 'jobs', 'callback': 'cb'}`

```python
            if not glob.has_magic(fs_path):
                return fs._get(fs_path, to, batch_size=jobs, callback=cb)

```

#### 34. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L71) (Line 71)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        # download atomic and avoids fsspec glob/regex path expansion.
        if fs.isdir(fs_path):
            from_infos = [
```

#### 35. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L73) (Line 73)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            from_infos = [
                path for path in fs.find(fs_path) if not path.endswith(fs.flavour.sep)
            ]
```

#### 36. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L79) (Line 79)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `download`
- **Arguments:** `info, fs_path`
- **Keywords:** `{}`

```python
            to_infos = [
                localfs.join(to, *fs.relparts(info, fs_path)) for info in from_infos
            ]
```

#### 37. [dvc/fs/data.py](https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L31) (Line 31)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 38. [dvc/fs/data.py](https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L34) (Line 34)
- **Target Call:** `self.fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataFileSystem.isdvc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def isdvc(self, path, **kwargs):
        return self.fs.isdvc(path, **kwargs)

```

#### 39. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
        assert self.repo is not None
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

#### 40. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        assert self.repo is not None
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

#### 41. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
        return self.root_marker + self.sep.join(relparts)
```

#### 42. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
        return self.root_marker + self.sep.join(relparts)
```

#### 43. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L237) (Line 237)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.fsid`
- **Arguments:** `self.repo.url or self.repo.root_dir, self.repo.get_rev() if not isinstance(self.repo.scm, NoSCM) else None`
- **Keywords:** `{}`

```python

        return "dvcfs_" + tokenize(
            self.repo.url or self.repo.root_dir,
            self.repo.get_rev() if not isinstance(self.repo.scm, NoSCM) else None,
        )

```

#### 44. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L244) (Line 244)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._get_key`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        path = os.fspath(path)
        parts = self.repo.fs.relparts(path, self.repo.root_dir)
        if parts == (os.curdir,):
```

#### 45. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L268) (Line 268)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._from_key`
- **Arguments:** `self.repo.root_dir, *parts`
- **Keywords:** `{}`

```python
    def _from_key(self, parts: Key) -> str:
        return self.repo.fs.join(self.repo.root_dir, *parts)

```

#### 46. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L334) (Line 334)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `dir_path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python

        repo_path = self.repo.fs.join(dir_path, Repo.DVC_DIR)
        return self.repo.fs.isdir(repo_path)
```

#### 47. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L335) (Line 335)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = self.repo.fs.join(dir_path, Repo.DVC_DIR)
        return self.repo.fs.isdir(repo_path)

```

#### 48. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L362) (Line 362)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode'}`

```python
        try:
            return self.repo.fs.open(fs_path, mode=mode)
        except FileNotFoundError:
```

#### 49. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L401) (Line 401)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            try:
                fs_info = fs.info(fs_path)
                if fs_info["type"] == "file":
```

#### 50. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L408) (Line 408)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `info['name']`
- **Keywords:** `{}`

```python
                    ):
                        fs_infos[fs.name(info["name"])] = info
            except (FileNotFoundError, NotADirectoryError):
```

#### 51. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L465) (Line 465)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        try:
            fs_info = fs.info(fs_path)
            if check_ignored and repo.dvcignore.is_ignored(
```

#### 52. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L477) (Line 477)
- **Target Call:** `fs.parents` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if dvc_info and not fs_info:
            for parent in fs.parents(fs_path):
                try:
```

#### 53. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L479) (Line 479)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `parent`
- **Keywords:** `{}`

```python
                try:
                    if fs.info(parent)["type"] != "directory":
                        dvc_info = None
```

#### 54. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L591) (Line 591)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `src, dest`
- **Keywords:** `{'callback': 'child'}`

```python
            with callback.branched(src, dest) as child:
                fs.get_file(src, dest, callback=child, **kw)

```

#### 55. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L615) (Line 615)
- **Target Call:** `self.fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `fs_path, lpath`
- **Keywords:** `{}`

```python
        try:
            return self.repo.fs.get_file(fs_path, lpath, **kwargs)
        except FileNotFoundError:
```

#### 56. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L688) (Line 688)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 57. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L702) (Line 702)
- **Target Call:** `self.fs._get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DVCFileSystem._get`
- **Arguments:** `from_info, to_info`
- **Keywords:** `{'callback': 'callback', 'recursive': 'recursive', 'batch_size': 'batch_size'}`

```python
        recursive = not (isinstance(from_info, list) and isinstance(to_info, list))
        return self.fs._get(
            from_info,
            to_info,
            callback=callback,
            recursive=recursive,
            batch_size=batch_size,
            **kwargs,
        )

```

#### 58. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L734) (Line 734)
- **Target Call:** `self.fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DVCFileSystem.isdvc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def isdvc(self, path, **kwargs) -> bool:
        return self.fs.isdvc(path, **kwargs)

```

#### 59. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L753) (Line 753)
- **Target Call:** `self.fs.close` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DVCFileSystem.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if "fs" in self.__dict__:
            self.fs.close()
```

#### 60. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L48) (Line 48)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GitFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 61. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L51) (Line 51)
- **Target Call:** `self.fs.chdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GitFileSystem.chdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def chdir(self, path):
        self.fs.chdir(path)

```

#### 62. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L58) (Line 58)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `GitFileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'detail'}`

```python
    def ls(self, path, detail=True, **kwargs):
        return self.fs.ls(path, detail=detail, **kwargs) or []
```

#### 63. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L115) (Line 115)
- **Target Call:** `fs.isabs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def from_file(cls, path: str, fs: "FileSystem", name: str) -> "Self":
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
```

#### 64. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116) (Line 116)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `fs.dirname(path)`
- **Keywords:** `{}`

```python
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
```

#### 65. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116) (Line 116)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
```

#### 66. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L117) (Line 117)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
            path_spec_lines = [
```

#### 67. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L300) (Line 300)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._get_key`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
    def _get_key(self, path: str) -> tuple[str, ...]:
        parts = self.fs.relparts(path, self.root_dir)
        if parts == (os.curdir,):
```

#### 68. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L310) (Line 310)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `dirname, DvcIgnore.DVCIGNORE_FILE`
- **Keywords:** `{}`

```python

        path = self.fs.join(dirname, DvcIgnore.DVCIGNORE_FILE)
        if not matches and self.fs.exists(path):
```

#### 69. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L311) (Line 311)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = self.fs.join(dirname, DvcIgnore.DVCIGNORE_FILE)
        if not matches and self.fs.exists(path):
            name = self.fs.relpath(path, self.root_dir)
```

#### 70. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L312) (Line 312)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
        if not matches and self.fs.exists(path):
            name = self.fs.relpath(path, self.root_dir)
            new_pattern = DvcIgnorePatterns.from_file(path, self.fs, name)
```

#### 71. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L340) (Line 340)
- **Target Call:** `self.fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname`
- **Keywords:** `{}`

```python
                try:
                    _, dnames, _ = next(self.fs.walk(dirname))
                except StopIteration:
```

#### 72. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L345) (Line 345)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname, dname`
- **Keywords:** `{}`

```python
            for dname in dnames:
                self._update_sub_repo(self.fs.join(dirname, dname), ignore_trie)

```

#### 73. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L353) (Line 353)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python

        dvc_dir = self.fs.join(path, Repo.DVC_DIR)
        if not self.fs.exists(dvc_dir):
```

#### 74. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L354) (Line 354)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
        dvc_dir = self.fs.join(path, Repo.DVC_DIR)
        if not self.fs.exists(dvc_dir):
            return
```

#### 75. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L357) (Line 357)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        root, dname = self.fs.split(path)
        key = self._get_key(root)
```

#### 76. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L377) (Line 377)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.__call__`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
    ) -> tuple[list[str], list[str]]:
        abs_root = self.fs.abspath(root)
        ignore_pattern = self._get_trie_pattern(
```

#### 77. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L407) (Line 407)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python

        for entry in fs.ls(path, detail=True, **kwargs):
            name = fs.name(entry["name"])
```

#### 78. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L408) (Line 408)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.ls`
- **Arguments:** `entry['name']`
- **Keywords:** `{}`

```python
        for entry in fs.ls(path, detail=True, **kwargs):
            name = fs.name(entry["name"])
            fs_dict[name] = entry
```

#### 79. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L433) (Line 433)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.protocol == Schemes.LOCAL:
            for root, dirs, files in fs.walk(path, **kwargs):
                if detail:
```

#### 80. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L451) (Line 451)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        else:
            yield from fs.walk(path, **kwargs)

```

#### 81. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L460) (Line 460)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.find`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        else:
            yield from fs.find(path)

```

#### 82. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L470) (Line 470)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._get_trie_pattern`
- **Arguments:** `dirname, self.root_dir`
- **Keywords:** `{}`

```python

        if not self.fs.isin_or_eq(dirname, self.root_dir):
            # outside of the repo
```

#### 83. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L481) (Line 481)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._get_trie_pattern`
- **Arguments:** `self.root_dir, *prefix_key`
- **Keywords:** `{}`

```python
        prefix_key = ignores_trie.longest_prefix(key).key or ()
        prefix = self.fs.join(self.root_dir, *prefix_key)

```

#### 84. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `self.fs.normpath(path)`
- **Keywords:** `{}`

```python
            return False
        dirname, basename = self.fs.split(self.fs.normpath(path))
        ignore_pattern = self._get_trie_pattern(dirname, None, ignore_subrepos)
```

#### 85. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return False
        dirname, basename = self.fs.split(self.fs.normpath(path))
        ignore_pattern = self._get_trie_pattern(dirname, None, ignore_subrepos)
```

#### 86. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L510) (Line 510)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.is_ignored_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # only used in LocalFileSystem
        path = self.fs.abspath(path)
        if path == self.root_dir:
```

#### 87. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L518) (Line 518)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.is_ignored_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # only used in LocalFileSystem
        path = self.fs.abspath(path)
        return self._is_ignored(path, False, ignore_subrepos=ignore_subrepos)
```

#### 88. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L522) (Line 522)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter._outside_repo`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
    def _outside_repo(self, path: str) -> bool:
        return not self.fs.isin_or_eq(path, self.root_dir)

```

#### 89. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L527) (Line 527)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        # https://github.com/treeverse/dvc/issues/5046
        full_target = self.fs.abspath(target)
        matched_patterns: list[PatternInfo] = []
```

#### 90. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `self.fs.normpath(full_target)`
- **Keywords:** `{}`

```python
        if not self._outside_repo(full_target):
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
            pattern = self._get_trie_pattern(dirname)
```

#### 91. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
        if not self._outside_repo(full_target):
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
            pattern = self._get_trie_pattern(dirname)
```

#### 92. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L535) (Line 535)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
                ignore, matched_patterns = pattern.matches(
                    dirname, basename, self.fs.isdir(full_target), details=True
                )
```

#### 93. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L546) (Line 546)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return False
        if fs.isfile(path):
            return self.is_ignored_file(path, ignore_subrepos)
```

#### 94. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L548) (Line 548)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return self.is_ignored_file(path, ignore_subrepos)
        if fs.isdir(path):
            return self.is_ignored_dir(path, ignore_subrepos)
```

#### 95. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L367) (Line 367)
- **Target Call:** `self.fs.isabs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__init__`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python
            and self.fs.protocol == "local"
            and not self.fs.isabs(self.def_path)
        ):
```

#### 96. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L399) (Line 399)
- **Target Call:** `self.fs.coalesce_version` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__init__`
- **Arguments:** `self.def_path, self.meta.version_id`
- **Keywords:** `{}`

```python
        if self.fs.version_aware:
            _, version_id = self.fs.coalesce_version(
                self.def_path, self.meta.version_id
            )
            self.meta.version_id = version_id
```

#### 97. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L448) (Line 448)
- **Target Call:** `fs.isabs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._parse_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            and self.stage.repo.fs == fs
            and not fs.isabs(fs_path)
        ):
```

#### 98. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L456) (Line 456)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._parse_path`
- **Arguments:** `self.stage.wdir, fs_path`
- **Keywords:** `{}`

```python
            # then we have #2059 bug and can't really handle that.
            fs_path = fs.join(self.stage.wdir, fs_path)

```

#### 99. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._parse_path`
- **Arguments:** `fs.normpath(fs_path)`
- **Keywords:** `{}`

```python

        return fs.abspath(fs.normpath(fs_path))

```

#### 100. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._parse_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

        return fs.abspath(fs.normpath(fs_path))

```

#### 101. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L474) (Line 474)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        if not self.fs.isin(self.fs_path, self.repo.root_dir):
            return self.fs_path
```

#### 102. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L477) (Line 477)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__str__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        cur_dir = self.fs.getcwd()
        if self.fs.isin(cur_dir, self.repo.root_dir):
```

#### 103. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L478) (Line 478)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__str__`
- **Arguments:** `cur_dir, self.repo.root_dir`
- **Keywords:** `{}`

```python
        cur_dir = self.fs.getcwd()
        if self.fs.isin(cur_dir, self.repo.root_dir):
            return self.fs.relpath(self.fs_path, cur_dir)
```

#### 104. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L479) (Line 479)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, cur_dir`
- **Keywords:** `{}`

```python
        if self.fs.isin(cur_dir, self.repo.root_dir):
            return self.fs.relpath(self.fs_path, cur_dir)

```

#### 105. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L481) (Line 481)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        return self.fs.relpath(self.fs_path, self.repo.root_dir)

```

#### 106. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L498) (Line 498)
- **Target Call:** `self.fs.isabs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.is_in_repo`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python

        if self.fs.isabs(self.def_path):
            return False
```

#### 107. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L501) (Line 501)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.is_in_repo`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        return self.repo and self.fs.isin(self.fs_path, self.repo.root_dir)

```

#### 108. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L530) (Line 530)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.cache_path`
- **Arguments:** `self.cache.oid_to_path(self.hash_info.value)`
- **Keywords:** `{}`

```python
    def cache_path(self):
        return self.cache.fs.unstrip_protocol(
            self.cache.oid_to_path(self.hash_info.value)
        )

```

#### 109. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L585) (Line 585)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.exists`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python

        return self.fs.exists(self.fs_path)

```

#### 110. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L592) (Line 592)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.index_key`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
            assert self.repo
            key = self.repo.fs.relparts(self.fs_path, self.repo.root_dir)
        else:
```

#### 111. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L596) (Line 596)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.index_key`
- **Arguments:** `no_drive`
- **Keywords:** `{}`

```python
            no_drive = self.fs.flavour.splitdrive(self.fs_path)[1]
            key = self.fs.parts(no_drive)[1:]
        return workspace, key
```

#### 112. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L653) (Line 653)
- **Target Call:** `self.fs.is_empty` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.is_empty`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
    def is_empty(self) -> bool:
        return self.fs.is_empty(self.fs_path)

```

#### 113. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L658) (Line 658)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.isdir`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
            return False
        return self.fs.isdir(self.fs_path)

```

#### 114. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L663) (Line 663)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.isfile`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
            return False
        return self.fs.isfile(self.fs_path)

```

#### 115. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L787) (Line 787)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.commit`
- **Arguments:** `filter_info or self.fs_path`
- **Keywords:** `{}`

```python
                assert self.repo
                rel = self.fs.relpath(filter_info or self.fs_path)
                with CheckoutCallback(desc=f"Checking out {rel}", unit="files") as cb:
```

#### 116. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
    def _commit_granular_dir(self, filter_info, hardlink) -> Optional["HashFile"]:
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
        staging, _, obj = self._build(
```

#### 117. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
    def _commit_granular_dir(self, filter_info, hardlink) -> Optional["HashFile"]:
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
        staging, _, obj = self._build(
```

#### 118. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L844) (Line 844)
- **Target Call:** `self.fs.as_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.dumpd`
- **Arguments:** `relpath(self.fs_path, self.stage.wdir)`
- **Keywords:** `{}`

```python
        if self.is_in_repo:
            path = self.fs.as_posix(relpath(self.fs_path, self.stage.wdir))
        else:
```

#### 119. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L990) (Line 990)
- **Target Call:** `self.fs.remove` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.remove`
- **Arguments:** `self.fs_path`
- **Keywords:** `{'recursive': 'True'}`

```python
        try:
            self.fs.remove(self.fs_path, recursive=True)
        except FileNotFoundError:
```

#### 120. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1002) (Line 1002)
- **Target Call:** `self.fs.move` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.move`
- **Arguments:** `self.fs_path, out.fs_path`
- **Keywords:** `{}`

```python
        if src_exists:
            self.fs.move(self.fs_path, out.fs_path)
        else:
```

#### 121. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1049) (Line 1049)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.transfer`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Transferring to {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 122. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
            assert obj
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
            return obj.filter(prefix)
```

#### 123. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
            assert obj
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
            return obj.filter(prefix)
```

#### 124. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.unstage`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python

        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 125. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.unstage`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python

        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 126. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.apply`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python
        append_only = True
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 127. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Output.apply`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python
        append_only = True
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 128. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L143) (Line 143)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataResolver.__init__`
- **Arguments:** `wdir`
- **Keywords:** `{}`

```python
        if os.path.isabs(wdir):
            wdir = fs.relpath(wdir)
            wdir = "" if wdir == os.curdir else wdir
```

#### 129. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataResolver.__init__`
- **Arguments:** `fs.join(self.wdir, 'dvc.yaml')`
- **Keywords:** `{}`

```python
        self.wdir = wdir
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))

```

#### 130. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DataResolver.__init__`
- **Arguments:** `self.wdir, 'dvc.yaml'`
- **Keywords:** `{}`

```python
        self.wdir = wdir
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))

```

#### 131. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L290) (Line 290)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `EntryDefinition._resolve_wdir`
- **Arguments:** `self.wdir, wdir`
- **Keywords:** `{}`

```python
            format_and_raise(exc, f"'{self.where}.{name}.wdir'", self.relpath)
        return self.resolver.fs.join(self.wdir, wdir)

```

#### 132. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L356) (Line 356)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if not fs.exists(path):
            raise ParamsLoadError(f"'{path}' does not exist")
```

#### 133. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L358) (Line 358)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            raise ParamsLoadError(f"'{path}' does not exist")
        if fs.isdir(path):
            raise ParamsLoadError(f"'{path}' is a directory")
```

#### 134. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.merge_from`
- **Arguments:** `fs.join(wdir, path)`
- **Keywords:** `{}`

```python
        path, _, keys_str = item.partition(":")
        path = fs.normpath(fs.join(wdir, path))

```

#### 135. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.merge_from`
- **Arguments:** `wdir, path`
- **Keywords:** `{}`

```python
        path, _, keys_str = item.partition(":")
        path = fs.normpath(fs.join(wdir, path))

```

#### 136. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L433) (Line 433)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.load_from_vars`
- **Arguments:** `wdir, default`
- **Keywords:** `{}`

```python
        if default:
            to_import = fs.join(wdir, default)
            if fs.exists(to_import):
```

#### 137. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L434) (Line 434)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Context.load_from_vars`
- **Arguments:** `to_import`
- **Keywords:** `{}`

```python
            to_import = fs.join(wdir, default)
            if fs.exists(to_import):
                self.merge_from(fs, default, wdir)
```

#### 138. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L116) (Line 116)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo._get_repo_dirs`
- **Arguments:** `root_dir, self.DVC_DIR`
- **Keywords:** `{}`

```python
            fs = fs or localfs
            dvc_dir = fs.join(root_dir, self.DVC_DIR)
        except NotDvcRepoError:
```

#### 139. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L203) (Line 203)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                assert self.tmp_dir
                self.fs.makedirs(self.tmp_dir, exist_ok=True)

```

#### 140. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L206) (Line 206)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir, 'lock'`
- **Keywords:** `{}`

```python
                self.lock = make_lock(
                    self.fs.join(self.tmp_dir, "lock"),
                    tmp_dir=self.tmp_dir,
```

#### 141. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L272) (Line 272)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.local_dvc_dir`
- **Arguments:** `self.root_dir, '/'`
- **Keywords:** `{}`

```python
            # subrepo
            relparts = self.fs.relparts(self.root_dir, "/")

```

#### 142. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L393) (Line 393)
- **Target Call:** `fs._get_key_from_relative` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            fs = self.dvcfs.fs
            key = fs._get_key_from_relative(fs_path)
            subrepo, _, key = fs._get_subrepo_info(key)
```

#### 143. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L394) (Line 394)
- **Target Call:** `fs._get_subrepo_info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
            key = fs._get_key_from_relative(fs_path)
            subrepo, _, key = fs._get_subrepo_info(key)
            index = subrepo.index.data[workspace]
```

#### 144. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L398) (Line 398)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
            index = self.index.data[workspace]
            key = self.fs.relparts(path, self.root_dir)

```

#### 145. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L414) (Line 414)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_root`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
        root = root or os.curdir
        root_dir = fs.abspath(root)

```

#### 146. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L416) (Line 416)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python

        if not fs.isdir(root_dir):
            raise NotDvcRepoError(f"directory '{root}' does not exist")
```

#### 147. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L420) (Line 420)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
        while True:
            dvc_dir = fs.join(root_dir, cls.DVC_DIR)
            if fs.isdir(dvc_dir):
```

#### 148. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L421) (Line 421)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_root`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
            dvc_dir = fs.join(root_dir, cls.DVC_DIR)
            if fs.isdir(dvc_dir):
                return root_dir
```

#### 149. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L425) (Line 425)
- **Target Call:** `fs.parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
                break
            parent = fs.parent(root_dir)
            if parent == root_dir:
```

#### 150. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L443) (Line 443)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_dvc_dir`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
        root_dir = cls.find_root(root, fs=fs)
        return fs.join(root_dir, cls.DVC_DIR)

```

#### 151. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L554) (Line 554)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.find_outs_by_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        abs_path = self.fs.abspath(path)
        fs_path = abs_path
```

#### 152. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L565) (Line 565)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.func`
- **Arguments:** `out.fs_path, fs_path`
- **Keywords:** `{}`

```python
                return True
            return recursive and out.fs.isin(out.fs_path, fs_path)

```

#### 153. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L574) (Line 574)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Repo.is_dvc_internal`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def is_dvc_internal(self, path):
        path_parts = self.fs.normpath(path).split(self.fs.sep)
        return self.DVC_DIR in path_parts
```

#### 154. [dvc/repo/add.py](https://github.com/iterative/dvc/blob/main/dvc/repo/add.py#L181) (Line 181)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_add`
- **Arguments:** `source`
- **Keywords:** `{}`

```python
    out = stage.outs[0]
    path = out.fs.abspath(source) if source else None
    try:
```

#### 155. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L102) (Line 102)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.read`
- **Arguments:** `dvcfile, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for dvcfile, dvcfile_artifacts in self.repo.index._artifacts.items():
            dvcyaml = self.repo.fs.relpath(dvcfile, self.repo.root_dir)
            artifacts[dvcyaml] = {}
```

#### 156. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L180) (Line 180)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.get_path`
- **Arguments:** `scm_root, *dirparts, PROJECT_FILE`
- **Keywords:** `{}`

```python
        dirparts = posixpath.normpath(dirname).split(posixpath.sep) if dirname else ()
        abspath = fs.join(scm_root, *dirparts, PROJECT_FILE)
        rela = fs.relpath(abspath, self.repo.root_dir)
```

#### 157. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L181) (Line 181)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.get_path`
- **Arguments:** `abspath, self.repo.root_dir`
- **Keywords:** `{}`

```python
        abspath = fs.join(scm_root, *dirparts, PROJECT_FILE)
        rela = fs.relpath(abspath, self.repo.root_dir)
        try:
```

#### 158. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L210) (Line 210)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.download`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            root = self.repo.fs.root_marker
            _dirname = self.repo.fs.join(root, dirname) if dirname else root
            with Repo(_dirname, fs=self.repo.fs, scm=self.repo.scm) as r:
```

#### 159. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L213) (Line 213)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.download`
- **Arguments:** `root, as_posix(path)`
- **Keywords:** `{}`

```python
                path = r.artifacts.get_path(name)
                path = self.repo.fs.join(root, as_posix(path))
                path = self.repo.fs.relpath(path, self.repo.root_dir)
```

#### 160. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L214) (Line 214)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.download`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, as_posix(path))
                path = self.repo.fs.relpath(path, self.repo.root_dir)
                # when the `repo` is a subrepo, the path `/subrepo/myart.pkl` for dvcfs
```

#### 161. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L218) (Line 218)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.download`
- **Arguments:** `root, path`
- **Keywords:** `{}`

```python
                # i.e. relative to the root of the subrepo
                path = self.repo.fs.join(root, path)
                path = self.repo.fs.normpath(path)
```

#### 162. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L219) (Line 219)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Artifacts.download`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, path)
                path = self.repo.fs.normpath(path)

```

#### 163. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L64) (Line 64)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
    repo_root_parts: tuple[str, ...] = ()
    if self.fs.isin(self.root_dir, self.scm.root_dir):
        repo_root_parts = self.fs.relparts(self.root_dir, self.scm.root_dir)
```

#### 164. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L65) (Line 65)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.root_dir, self.scm.root_dir):
        repo_root_parts = self.fs.relparts(self.root_dir, self.scm.root_dir)

```

#### 165. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

#### 166. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

#### 167. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)

```

#### 168. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)

```

#### 169. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L129) (Line 129)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *repo_root_parts`
- **Keywords:** `{}`

```python
    fs = GitFileSystem(scm=repo.scm, rev=rev)
    root_dir = repo.fs.join("/", *repo_root_parts)
    if not fs.exists(root_dir):
```

#### 170. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L130) (Line 130)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
    root_dir = repo.fs.join("/", *repo_root_parts)
    if not fs.exists(root_dir):
        raise NotDvcRepoError(f"Commit '{rev[:7]}' does not contain a DVC repo")
```

#### 171. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L135) (Line 135)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir, repo.DVC_DIR`
- **Keywords:** `{}`

```python
    repo.root_dir = root_dir
    repo.dvc_dir = fs.join(root_dir, repo.DVC_DIR)
    repo._reset()
```

#### 172. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L139) (Line 139)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *cwd_parts`
- **Keywords:** `{}`

```python
    if cwd_parts:
        cwd = repo.fs.join("/", *cwd_parts)
        repo.fs.chdir(cwd)
```

#### 173. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L140) (Line 140)
- **Target Call:** `self.fs.chdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_switch_fs`
- **Arguments:** `cwd`
- **Keywords:** `{}`

```python
        cwd = repo.fs.join("/", *cwd_parts)
        repo.fs.chdir(cwd)

```

#### 174. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L152) (Line 152)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    repo_root_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.root_dir, repo.scm.root_dir):
        repo_root_parts = repo.fs.relparts(repo.root_dir, repo.scm.root_dir)
```

#### 175. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L153) (Line 153)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.root_dir, repo.scm.root_dir):
        repo_root_parts = repo.fs.relparts(repo.root_dir, repo.scm.root_dir)

```

#### 176. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

#### 177. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

#### 178. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)

```

#### 179. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)

```

#### 180. [dvc/repo/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/cache.py#L24) (Line 24)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `check_missing`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if not fs.exists(path):
            typ = "directory" if (entry.meta and entry.meta.isdir) else "file"
```

#### 181. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L98) (Line 98)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_check_can_delete`
- **Arguments:** `path, *(entry.key or ())`
- **Keywords:** `{}`

```python

        entry_paths.append(fs.join(path, *(entry.key or ())))

```

#### 182. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L174) (Line 174)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `checkout_onerror`
- **Arguments:** `dest_path, out_path`
- **Keywords:** `{}`

```python
        for out_path in out_paths:
            if self.fs.isin_or_eq(dest_path, out_path):
                failed.add(out_path)
```

#### 183. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L193) (Line 193)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `checkout`
- **Arguments:** `self.root_dir, *key`
- **Keywords:** `{}`

```python
    for key, (typ, _stats) in out_changes.items():
        out_path = self.fs.join(self.root_dir, *key)

```

#### 184. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L196) (Line 196)
- **Target Call:** `self.fs.remove` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `checkout`
- **Arguments:** `out_path`
- **Keywords:** `{'recursive': 'True'}`

```python
        if out_path in failed:
            self.fs.remove(out_path, recursive=True)
            continue
```

#### 185. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L34) (Line 34)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_paths`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=repo)
    fs_paths = [fs.from_os_path(target) for target in targets]

```

#### 186. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L38) (Line 38)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    for fs_path in fs_paths:
        if recursive and fs.isdir(fs_path):
            target_paths.extend(fs.find(fs_path))
```

#### 187. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L39) (Line 39)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if recursive and fs.isdir(fs_path):
            target_paths.extend(fs.find(fs_path))
        target_paths.append(fs_path)
```

#### 188. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L61) (Line 61)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_missing_paths`
- **Arguments:** `list(paths_map)`
- **Keywords:** `{'batch_size': 'batch_size', 'callback': 'callback'}`

```python
        else:
            results = fs.exists(
                list(paths_map), batch_size=batch_size, callback=callback
            )

```

#### 189. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L371) (Line 371)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    """Transform files rel. to Git root to DVC root, and drop outside files."""
    rel = repo.fs.relpath(repo.root_dir, repo.scm.root_dir).rstrip("/")

```

#### 190. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.fs.getcwd(), repo.root_dir`
- **Keywords:** `{}`

```python

    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
    if start in (os.curdir, ""):
```

#### 191. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** ``
- **Keywords:** `{}`

```python

    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
    if start in (os.curdir, ""):
```

#### 192. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L385) (Line 385)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `file, start`
- **Keywords:** `{}`

```python
    # we need to convert repo relative paths to curdir relative.
    return [repo.fs.relpath(file, start) for file in files]

```

#### 193. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L513) (Line 513)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `status`
- **Arguments:** `os.fspath(t)`
- **Keywords:** `{}`

```python
    targets = targets or []
    filter_keys: list[DataIndexKey] = [repo.fs.relparts(os.fspath(t)) for t in targets]
    # try to remove duplicate and overlapping keys
```

#### 194. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L35) (Line 35)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if summarize or not fs.isdir(path):
            return [(path, fs.du(path, total=True))]
```

#### 195. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L36) (Line 36)
- **Target Call:** `fs.du` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{'total': 'True'}`

```python
        if summarize or not fs.isdir(path):
            return [(path, fs.du(path, total=True))]

```

#### 196. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Target Call:** `fs.du` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `du`
- **Arguments:** `entry_path`
- **Keywords:** `{'total': 'True'}`

```python
        ret = [
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
        ]
```

#### 197. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        ret = [
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
        ]
```

#### 198. [dvc/repo/experiments/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L53) (Line 53)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ExpCache.get`
- **Arguments:** `obj.path, 'rb'`
- **Keywords:** `{}`

```python
        try:
            with obj.fs.open(obj.path, "rb") as fobj:
                data = fobj.read()
```

#### 199. [dvc/repo/experiments/executor/base.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/executor/base.py#L362) (Line 362)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `BaseExecutor.pack_repro_args`
- **Arguments:** `dpath`
- **Keywords:** `{}`

```python
            open_func = fs.open
            fs.makedirs(dpath)
        else:
```

#### 200. [dvc/repo/experiments/utils.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/utils.py#L44) (Line 44)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get_exp_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    path = os.path.join(repo.tmp_dir, EXEC_TMP_DIR)
    repo.fs.makedirs(path, exist_ok=True)

```

#### 201. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L169) (Line 169)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fetch`
- **Arguments:** `sorted((idx.data_tree.hash_info.value for idx in indexes.values()))`
- **Keywords:** `{}`

```python
        "fetch",
        tokenize(sorted(idx.data_tree.hash_info.value for idx in indexes.values())),
    )
```

#### 202. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224) (Line 224)
- **Target Call:** `fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_log_unversioned`
- **Arguments:** `fs.join(remote.path, *key)`
- **Keywords:** `{}`

```python
            if entry.meta and not entry.meta.isdir and entry.meta.version_id is None:
                unversioned.append(fs.unstrip_protocol(fs.join(remote.path, *key)))
            else:
```

#### 203. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224) (Line 224)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_log_unversioned`
- **Arguments:** `remote.path, *key`
- **Keywords:** `{}`

```python
            if entry.meta and not entry.meta.isdir and entry.meta.version_id is None:
                unversioned.append(fs.unstrip_protocol(fs.join(remote.path, *key)))
            else:
```

#### 204. [dvc/repo/get.py](https://github.com/iterative/dvc/blob/main/dvc/repo/get.py#L60) (Line 60)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs = DataFileSystem(index=repo.index.data["local"])
            fs_path = fs.from_os_path(path)
        else:
```

#### 205. [dvc/repo/get.py](https://github.com/iterative/dvc/blob/main/dvc/repo/get.py#L63) (Line 63)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs = repo.dvcfs
            fs_path = fs.from_os_path(path)
        download(fs, fs_path, os.path.abspath(out), jobs=jobs)
```

#### 206. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L146) (Line 146)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
                continue
            dep_key = dep.fs.parts(dep.fs_path)
            overlapping = [n.value for n in outs_trie.prefixes(dep_key)]
```

#### 207. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L176) (Line 176)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_outs_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
                continue
            dep_key = dep.fs.parts(dep.fs_path)
            overlapping = [n.value for n in outs_trie.prefixes(dep_key)]
```

#### 208. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L91) (Line 91)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `collect_files`
- **Arguments:** `root, file`
- **Keywords:** `{}`

```python
        for file in filter(dvcfile_filter, files):
            file_path = fs.join(root, file)
            try:
```

#### 209. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L203) (Line 203)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_load_storage_from_import`
- **Arguments:** `dep.meta.to_dict()`
- **Keywords:** `{}`

```python
        else:
            meta_token = tokenize(dep.meta.to_dict())

```

#### 210. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L210) (Line 210)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_load_storage_from_import`
- **Arguments:** `fs_cache.path, dep.fs.protocol, tokenize(dep.fs_path, meta_token)`
- **Keywords:** `{}`

```python
                fs_cache.fs,
                fs_cache.fs.join(
                    fs_cache.path,
                    dep.fs.protocol,
                    tokenize(dep.fs_path, meta_token),
                ),
            )
```

#### 211. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L213) (Line 213)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_load_storage_from_import`
- **Arguments:** `dep.fs_path, meta_token`
- **Keywords:** `{}`

```python
                    dep.fs.protocol,
                    tokenize(dep.fs_path, meta_token),
                ),
```

#### 212. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L513) (Line 513)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Index.metric_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for path in _collect_top_level_metrics(self.repo):
            key = self.repo.fs.relparts(path, self.repo.root_dir)
            by_workspace["repo"].add(key)
```

#### 213. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L527) (Line 527)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Index.param_keys`
- **Arguments:** `f'{self.repo.fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        default_file: str = ParamsDependency.DEFAULT_PARAMS_FILE
        if self.repo.fs.exists(f"{self.repo.fs.root_marker}{default_file}"):
            param_paths = chain(param_paths, [default_file])
```

#### 214. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L531) (Line 531)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Index.param_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for path in param_paths:
            key = self.repo.fs.relparts(path, self.repo.root_dir)
            by_workspace["repo"].add(key)
```

#### 215. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L550) (Line 550)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Index.plot_keys`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        for path in self._plot_sources:
            key = self.repo.fs.parts(path)
            by_workspace["repo"].add(key)
```

#### 216. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L788) (Line 788)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            workspace, key = out.index_key
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

#### 217. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L789) (Line 789)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
            entry = self._index.data[workspace].get(key)
```

#### 218. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L805) (Line 805)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            workspace, key = out.index_key
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

#### 219. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L806) (Line 806)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
            ret[workspace].add(key)
```

#### 220. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L856) (Line 856)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
    for key in index.data_keys.get(workspace, set()):
        out_path = fs.join(path, *key)

```

#### 221. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L861) (Line 861)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_data_index`
- **Arguments:** `out_path`
- **Keywords:** `{}`

```python

        if not fs.exists(out_path):
            continue
```

#### 222. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L901) (Line 901)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
    for key in parents:
        parent_path = fs.join(path, *key)
        if not fs.exists(parent_path):
```

#### 223. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L902) (Line 902)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_data_index`
- **Arguments:** `parent_path`
- **Keywords:** `{}`

```python
        parent_path = fs.join(path, *key)
        if not fs.exists(parent_path):
            continue
```

#### 224. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L84) (Line 84)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs: DVCFileSystem = repo.dvcfs
        fs_path = fs.from_os_path(path)
        return _ls(fs, fs_path, recursive, dvc_only, maxdepth)
```

#### 225. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L101) (Line 101)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls_tree`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs: DVCFileSystem = repo.dvcfs
        fs_path = fs.from_os_path(path)
        return _ls_tree(
```

#### 226. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L114) (Line 114)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
):
    fs_path = fs.info(path)["name"]

```

#### 227. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L120) (Line 120)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    maxdepth = maxdepth if recursive else None
    if maxdepth == 0 or fs.isfile(fs_path):
        infos[os.path.basename(path) or os.curdir] = fs.info(fs_path)
```

#### 228. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L121) (Line 121)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if maxdepth == 0 or fs.isfile(fs_path):
        infos[os.path.basename(path) or os.curdir] = fs.info(fs_path)
    else:
```

#### 229. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L123) (Line 123)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{'dvcfiles': 'True', 'dvc_only': 'dvc_only', 'detail': 'True', 'maxdepth': 'maxdepth'}`

```python
    else:
        for root, dirs, files in fs.walk(
            fs_path,
            dvcfiles=True,
            dvc_only=dvc_only,
            detail=True,
            maxdepth=maxdepth,
        ):
            parts = fs.relparts(root, fs_path)
```

#### 230. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L130) (Line 130)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
        ):
            parts = fs.relparts(root, fs_path)
            if parts == (".",):
```

#### 231. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L151) (Line 151)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def _ls_tree(fs, path, maxdepth=None, _info=None, **fs_kwargs):
    info = _info or fs.info(path)
    if _info is None:
```

#### 232. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L168) (Line 168)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python
        try:
            infos = fs.ls(path, detail=True, **fs_kwargs)
        except FileNotFoundError:
```

#### 233. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L10) (Line 10)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls_url`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    try:
        info = fs.info(fs_path)
    except FileNotFoundError as exc:
```

#### 234. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L18) (Line 18)
- **Target Call:** `_LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls_url`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        # dvc's LocalFileSystem does not support maxdepth yet
        walk = _LocalFileSystem().walk
    else:
```

#### 235. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L24) (Line 24)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls_url`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
    for root, dirs, files in walk(fs_path, detail=True, maxdepth=maxdepth):
        parts = fs.relparts(root, fs_path)
        if parts == (".",):
```

#### 236. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L32) (Line 32)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ls_url`
- **Arguments:** `info['name'], fs_path`
- **Keywords:** `{}`

```python
            ls_info = {
                "path": fs.relpath(info["name"], fs_path),
                "isdir": info["type"] == "directory",
```

#### 237. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28) (Line 28)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
    for dvcfile, metrics in top_metrics.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in metrics:
```

#### 238. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28) (Line 28)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `dvcfile`
- **Keywords:** `{}`

```python
    for dvcfile, metrics in top_metrics.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in metrics:
```

#### 239. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L30) (Line 30)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
        for file in metrics:
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)
```

#### 240. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L31) (Line 31)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)

```

#### 241. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L104) (Line 104)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_metrics`
- **Arguments:** `metric`
- **Keywords:** `{}`

```python
    # convert to posixpath for DVCFileSystem
    paths = (fs.from_os_path(metric) for metric in metrics)
    # make paths absolute for DVCFileSystem
```

#### 242. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L123) (Line 123)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        try:
            if fs.isdir(path):
                yield from fs.find(path)
```

#### 243. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L124) (Line 124)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if fs.isdir(path):
                yield from fs.find(path)
                continue
```

#### 244. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L138) (Line 138)
- **Target Call:** `fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `to_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    relpath = fs.relpath
    cwd = fs.getcwd()

```

#### 245. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L165) (Line 165)
- **Target Call:** `fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_gather_metrics`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = fs_path.lstrip(fs.root_marker)
        repo_os_path = os.sep.join(fs.parts(repo_path))
        if not isinstance(result, Exception):
```

#### 246. [dvc/repo/open_repo.py](https://github.com/iterative/dvc/blob/main/dvc/repo/open_repo.py#L70) (Line 70)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `make_repo`
- **Arguments:** `path, root_dir`
- **Keywords:** `{}`

```python
            fs = fs or localfs
            repo_path = os.path.join(url, *fs.relparts(path, root_dir))
            _config.update(_get_remote_config(repo_path))
```

#### 247. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24) (Line 24)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_params`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
    for dvcfile, params in top_params.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in params:
```

#### 248. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24) (Line 24)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_params`
- **Arguments:** `dvcfile`
- **Keywords:** `{}`

```python
    for dvcfile, params in top_params.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in params:
```

#### 249. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L26) (Line 26)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_params`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
        for file in params:
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)
```

#### 250. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L27) (Line 27)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_top_level_params`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)

```

#### 251. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L68) (Line 68)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_params`
- **Arguments:** `f'{fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        params.extend({param: []} for param in _collect_top_level_params(repo))
        if default_file and fs.exists(f"{fs.root_marker}{default_file}"):
            params.append({default_file: []})
```

#### 252. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L77) (Line 77)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_params`
- **Arguments:** `param`
- **Keywords:** `{}`

```python
        # convert to posixpath for DVCFileSystem
        path = fs.from_os_path(param)
        # make paths absolute for DVCFileSystem
```

#### 253. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L96) (Line 96)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_vars`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
                # `file` is relative
                abspath = repo.fs.abspath(file)
                repo_path = repo.dvcfs.from_os_path(abspath)
```

#### 254. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L141) (Line 141)
- **Target Call:** `fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_gather_params`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = fs_path.lstrip(fs.root_marker)
        repo_os_path = os.sep.join(fs.parts(repo_path))
        if not isinstance(result, Exception):
```

#### 255. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L63) (Line 63)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def _unpack_dir_files(fs, path, **kwargs):
    ret = list(fs.find(path))
    if not ret:
```

#### 256. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L66) (Line 66)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # This will raise FileNotFoundError if it is a broken symlink or TreeError
        next(iter(fs.ls(path)), None)
    return ret
```

#### 257. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_relpath`
- **Arguments:** `fs.join('/', fs.from_os_path(path)), fs.getcwd()`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 258. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_relpath`
- **Arguments:** `'/', fs.from_os_path(path)`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 259. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_relpath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 260. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 261. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L405) (Line 405)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_output_plots`
- **Arguments:** `wdir_relpath, plot.def_path`
- **Keywords:** `{}`

```python
                fs,
                _normpath(fs.join(wdir_relpath, plot.def_path)),
                props=plot_props | props,
```

#### 262. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L433) (Line 433)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_adjust_sources`
- **Arguments:** `config_dir, filepath`
- **Keywords:** `{}`

```python
        for filepath, val in old.items():
            new[_normpath(fs.join(config_dir, filepath))] = val
        new_plot_props[axis] = new
```

#### 263. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L447) (Line 447)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
    config_path = os.fspath(config_path)
    config_dir = fs.dirname(config_path)
    result: dict[str, dict] = {}
```

#### 264. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L451) (Line 451)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
    plot_ids_parents = [
        _normpath(fs.join(config_dir, plot_id)) for plot_id in definitions
    ]
```

#### 265. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L457) (Line 457)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
        if _id_is_path(plot_props):
            data_path = _normpath(fs.join(config_dir, plot_id))
            if _matches(targets, config_path, plot_id):
```

#### 266. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L480) (Line 480)
- **Target Call:** `fs.commonpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_closest_parent`
- **Arguments:** `[path, parent]`
- **Keywords:** `{}`

```python
    for parent in parents:
        common_path = fs.commonpath([path, parent])
        if len(common_path) > len(best_result):
```

#### 267. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L524) (Line 524)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_definitions`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
    for target in targets:
        if not result or fs.exists(target):
            unpacked = unpack_if_dir(fs, target, props=props, onerror=onerror)
```

#### 268. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L533) (Line 533)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `unpack_if_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    result: dict[str, dict] = defaultdict(dict)
    if fs.isdir(path):
        unpacked = _unpack_dir_files(fs, path, onerror=onerror)
```

#### 269. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L552) (Line 552)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'"}`

```python
    if extension in SUPPORTED_IMAGE_EXTENSIONS:
        with fs.open(path, mode="rb", **fs_kwargs) as fd:
            return fd.read()
```

#### 270. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L559) (Line 559)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf8'"}`

```python
    with reraise(UnicodeDecodeError, EncodingError(path, "utf8")):
        with fs.open(path, mode="r", encoding="utf8", **fs_kwargs) as fd:
            contents = fd.read()
```

#### 271. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_rebuild`
- **Arguments:** `fs.join(path, *key)`
- **Keywords:** `{}`

```python
            try:
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
            except FileNotFoundError:
```

#### 272. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_rebuild`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
            try:
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
            except FileNotFoundError:
```

#### 273. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L127) (Line 127)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `push`
- **Arguments:** `sorted((idx.data_tree.hash_info.value for idx in indexes.values()))`
- **Keywords:** `{}`

```python
        "push",
        tokenize(sorted(idx.data_tree.hash_info.value for idx in indexes.values())),
    )
```

#### 274. [dvc/repo/remove.py](https://github.com/iterative/dvc/blob/main/dvc/repo/remove.py#L27) (Line 27)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `remove`
- **Arguments:** `target + DVC_FILE_SUFFIX`
- **Keywords:** `{}`

```python
        # give a more helpful error message.
        if self.fs.exists(target + DVC_FILE_SUFFIX):
            raise StageFileIsNotDvcFileError(target) from e
```

#### 275. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L63) (Line 63)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_maybe_collect_from_dvc_yaml`
- **Arguments:** `PROJECT_FILE`
- **Keywords:** `{}`

```python
    stages: StageList = []
    if loader.fs.exists(PROJECT_FILE):
        with suppress(StageNotFound):
```

#### 276. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L90) (Line 90)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_collect_specific_target`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        logger.debug(msg, target, PROJECT_FILE)
        if not (recursive and loader.fs.isdir(target)):
            stages = _maybe_collect_from_dvc_yaml(loader, target, with_deps)
```

#### 277. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L223) (Line 223)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `StageLoad._get_filepath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if path:
            return self.repo.fs.abspath(path)

```

#### 278. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L349) (Line 349)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python

        if recursive and self.fs.isdir(target):
            from dvc.repo.graph import collect_inside_path
```

#### 279. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L352) (Line 352)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python

            path = self.fs.abspath(target)
            return collect_inside_path(path, graph or self.repo.index.graph)
```

#### 280. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L394) (Line 394)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        if not stages:
            if not (recursive and self.fs.isdir(target)):
                try:
```

#### 281. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L397) (Line 397)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
                    (out,) = self.repo.find_outs_by_path(target, strict=False)
                    return [StageInfo(out.stage, self.fs.abspath(target))]
                except OutputNotFoundError:
```

#### 282. [dvc/repo/trie.py](https://github.com/iterative/dvc/blob/main/dvc/repo/trie.py#L12) (Line 12)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `build_outs_trie`
- **Arguments:** `out.fs_path`
- **Keywords:** `{}`

```python
        for out in stage.outs:
            out_key = out.fs.parts(out.fs_path)

```

#### 283. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L131) (Line 131)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_merge_push_meta`
- **Arguments:** `repo.root_dir, *subkey`
- **Keywords:** `{}`

```python
                continue
            fs_path = repo.fs.join(repo.root_dir, *subkey)
            meta, hash_info = old_tree.get(repo.fs.relparts(fs_path, out.fs_path)) or (
```

#### 284. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L132) (Line 132)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_merge_push_meta`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
            fs_path = repo.fs.join(repo.root_dir, *subkey)
            meta, hash_info = old_tree.get(repo.fs.relparts(fs_path, out.fs_path)) or (
                None,
```

#### 285. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L331) (Line 331)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_update_diff_index`
- **Arguments:** `repo.root_dir, *entry.key`
- **Keywords:** `{}`

```python
                if not entry.meta.isdir:
                    fs_path = repo.fs.join(repo.root_dir, *entry.key)
                    tree = out.obj
```

#### 286. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L335) (Line 335)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_update_diff_index`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
                    _, entry.hash_info = tree.get(  # type: ignore[misc]
                        repo.fs.relparts(fs_path, out.fs_path)
                    )
```

#### 287. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L46) (Line 46)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_FILE`
- **Keywords:** `{}`

```python
def _edit_rwlock(lock_dir, fs, hardlink):
    path = fs.join(lock_dir, RWLOCK_FILE)

```

#### 288. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L49) (Line 49)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_LOCK`
- **Keywords:** `{}`

```python
    rwlock_guard = make_lock(
        fs.join(lock_dir, RWLOCK_LOCK),
        tmp_dir=lock_dir,
```

#### 289. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L55) (Line 55)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_edit_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        try:
            with fs.open(path, encoding="utf-8") as fobj:
                lock = SCHEMA(json.load(fobj))
```

#### 290. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L66) (Line 66)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_edit_rwlock`
- **Arguments:** `path, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        yield lock
        with fs.open(path, "w", encoding="utf-8") as fobj:
            json.dump(lock, fobj)
```

#### 291. [dvc/stage/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/stage/__init__.py#L640) (Line 640)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Stage._func`
- **Arguments:** `fs_path, o.fs_path`
- **Keywords:** `{}`

```python
        def _func(o):
            return o.fs.isin_or_eq(fs_path, o.fs_path)

```

#### 292. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L185) (Line 185)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def resolve_paths(fs, path, wdir=None):
    path = fs.abspath(path)
    wdir = wdir or os.curdir
```

#### 293. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_paths`
- **Arguments:** `fs.join(fs.dirname(path), wdir)`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 294. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_paths`
- **Arguments:** `fs.dirname(path), wdir`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 295. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 296. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L72) (Line 72)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{'detail': 'False'}`

```python

        assert fs.ls("/", detail=False) == M.unordered(
            "/.gitignore", "/scripts", "/data"
```

#### 297. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L75) (Line 75)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts'`
- **Keywords:** `{'detail': 'False'}`

```python
        )
        assert fs.ls("scripts", detail=False) == ["scripts/script1"]
        assert fs.ls("data", detail=False) == M.unordered("data/foo", "data/bar")
```

#### 298. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L76) (Line 76)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data'`
- **Keywords:** `{'detail': 'False'}`

```python
        assert fs.ls("scripts", detail=False) == ["scripts/script1"]
        assert fs.ls("data", detail=False) == M.unordered("data/foo", "data/bar")

```

#### 299. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L85) (Line 85)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert sorted(fs.ls("/"), key=lambda i: i["name"]) == [
            M.dict(name="/.gitignore", type="file", isexec=False),
```

#### 300. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L92) (Line 92)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/not-existing-path'`
- **Keywords:** `{}`

```python
        with pytest.raises(FileNotFoundError):
            fs.info("/not-existing-path")

```

#### 301. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L94) (Line 94)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert fs.info("/") == M.dict(name="/", isexec=False, type="directory")
        assert fs.info("/data") == data_info
```

#### 302. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L95) (Line 95)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data'`
- **Keywords:** `{}`

```python
        assert fs.info("/") == M.dict(name="/", isexec=False, type="directory")
        assert fs.info("/data") == data_info
        assert fs.info("/scripts") == scripts_info
```

#### 303. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L96) (Line 96)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts'`
- **Keywords:** `{}`

```python
        assert fs.info("/data") == data_info
        assert fs.info("/scripts") == scripts_info
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
```

#### 304. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L97) (Line 97)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
        assert fs.info("/scripts") == scripts_info
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
        assert fs.info("/scripts/script1") == M.dict(
```

#### 305. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L98) (Line 98)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
        assert fs.info("/scripts/script1") == M.dict(
            name="/scripts/script1", type="file"
```

#### 306. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L102) (Line 102)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert not fs.isdvc("/")
        assert fs.isdvc("/data")
```

#### 307. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L103) (Line 103)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data'`
- **Keywords:** `{}`

```python
        assert not fs.isdvc("/")
        assert fs.isdvc("/data")
        assert fs.isdvc("/data/foo")
```

#### 308. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L104) (Line 104)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
        assert fs.isdvc("/data")
        assert fs.isdvc("/data/foo")
        assert not fs.isdvc("/scripts")
```

#### 309. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L105) (Line 105)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts'`
- **Keywords:** `{}`

```python
        assert fs.isdvc("/data/foo")
        assert not fs.isdvc("/scripts")
        assert not fs.isdvc("/scripts/script1")
```

#### 310. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L106) (Line 106)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
        assert not fs.isdvc("/scripts")
        assert not fs.isdvc("/scripts/script1")

```

#### 311. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L109) (Line 109)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data'`
- **Keywords:** `{}`

```python
        with pytest.raises((IsADirectoryError, PermissionError)):
            fs.open("data")
        with pytest.raises((IsADirectoryError, PermissionError)):
```

#### 312. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L111) (Line 111)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts'`
- **Keywords:** `{}`

```python
        with pytest.raises((IsADirectoryError, PermissionError)):
            fs.open("scripts")
        with fs.open("/data/foo") as fobj:
```

#### 313. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L112) (Line 112)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
            fs.open("scripts")
        with fs.open("/data/foo") as fobj:
            assert fobj.read() == b"foo"
```

#### 314. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L114) (Line 114)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
            assert fobj.read() == b"foo"
        with fs.open("/scripts/script1") as fobj:
            assert fobj.read() == b"script1"
```

#### 315. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L118) (Line 118)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data/foo', (tmp / 'foo').fs_path`
- **Keywords:** `{}`

```python
        tmp = make_tmp_dir("temp-download")
        fs.get_file("data/foo", (tmp / "foo").fs_path)
        assert (tmp / "foo").read_text() == "foo"
```

#### 316. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L121) (Line 121)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts/script1', (tmp / 'script1').fs_path`
- **Keywords:** `{}`

```python

        fs.get_file("scripts/script1", (tmp / "script1").fs_path)
        assert (tmp / "script1").read_text() == "script1"
```

#### 317. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L124) (Line 124)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/', (tmp / 'all').fs_path`
- **Keywords:** `{'recursive': 'True'}`

```python

        fs.get("/", (tmp / "all").fs_path, recursive=True)
        assert (tmp / "all").read_text() == {
```

#### 318. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L195) (Line 195)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `match_files`
- **Arguments:** `d['path']`
- **Keywords:** `{}`

```python
def match_files(fs, entries, expected):
    entries_content = {(fs.normpath(d["path"]), d["isdir"]) for d in entries}
    expected_content = {(fs.normpath(d["path"]), d["isdir"]) for d in expected}
```

#### 319. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L196) (Line 196)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `match_files`
- **Arguments:** `d['path']`
- **Keywords:** `{}`

```python
    entries_content = {(fs.normpath(d["path"]), d["isdir"]) for d in entries}
    expected_content = {(fs.normpath(d["path"]), d["isdir"]) for d in expected}
    assert entries_content == expected_content
```

#### 320. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L206) (Line 206)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestLsUrl.test_file`
- **Arguments:** `fs_path, fname`
- **Keywords:** `{}`

```python
        result = ls_url(str(cloud / fname), fs_config=cloud.config)
        match_files(fs, result, [{"path": fs.join(fs_path, fname), "isdir": False}])

```

#### 321. [dvc/utils/serialize/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/__init__.py#L23) (Line 23)
- **Target Call:** `fs.suffix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
def load_path(fs_path, fs, **kwargs):
    suffix = fs.suffix(fs_path).lower()
    loader = LOADERS[suffix]
```

#### 322. [dvc/utils/serialize/_common.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_common.py#L88) (Line 88)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_modify_data`
- **Arguments:** `os.fspath(path)`
- **Keywords:** `{}`

```python
):
    file_exists = fs.exists(os.fspath(path)) if fs else os.path.exists(path)
    data = _load_data(path, parser=parser, fs=fs) if file_exists else {}
```

#### 323. [dvc/utils/strictyaml.py](https://github.com/iterative/dvc/blob/main/dvc/utils/strictyaml.py#L47) (Line 47)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `make_relpath`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if fs and not isinstance(fs, LocalFileSystem):
        rel = fs.relpath(fs_path).replace(fs.sep, sep)
    else:
```

#### 324. [dvc/utils/studio.py](https://github.com/iterative/dvc/blob/main/dvc/utils/studio.py#L126) (Line 126)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `get_subrepo_relpath`
- **Arguments:** `repo.root_dir, scm_root_dir`
- **Keywords:** `{}`

```python

    relpath = as_posix(repo.fs.relpath(repo.root_dir, scm_root_dir))

```

#### 325. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L50) (Line 50)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_new_simple`
- **Arguments:** `'metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
    fs = scm.get_fs(exp)
    with fs.open("metrics.yaml", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "foo: 2"
```

#### 326. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L89) (Line 89)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_experiment_exists`
- **Arguments:** `'metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
    fs = scm.get_fs(exp)
    with fs.open("metrics.yaml", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "foo: 3"
```

#### 327. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L109) (Line 109)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_failed_exp_workspace`
- **Arguments:** `os.path.join(dvc.experiments.workspace_queue.pid_dir, 'workspace')`
- **Keywords:** `{}`

```python
        dvc.experiments.run(failed_exp_stage.addressing)
    assert not dvc.fs.exists(
        os.path.join(dvc.experiments.workspace_queue.pid_dir, "workspace")
    )

```

#### 328. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L156) (Line 156)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_update_py_params`
- **Arguments:** `'params.py'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
    fs = scm.get_fs(exp_a)
    with fs.open("params.py", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "INT = 2"
```

#### 329. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L158) (Line 158)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_update_py_params`
- **Arguments:** `'metrics.py'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
        assert fobj.read().strip() == "INT = 2"
    with fs.open("metrics.py", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "INT = 2"
```

#### 330. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L204) (Line 204)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_update_py_params`
- **Arguments:** `'params.py'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
    fs = scm.get_fs(exp_a)
    with fs.open("params.py", mode="r", encoding="utf-8") as fobj:
        assert _dos2unix(fobj.read().strip()) == result
```

#### 331. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L206) (Line 206)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_update_py_params`
- **Arguments:** `'metrics.py'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
        assert _dos2unix(fobj.read().strip()) == result
    with fs.open("metrics.py", mode="r", encoding="utf-8") as fobj:
        assert _dos2unix(fobj.read().strip()) == result
```

#### 332. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L323) (Line 323)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked`
- **Arguments:** `'dvc.yaml'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert fs.exists("dvc.yaml")
    assert fs.exists("dvc.lock")
```

#### 333. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L324) (Line 324)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked`
- **Arguments:** `'dvc.lock'`
- **Keywords:** `{}`

```python
    assert fs.exists("dvc.yaml")
    assert fs.exists("dvc.lock")
    assert fs.exists("copy.py")
```

#### 334. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L325) (Line 325)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked`
- **Arguments:** `'copy.py'`
- **Keywords:** `{}`

```python
    assert fs.exists("dvc.lock")
    assert fs.exists("copy.py")
    with fs.open("metrics.yaml", mode="r", encoding="utf-8") as fobj:
```

#### 335. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L326) (Line 326)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked`
- **Arguments:** `'metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
    assert fs.exists("copy.py")
    with fs.open("metrics.yaml", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "foo: 2"
```

#### 336. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L417) (Line 417)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subdir`
- **Arguments:** `f'dir/{fname}'`
- **Keywords:** `{}`

```python
    for fname in ["metrics.yaml", "dvc.lock"]:
        assert fs.exists(f"dir/{fname}")
    with fs.open("dir/metrics.yaml", mode="r", encoding="utf-8") as fobj:
```

#### 337. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L418) (Line 418)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subdir`
- **Arguments:** `'dir/metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
        assert fs.exists(f"dir/{fname}")
    with fs.open("dir/metrics.yaml", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "foo: 2"
```

#### 338. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L456) (Line 456)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepo`
- **Arguments:** `f'dir/repo/{fname}'`
- **Keywords:** `{}`

```python
    for fname in ["metrics.yaml", "dvc.lock"]:
        assert fs.exists(f"dir/repo/{fname}")
    with fs.open("dir/repo/metrics.yaml", mode="r", encoding="utf-8") as fobj:
```

#### 339. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L457) (Line 457)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepo`
- **Arguments:** `'dir/repo/metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
        assert fs.exists(f"dir/repo/{fname}")
    with fs.open("dir/repo/metrics.yaml", mode="r", encoding="utf-8") as fobj:
        assert fobj.read().strip() == "foo: 2"
```

#### 340. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L479) (Line 479)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_run_celery`
- **Arguments:** `'metrics.yaml'`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf-8'"}`

```python
        fs = scm.get_fs(exp)
        with fs.open("metrics.yaml", mode="r", encoding="utf-8") as fobj:
            metrics.add(fobj.read().strip())
```

#### 341. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L705) (Line 705)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_local_config_is_propagated_to_tmp`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python

    with fs.open("file") as fobj:
        conf_obj = ConfigObj(fobj)
```

#### 342. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L724) (Line 724)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked_top_level_files_are_included_in_exp`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
    for file in ["metrics.json", "params.yaml", "plots.csv"]:
        assert fs.exists(file)

```

#### 343. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L743) (Line 743)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_copy_paths`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert not fs.exists("dir")
    assert not fs.exists("file")
```

#### 344. [tests/func/experiments/test_experiments.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_experiments.py#L744) (Line 744)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_copy_paths`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    assert not fs.exists("dir")
    assert not fs.exists("file")

```

#### 345. [tests/func/experiments/test_queue.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_queue.py#L53) (Line 53)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_copy_paths_queue`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert not fs.exists("dir")
    assert not fs.exists("file")
```

#### 346. [tests/func/experiments/test_queue.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_queue.py#L54) (Line 54)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_copy_paths_queue`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    assert not fs.exists("dir")
    assert not fs.exists("file")

```

#### 347. [tests/func/experiments/test_save.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_save.py#L135) (Line 135)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked_top_level_files_are_included_in_exp`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
    for file in ["metrics.json", "params.yaml", "plots.csv", "dvc.lock"]:
        assert fs.exists(file)

```

#### 348. [tests/func/experiments/test_save.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_save.py#L149) (Line 149)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_untracked_dvclock_is_included_in_exp`
- **Arguments:** `'dvc.lock'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert fs.exists("dvc.lock")

```

#### 349. [tests/func/experiments/test_save.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_save.py#L161) (Line 161)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exp_save_include_untracked_force`
- **Arguments:** `'new_file'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert fs.exists("new_file")

```

#### 350. [tests/func/experiments/test_stash_exp.py](https://github.com/iterative/dvc/blob/main/tests/func/experiments/test_stash_exp.py#L57) (Line 57)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_staged_new_file`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    fs = scm.get_fs(exp)
    assert fs.exists("file")
```

#### 351. [tests/func/test_data_cloud.py](https://github.com/iterative/dvc/blob/main/tests/func/test_data_cloud.py#L478) (Line 478)
- **Target Call:** `fs.keys` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fetch_stats`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    dvc.push()
    clean(list(fs.keys()), dvc)

```

#### 352. [tests/func/test_data_status.py](https://github.com/iterative/dvc/blob/main/tests/func/test_data_status.py#L346) (Line 346)
- **Target Call:** `self.fs.rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_partial_missing_cache`
- **Arguments:** `odb.oid_to_path('acbd18db4cc2f85cedef654fccc4a4d8')`
- **Keywords:** `{}`

```python
    odb = dvc.cache.repo
    odb.fs.rm(odb.oid_to_path("acbd18db4cc2f85cedef654fccc4a4d8"))

```

#### 353. [tests/func/test_data_status.py](https://github.com/iterative/dvc/blob/main/tests/func/test_data_status.py#L370) (Line 370)
- **Target Call:** `self.fs.rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_missing_dir_object_from_head`
- **Arguments:** `odb.oid_to_path(stage.outs[0].hash_info.value)`
- **Keywords:** `{}`

```python
    odb = dvc.cache.repo
    odb.fs.rm(odb.oid_to_path(stage.outs[0].hash_info.value))

```

#### 354. [tests/func/test_data_status.py](https://github.com/iterative/dvc/blob/main/tests/func/test_data_status.py#L392) (Line 392)
- **Target Call:** `self.fs.rm` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_missing_dir_object_from_index`
- **Arguments:** `odb.oid_to_path(stage.outs[0].hash_info.value)`
- **Keywords:** `{}`

```python
    odb = dvc.cache.repo
    odb.fs.rm(odb.oid_to_path(stage.outs[0].hash_info.value))

```

#### 355. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L16) (Line 16)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `dvc.fs.join(path, 'foo')`
- **Keywords:** `{}`

```python

    assert dvc.fs.exists(dvc.fs.join(path, "foo"))
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
```

#### 356. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L16) (Line 16)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'foo'`
- **Keywords:** `{}`

```python

    assert dvc.fs.exists(dvc.fs.join(path, "foo"))
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
```

#### 357. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L17) (Line 17)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `dvc.fs.join(path, 'foo')`
- **Keywords:** `{}`

```python
    assert dvc.fs.exists(dvc.fs.join(path, "foo"))
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
```

#### 358. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L17) (Line 17)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'foo'`
- **Keywords:** `{}`

```python
    assert dvc.fs.exists(dvc.fs.join(path, "foo"))
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
```

#### 359. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L18) (Line 18)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `dvc.fs.join(path, 'dir')`
- **Keywords:** `{}`

```python
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
    assert dvc.fs.isdir(dvc.fs.join(path, "dir"))
```

#### 360. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L18) (Line 18)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'dir'`
- **Keywords:** `{}`

```python
    assert dvc.fs.isfile(dvc.fs.join(path, "foo"))
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
    assert dvc.fs.isdir(dvc.fs.join(path, "dir"))
```

#### 361. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L19) (Line 19)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `dvc.fs.join(path, 'dir')`
- **Keywords:** `{}`

```python
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
    assert dvc.fs.isdir(dvc.fs.join(path, "dir"))

```

#### 362. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L19) (Line 19)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'dir'`
- **Keywords:** `{}`

```python
    assert dvc.fs.exists(dvc.fs.join(path, "dir"))
    assert dvc.fs.isdir(dvc.fs.join(path, "dir"))

```

#### 363. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L21) (Line 21)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `subrepo.fs.join(path, 'foo')`
- **Keywords:** `{}`

```python

    assert subrepo.fs.exists(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
```

#### 364. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L21) (Line 21)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'foo'`
- **Keywords:** `{}`

```python

    assert subrepo.fs.exists(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
```

#### 365. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L22) (Line 22)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `subrepo.fs.join(path, 'foo')`
- **Keywords:** `{}`

```python
    assert subrepo.fs.exists(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
```

#### 366. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L22) (Line 22)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'foo'`
- **Keywords:** `{}`

```python
    assert subrepo.fs.exists(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
```

#### 367. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L23) (Line 23)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `subrepo.fs.join(path, 'dir')`
- **Keywords:** `{}`

```python
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
    assert subrepo.fs.isdir(subrepo.fs.join(path, "dir"))
```

#### 368. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L23) (Line 23)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'dir'`
- **Keywords:** `{}`

```python
    assert subrepo.fs.isfile(subrepo.fs.join(path, "foo"))
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
    assert subrepo.fs.isdir(subrepo.fs.join(path, "dir"))
```

#### 369. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L24) (Line 24)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `subrepo.fs.join(path, 'dir')`
- **Keywords:** `{}`

```python
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
    assert subrepo.fs.isdir(subrepo.fs.join(path, "dir"))

```

#### 370. [tests/func/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/func/test_fs.py#L24) (Line 24)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_cleanfs_subrepo`
- **Arguments:** `path, 'dir'`
- **Keywords:** `{}`

```python
    assert subrepo.fs.exists(subrepo.fs.join(path, "dir"))
    assert subrepo.fs.isdir(subrepo.fs.join(path, "dir"))

```

#### 371. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L66) (Line 66)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / 'dir')`
- **Keywords:** `{}`

```python
            str(tmp_dir),
            {"dir": dvc.fs.info(str(tmp_dir / "dir"))},
            {
```

#### 372. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L68) (Line 68)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / 'bar')`
- **Keywords:** `{}`

```python
            {
                "bar": dvc.fs.info(str(tmp_dir / "bar")),
                ".dvcignore": dvc.fs.info(str(tmp_dir / ".dvcignore")),
```

#### 373. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L69) (Line 69)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / '.dvcignore')`
- **Keywords:** `{}`

```python
                "bar": dvc.fs.info(str(tmp_dir / "bar")),
                ".dvcignore": dvc.fs.info(str(tmp_dir / ".dvcignore")),
            },
```

#### 374. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L75) (Line 75)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / 'dir' / 'subdir')`
- **Keywords:** `{}`

```python
            {
                "subdir": dvc.fs.info(str(tmp_dir / "dir" / "subdir")),
            },
```

#### 375. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L78) (Line 78)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / 'dir' / 'baz')`
- **Keywords:** `{}`

```python
            {
                "baz": dvc.fs.info(str(tmp_dir / "dir" / "baz")),
            },
```

#### 376. [tests/func/test_ignore.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ignore.py#L84) (Line 84)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `str(tmp_dir / 'dir' / 'subdir' / 'qux')`
- **Keywords:** `{}`

```python
            {},
            {"qux": dvc.fs.info(str(tmp_dir / "dir" / "subdir" / "qux"))},
        ),
```

#### 377. [tests/func/test_ls.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ls.py#L1007) (Line 1007)
- **Target Call:** `fs.pipe` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fs_ls_tree`
- **Arguments:** `{f: content.encode() for f, content in FS_STRUCTURE.items()}`
- **Keywords:** `{}`

```python
    fs = MemoryFileSystem(global_store=False)
    fs.pipe({f: content.encode() for f, content in FS_STRUCTURE.items()})
    root = fs.root_marker
```

#### 378. [tests/func/test_ls.py](https://github.com/iterative/dvc/blob/main/tests/func/test_ls.py#L1036) (Line 1036)
- **Target Call:** `fs.pipe` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fs_ls_tree_maxdepth`
- **Arguments:** `{f: content.encode() for f, content in FS_STRUCTURE.items()}`
- **Keywords:** `{}`

```python
    fs = MemoryFileSystem(global_store=False)
    fs.pipe({f: content.encode() for f, content in FS_STRUCTURE.items()})

```

#### 379. [tests/func/test_remote.py](https://github.com/iterative/dvc/blob/main/tests/func/test_remote.py#L161) (Line 161)
- **Target Call:** `self.fs.remove` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dir_hash_should_be_key_order_agnostic`
- **Arguments:** `dvc.cache.local.oid_to_path(hash1.as_raw().value)`
- **Keywords:** `{}`

```python
    # remove the raw dir obj to force building the tree on the next build call
    dvc.cache.local.fs.remove(dvc.cache.local.oid_to_path(hash1.as_raw().value))

```

#### 380. [tests/remotes/git_server.py](https://github.com/iterative/dvc/blob/main/tests/remotes/git_server.py#L34) (Line 34)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_check`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python
            fs = get_fs()
            fs.exists("/")
            fs.execute("git --version")
```

#### 381. [tests/remotes/git_server.py](https://github.com/iterative/dvc/blob/main/tests/remotes/git_server.py#L35) (Line 35)
- **Target Call:** `fs.execute` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_check`
- **Arguments:** `'git --version'`
- **Keywords:** `{}`

```python
            fs.exists("/")
            fs.execute("git --version")
        except asyncssh.Error:
```

#### 382. [tests/unit/data/db/test_local.py](https://github.com/iterative/dvc/blob/main/tests/unit/data/db/test_local.py#L106) (Line 106)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_staging_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = local_odb.oid_to_path(obj.hash_info.value)
    assert fs.exists(path)

```

#### 383. [tests/unit/data/db/test_local.py](https://github.com/iterative/dvc/blob/main/tests/unit/data/db/test_local.py#L132) (Line 132)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_staging_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = local_odb.oid_to_path(obj.hash_info.value)
    assert fs.exists(path)
```

#### 384. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L26) (Line 26)
- **Target Call:** `self.fs._get_key` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_key`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert fs.fs._get_key(path) == key

```

#### 385. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L35) (Line 35)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert fs.exists("foo")

```

#### 386. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L44) (Line 44)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open`
- **Arguments:** `'foo', 'r'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    with fs.open("foo", "r") as fobj:
        assert fobj.read() == "foo"
```

#### 387. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L53) (Line 53)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_dirty_hash`
- **Arguments:** `'file', 'r'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    with fs.open("file", "r") as fobj:
        # NOTE: Unlike DVCFileSystem, DataFileSystem should not
```

#### 388. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L66) (Line 66)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_no_remote`
- **Arguments:** `'file', 'r'`
- **Keywords:** `{}`

```python
    with pytest.raises(FileNotFoundError):
        with fs.open("file", "r"):
            pass
```

#### 389. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L78) (Line 78)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_dirty_no_hash`
- **Arguments:** `'file', 'r'`
- **Keywords:** `{}`

```python
    with pytest.raises(FileNotFoundError):
        with fs.open("file", "r"):
            pass
```

#### 390. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L95) (Line 95)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_in_history`
- **Arguments:** `'foo', 'r'`
- **Keywords:** `{}`

```python
        fs = DataFileSystem(index=dvc.index.data["repo"])
        with fs.open("foo", "r") as fobj:
            assert fobj.read() == "foo"
```

#### 391. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L103) (Line 103)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert not fs.isdir("datadir")
    assert not fs.isfile("datadir")
```

#### 392. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L104) (Line 104)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datadir")
    assert not fs.isfile("datadir")
    assert not fs.isdir("datafile")
```

#### 393. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L105) (Line 105)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir")
    assert not fs.isdir("datafile")
    assert not fs.isfile("datafile")
```

#### 394. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L106) (Line 106)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datafile")
    assert not fs.isfile("datafile")

```

#### 395. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L113) (Line 113)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
```

#### 396. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L114) (Line 114)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
    assert not fs.isdir("datafile")
```

#### 397. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L115) (Line 115)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir")
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")
```

#### 398. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L116) (Line 116)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")

```

#### 399. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L125) (Line 125)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_mixed`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert fs.isdir("dir")
    assert not fs.isfile("dir")
```

#### 400. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L126) (Line 126)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_mixed`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir")
    assert not fs.isfile("dir")

```

#### 401. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L155) (Line 155)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir"):
        for entry in dirs + files:
```

#### 402. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L189) (Line 189)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir"):
        for entry in dirs + files:
```

#### 403. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L200) (Line 200)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_missing`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python

    for _ in fs.walk("dir"):
        pass
```

#### 404. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L208) (Line 208)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_not_a_dir`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python

    for _ in fs.walk("foo"):
        pass
```

#### 405. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L215) (Line 215)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_file`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    fs = DataFileSystem(index=dvc.index.data["repo"])
    assert fs.info("foo")["md5"] == "acbd18db4cc2f85cedef654fccc4a4d8"

```

#### 406. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L222) (Line 222)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    hash_file_spy = mocker.spy(dvc_data.hashfile.hash, "hash_file")
    assert fs.info("dir")["md5"] == "8761c4e9acad696bee718615e23e22db.dir"
    assert not hash_file_spy.called
```

#### 407. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L230) (Line 230)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_granular`
- **Arguments:** `subdir`
- **Keywords:** `{}`

```python
    subdir = "dir/subdir"
    assert fs.info(subdir).get("md5") is None
    _, _, obj = build(dvc.cache.local, subdir, fs, "md5", dry_run=True)
```

#### 408. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L234) (Line 234)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_granular`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
    data = posixpath.join(subdir, "data")
    assert fs.info(data)["md5"] == "8d777f385d3dfec8815d20f7496026dc"
    _, _, obj = build(dvc.cache.local, data, fs, "md5", dry_run=True)
```

#### 409. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L245) (Line 245)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_dirty_file`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    expected = "8c7dd922ad47494fc02c388e12c00eac"
    assert fs.info("file").get("md5") == expected
    _, _, obj = build(dvc.cache.local, "file", fs, "md5", dry_run=True)
```

#### 410. [tests/unit/fs/test_data.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_data.py#L256) (Line 256)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_dirty_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    expected = "5ea40360f5b4ec688df672a4db9c17d1.dir"
    assert fs.info("dir").get("md5") == expected
    _, _, obj = build(dvc.cache.local, "dir", fs, "md5", dry_run=True)
```

#### 411. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L21) (Line 21)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.exists("foo")

```

#### 412. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L30) (Line 30)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open`
- **Arguments:** `'foo', 'r'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    with fs.open("foo", "r") as fobj:
        assert fobj.read() == "foo"
```

#### 413. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L39) (Line 39)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_dirty_hash`
- **Arguments:** `'file', 'r'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    with fs.open("file", "r") as fobj:
        assert fobj.read() == "something"
```

#### 414. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L48) (Line 48)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_dirty_no_hash`
- **Arguments:** `'file', 'r'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    with fs.open("file", "r") as fobj:
        assert fobj.read() == "file"
```

#### 415. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L65) (Line 65)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_open_in_history`
- **Arguments:** `'foo', 'r'`
- **Keywords:** `{}`

```python
        fs = DVCFileSystem(repo=dvc)
        with fs.open("foo", "r") as fobj:
            assert fobj.read() == "foo"
```

#### 416. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L88) (Line 88)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
```

#### 417. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L89) (Line 89)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
    assert not fs.isdvc("datadir")
```

#### 418. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L90) (Line 90)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir")
    assert not fs.isdvc("datadir")
    assert not fs.isdir("datafile")
```

#### 419. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L91) (Line 91)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isdvc("datadir")
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")
```

#### 420. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L92) (Line 92)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")
    assert not fs.isdvc("datafile")
```

#### 421. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L93) (Line 93)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datafile")
    assert not fs.isdvc("datafile")

```

#### 422. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L109) (Line 109)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
```

#### 423. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L110) (Line 110)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("datadir")
    assert not fs.isfile("datadir")
    assert fs.isdvc("datadir")
```

#### 424. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L111) (Line 111)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir")
    assert fs.isdvc("datadir")
    assert not fs.isdir("datafile")
```

#### 425. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L112) (Line 112)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.isdvc("datadir")
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")
```

#### 426. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L113) (Line 113)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datafile")
    assert fs.isfile("datafile")
    assert fs.isdvc("datafile")
```

#### 427. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L114) (Line 114)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datafile")
    assert fs.isdvc("datafile")

```

#### 428. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L116) (Line 116)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'subdir'`
- **Keywords:** `{}`

```python

    assert fs.isdir("subdir")
    assert not fs.isfile("subdir")
```

#### 429. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L117) (Line 117)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'subdir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("subdir")
    assert not fs.isfile("subdir")
    assert not fs.isdvc("subdir")
```

#### 430. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L118) (Line 118)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'subdir'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("subdir")
    assert not fs.isdvc("subdir")
    assert fs.isfile("subdir/baz")
```

#### 431. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L119) (Line 119)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'subdir/baz'`
- **Keywords:** `{}`

```python
    assert not fs.isdvc("subdir")
    assert fs.isfile("subdir/baz")
    assert fs.isdir("subdir/data")
```

#### 432. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L120) (Line 120)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_isfile`
- **Arguments:** `'subdir/data'`
- **Keywords:** `{}`

```python
    assert fs.isfile("subdir/baz")
    assert fs.isdir("subdir/data")

```

#### 433. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L130) (Line 130)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python

    assert fs.exists("datafile")
    assert fs.exists("datadir")
```

#### 434. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L131) (Line 131)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.exists("datafile")
    assert fs.exists("datadir")
    assert fs.exists("datadir/foo")
```

#### 435. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L132) (Line 132)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert fs.exists("datadir")
    assert fs.exists("datadir/foo")
    assert fs.isfile("datafile")
```

#### 436. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L133) (Line 133)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.exists("datadir/foo")
    assert fs.isfile("datafile")
    assert not fs.isfile("datadir")
```

#### 437. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L134) (Line 134)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datafile")
    assert not fs.isfile("datadir")
    assert fs.isfile("datadir/foo")
```

#### 438. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L135) (Line 135)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir")
    assert fs.isfile("datadir/foo")
    assert not fs.isdir("datafile")
```

#### 439. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L136) (Line 136)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datadir/foo")
    assert not fs.isdir("datafile")
    assert fs.isdir("datadir")
```

#### 440. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L137) (Line 137)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datafile")
    assert fs.isdir("datadir")
    assert not fs.isdir("datadir/foo")
```

#### 441. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L138) (Line 138)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert fs.isdir("datadir")
    assert not fs.isdir("datadir/foo")

```

#### 442. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L142) (Line 142)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    tmp_dir.gen({"datadir": "data", "datafile": {"foo": "foo", "bar": "bar"}})
    assert fs.exists("datafile")
    assert fs.exists("datadir")
```

#### 443. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L143) (Line 143)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.exists("datafile")
    assert fs.exists("datadir")
    assert not fs.exists("datadir/foo")
```

#### 444. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L144) (Line 144)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert fs.exists("datadir")
    assert not fs.exists("datadir/foo")
    assert fs.exists("datafile/foo")
```

#### 445. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L145) (Line 145)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile/foo'`
- **Keywords:** `{}`

```python
    assert not fs.exists("datadir/foo")
    assert fs.exists("datafile/foo")
    assert not fs.isfile("datafile")
```

#### 446. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L146) (Line 146)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.exists("datafile/foo")
    assert not fs.isfile("datafile")
    assert fs.isfile("datadir")
```

#### 447. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L147) (Line 147)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datafile")
    assert fs.isfile("datadir")
    assert not fs.isfile("datadir/foo")
```

#### 448. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L148) (Line 148)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datadir")
    assert not fs.isfile("datadir/foo")
    assert fs.isfile("datafile/foo")
```

#### 449. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L149) (Line 149)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile/foo'`
- **Keywords:** `{}`

```python
    assert not fs.isfile("datadir/foo")
    assert fs.isfile("datafile/foo")
    assert fs.isdir("datafile")
```

#### 450. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L150) (Line 150)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile'`
- **Keywords:** `{}`

```python
    assert fs.isfile("datafile/foo")
    assert fs.isdir("datafile")
    assert not fs.isdir("datadir")
```

#### 451. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L151) (Line 151)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("datafile")
    assert not fs.isdir("datadir")
    assert not fs.isdir("datadir/foo")
```

#### 452. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L152) (Line 152)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datadir/foo'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datadir")
    assert not fs.isdir("datadir/foo")
    assert not fs.isdir("datafile/foo")
```

#### 453. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L153) (Line 153)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_exists_isdir_isfile_dirty`
- **Arguments:** `'datafile/foo'`
- **Keywords:** `{}`

```python
    assert not fs.isdir("datadir/foo")
    assert not fs.isdir("datafile/foo")

```

#### 454. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L162) (Line 162)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_mixed`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.isdir("dir")
    assert not fs.isfile("dir")
```

#### 455. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L163) (Line 163)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdir_mixed`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir")
    assert not fs.isfile("dir")

```

#### 456. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L173) (Line 173)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ls_dirty`
- **Arguments:** `'data'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert set(fs.ls("data")) == {"data/foo", "data/bar"}

```

#### 457. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L181) (Line 181)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ls_file_not_found`
- **Arguments:** `'missing'`
- **Keywords:** `{}`

```python
    with pytest.raises(FileNotFoundError):
        fs.ls("missing")

```

#### 458. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L190) (Line 190)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_ls_dir_empty`
- **Arguments:** `'empty'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert set(fs.ls("empty")) == set()

```

#### 459. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L231) (Line 231)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk`
- **Arguments:** `'dir'`
- **Keywords:** `{'dvcfiles': 'dvcfiles'}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir", dvcfiles=dvcfiles):
        for entry in dirs + files:
```

#### 460. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L267) (Line 267)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_dirty`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir"):
        for entry in dirs + files:
```

#### 461. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L282) (Line 282)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_dirty_cached_dir`
- **Arguments:** `'data'`
- **Keywords:** `{}`

```python
    actual = []
    for root, dirs, files in fs.walk("data"):
        for entry in dirs + files:
```

#### 462. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L307) (Line 307)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_mixed_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir"):
        for entry in dirs + files:
```

#### 463. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L318) (Line 318)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_missing`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python

    for _ in fs.walk("dir"):
        pass
```

#### 464. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L326) (Line 326)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_not_a_dir`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python

    for _ in fs.walk("foo"):
        pass
```

#### 465. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L335) (Line 335)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdvc`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.isdvc("foo")
    assert not fs.isdvc("bar")
```

#### 466. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L336) (Line 336)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdvc`
- **Arguments:** `'bar'`
- **Keywords:** `{}`

```python
    assert fs.isdvc("foo")
    assert not fs.isdvc("bar")
    assert fs.isdvc("dir")
```

#### 467. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L337) (Line 337)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdvc`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    assert not fs.isdvc("bar")
    assert fs.isdvc("dir")
    assert fs.isdvc("dir/baz")
```

#### 468. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L338) (Line 338)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdvc`
- **Arguments:** `'dir/baz'`
- **Keywords:** `{}`

```python
    assert fs.isdvc("dir")
    assert fs.isdvc("dir/baz")
    assert fs.isdvc("dir/baz", recursive=True)
```

#### 469. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L339) (Line 339)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_isdvc`
- **Arguments:** `'dir/baz'`
- **Keywords:** `{'recursive': 'True'}`

```python
    assert fs.isdvc("dir/baz")
    assert fs.isdvc("dir/baz", recursive=True)

```

#### 470. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L375) (Line 375)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/foo'`
- **Keywords:** `{}`

```python
    )
    assert fs.exists("dir/repo/foo") is True
    assert fs.exists("dir/repo/bar") is False
```

#### 471. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L376) (Line 376)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/bar'`
- **Keywords:** `{}`

```python
    assert fs.exists("dir/repo/foo") is True
    assert fs.exists("dir/repo/bar") is False

```

#### 472. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L378) (Line 378)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/foo'`
- **Keywords:** `{}`

```python

    assert fs.isfile("dir/repo/foo") is True
    assert fs.isfile("dir/repo/dir1/bar") is True
```

#### 473. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L379) (Line 379)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/dir1/bar'`
- **Keywords:** `{}`

```python
    assert fs.isfile("dir/repo/foo") is True
    assert fs.isfile("dir/repo/dir1/bar") is True
    assert fs.isfile("dir/repo/dir1") is False
```

#### 474. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L380) (Line 380)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/dir1'`
- **Keywords:** `{}`

```python
    assert fs.isfile("dir/repo/dir1/bar") is True
    assert fs.isfile("dir/repo/dir1") is False

```

#### 475. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L382) (Line 382)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/dir1'`
- **Keywords:** `{}`

```python

    assert fs.isdir("dir/repo/dir1") is True
    assert fs.isdir("dir/repo/dir1/bar") is False
```

#### 476. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L383) (Line 383)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/dir1/bar'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir/repo/dir1") is True
    assert fs.isdir("dir/repo/dir1/bar") is False
    assert fs.isdvc("dir/repo/foo") is True
```

#### 477. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L384) (Line 384)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo/foo'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir/repo/dir1/bar") is False
    assert fs.isdvc("dir/repo/foo") is True
    mocker.stop(mock_subrepo1)
```

#### 478. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L390) (Line 390)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/lorem'`
- **Keywords:** `{}`

```python
    )
    assert fs.exists("dir/repo2/lorem") is True
    assert fs.exists("dir/repo2/ipsum") is False
```

#### 479. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L391) (Line 391)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/ipsum'`
- **Keywords:** `{}`

```python
    assert fs.exists("dir/repo2/lorem") is True
    assert fs.exists("dir/repo2/ipsum") is False

```

#### 480. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L393) (Line 393)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/lorem'`
- **Keywords:** `{}`

```python

    assert fs.isfile("dir/repo2/lorem") is True
    assert fs.isfile("dir/repo2/dir2/ipsum") is True
```

#### 481. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L394) (Line 394)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/dir2/ipsum'`
- **Keywords:** `{}`

```python
    assert fs.isfile("dir/repo2/lorem") is True
    assert fs.isfile("dir/repo2/dir2/ipsum") is True
    assert fs.isfile("dir/repo2/dir2") is False
```

#### 482. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L395) (Line 395)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/dir2'`
- **Keywords:** `{}`

```python
    assert fs.isfile("dir/repo2/dir2/ipsum") is True
    assert fs.isfile("dir/repo2/dir2") is False

```

#### 483. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L397) (Line 397)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/dir2'`
- **Keywords:** `{}`

```python

    assert fs.isdir("dir/repo2/dir2") is True
    assert fs.isdir("dir/repo2/dir2/ipsum") is False
```

#### 484. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L398) (Line 398)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/dir2/ipsum'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir/repo2/dir2") is True
    assert fs.isdir("dir/repo2/dir2/ipsum") is False
    assert fs.isdvc("dir/repo2/lorem") is True
```

#### 485. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L399) (Line 399)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepos`
- **Arguments:** `'dir/repo2/lorem'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir/repo2/dir2/ipsum") is False
    assert fs.isdvc("dir/repo2/lorem") is True
    mocker.stop(mock_subrepo2)
```

#### 486. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L456) (Line 456)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_subrepo_walk`
- **Arguments:** `'dir'`
- **Keywords:** `{'dvcfiles': 'dvcfiles', 'ignore_subrepos': 'False'}`

```python
    actual = []
    for root, dirs, files in fs.walk("dir", dvcfiles=dvcfiles, ignore_subrepos=False):
        for entry in dirs + files:
```

#### 487. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L491) (Line 491)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'/'`
- **Keywords:** `{'dvcfiles': 'True'}`

```python
    actual = []
    for root, dirs, files in fs.walk("/", dvcfiles=True):
        for entry in dirs + files:
```

#### 488. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L498) (Line 498)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'lorem'`
- **Keywords:** `{}`

```python

    assert fs.isfile("lorem") is True
    assert fs.isfile("dir/repo/foo") is False
```

#### 489. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L499) (Line 499)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'dir/repo/foo'`
- **Keywords:** `{}`

```python
    assert fs.isfile("lorem") is True
    assert fs.isfile("dir/repo/foo") is False
    assert fs.isdir("dir/repo") is False
```

#### 490. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L500) (Line 500)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'dir/repo'`
- **Keywords:** `{}`

```python
    assert fs.isfile("dir/repo/foo") is False
    assert fs.isdir("dir/repo") is False
    assert fs.isdir("dir") is True
```

#### 491. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L501) (Line 501)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    assert fs.isdir("dir/repo") is False
    assert fs.isdir("dir") is True

```

#### 492. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L503) (Line 503)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'lorem'`
- **Keywords:** `{}`

```python

    assert fs.isdvc("lorem") is True
    assert fs.isdvc("dir/repo/dir1") is False
```

#### 493. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L504) (Line 504)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'dir/repo/dir1'`
- **Keywords:** `{}`

```python
    assert fs.isdvc("lorem") is True
    assert fs.isdvc("dir/repo/dir1") is False

```

#### 494. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L506) (Line 506)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'dir/repo.txt'`
- **Keywords:** `{}`

```python

    assert fs.exists("dir/repo.txt") is True
    assert fs.exists("repo/ipsum") is False
```

#### 495. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L507) (Line 507)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dvcfs_no_subrepos`
- **Arguments:** `'repo/ipsum'`
- **Keywords:** `{}`

```python
    assert fs.exists("dir/repo.txt") is True
    assert fs.exists("repo/ipsum") is False

```

#### 496. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L514) (Line 514)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_file`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    expected = "acbd18db4cc2f85cedef654fccc4a4d8"
    assert fs.info("foo").get("md5") is None
    _, _, obj = build(dvc.cache.local, "foo", fs, "md5")
```

#### 497. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L518) (Line 518)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_file`
- **Arguments:** `'foo'`
- **Keywords:** `{}`

```python
    (tmp_dir / "foo").unlink()
    assert fs.info("foo")["md5"] == expected

```

#### 498. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L525) (Line 525)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    expected = "8761c4e9acad696bee718615e23e22db.dir"
    assert fs.info("dir").get("md5") is None
    _, _, obj = build(dvc.cache.local, "dir", fs, "md5")
```

#### 499. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L530) (Line 530)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_dir`
- **Arguments:** `'dir'`
- **Keywords:** `{}`

```python
    shutil.rmtree(tmp_dir / "dir")
    assert fs.info("dir")["md5"] == expected
    _, _, obj = build(dvc.cache.local, "dir", fs, "md5")
```

#### 500. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L539) (Line 539)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_granular`
- **Arguments:** `subdir`
- **Keywords:** `{}`

```python
    subdir = "dir/subdir"
    assert fs.info(subdir).get("md5") is None
    _, _, obj = build(dvc.cache.local, subdir, fs, "md5")
```

#### 501. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L542) (Line 542)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_granular`
- **Arguments:** `posixpath.join(subdir, 'data')`
- **Keywords:** `{}`

```python
    assert obj.hash_info == HashInfo("md5", "af314506f1622d107e0ed3f14ec1a3b5.dir")
    assert fs.info(posixpath.join(subdir, "data")).get("md5") is None
    _, _, obj = build(dvc.cache.local, posixpath.join(subdir, "data"), fs, "md5")
```

#### 502. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L547) (Line 547)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_cached_granular`
- **Arguments:** `posixpath.join(subdir, 'data')`
- **Keywords:** `{}`

```python
    assert (
        fs.info(posixpath.join(subdir, "data"))["md5"]
        == "8d777f385d3dfec8815d20f7496026dc"
```

#### 503. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L586) (Line 586)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_dirty_file`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.info("file").get("md5") is None
    staging, _, obj = build(dvc.cache.local, "file", fs, "md5")
```

#### 504. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L593) (Line 593)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_hash_dirty_file`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
    (tmp_dir / "file").unlink()
    assert fs.info("file")["md5"] == file_hash_info.value
    _, hash_info = hash_file("file", fs, "md5", state=dvc.state)
```

#### 505. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L662) (Line 662)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_walk_nested_subrepos`
- **Arguments:** `'/'`
- **Keywords:** `{'ignore_subrepos': 'not traverse_subrepos'}`

```python
    fs = DVCFileSystem(repo=dvc)
    for root, dirs, files in fs.walk("/", ignore_subrepos=not traverse_subrepos):
        actual[root] = set(dirs + files)
```

#### 506. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L669) (Line 669)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsid_noscm`
- **Arguments:** `dvc.root_dir, None`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.fsid == "dvcfs_" + tokenize(dvc.root_dir, None)

```

#### 507. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L674) (Line 674)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsid`
- **Arguments:** `dvc.root_dir, scm.get_rev()`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=dvc)
    assert fs.fsid == "dvcfs_" + tokenize(dvc.root_dir, scm.get_rev())
    old_fsid = fs.fsid
```

#### 508. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L680) (Line 680)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsid`
- **Arguments:** `dvc.root_dir, scm.get_rev()`
- **Keywords:** `{}`

```python
    assert fs.fsid != old_fsid
    assert fs.fsid == "dvcfs_" + tokenize(dvc.root_dir, scm.get_rev())

```

#### 509. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L689) (Line 689)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsid_url`
- **Arguments:** `url, erepo_dir.scm.get_rev()`
- **Keywords:** `{}`

```python
        fs = DVCFileSystem(repo=dvc)
        assert fs.fsid == "dvcfs_" + tokenize(url, erepo_dir.scm.get_rev())
        old_fsid = fs.fsid
```

#### 510. [tests/unit/fs/test_dvc.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvc.py#L698) (Line 698)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fsid_url`
- **Arguments:** `url, erepo_dir.scm.get_rev()`
- **Keywords:** `{}`

```python
        assert fs.fsid != old_fsid
        assert fs.fsid == "dvcfs_" + tokenize(url, erepo_dir.scm.get_rev())

```

#### 511. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L164) (Line 164)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DVCFixtures.local_fs`
- **Arguments:** ``
- **Keywords:** `{'auto_mkdir': 'True'}`

```python
        # for certain implementations.
        return LocalFileSystem(auto_mkdir=True)

```

#### 512. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L217) (Line 217)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_existing_directory`
- **Arguments:** `fs_join(source, 'file2'), target`
- **Keywords:** `{}`

```python
        # Copy from source directory
        fs.get(fs_join(source, "file2"), target)
        assert local_fs.isfile(target_file2)
```

#### 513. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L221) (Line 221)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', 'subfile1'), target`
- **Keywords:** `{}`

```python
        # Copy from sub directory
        fs.get(fs_join(source, "subdir", "subfile1"), target)
        assert local_fs.isfile(target_subfile1)
```

#### 514. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L230) (Line 230)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_existing_directory`
- **Arguments:** `fs_join(source, 'file2'), target + '/'`
- **Keywords:** `{}`

```python
        # Repeat with trailing slash on target
        fs.get(fs_join(source, "file2"), target + "/")
        assert local_fs.isdir(target)
```

#### 515. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L234) (Line 234)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', 'subfile1'), target + '/'`
- **Keywords:** `{}`

```python

        fs.get(fs_join(source, "subdir", "subfile1"), target + "/")
        assert local_fs.isfile(target_subfile1)
```

#### 516. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L252) (Line 252)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_new_directory`
- **Arguments:** `fs_join(source, 'subdir', 'subfile1'), local_join(target, 'newdir/')`
- **Keywords:** `{}`

```python

        fs.get(
            fs_join(source, "subdir", "subfile1"), local_join(target, "newdir/")
        )  # Note trailing slash

```

#### 517. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L275) (Line 275)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_file_in_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', 'subfile1'), local_join(target, 'newfile')`
- **Keywords:** `{}`

```python

        fs.get(fs_join(source, "subdir", "subfile1"), local_join(target, "newfile"))
        assert local_fs.isfile(local_join(target, "newfile"))
```

#### 518. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L293) (Line 293)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_file_to_file_in_new_directory`
- **Arguments:** `fs_join(source, 'subdir', 'subfile1'), local_join(target, 'newdir', 'newfile')`
- **Keywords:** `{}`

```python

        fs.get(
            fs_join(source, "subdir", "subfile1"),
            local_join(target, "newdir", "newfile"),
        )
        assert local_fs.isdir(local_join(target, "newdir"))
```

#### 519. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L323) (Line 323)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_existing_directory`
- **Arguments:** `s, t`
- **Keywords:** `{}`

```python
            # Without recursive does nothing
            fs.get(s, t)
            assert local_fs.ls(target) == []
```

#### 520. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L327) (Line 327)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_existing_directory`
- **Arguments:** `s, t`
- **Keywords:** `{'recursive': 'True'}`

```python
            # With recursive
            fs.get(s, t, recursive=True)
            if source_slash:
```

#### 521. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L356) (Line 356)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_existing_directory`
- **Arguments:** `s, t`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '1'}`

```python
            # Limit recursive by maxdepth
            fs.get(s, t, recursive=True, maxdepth=1)
            if source_slash:
```

#### 522. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L403) (Line 403)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_new_directory`
- **Arguments:** `s, t`
- **Keywords:** `{}`

```python
            # Without recursive does nothing
            fs.get(s, t)
            assert local_fs.ls(target) == []
```

#### 523. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L407) (Line 407)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_new_directory`
- **Arguments:** `s, t`
- **Keywords:** `{'recursive': 'True'}`

```python
            # With recursive
            fs.get(s, t, recursive=True)
            assert local_fs.isdir(local_join(target, "newdir"))
```

#### 524. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L421) (Line 421)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_to_new_directory`
- **Arguments:** `s, t`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '1'}`

```python
            # Limit recursive by maxdepth
            fs.get(s, t, recursive=True, maxdepth=1)
            assert local_fs.isdir(local_join(target, "newdir"))
```

#### 525. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L450) (Line 450)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', '*'), t`
- **Keywords:** `{}`

```python
            # Without recursive
            fs.get(fs_join(source, "subdir", "*"), t)
            assert local_fs.isfile(local_join(target, "subfile1"))
```

#### 526. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L468) (Line 468)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', glob), t`
- **Keywords:** `{'recursive': 'recursive'}`

```python
            for glob, recursive in zip(["*", "**"], [True, False]):
                fs.get(fs_join(source, "subdir", glob), t, recursive=recursive)
                assert local_fs.isfile(local_join(target, "subfile1"))
```

#### 527. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L486) (Line 486)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_existing_directory`
- **Arguments:** `fs_join(source, 'subdir', glob), t`
- **Keywords:** `{'recursive': 'recursive', 'maxdepth': '1'}`

```python
                # Limit recursive by maxdepth
                fs.get(
                    fs_join(source, "subdir", glob), t, recursive=recursive, maxdepth=1
                )
                assert local_fs.isfile(local_join(target, "subfile1"))
```

#### 528. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L524) (Line 524)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_new_directory`
- **Arguments:** `fs_join(source, 'subdir', '*'), t`
- **Keywords:** `{}`

```python
            # Without recursive
            fs.get(fs_join(source, "subdir", "*"), t)
            assert local_fs.isdir(local_join(target, "newdir"))
```

#### 529. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L540) (Line 540)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_new_directory`
- **Arguments:** `fs_join(source, 'subdir', glob), t`
- **Keywords:** `{'recursive': 'recursive'}`

```python
            for glob, recursive in zip(["*", "**"], [True, False]):
                fs.get(fs_join(source, "subdir", glob), t, recursive=recursive)
                assert local_fs.isdir(local_join(target, "newdir"))
```

#### 530. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L555) (Line 555)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_to_new_directory`
- **Arguments:** `fs_join(source, 'subdir', glob), t`
- **Keywords:** `{'recursive': 'recursive', 'maxdepth': '1'}`

```python
                # Limit recursive by maxdepth
                fs.get(
                    fs_join(source, "subdir", glob), t, recursive=recursive, maxdepth=1
                )
                assert local_fs.isdir(local_join(target, "newdir"))
```

#### 531. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L596) (Line 596)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_edge_cases`
- **Arguments:** `fs_join(source, path), t`
- **Keywords:** `{'recursive': 'recursive', 'maxdepth': 'maxdepth'}`

```python

            fs.get(fs_join(source, path), t, recursive=recursive, maxdepth=maxdepth)

```

#### 532. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L601) (Line 601)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_edge_cases`
- **Arguments:** `local_join(target, 'newdir', p)`
- **Keywords:** `{}`

```python
                prefixed_expected = [
                    make_path_posix(local_join(target, "newdir", p)) for p in expected
                ]
```

#### 533. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L605) (Line 605)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_glob_edge_cases`
- **Arguments:** `local_join(target, p)`
- **Keywords:** `{}`

```python
                prefixed_expected = [
                    make_path_posix(local_join(target, p)) for p in expected
                ]
```

#### 534. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L638) (Line 638)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_list_of_files_to_existing_directory`
- **Arguments:** `source_files, t`
- **Keywords:** `{}`

```python

            fs.get(source_files, t)
            assert local_fs.isfile(local_join(target, "file1"))
```

#### 535. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L674) (Line 674)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_list_of_files_to_new_directory`
- **Arguments:** `source_files, local_join(target, 'newdir') + '/'`
- **Keywords:** `{}`

```python

        fs.get(source_files, local_join(target, "newdir") + "/")  # Note trailing slash
        assert local_fs.isdir(local_join(target, "newdir"))
```

#### 536. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L689) (Line 689)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_recursive`
- **Arguments:** `src, target`
- **Keywords:** `{'recursive': 'True'}`

```python
        for loop in range(2):
            fs.get(src, target, recursive=True)
            assert local_fs.isdir(target)
```

#### 537. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L705) (Line 705)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_recursive`
- **Arguments:** `src + '/', target`
- **Keywords:** `{'recursive': 'True'}`

```python
        for _ in range(2):
            fs.get(src + "/", target, recursive=True)
            assert local_fs.isdir(target)
```

#### 538. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L724) (Line 724)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_without_files_with_same_name_prefix`
- **Arguments:** `fs_join(source, 'subdir'), target`
- **Keywords:** `{'recursive': 'True'}`

```python
        # Test without glob
        fs.get(fs_join(source, "subdir"), target, recursive=True)

```

#### 539. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L733) (Line 733)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_directory_without_files_with_same_name_prefix`
- **Arguments:** `fs_join(source, 'subdir*'), target`
- **Keywords:** `{'recursive': 'True'}`

```python
        # Test with glob
        fs.get(fs_join(source, "subdir*"), target, recursive=True)

```

#### 540. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L759) (Line 759)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_with_source_and_destination_as_list`
- **Arguments:** `local_join(target, f'{hashed_i}.txt')`
- **Keywords:** `{}`

```python
            destination_files.append(
                make_path_posix(local_join(target, f"{hashed_i}.txt"))
            )
```

#### 541. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L763) (Line 763)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDVCFileSystemGet.test_get_with_source_and_destination_as_list`
- **Arguments:** ``
- **Keywords:** `{'rpath': 'source_files', 'lpath': 'destination_files'}`

```python
        # Copy and assert order was kept
        fs.get(rpath=source_files, lpath=destination_files)

```

#### 542. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L785) (Line 785)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_maxdepth`
- **Arguments:** `'dir', 'dir1'`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '1'}`

```python
    fs = DVCFileSystem(tmp_dir)
    fs.get("dir", "dir1", recursive=True, maxdepth=1)
    assert (tmp_dir / "dir1").read_text() == {"file1": "file1"}
```

#### 543. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L788) (Line 788)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_maxdepth`
- **Arguments:** `'dir', 'dir2'`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '2'}`

```python

    fs.get("dir", "dir2", recursive=True, maxdepth=2)
    assert (tmp_dir / "dir2").read_text() == {
```

#### 544. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L794) (Line 794)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_maxdepth`
- **Arguments:** `'dir', 'dir3'`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '3'}`

```python

    fs.get("dir", "dir3", recursive=True, maxdepth=3)
    assert (tmp_dir / "dir3").read_text() == {
```

#### 545. [tests/unit/fs/test_dvcfs.py](https://github.com/iterative/dvc/blob/main/tests/unit/fs/test_dvcfs.py#L800) (Line 800)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_maxdepth`
- **Arguments:** `'dir', 'dir4'`
- **Keywords:** `{'recursive': 'True', 'maxdepth': '4'}`

```python

    fs.get("dir", "dir4", recursive=True, maxdepth=4)
    assert (tmp_dir / "dir4").read_text() == {
```

#### 546. [tests/unit/remote/test_remote.py](https://github.com/iterative/dvc/blob/main/tests/unit/remote/test_remote.py#L52) (Line 52)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_makedirs_not_create_for_top_level_path`
- **Arguments:** `url`
- **Keywords:** `{}`

```python

    fs.makedirs(url)
    assert not mocked_client.called
```

#### 547. [tests/unit/utils/test_fs.py](https://github.com/iterative/dvc/blob/main/tests/unit/utils/test_fs.py#L70) (Line 70)
- **Target Call:** `self.fs.contains_symlink_up_to` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_should_call_recursive_on_no_condition_matched`
- **Arguments:** `os.path.join('foo', 'path'), 'foo'`
- **Keywords:** `{}`

```python
    # call from full path to match contains_symlink_spy patch path
    assert not dvc.utils.fs.contains_symlink_up_to(os.path.join("foo", "path"), "foo")
    assert contains_symlink_spy.mock.call_count == 2
```

### Kedro ([kedro-org/kedro](https://github.com/kedro-org/kedro))
- **Usages Found:** `9` in `3` files.

#### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L397) (Line 397)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'tar'", 'fo': 'conf_source'}`

```python
        if file_mimetype == "application/x-tar":
            return fsspec.filesystem(protocol="tar", fo=conf_source), "tar"
        elif file_mimetype in (
```

#### 2. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L403) (Line 403)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'zip'", 'fo': 'conf_source'}`

```python
        ):
            return fsspec.filesystem(protocol="zip", fo=conf_source), "zip"

```

#### 3. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L412) (Line 412)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': 'protocol'}`

```python
            # For HTTP and cloud storage protocols, create the appropriate filesystem
            return fsspec.filesystem(protocol=protocol), protocol
        else:
```

#### 4. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L415) (Line 415)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'file'", 'fo': 'conf_source'}`

```python
            # Default to local filesystem
            return fsspec.filesystem(protocol="file", fo=conf_source), "file"

```

#### 5. [tests/io/test_core.py](https://github.com/kedro-org/kedro/blob/main/tests/io/test_core.py#L86) (Line 86)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MyVersionedDataset.__init__`
- **Arguments:** `self._protocol`
- **Keywords:** `{}`

```python
        self._protocol = protocol
        self._fs = fsspec.filesystem(self._protocol, **_fs_args)

```

#### 6. [tests/io/test_core.py](https://github.com/kedro-org/kedro/blob/main/tests/io/test_core.py#L130) (Line 130)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MyLocalVersionedDataset.__init__`
- **Arguments:** `self._protocol`
- **Keywords:** `{}`

```python
        self._protocol = protocol
        self._fs = fsspec.filesystem(self._protocol, **_fs_args)

```

#### 7. [tests/io/test_core.py](https://github.com/kedro-org/kedro/blob/main/tests/io/test_core.py#L827) (Line 827)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MyLegacyVersionedDataset.__init__`
- **Arguments:** `self._protocol`
- **Keywords:** `{}`

```python
        self._protocol = protocol
        self._fs = fsspec.filesystem(self._protocol, **_fs_args)

```

#### 8. [tests/io/test_data_catalog.py](https://github.com/kedro-org/kedro/blob/main/tests/io/test_data_catalog.py#L580) (Line 580)
- **Target Call:** `self.filesystem.assert_called_with` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDataCatalogFromConfig.test_link_credentials`
- **Arguments:** `'s3'`
- **Keywords:** `{}`

```python
            expected_client_kwargs = correct_config["credentials"]["s3_credentials"]
            mock_client.filesystem.assert_called_with("s3", **expected_client_kwargs)

```

#### 9. [tests/io/test_data_catalog.py](https://github.com/kedro-org/kedro/blob/main/tests/io/test_data_catalog.py#L599) (Line 599)
- **Target Call:** `self.filesystem.assert_called_once_with` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestDataCatalogFromConfig.test_nested_credentials`
- **Arguments:** `'s3'`
- **Keywords:** `{}`

```python
            }
            mock_client.filesystem.assert_called_once_with(
                "s3", **expected_client_kwargs
            )

```

### Hugging Face Datasets ([huggingface/datasets](https://github.com/huggingface/datasets))
- **Usages Found:** `118` in `25` files.

#### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1851) (Line 1851)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, _ = url_to_fs(dataset_path, **(storage_options or {}))

```

#### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1863) (Line 1863)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python

        fs.makedirs(dataset_path, exist_ok=True)

```

#### 3. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1931) (Line 1931)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
                            pbar.update(content)
        with fs.open(
            posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME), "w", encoding="utf-8"
        ) as state_file:
            json.dump(state, state_file, indent=2, sort_keys=True)
```

#### 4. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1935) (Line 1935)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_INFO_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            json.dump(state, state_file, indent=2, sort_keys=True)
        with fs.open(
            posixpath.join(dataset_path, config.DATASET_INFO_FILENAME), "w", encoding="utf-8"
        ) as dataset_info_file:
            # Sort only the first level of keys, or we might shuffle fields of nested features if we use sort_keys=True
```

#### 5. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2022) (Line 2022)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, dataset_path = url_to_fs(dataset_path, **(storage_options or {}))

```

#### 6. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2029) (Line 2029)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python

        dataset_dict_is_file = fs.isfile(dataset_dict_json_path)
        dataset_info_is_file = fs.isfile(dataset_info_path)
```

#### 7. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2030) (Line 2030)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
        dataset_dict_is_file = fs.isfile(dataset_dict_json_path)
        dataset_info_is_file = fs.isfile(dataset_info_path)
        dataset_state_is_file = fs.isfile(dataset_state_json_path)
```

#### 8. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2031) (Line 2031)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
        dataset_info_is_file = fs.isfile(dataset_info_path)
        dataset_state_is_file = fs.isfile(dataset_state_json_path)
        if not dataset_info_is_file and not dataset_state_is_file:
```

#### 9. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2061) (Line 2061)
- **Target Call:** `fs.download` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `src_dataset_path, dest_dataset_path.as_posix()`
- **Keywords:** `{'recursive': 'True'}`

```python
            dest_dataset_path = Dataset._build_local_temp_path(src_dataset_path)
            fs.download(src_dataset_path, dest_dataset_path.as_posix(), recursive=True)
            dataset_state_json_path = posixpath.join(dest_dataset_path, config.DATASET_STATE_JSON_FILENAME)
```

#### 10. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6754) (Line 6754)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_push_to_repo`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
        hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
        dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 11. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6844) (Line 6844)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_push_to_bucket`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
    hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
    dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 12. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6911) (Line 6911)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    try:
        legacy_dataset_info: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8")).get(
            config_name, None
```

#### 13. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6920) (Line 6920)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.REPOCARD_FILENAME`
- **Keywords:** `{'newline': "''", 'encoding': "'utf-8'"}`

```python
    try:
        dataset_card = DatasetCard(fs.read_text(config.REPOCARD_FILENAME, newline="", encoding="utf-8"))
        dataset_card_data = dataset_card.data
```

#### 14. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6966) (Line 6966)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace('{split}', '*')`
- **Keywords:** `{}`

```python
    pattern = glob_pattern_to_regex(PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED)
    for file_path in fs.glob(PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace("{split}", "*")):
        split_pattern_fields = string_to_dict(file_path, pattern)
```

#### 15. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L7019) (Line 7019)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    if legacy_dataset_info:
        legacy_dataset_infos: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8"))
        legacy_dataset_infos[config_name] = asdict(info_to_dump)
```

#### 16. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L521) (Line 521)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ArrowWriter.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if stream is None:
            fs, path = url_to_fs(path, **(storage_options or {}))
            self._fs: fsspec.AbstractFileSystem = fs
```

#### 17. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L422) (Line 422)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetBuilder.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self._output_dir = self._cache_dir
        self._fs: fsspec.AbstractFileSystem = fsspec.filesystem("file")

```

#### 18. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L789) (Line 789)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetBuilder.download_and_prepare`
- **Arguments:** `output_dir`
- **Keywords:** `{}`

```python
        # output_dir can be a remote bucket on GCS or S3
        fs, output_dir = url_to_fs(output_dir, **(storage_options or {}))
        self._fs = fs
```

#### 19. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L356) (Line 356)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_pattern`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    pattern, storage_options = _prepare_path_and_storage_options(pattern, download_config=download_config)
    fs, fs_pattern = url_to_fs(pattern, **storage_options)
    files_to_ignore = set(FILES_TO_IGNORE) - {xbasename(pattern)}
```

#### 20. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L372) (Line 372)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolve_pattern`
- **Arguments:** `fs_pattern`
- **Keywords:** `{'detail': 'True'}`

```python
    matched_paths = []
    for filepath, info in fs.glob(fs_pattern, detail=True, **glob_kwargs).items():
        if not (info["type"] == "file" or (info.get("islink") and os.path.isfile(os.path.realpath(filepath)))) or (
```

#### 21. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L509) (Line 509)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `data_file`
- **Keywords:** `{}`

```python
        data_file, storage_options = _prepare_path_and_storage_options(data_file, download_config=download_config)
        fs, fs_path = url_to_fs(data_file, **storage_options)
    if isinstance(fs, HfFileSystem):
```

#### 22. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L511) (Line 511)
- **Target Call:** `fs.resolve_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if isinstance(fs, HfFileSystem):
        resolved_path = fs.resolve_path(fs_path)
        if hasattr(resolved_path, "revision"):  # no revision for buckets
```

#### 23. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L514) (Line 514)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            return resolved_path.repo_id, resolved_path.revision
    info = fs.info(fs_path)
    # s3fs uses "ETag", gcsfs uses "etag", and for local we simply check mtime
```

#### 24. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1359) (Line 1359)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, _ = url_to_fs(dataset_dict_path, **(storage_options or {}))

```

#### 25. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1368) (Line 1368)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python

        fs.makedirs(dataset_dict_path, exist_ok=True)

```

#### 26. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1370) (Line 1370)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `posixpath.join(dataset_dict_path, config.DATASETDICT_JSON_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python

        with fs.open(
            posixpath.join(dataset_dict_path, config.DATASETDICT_JSON_FILENAME),
            "w",
            encoding="utf-8",
        ) as f:
            json.dump({"splits": list(self)}, f)
```

#### 27. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1418) (Line 1418)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, dataset_dict_path = url_to_fs(dataset_dict_path, **(storage_options or {}))

```

#### 28. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1423) (Line 1423)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python
        dataset_info_path = posixpath.join(dataset_dict_path, config.DATASET_INFO_FILENAME)
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
```

#### 29. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
                raise FileNotFoundError(
```

#### 30. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
                raise FileNotFoundError(
```

#### 31. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1432) (Line 1432)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python

        with fs.open(dataset_dict_json_path, "r", encoding="utf-8") as f:
            splits = json.load(f)["splits"]
```

#### 32. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1437) (Line 1437)
- **Target Call:** `fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        for k in splits:
            dataset_dict_split_path = posixpath.join(fs.unstrip_protocol(dataset_dict_path), k)
            dataset_dict[k] = Dataset.load_from_disk(
```

#### 33. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2626) (Line 2626)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_push_to_repo`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
        hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
        dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 34. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2713) (Line 2713)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_push_to_bucket`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
    hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
    dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 35. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L196) (Line 196)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                path = url_or_path_join(self._base_path, path)
            fs, path = url_to_fs(path, **download_config.storage_options)
            size = 0
```

#### 36. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L199) (Line 199)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            try:
                size = fs.info(path).get("size", 0)
            except Exception:
```

#### 37. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L27) (Line 27)
- **Target Call:** `fsspec.register_implementation` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `global`
- **Arguments:** `fs_class.protocol, fs_class`
- **Keywords:** `{'clobber': 'True'}`

```python
        warnings.warn(f"A filesystem protocol was already set for {fs_class.protocol} and will be overwritten.")
    fsspec.register_implementation(fs_class.protocol, fs_class, clobber=True)
    for extension in fs_class.extensions:
```

#### 38. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L50) (Line 50)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `rename`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
        # LocalFileSystem.mv does copy + rm, it is more efficient to simply move a local directory
        shutil.move(fs._strip_protocol(src), fs._strip_protocol(dst))
    else:
```

#### 39. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L50) (Line 50)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `rename`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
        # LocalFileSystem.mv does copy + rm, it is more efficient to simply move a local directory
        shutil.move(fs._strip_protocol(src), fs._strip_protocol(dst))
    else:
```

#### 40. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L52) (Line 52)
- **Target Call:** `fs.mv` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `rename`
- **Arguments:** `src, dst`
- **Keywords:** `{'recursive': 'True'}`

```python
    else:
        fs.mv(src, dst, recursive=True)
```

#### 41. [src/datasets/filesystems/compression.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/compression.py#L66) (Line 66)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `BaseCompressedFileFileSystem._get_dirs`
- **Arguments:** `self.fo`
- **Keywords:** `{}`

```python
        if self.dir_cache is None:
            f = {**self._open_with_fsspec().fs.info(self.fo), "name": self.uncompressed_name}
            self.dir_cache = {f["name"]: f}
```

#### 42. [src/datasets/hub.py](https://github.com/huggingface/datasets/blob/main/src/datasets/hub.py#L44) (Line 44)
- **Target Call:** `fs.resolve_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `delete_from_hub`
- **Arguments:** `data_file`
- **Keywords:** `{}`

```python
    for data_file in chain(*builder.config.data_files.values()):
        data_file_resolved_path = fs.resolve_path(data_file)
        if data_file_resolved_path.repo_id == repo_id:
```

#### 43. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L208) (Line 208)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "wb") as f:
```

#### 44. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L209) (Line 209)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "wb") as f:
            self._dump_info(f, pretty_print=pretty_print)
```

#### 45. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L212) (Line 212)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
        if self.license:
            with fs.open(posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), "wb") as f:
                self._dump_license(f)
```

#### 46. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L273) (Line 273)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        logger.debug(f"Loading Dataset info from {dataset_info_dir}")
```

#### 47. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L277) (Line 277)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            raise ValueError("Calling DatasetInfo.from_directory() with undefined dataset_info_dir.")
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "r", encoding="utf-8") as f:
            dataset_info_dict = json.load(f)
```

#### 48. [src/datasets/io/csv.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L94) (Line 94)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `CsvDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
        if isinstance(self.path_or_buf, (str, bytes, os.PathLike)):
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
                written = self._write(file_obj=buffer, header=header, index=index, **self.to_csv_kwargs)
```

#### 49. [src/datasets/io/json.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L113) (Line 113)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `JsonDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{'compression': 'compression'}`

```python
        if isinstance(self.path_or_buf, (str, bytes, os.PathLike)):
            with fsspec.open(
                self.path_or_buf, "wb", compression=compression, **(self.storage_options or {})
            ) as buffer:
                written = self._write(file_obj=buffer, orient=orient, lines=lines, **self.to_json_kwargs)
```

#### 50. [src/datasets/io/parquet.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/parquet.py#L100) (Line 100)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `ParquetDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
        if isinstance(self.path_or_buf, (str, bytes, os.PathLike)):
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
                written = self._write(
```

#### 51. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1768) (Line 1768)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    fs: fsspec.AbstractFileSystem
    fs, *_ = url_to_fs(dataset_path, **(storage_options or {}))
    if not fs.exists(dataset_path):
```

#### 52. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1769) (Line 1769)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    fs, *_ = url_to_fs(dataset_path, **(storage_options or {}))
    if not fs.exists(dataset_path):
        raise FileNotFoundError(f"Directory {dataset_path} not found")
```

#### 53. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1771) (Line 1771)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)`
- **Keywords:** `{}`

```python
        raise FileNotFoundError(f"Directory {dataset_path} not found")
    if fs.isfile(posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)) and fs.isfile(
        posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)
```

#### 54. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1771) (Line 1771)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)`
- **Keywords:** `{}`

```python
        raise FileNotFoundError(f"Directory {dataset_path} not found")
    if fs.isfile(posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)) and fs.isfile(
        posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)
    ):
        return Dataset.load_from_disk(dataset_path, keep_in_memory=keep_in_memory, storage_options=storage_options)
```

#### 55. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1775) (Line 1775)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)`
- **Keywords:** `{}`

```python
        return Dataset.load_from_disk(dataset_path, keep_in_memory=keep_in_memory, storage_options=storage_options)
    elif fs.isfile(posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)):
        return DatasetDict.load_from_disk(dataset_path, keep_in_memory=keep_in_memory, storage_options=storage_options)
```

#### 56. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L396) (Line 396)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FaissIndex.save`
- **Arguments:** `str(file), 'wb'`
- **Keywords:** `{}`

```python

        with fsspec.open(str(file), "wb", **(storage_options or {})) as f:
            faiss.write_index(index, faiss.BufferedIOWriter(faiss.PyCallbackIOWriter(f.write)))
```

#### 57. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L411) (Line 411)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `FaissIndex.load`
- **Arguments:** `str(file), 'rb'`
- **Keywords:** `{}`

```python
        faiss_index = cls(device=device)
        with fsspec.open(str(file), "rb", **(storage_options or {})) as f:
            index = faiss.read_index(faiss.BufferedIOReader(faiss.PyCallbackIOReader(f.read)))
```

#### 58. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L166) (Line 166)
- **Target Call:** `can_be_local` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `cached_path`
- **Arguments:** `url_or_filename`
- **Keywords:** `{}`

```python
    # Convert fsspec URL in the format "file://local/path" to "local/path"
    if can_be_local(url_or_filename):
        url_or_filename = strip_protocol(url_or_filename)
```

#### 59. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L167) (Line 167)
- **Target Call:** `strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `cached_path`
- **Arguments:** `url_or_filename`
- **Keywords:** `{}`

```python
    if can_be_local(url_or_filename):
        url_or_filename = strip_protocol(url_or_filename)

```

#### 60. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L295) (Line 295)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspec_head`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    _raise_if_offline_mode_is_enabled(f"Tried to reach {url}")
    fs, path = url_to_fs(url, **(storage_options or {}))
    return fs.info(path)
```

#### 61. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L296) (Line 296)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspec_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    fs, path = url_to_fs(url, **(storage_options or {}))
    return fs.info(path)

```

#### 62. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L317) (Line 317)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspec_get`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    _raise_if_offline_mode_is_enabled(f"Tried to reach {url}")
    fs, path = url_to_fs(url, **(storage_options or {}))
    callback = TqdmCallback(
```

#### 63. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L330) (Line 330)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `fsspec_get`
- **Arguments:** `path, temp_file.name`
- **Keywords:** `{'callback': 'callback'}`

```python
    )
    fs.get_file(path, temp_file.name, callback=callback)

```

#### 64. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L559) (Line 559)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_get_extraction_protocol`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
    try:
        with fsspec.open(urlpath, **(storage_options or {})) as f:
            return _get_extraction_protocol_with_magic_number(f)
```

#### 65. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L645) (Line 645)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xexists`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        return fs.exists(main_hop)
```

#### 66. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L646) (Line 646)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xexists`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(urlpath, **storage_options)
        return fs.exists(main_hop)

```

#### 67. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L745) (Line 745)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xisfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = url_to_fs(path, **storage_options)
        return fs.isfile(main_hop)
```

#### 68. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L746) (Line 746)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xisfile`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(path, **storage_options)
        return fs.isfile(main_hop)

```

#### 69. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L765) (Line 765)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xgetsize`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
        try:
```

#### 70. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L767) (Line 767)
- **Target Call:** `fs.size` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xgetsize`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        try:
            size = fs.size(main_hop)
        except huggingface_hub.utils.EntryNotFoundError:
```

#### 71. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L793) (Line 793)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xisdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 72. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L797) (Line 797)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xisdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
            return True
        return fs.isdir(inner_path)

```

#### 73. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L913) (Line 913)
- **Target Call:** `fsspec.available_protocols` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_prepare_single_hop_path_and_storage_options`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            for option_name, option_value in download_config.storage_options.items()
            if option_name not in fsspec.available_protocols()
        }
```

#### 74. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L977) (Line 977)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xopen`
- **Arguments:** `file, mode`
- **Keywords:** `{'storage_options': 'kwargs'}`

```python
        try:
            fs, fs_token, paths = fsspec.get_fs_token_paths(
                file,
                mode,
                storage_options=kwargs,
            )
            file_obj = fs.open(paths[0], mode)
```

#### 75. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L982) (Line 982)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xopen`
- **Arguments:** `paths[0], mode`
- **Keywords:** `{}`

```python
            )
            file_obj = fs.open(paths[0], mode)
            if hasattr(fs, "of") and hasattr(fs.of, "__exit__"):
```

#### 76. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1030) (Line 1030)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xlistdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = url_to_fs(path, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 77. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1032) (Line 1032)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[-1]
        if inner_path.strip("/") and not fs.isdir(inner_path):
            raise FileNotFoundError(f"Directory doesn't exist: {path}")
```

#### 78. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1034) (Line 1034)
- **Target Call:** `fs.listdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{'detail': 'False'}`

```python
            raise FileNotFoundError(f"Directory doesn't exist: {path}")
        paths = fs.listdir(inner_path, detail=False)
        return [os.path.basename(path.rstrip("/")) for path in paths]
```

#### 79. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1057) (Line 1057)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xglob`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        inner_path = main_hop.split("://")[1]
```

#### 80. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1059) (Line 1059)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xglob`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[1]
        globbed_paths = fs.glob(inner_path)
        protocol = fs.protocol if isinstance(fs.protocol, str) else fs.protocol[-1]
```

#### 81. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1083) (Line 1083)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xwalk`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 82. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1085) (Line 1085)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[-1]
        if inner_path.strip("/") and not fs.isdir(inner_path):
            return []
```

#### 83. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1088) (Line 1088)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        protocol = fs.protocol if isinstance(fs.protocol, str) else fs.protocol[-1]
        for dirpath, dirnames, filenames in fs.walk(inner_path, **kwargs):
            yield "::".join([f"{protocol}://{dirpath}"] + rest_hops), dirnames, filenames
```

#### 84. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1161) (Line 1161)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(posix_path, pattern)`
- **Keywords:** `{}`

```python
                storage_options = None
            fs, *_ = url_to_fs(xjoin(posix_path, pattern), **(storage_options or {}))
            globbed_paths = fs.glob(xjoin(main_hop, pattern))
```

#### 85. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1162) (Line 1162)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(main_hop, pattern)`
- **Keywords:** `{}`

```python
            fs, *_ = url_to_fs(xjoin(posix_path, pattern), **(storage_options or {}))
            globbed_paths = fs.glob(xjoin(main_hop, pattern))
            for globbed_path in globbed_paths:
```

#### 86. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L15) (Line 15)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MockFileSystem.__init__`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
        super().__init__()
        self._fs = LocalFileSystem(*args, **kwargs)
        self.local_root_dir = Path(local_root_dir).resolve().as_posix() + "/"
```

#### 87. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L71) (Line 71)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `MockFileSystem._strip_protocol`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def _strip_protocol(cls, path):
        path = stringify_path(path)
        if path.startswith("mock://"):
```

#### 88. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L87) (Line 87)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TmpDirFileSystem._strip_protocol`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def _strip_protocol(cls, path):
        path = stringify_path(path)
        if path.startswith("tmp://"):
```

#### 89. [tests/io/test_csv.py](https://github.com/huggingface/datasets/blob/main/tests/io/test_csv.py#L174) (Line 174)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dataset_to_csv_fsspec`
- **Arguments:** `dataset_path, 'rb'`
- **Keywords:** `{}`

```python

    with fsspec.open(dataset_path, "rb", **mockfs.storage_options) as f:
        assert f.read()
```

#### 90. [tests/io/test_json.py](https://github.com/huggingface/datasets/blob/main/tests/io/test_json.py#L294) (Line 294)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestJsonDatasetWriter.test_dataset_to_json_compression`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{'compression': "'infer'"}`

```python

        with fsspec.open(path, "rb", compression="infer") as f:
            exported_content = f.read()
```

#### 91. [tests/io/test_json.py](https://github.com/huggingface/datasets/blob/main/tests/io/test_json.py#L296) (Line 296)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestJsonDatasetWriter.test_dataset_to_json_compression`
- **Arguments:** `original_path, 'rb'`
- **Keywords:** `{'compression': "'infer'"}`

```python
            exported_content = f.read()
        with fsspec.open(original_path, "rb", compression="infer") as f:
            original_content = f.read()
```

#### 92. [tests/io/test_json.py](https://github.com/huggingface/datasets/blob/main/tests/io/test_json.py#L306) (Line 306)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `TestJsonDatasetWriter.test_dataset_to_json_fsspec`
- **Arguments:** `dataset_path, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(dataset_path, "rb", **mockfs.storage_options) as f:
            assert f.read()
```

#### 93. [tests/io/test_parquet.py](https://github.com/huggingface/datasets/blob/main/tests/io/test_parquet.py#L310) (Line 310)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_dataset_to_parquet_fsspec`
- **Arguments:** `dataset_path, 'rb'`
- **Keywords:** `{}`

```python

    with fsspec.open(dataset_path, "rb", **mockfs.storage_options) as f:
        assert f.read()
```

#### 94. [tests/test_arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/tests/test_arrow_dataset.py#L4539) (Line 4539)
- **Target Call:** `strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_build_local_temp_path`
- **Arguments:** `uri_or_path`
- **Keywords:** `{}`

```python
def test_build_local_temp_path(uri_or_path):
    extracted_path = strip_protocol(uri_or_path)
    local_temp_path = Dataset._build_local_temp_path(extracted_path).as_posix()
```

#### 95. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L29) (Line 29)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `_load_bucket_module`
- **Arguments:** ``
- **Keywords:** `{'skip_instance_cache': 'True'}`

```python
    # resolution so only the card / metadata handling under test runs for real
    mem = MemoryFileSystem(skip_instance_cache=True)
    # Write files with full paths relative to the bucket path (forward slashes for MemoryFileSystem)
```

#### 96. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L112) (Line 112)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_returns_legacy_infos_as_dict`
- **Arguments:** ``
- **Keywords:** `{'skip_instance_cache': 'True'}`

```python
def test_get_updated_dataset_card_returns_legacy_infos_as_dict():
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/repo", fs=mem)
```

#### 97. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L113) (Line 113)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_returns_legacy_infos_as_dict`
- **Arguments:** `'/repo'`
- **Keywords:** `{'fs': 'mem'}`

```python
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/repo", fs=mem)

```

#### 98. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L120) (Line 120)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_returns_legacy_infos_as_dict`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME, 'w'`
- **Keywords:** `{}`

```python
    }
    with fs.open(config.DATASETDICT_INFOS_FILENAME, "w") as f:
        f.write(json.dumps(existing))
```

#### 99. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L143) (Line 143)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_drops_removed_splits_when_replacing_split_set`
- **Arguments:** ``
- **Keywords:** `{'skip_instance_cache': 'True'}`

```python
def test_get_updated_dataset_card_drops_removed_splits_when_replacing_split_set():
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/shrink", fs=mem)
```

#### 100. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L144) (Line 144)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_drops_removed_splits_when_replacing_split_set`
- **Arguments:** `'/shrink'`
- **Keywords:** `{'fs': 'mem'}`

```python
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/shrink", fs=mem)

```

#### 101. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L146) (Line 146)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_drops_removed_splits_when_replacing_split_set`
- **Arguments:** `config.REPOCARD_FILENAME, 'w'`
- **Keywords:** `{}`

```python

    with fs.open(config.REPOCARD_FILENAME, "w") as f:
        f.write(
```

#### 102. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L176) (Line 176)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_keeps_existing_splits_when_appending`
- **Arguments:** ``
- **Keywords:** `{'skip_instance_cache': 'True'}`

```python
def test_get_updated_dataset_card_keeps_existing_splits_when_appending():
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/append", fs=mem)
```

#### 103. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L177) (Line 177)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_keeps_existing_splits_when_appending`
- **Arguments:** `'/append'`
- **Keywords:** `{'fs': 'mem'}`

```python
    mem = MemoryFileSystem(skip_instance_cache=True)
    fs = DirFileSystem("/append", fs=mem)

```

#### 104. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L179) (Line 179)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_updated_dataset_card_keeps_existing_splits_when_appending`
- **Arguments:** `config.REPOCARD_FILENAME, 'w'`
- **Keywords:** `{}`

```python

    with fs.open(config.REPOCARD_FILENAME, "w") as f:
        f.write(README_WITH_CONFIG)
```

#### 105. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L104) (Line 104)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `pattern_results`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
            Path(os.path.abspath(path)).as_posix()
            for path in fsspec.filesystem("file").glob(os.path.join(complex_data_dir, pattern))
            if Path(path).name not in _FILES_TO_IGNORE
```

#### 106. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L669) (Line 669)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolver`
- **Arguments:** `base_path`
- **Keywords:** `{}`

```python
        return [
            file_path[len(fs._strip_protocol(base_path)) :].lstrip("/")
            for file_path in fs.glob(pattern)
```

#### 107. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L670) (Line 670)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolver`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
            file_path[len(fs._strip_protocol(base_path)) :].lstrip("/")
            for file_path in fs.glob(pattern)
            if fs.isfile(file_path)
```

#### 108. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L671) (Line 671)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `resolver`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
            for file_path in fs.glob(pattern)
            if fs.isfile(file_path)
        ]
```

#### 109. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L679) (Line 679)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_data_files_patterns`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
        expected = [
            fs._strip_protocol(file_path)[len(fs._strip_protocol(base_path)) :].lstrip("/")
            for file_path in data_file_per_split[split]
```

#### 110. [tests/test_data_files.py](https://github.com/huggingface/datasets/blob/main/tests/test_data_files.py#L679) (Line 679)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_get_data_files_patterns`
- **Arguments:** `base_path`
- **Keywords:** `{}`

```python
        expected = [
            fs._strip_protocol(file_path)[len(fs._strip_protocol(base_path)) :].lstrip("/")
            for file_path in data_file_per_split[split]
```

#### 111. [tests/test_dataset_dict.py](https://github.com/huggingface/datasets/blob/main/tests/test_dataset_dict.py#L429) (Line 429)
- **Target Call:** `MemoryFileSystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `DatasetDictTest.test_iterable_dataset_dict_push_to_hub_forwards_max_shard_size_to_each_split`
- **Arguments:** ``
- **Keywords:** `{'skip_instance_cache': 'True'}`

```python

        dummy_fs = MemoryFileSystem(skip_instance_cache=True)
        dummy_fs.touch("datasets/user/dataset@dummy-sha/README.md")
```

#### 112. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L27) (Line 27)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_is_remote_filesystem`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python

    fs = fsspec.filesystem("file")

```

#### 113. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L44) (Line 44)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_compression_filesystems`
- **Arguments:** `compression_fs_class.protocol`
- **Keywords:** `{'fo': 'input_path'}`

```python
        pytest.skip(reason)
    fs = fsspec.filesystem(compression_fs_class.protocol, fo=input_path)
    expected_filename = os.path.basename(input_path)
```

#### 114. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L47) (Line 47)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_compression_filesystems`
- **Arguments:** `'*'`
- **Keywords:** `{}`

```python
    expected_filename = expected_filename[: expected_filename.rindex(".")]
    assert fs.glob("*") == [expected_filename]
    with fs.open(expected_filename, "r", encoding="utf-8") as f, open(text_file, encoding="utf-8") as expected_file:
```

#### 115. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L48) (Line 48)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_compression_filesystems`
- **Arguments:** `expected_filename, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    assert fs.glob("*") == [expected_filename]
    with fs.open(expected_filename, "r", encoding="utf-8") as f, open(text_file, encoding="utf-8") as expected_file:
        assert f.read() == expected_file.read()
```

#### 116. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L58) (Line 58)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fs_isfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = f"{protocol}://{member_file_path}::{compressed_file_path}"
    fs, *_ = url_to_fs(path)
    assert fs.isfile(member_file_path)
```

#### 117. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L59) (Line 59)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fs_isfile`
- **Arguments:** `member_file_path`
- **Keywords:** `{}`

```python
    fs, *_ = url_to_fs(path)
    assert fs.isfile(member_file_path)
    assert not fs.isfile("non_existing_" + member_file_path)
```

#### 118. [tests/test_filesystem.py](https://github.com/huggingface/datasets/blob/main/tests/test_filesystem.py#L60) (Line 60)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT`
- **Context:** `test_fs_isfile`
- **Arguments:** `'non_existing_' + member_file_path`
- **Keywords:** `{}`

```python
    assert fs.isfile(member_file_path)
    assert not fs.isfile("non_existing_" + member_file_path)
```
