# Master FSSPEC Usage Report Across 12 Major Python Ecosystem & AI Repositories

- **Repositories Crawled:** `12`
- **Total Files Scanned:** `9645`
- **Files with FSSPEC Usages:** `167`
- **Total FSSPEC Usages Detected:** `867`
- **Time Elapsed:** `459.47 seconds`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project Name | Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dask** | [dask/dask](https://github.com/dask/dask) | `201` | `15` | `79` | `NOT_EXPLICIT:77, parts:2` |
| **Intake** | [intake/intake](https://github.com/intake/intake) | `71` | `15` | `86` | `NOT_EXPLICIT:86` |
| **pandas** | [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `538` | `2` | `4` | `NOT_EXPLICIT:4` |
| **xarray** | [pydata/xarray](https://github.com/pydata/xarray) | `162` | `1` | `5` | `NOT_EXPLICIT:5` |
| **zarr** | [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `238` | `1` | `18` | `NOT_EXPLICIT:18` |
| **DVC** | [iterative/dvc](https://github.com/iterative/dvc) | `326` | `55` | `326` | `NOT_EXPLICIT:326` |
| **Kedro** | [kedro-org/kedro](https://github.com/kedro-org/kedro) | `152` | `1` | `4` | `NOT_EXPLICIT:4` |
| **Hugging Face Datasets** | [huggingface/datasets](https://github.com/huggingface/datasets) | `162` | `17` | `88` | `NOT_EXPLICIT:88` |
| **PyTorch** | [pytorch/pytorch](https://github.com/pytorch/pytorch) | `3412` | `6` | `38` | `NOT_EXPLICIT:38` |
| **PyTorch Lightning** | [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | `767` | `17` | `69` | `NOT_EXPLICIT:69` |
| **TorchTitan** | [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | `330` | `3` | `27` | `NOT_EXPLICIT:27` |
| **Ray** | [ray-project/ray](https://github.com/ray-project/ray) | `3286` | `34` | `123` | `NOT_EXPLICIT:123` |

---

## 📈 Global Cache_Type Breakdown

| Cache_Type Option | Total Occurrences | Is Specified Keyword | Description |
| :--- | :--- | :--- | :--- |
| `NOT_EXPLICIT` | `865` | `False` | cache_type keyword omitted (uses default fsspec strategy) |
| `parts` | `2` | `True` | Parquet section/column block caching (required for fsspec.parquet precaching) |

---

## 🔍 Detailed Usage Breakdown by Repository

### Dask ([dask/dask](https://github.com/dask/dask))
- **Usages Found:** `79` in `15` files.

#### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L67) (Line 67)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `open_head`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
    """Open a file just to read its head and size"""
    with OpenFile(fs, path, compression=compression) as f:
        head = read_header(f)
```

#### 2. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L69) (Line 69)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `open_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        head = read_header(f)
    size = fs.info(path)["size"]
    return head, size
```

#### 3. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L104) (Line 104)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_avro`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
            delimiter = head["sync"]
            f = OpenFile(fs, path, compression=compression)
            token = fs_tokenize(
```

#### 5. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L124) (Line 124)
- **Target Call:** `fs_tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.ukey` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_avro`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            token = fs_tokenize(
                fs_token, delimiter, path, fs.ukey(path), compression, offset
            )
```

#### 7. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L136) (Line 136)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_avro`
- **Arguments:** `urlpath`
- **Keywords:** `{'compression': 'compression'}`

```python
    else:
        files = open_files(urlpath, compression=compression, **storage_options)
        dread = delayed(read_file)
```

#### 8. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L152) (Line 152)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_chunk`
- **Arguments:** `f, off, l, head['sync']`
- **Keywords:** `{}`

```python
    with fobj as f:
        chunk = read_block(f, off, l, head["sync"])
    head_bytes = head["head_bytes"]
```

#### 9. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L256) (Line 256)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'kwargs'}`

```python

    fs, fs_token, paths = get_fs_token_paths(urlpath, mode="rb", storage_options=kwargs)

```

#### 13. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L103) (Line 103)
- **Target Call:** `infer_compression` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if compression == "infer":
                comp = infer_compression(path)
            else:
```

#### 14. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L111) (Line 111)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                )
            size = fs.info(path)["size"]
            if size is None:
```

#### 15. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L149) (Line 149)
- **Target Call:** `fs.ukey` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    for path, offset, length in zip(paths, offsets, lengths):
        token = tokenize(fs_token, delimiter, path, fs.ukey(path), compression, offset)
        keys = [f"read-block-{o}-{token}" for o in offset]
```

#### 16. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L153) (Line 153)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `fs, path`
- **Keywords:** `{'compression': 'compression'}`

```python
            delayed_read(
                OpenFile(fs, path, compression=compression),
                o,
```

#### 17. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L168) (Line 168)
- **Target Call:** `OpenFile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_bytes`
- **Arguments:** `fs, paths[0]`
- **Keywords:** `{'compression': 'compression'}`

```python
            sample = parse_bytes(sample)
        with OpenFile(fs, paths[0], compression=compression) as f:
            # read block without seek (because we start at zero)
```

#### 18. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L194) (Line 194)
- **Target Call:** `read_block` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_block_from_file`
- **Arguments:** `f, off, bs, delimiter`
- **Keywords:** `{}`

```python
            return f.read()
        return read_block(f, off, bs, delimiter)
```

#### 19. [dask/dataframe/dask_expr/_collection.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5359) (Line 5359)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if not isinstance(path, str):
        path = stringify_path(path)

```

#### 20. [dask/dataframe/dask_expr/_collection.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5374) (Line 5374)
- **Target Call:** `filesystem.lower` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_parquet`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        or isinstance(filesystem, str)
        and filesystem.lower() in ("arrow", "pyarrow")
    ):
```

#### 21. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L140) (Line 140)
- **Target Call:** `fs.equals` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FragmentWrapper.pack`
- **Arguments:** `self._fragment.filesystem`
- **Keywords:** `{}`

```python
            fs = self._filesystem or self._fragment.filesystem
            assert fs.equals(self._fragment.filesystem)
            if self._filesystem_pickle_cache[0] != id(fs):
```

#### 22. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L489) (Line 489)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if hasattr(path, "name"):
        path = stringify_path(path)

```

#### 23. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if fs.exists(path) and fs.isdir(path):
            # Check for any previous parquet ops reading from a file in the
```

#### 24. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if fs.exists(path) and fs.isdir(path):
            # Check for any previous parquet ops reading from a file in the
```

#### 25. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L520) (Line 520)
- **Target Call:** `fs.expand_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `'.'`
- **Keywords:** `{}`

```python
            if _is_local_fs(fs):
                working_dir = fs.expand_path(".")[0]
                if path.rstrip("/") == working_dir.rstrip("/"):
```

#### 26. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L527) (Line 527)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
            # It's safe to clear the output directory
            fs.rm(path, recursive=True)

```

#### 27. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L666) (Line 666)
- **Target Call:** `fs.invalidate_cache` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # that reading files that were just written succeeds.
    fs.invalidate_cache(path)

```

#### 28. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1023) (Line 1023)
- **Target Call:** `self.fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ReadParquetPyarrowFS._dataset_info`
- **Arguments:** `dataset_selector`
- **Keywords:** `{}`

```python
                        finfo
                        for finfo in self.fs.get_file_info(dataset_selector)
                        if finfo.type == pa.fs.FileType.File
```

#### 29. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1028) (Line 1028)
- **Target Call:** `self.fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ReadParquetPyarrowFS._dataset_info`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        except (NotADirectoryError, FileNotFoundError):
            all_files = [self.fs.get_file_info(path) for path in path_normalized]
        # TODO: At this point we could verify if we're dealing with a very
```

#### 30. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1394) (Line 1394)
- **Target Call:** `fs.checksum` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ReadParquetFSSpec._dataset_info`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            # _collect_dataset_info
            checksum.append(fs.checksum(file))
        dataset_info["checksum"] = tokenize(checksum)
```

#### 31. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1781) (Line 1781)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_partition_stats`
- **Arguments:** `path`
- **Keywords:** `{'default_cache': "'none'"}`

```python
            row_groups = None if piece[1] == [None] else piece[1]
            with fs.open(path, default_cache="none") as f:
                md = pq.ParquetFile(f).metadata
```

#### 32. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L488) (Line 488)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_pandas`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        # Translate the input urlpath to a simple path list
        paths = get_fs_token_paths(urlpath, mode="rb", storage_options=storage_options)[
            2
```

#### 33. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L497) (Line 497)
- **Target Call:** `infer_compression` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_pandas`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        # Infer compression from first path
        compression = infer_compression(paths[0])

```

#### 34. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L911) (Line 911)
- **Target Call:** `open_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'mode'}`

```python
    if single_file:
        first_file = open_file(filename, mode=mode, **file_options)
        value = to_csv_chunk(dfs[0], first_file, **kwargs)
```

#### 35. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L915) (Line 915)
- **Target Call:** `open_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'append_mode'}`

```python
        append_mode = append_mode.replace("w", "").replace("x", "")
        append_file = open_file(filename, mode=append_mode, **file_options)
        kwargs["header"] = False
```

#### 36. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L922) (Line 922)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 37. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L147) (Line 147)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_hdf`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

    path = stringify_path(path)

```

#### 38. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L176) (Line 176)
- **Target Call:** `build_name_function` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_hdf`
- **Arguments:** `df.npartitions - 1`
- **Keywords:** `{}`

```python
    if name_function is None:
        name_function = build_name_function(df.npartitions - 1)

```

#### 39. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L381) (Line 381)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_hdf`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    # Convert path-like objects to a string
    pattern = stringify_path(pattern)

```

#### 40. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L78) (Line 78)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 41. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L268) (Line 268)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 42. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L23) (Line 23)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        # TODO: Handle hive-partitioned data
        if len(paths) == 1 and not fs.isfile(paths[0]):
            paths = fs.find(paths[0])
```

#### 43. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L24) (Line 24)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        if len(paths) == 1 and not fs.isfile(paths[0]):
            paths = fs.find(paths[0])

```

#### 44. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L39) (Line 39)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
            for path in paths:
                with fs.open(path, "rb") as f:
                    o = orc.ORCFile(f)
```

#### 45. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L60) (Line 60)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0], 'rb'`
- **Keywords:** `{}`

```python
                if schema is None:
                    with fs.open(paths[0], "rb") as f:
                        o = orc.ORCFile(f)
```

#### 46. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L111) (Line 111)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowORCEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
        table = pa.Table.from_pandas(df)
        with fs.open(fs.sep.join([path, filename]), "wb") as f:
            orc.write_table(table, f)
```

#### 47. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L122) (Line 122)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_orc_stripes`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    batches = []
    with fs.open(path, "rb") as f:
        o = orc.ORCFile(f)
```

#### 48. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L81) (Line 81)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
    storage_options = storage_options or {}
    fs, fs_token, paths = get_fs_token_paths(
        path, mode="rb", storage_options=storage_options
    )

```

#### 49. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L174) (Line 174)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if hasattr(path, "name"):
        path = stringify_path(path)
    fs, _, _ = get_fs_token_paths(path, mode="wb", storage_options=storage_options)
```

#### 50. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L175) (Line 175)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wb'", 'storage_options': 'storage_options'}`

```python
        path = stringify_path(path)
    fs, _, _ = get_fs_token_paths(path, mode="wb", storage_options=storage_options)
    # Trim any protocol information from the path before forwarding
```

#### 51. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L177) (Line 177)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # Trim any protocol information from the path before forwarding
    path = fs._strip_protocol(path)

```

#### 52. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L184) (Line 184)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    # Use df.npartitions to define file-name list
    fs.mkdirs(path, exist_ok=True)
    filenames = [f"part.{i}.orc" for i in range(df.npartitions)]
```

#### 53. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L112) (Line 112)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_write_partitioned`
- **Arguments:** `root_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    """
    fs.mkdirs(root_path, exist_ok=True)

```

#### 54. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L148) (Line 148)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_write_partitioned`
- **Arguments:** `prefix`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        prefix = fs.sep.join([root_path, subdir])
        fs.mkdirs(prefix, exist_ok=True)
        full_path = fs.sep.join([prefix, filename])
```

#### 55. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L150) (Line 150)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_write_partitioned`
- **Arguments:** `full_path, 'wb'`
- **Keywords:** `{}`

```python
        full_path = fs.sep.join([prefix, filename])
        with fs.open(full_path, "wb") as f:
            pq.write_table(
```

#### 56. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L470) (Line 470)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                    raise ValueError("empty urlpath sequence")
                urlpath = [stringify_path(u) for u in urlpath]
            else:
```

#### 57. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L472) (Line 472)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
            else:
                urlpath = [stringify_path(urlpath)]

```

#### 58. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L483) (Line 483)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `fs`
- **Keywords:** `{}`

```python

            fsspec_fs = ArrowFSWrapper(fs)
            if urlpath[0].startswith("C:") and isinstance(fs, pa_fs.LocalFileSystem):
```

#### 59. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L489) (Line 489)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python

                fs_strip = LocalFileSystem()
            else:
```

#### 60. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L492) (Line 492)
- **Target Call:** `expand_paths_if_needed` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fsspec_fs, None`
- **Keywords:** `{}`

```python
                fs_strip = fsspec_fs
            paths = expand_paths_if_needed(urlpath, "rb", 1, fsspec_fs, None)
            return (
```

#### 61. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L670) (Line 670)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        # Check that target directory exists
        fs.mkdirs(path, exist_ok=True)
        if append and division_info is None:
```

#### 62. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L684) (Line 684)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `fs.sep.join([path, '_metadata'])`
- **Keywords:** `{'mode': "'rb'"}`

```python
                try:
                    with fs.open(fs.sep.join([path, "_metadata"]), mode="rb") as fil:
                        full_metadata = pq.read_metadata(fil)
```

#### 63. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L690) (Line 690)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 64. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L851) (Line 851)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
            md_list = []
            with fs.open(fs.sep.join([path, filename]), "wb") as fil:
                pq.write_table(
```

#### 65. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L882) (Line 882)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `common_metadata_path, 'wb'`
- **Keywords:** `{}`

```python
                kwargs_meta = {k: v for k, v in kwargs.items() if k in keywords}
                with fs.open(common_metadata_path, "wb") as fil:
                    pq.write_metadata(schema, fil, **kwargs_meta)
```

#### 66. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L895) (Line 895)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
                _append_row_groups(_meta, parts[i][0]["meta"])
            with fs.open(metadata_path, "wb") as fil:
                _meta.write_metadata_file(fil)
```

#### 67. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L940) (Line 940)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        has_metadata_file = False
        if len(paths) == 1 and fs.isdir(paths[0]):
            # Use _analyze_paths to avoid relative-path
```

#### 68. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L947) (Line 947)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `meta_path`
- **Keywords:** `{}`

```python
            meta_path = fs.sep.join([paths, "_metadata"])
            if not ignore_metadata_file and fs.exists(meta_path):
                # Use _metadata file
```

#### 69. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L961) (Line 961)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths`
- **Keywords:** `{}`

```python
                    path
                    for path in fs.find(paths)
                    if path.endswith(parquet_file_extension)
```

#### 70. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1820) (Line 1820)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.collect_file_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    def collect_file_metadata(cls, path, fs, file_path):
        with fs.open(path, "rb") as f:
            meta = pq.ParquetFile(f).metadata
```

#### 71. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1836) (Line 1836)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowDatasetEngine.aggregate_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
            metadata_path = fs.sep.join([out_path, "_metadata"])
            with fs.open(metadata_path, "wb") as fil:
                if not meta:
```

#### 72. [dask/dataframe/io/parquet/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/core.py#L289) (Line 289)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 73. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L72) (Line 72)
- **Target Call:** `get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 74. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L95) (Line 95)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                    raise ValueError("empty urlpath sequence")
                urlpath = [stringify_path(u) for u in urlpath]
            else:
```

#### 75. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L97) (Line 97)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
            else:
                urlpath = [stringify_path(urlpath)]

```

#### 76. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L99) (Line 99)
- **Target Call:** `expand_paths_if_needed` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fs, None`
- **Keywords:** `{}`

```python

            paths = expand_paths_if_needed(urlpath, "rb", 1, fs, None)
            return (
```

#### 77. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L102) (Line 102)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                fs,
                [fs._strip_protocol(u) for u in paths],
                dataset_options,
```

#### 78. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L210) (Line 210)
- **Target Call:** `fsspec_parquet.open_parquet_file` | **Cache_Type:** `parts` | **Is Specified Keyword:** `True`
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

#### 79. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L221) (Line 221)
- **Target Call:** `fs.open` | **Cache_Type:** `parts` | **Is Specified Keyword:** `True`
- **Context:** `_open_input_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    elif fs is not None:
        return [_set_context(fs.open(path, **kwargs), context_stack) for path in paths]
    return [_set_context(open(path, **kwargs), context_stack) for path in paths]
```

### Intake ([intake/intake](https://github.com/intake/intake))
- **Usages Found:** `86` in `15` files.

#### 1. [intake/catalog/base.py](https://github.com/intake/intake/blob/master/intake/catalog/base.py#L341) (Line 341)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Catalog.save`
- **Arguments:** `[url]`
- **Keywords:** `{'mode': "'wt'"}`

```python

        with open_files([url], **(storage_options or {}), mode="wt")[0] as f:
            f.write(self.serialize())
```

#### 2. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L575) (Line 575)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if "://" in path:
        protocol, _ = split_protocol(path)
        out = get_filesystem_class(protocol)._parent(path)
```

#### 3. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L576) (Line 576)
- **Target Call:** `get_filesystem_class` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_dir`
- **Arguments:** `protocol`
- **Keywords:** `{}`

```python
        protocol, _ = split_protocol(path)
        out = get_filesystem_class(protocol)._parent(path)
        if "://" not in out:
```

#### 4. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L639) (Line 639)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
            elif self.filesystem is None:
                file_open = open_files(self.path, mode="rb", **options)
                assert len(file_open) == 1
```

#### 5. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L644) (Line 644)
- **Target Call:** `self.filesystem.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
            else:
                file_open = self.filesystem.open(self.path, mode="rb")
            self._dir = get_dir(self.path)
```

#### 6. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L690) (Line 690)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[self.path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            options = self.storage_options or {}
            file_open = open_files([self.path], mode="wt", **options)
        else:
```

#### 7. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L693) (Line 693)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            options = storage_options or {}
            file_open = open_files([path], mode="wt", **options)
        assert len(file_open) == 1
```

#### 8. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L805) (Line 805)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `p`
- **Keywords:** `{'mode': "'rb'"}`

```python
        if isinstance(self.path, (list, tuple)):
            files = sum([open_files(p, mode="rb", **options) for p in self.path], [])
            self.name = self.name or "%i files" % len(files)
```

#### 9. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L812) (Line 812)
- **Target Call:** `open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
                self.path = self.path + "/*"
            files = open_files(self.path, mode="rb", **options)
            self.path = make_path_posix(self.path)
```

#### 10. [intake/catalog/zarr.py](https://github.com/intake/intake/blob/master/intake/catalog/zarr.py#L63) (Line 63)
- **Target Call:** `get_mapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrGroupCatalog._load`
- **Arguments:** `self._urlpath`
- **Keywords:** `{}`

```python

                    store = get_mapper(self._urlpath, **self._storage_options)
                else:
```

#### 11. [intake/config.py](https://github.com/intake/intake/blob/master/intake/config.py#L26) (Line 26)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `global`
- **Arguments:** `os.getenv('INTAKE_CONF_DIR', os.path.join(expanduser('~'), '.intake'))`
- **Keywords:** `{}`

```python

confdir = make_path_posix(os.getenv("INTAKE_CONF_DIR", os.path.join(expanduser("~"), ".intake")))

```

#### 12. [intake/config.py](https://github.com/intake/intake/blob/master/intake/config.py#L44) (Line 44)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `cfile`
- **Arguments:** `os.getenv('INTAKE_CONF_FILE', posixpath.join(confdir, 'conf.yaml'))`
- **Keywords:** `{}`

```python
def cfile():
    return make_path_posix(os.getenv("INTAKE_CONF_FILE", posixpath.join(confdir, "conf.yaml")))

```

#### 13. [intake/conftest.py](https://github.com/intake/intake/blob/master/intake/conftest.py#L42) (Line 42)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `tmp_config_path`
- **Arguments:** `os.path.join(tmp_path, 'test_config.yml')`
- **Keywords:** `{}`

```python
    original = os.getenv(key)
    temp_config_path = make_path_posix(os.path.join(tmp_path, "test_config.yml"))
    os.environ[key] = temp_config_path
```

#### 14. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L55) (Line 55)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSelector.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self.done_callback = done_callback
        self.fs = fsspec.filesystem("file")
        super().__init__(**kwargs)
```

#### 15. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L94) (Line 94)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 16. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L109) (Line 109)
- **Target Call:** `self.fs._parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSelector.move_up`
- **Arguments:** `self.path_text.value`
- **Keywords:** `{}`

```python
    def move_up(self, arg=None):
        self.path_text.value = self.fs._parent(self.path_text.value)
        self.make_options()
```

#### 17. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L121) (Line 121)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSelector.make_options`
- **Arguments:** `self.path, True`
- **Keywords:** `{}`

```python
        try:
            for f in self.fs.ls(self.path, True):
                bn = os.path.basename(f["name"].rstrip("/"))
```

#### 18. [intake/readers/catalogs.py](https://github.com/intake/intake/blob/master/intake/readers/catalogs.py#L376) (Line 376)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `STACIndex._read`
- **Arguments:** `'https://stacindex.org/api/catalogs'`
- **Keywords:** `{}`

```python
    def _read(self, *args, **kwargs):
        with fsspec.open("https://stacindex.org/api/catalogs") as f:
            data = json.load(f)
```

#### 19. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1927) (Line 1927)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `recommend`
- **Arguments:** `url2`
- **Keywords:** `{'refresh': 'True'}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
            mime = mime or fs.info(url2, refresh=True).get("ContentType", None)
        except (IOError, TypeError, AttributeError, ValueError):
```

#### 20. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1932) (Line 1932)
- **Target Call:** `fs.cat_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `recommend`
- **Arguments:** `url2[0] if isinstance(url2, list) else url2`
- **Keywords:** `{'end': '2 ** 20'}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
            head = fs.cat_file(url2[0] if isinstance(url2, list) else url2, end=2**20)
        except (IOError, IndexError, ValueError):
```

#### 21. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1989) (Line 1989)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    if url:
        if fs is not None and fs.isdir(url):
            try:
```

#### 22. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1991) (Line 1991)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{'detail': 'False'}`

```python
            try:
                allfiles = fs.ls(url, detail=False)
            except IOError:
```

#### 23. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L420) (Line 420)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Catalog.to_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wt'"}`

```python
        # TODO: remove ['CATALOG_DIR', 'CATALOG_PATH', 'STORAGE_OPTIONS'] UPs?
        with fsspec.open(path, mode="wt", **storage_options) as stream:
            yaml.safe_dump(self.to_dict(), stream)
```

#### 24. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L432) (Line 432)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        storage_options = kwargs.pop("storage_options", kwargs)
        of = fsspec.open(path, **storage_options)
        with of as stream:
```

#### 25. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L436) (Line 436)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `of.fs._parent(path)`
- **Keywords:** `{}`

```python
        cat.user_parameters["CATALOG_PATH"] = path
        cat.user_parameters["CATALOG_DIR"] = of.fs.unstrip_protocol(of.fs._parent(path))
        cat.user_parameters["STORAGE_OPTIONS"] = storage_options
```

#### 26. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L436) (Line 436)
- **Target Call:** `self.fs._parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        cat.user_parameters["CATALOG_PATH"] = path
        cat.user_parameters["CATALOG_DIR"] = of.fs.unstrip_protocol(of.fs._parent(path))
        cat.user_parameters["STORAGE_OPTIONS"] = storage_options
```

#### 27. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L681) (Line 681)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if any(c in path for c in ("*", "?", "[")):
                expanded = fs.glob(path)
                if not expanded:
```

#### 28. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L684) (Line 684)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_to_files`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
                    return []
                return [fs.info(p) for p in expanded]

```

#### 29. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L688) (Line 688)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            try:
                entry = fs.info(path)
            except FileNotFoundError:
```

#### 30. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L699) (Line 699)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_to_files`
- **Arguments:** `path.rstrip('/')`
- **Keywords:** `{'detail': 'True'}`

```python
                # List only immediate children that are files
                children = fs.ls(path.rstrip("/"), detail=True)
                files = [
```

#### 31. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L125) (Line 125)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NumpyToNumpyFile.run`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if storage_options or "://" in path or "::" in path:
            with fsspec.open(path, **storage_options) as f:
                self._func(x, f)
```

#### 32. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L158) (Line 158)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MatplotlibToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, metadata=None, storage_options=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.savefig(f, format="png", **kwargs)
```

#### 33. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L293) (Line 293)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NumpyToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        img = Image.fromarray(x)
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            img.save(f, format="PNG", **kwargs)
```

#### 34. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L320) (Line 320)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NumpyToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        if storage_options or "://" in url or "::" in url:
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
                tifffile.imwrite(f, x, **kwargs)
```

#### 35. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L337) (Line 337)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PILImageToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="PNG", **kwargs)
```

#### 36. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L353) (Line 353)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PILImageToJPEG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, quality=85, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="JPEG", quality=quality, **kwargs)
```

#### 37. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L368) (Line 368)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PILImageToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
    def run(self, x, url, storage_options=None, metadata=None, **kwargs):
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
            x.save(f, format="TIFF", **kwargs)
```

#### 38. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L402) (Line 402)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NumpyToWAV.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        if storage_options or "://" in url or "::" in url:
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
                sf.write(f, x, samplerate, **kwargs)
```

#### 39. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L682) (Line 682)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python

        protocol, _ = split_protocol(data.url)
        if protocol is None:
```

#### 40. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L695) (Line 695)
- **Target Call:** `fs._check_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        cached_fn = fs._check_file(path)
        if cached_fn:
```

#### 41. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L699) (Line 699)
- **Target Call:** `fs._mapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        sha = fs._mapper(path)
        cached_fn = os.path.join(fs.storage[-1], sha)
```

#### 42. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L702) (Line 702)
- **Target Call:** `self.fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path, cached_fn`
- **Keywords:** `{'callback': 'callback'}`

```python

        fs.fs.get_file(path, cached_fn, callback=callback)
        return cached_fn
```

#### 43. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L736) (Line 736)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LlamaServerReader._read`
- **Arguments:** `f'simplecache::{v}'`
- **Keywords:** `{}`

```python
            if k == "--system-prompt-file":
                path = fsspec.open_local(f"simplecache::{v}")
                cmd.extend([str(k), path])
```

#### 44. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L923) (Line 923)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SKLearnModelReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f)
```

#### 45. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L993) (Line 993)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
    def _extract(cls, meta, base):
        h = fsspec.filesystem("http")
        if "URL_ORIGINAL_DATA" in meta:
```

#### 46. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1000) (Line 1000)
- **Target Call:** `h.cat` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `[f"{base}/{u.lstrip('hdl:/')}" for u in ids]`
- **Keywords:** `{}`

```python
            ids = meta["HAS_PARTS"]["value"].split(";")
            rr = h.cat([f"{base}/{u.lstrip('hdl:/')}" for u in ids])
            rr2 = [{i["type"]: i["data"] for i in json.loads(r)["values"]} for r in rr.values()]
```

#### 47. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1006) (Line 1006)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
    def _read(self, data, base="https://hdl.handle.net/api/handles", **kwargs):
        h = fsspec.filesystem("http")
        r = h.cat(f"{base}/{data.url.lstrip('hdl:/')}")
```

#### 48. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1007) (Line 1007)
- **Target Call:** `h.cat` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `f"{base}/{data.url.lstrip('hdl:/')}"`
- **Keywords:** `{}`

```python
        h = fsspec.filesystem("http")
        r = h.cat(f"{base}/{data.url.lstrip('hdl:/')}")
        j = json.loads(r)
```

#### 49. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1044) (Line 1044)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PandasHDF5._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        if data.storage_options:  # or fsspec-like
            with fsspec.open(data.url, "rb", **data.storage_options) as f:
                self._func(f, data.path, **kw)
```

#### 50. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1286) (Line 1286)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PythonModule._read`
- **Arguments:** `data.url, 'rt'`
- **Keywords:** `{}`

```python
            module_name = data.url.rsplit("/", 1)[-1].split(".", 1)[0]
        with fsspec.open(data.url, "rt", **(data.storage_options or {})) as f:
            mod = ModuleType(module_name)
```

#### 51. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1318) (Line 1318)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NumpyText._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if data.storage_options or "://" in data.url or "::" in data.url:
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
                return self._func(f, **kw)
```

#### 52. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1415) (Line 1415)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            elif open_local:
                ofs = fsspec.open_local(data.url, **(data.storage_options or {}))
            elif (isinstance(data.url, str) and is_fsspec_url(data.url)) or is_fsspec_url(
```

#### 53. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1419) (Line 1419)
- **Target Call:** `fsspec.open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            ):
                ofs0 = fsspec.open_files(data.url, **(data.storage_options or {}))
                ofs = [_.open() for _ in ofs0]
```

#### 54. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1433) (Line 1433)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                if open_local:
                    f = fsspec.open_local(data.url, **(data.storage_options or {}))
                    return open_dataset(f, **kw)
```

#### 55. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436) (Line 1436)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                else:
                    f = fsspec.open(data.url, **(data.storage_options or {})).open()
                    return open_dataset(f, **kw)
```

#### 56. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1480) (Line 1480)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XArrayPatternReader._read`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            url = pattern_to_glob(data.url)
            fs, _, paths = fsspec.get_fs_token_paths(url, **(data.storage_options or {}))
            val_dict = reverse_formats(data.url, paths)
```

#### 57. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1513) (Line 1513)
- **Target Call:** `fsspec.open_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RasterIOXarrayReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python

        ofs = fsspec.open_files(data.url, **(data.storage_options or {}))
        opened = [open_rasterio(of.open(), **kwargs) for of in ofs]
```

#### 58. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1578) (Line 1578)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GeoPandasReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if with_fsspec:
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
                return geopandas.read_file(f, **kwargs)
```

#### 59. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1600) (Line 1600)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ScipyMatrixMarketReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **data.storage_options) as f:
            return self._func(f)
```

#### 60. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1612) (Line 1612)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NibabelNiftiReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f, **kw)
```

#### 61. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639) (Line 1639)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ASDFReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            # want the file to stay open, since array access is lazy by default
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
            return self._func(f, **kw)
```

#### 62. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1653) (Line 1653)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DicomReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
    def _read(self, data, **kw):
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
            return self._func(f, **kw)
```

#### 63. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683) (Line 1683)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PMTileReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if "://" in data.url or "::" in data.url:
            f = fsspec.open(data.url, **(data.storage_options or {})).open()

```

#### 64. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889) (Line 1889)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GeoPandasTabular._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        if "://" in data.url or "::" in data.url:
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
        else:
```

#### 65. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1971) (Line 1971)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MessagePackReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return msgpack.unpack(f, **kwargs)
```

#### 66. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1998) (Line 1998)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MarkdownReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            return f.read()
```

#### 67. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2005) (Line 2005)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MarkdownReader.discover`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        data = self.kwargs.get("data") or (self.kwargs.get("args") or [None])[0]
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            raw = f.read(head_bytes)
```

#### 68. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2036) (Line 2036)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TOMLReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return tomllib.load(f)
```

#### 69. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2081) (Line 2081)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `INIReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python
        cfg = configparser.ConfigParser(**kwargs)
        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            cfg.read_file(f)
```

#### 70. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2113) (Line 2113)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PDFTextReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            return extract_text(f, **kwargs)
```

#### 71. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2251) (Line 2251)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PILImageReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            img = Image.open(f)
```

#### 72. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2468) (Line 2468)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BioPythonFASTAReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
            return list(SeqIO.parse(f, fmt))
```

#### 73. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2664) (Line 2664)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        MAGIC = b"GGUF"
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            header = f.read(24)
```

#### 74. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2751) (Line 2751)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PMTilesMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        MAGIC = b"PMTiles"
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            raw = f.read(127)
```

#### 75. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2847) (Line 2847)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            # BlobHeader: 4-byte big-endian length, then protobuf BlobHeader
```

#### 76. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2980) (Line 2980)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SKLearnModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            model = pickle.load(f)
```

#### 77. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3073) (Line 3073)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        result: dict = {}
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as raw_f:
            with zipfile.ZipFile(raw_f) as zf:
```

#### 78. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3135) (Line 3135)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JoblibMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python

        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
            obj = joblib.load(f)
```

#### 79. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3513) (Line 3513)
- **Target Call:** `fsspec.open_local` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 80. [intake/readers/search.py](https://github.com/intake/intake/blob/master/intake/readers/search.py#L126) (Line 126)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `EnvironmentSatisfied._is_consistent`
- **Arguments:** `env, 'rt'`
- **Keywords:** `{}`

```python
            if "dependencies:" not in env:
                with fsspec.open(env, "rt") as f:
                    env = f.read()
```

#### 81. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L52) (Line 52)
- **Target Call:** `compressions.values` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JSONFileSource.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        VALID_COMPRESSIONS = list(compressions.values()) + ["infer"]

```

#### 82. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L74) (Line 74)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 83. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L132) (Line 132)
- **Target Call:** `compressions.values` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JSONLinesFileSource.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        VALID_COMPRESSIONS = list(compressions.values()) + ["infer"]

```

#### 84. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L157) (Line 157)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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

#### 85. [intake/source/utils.py](https://github.com/intake/intake/blob/master/intake/source/utils.py#L119) (Line 119)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `reverse_format`
- **Arguments:** `format_string`
- **Keywords:** `{}`

```python
    # ensure that format_string is in posix format
    format_string = make_path_posix(format_string)

```

#### 86. [intake/source/utils.py](https://github.com/intake/intake/blob/master/intake/source/utils.py#L131) (Line 131)
- **Target Call:** `make_path_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `reverse_format`
- **Arguments:** `resolved_string`
- **Keywords:** `{}`

```python
    # ensure that resolved string is in posix format
    resolved_string = make_path_posix(resolved_string)

```

### pandas ([pandas-dev/pandas](https://github.com/pandas-dev/pandas))
- **Usages Found:** `4` in `2` files.

#### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L452) (Line 452)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FastParquetImpl.read`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python

            parquet_kwargs["fs"] = fsspec.open(path, "rb", **(storage_options or {})).fs
        elif isinstance(path, str) and not os.path.isdir(path):
```

### xarray ([pydata/xarray](https://github.com/pydata/xarray))
- **Usages Found:** `5` in `1` files.

#### 1. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174) (Line 174)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_find_absolute_paths`
- **Arguments:** `fs._strip_protocol(paths)`
- **Keywords:** `{}`

```python
            )
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
```

#### 2. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174) (Line 174)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_find_absolute_paths`
- **Arguments:** `paths`
- **Keywords:** `{}`

```python
            )
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
```

#### 3. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L175) (Line 175)
- **Target Call:** `fs.get_mapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_find_absolute_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
            return [fs.get_mapper(path) for path in tmp_paths]
        elif is_remote_uri(paths):
```

#### 4. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L221) (Line 221)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_open_remote_file`
- **Arguments:** `file`
- **Keywords:** `{'mode': 'mode', 'storage_options': 'storage_options'}`

```python

    fs, _, paths = fsspec.get_fs_token_paths(
        file, mode=mode, storage_options=storage_options
    )

```

#### 5. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L227) (Line 227)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_open_remote_file`
- **Arguments:** `paths[0]`
- **Keywords:** `{'mode': 'mode'}`

```python

    return fs.open(paths[0], mode=mode, **open_kwargs)

```

### zarr ([zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python))
- **Usages Found:** `18` in `1` files.

#### 1. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L55) (Line 55)
- **Target Call:** `fs.to_json` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_make_async`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        # Convert sync instance of an async fs to an async instance
        fs_dict = json.loads(fs.to_json())
        fs_dict["asynchronous"] = True
```

#### 2. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L67) (Line 67)
- **Target Call:** `AsyncFileSystemWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_make_async`
- **Arguments:** `fs`
- **Keywords:** `{'asynchronous': 'True'}`

```python

    return AsyncFileSystemWrapper(fs, asynchronous=True)

```

#### 3. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L250) (Line 250)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.from_url`
- **Arguments:** `url`
- **Keywords:** `{}`

```python

        fs, path = url_to_fs(url, **opts)
        if not fs.async_impl:
```

#### 4. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L268) (Line 268)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.clear`
- **Arguments:** `self.path`
- **Keywords:** `{'withdirs': 'True'}`

```python
        try:
            for subpath in await self.fs._find(self.path, withdirs=True):
                if subpath != self.path:
```

#### 5. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L270) (Line 270)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.clear`
- **Arguments:** `subpath`
- **Keywords:** `{'recursive': 'True'}`

```python
                if subpath != self.path:
                    await self.fs._rm(subpath, recursive=True)
        except FileNotFoundError:
```

#### 6. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L298) (Line 298)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if byte_range is None:
                value = prototype.buffer.from_bytes(await self.fs._cat_file(path))
            elif isinstance(byte_range, RangeByteRequest):
```

#### 7. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L301) (Line 301)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{'start': 'byte_range.offset', 'end': 'None'}`

```python
                value = prototype.buffer.from_bytes(
                    await self.fs._cat_file(path, start=byte_range.offset, end=None)
                )
```

#### 9. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L313) (Line 313)
- **Target Call:** `self.fs._cat_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.get`
- **Arguments:** `path`
- **Keywords:** `{'start': '-byte_range.suffix', 'end': 'None'}`

```python
                value = prototype.buffer.from_bytes(
                    await self.fs._cat_file(path, start=-byte_range.suffix, end=None)
                )
```

#### 10. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L345) (Line 345)
- **Target Call:** `self.fs._pipe_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.set`
- **Arguments:** `path, value.to_bytes()`
- **Keywords:** `{}`

```python
            raise NotImplementedError
        await self.fs._pipe_file(path, value.to_bytes())

```

#### 11. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L352) (Line 352)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.delete`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        try:
            await self.fs._rm(path)
        except FileNotFoundError:
```

#### 12. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L369) (Line 369)
- **Target Call:** `self.fs._rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.delete_dir`
- **Arguments:** `path_to_delete`
- **Keywords:** `{'recursive': 'True'}`

```python
        with suppress(*self.allowed_exceptions):
            await self.fs._rm(path_to_delete, recursive=True)

```

#### 13. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L374) (Line 374)
- **Target Call:** `self.fs._exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.exists`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = _dereference_path(self.path, key)
        exists: bool = await self.fs._exists(path)
        return exists
```

#### 14. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L409) (Line 409)
- **Target Call:** `self.fs._cat_ranges` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.get_partial_values`
- **Arguments:** `paths, starts, stops`
- **Keywords:** `{'on_error': "'return'"}`

```python
        # TODO: expectations for exceptions or missing keys?
        res = await self.fs._cat_ranges(paths, starts, stops, on_error="return")
        # the following is an s3-specific condition we probably don't want to leak
```

#### 15. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L420) (Line 420)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.list`
- **Arguments:** `self.path`
- **Keywords:** `{'detail': 'False', 'withdirs': 'False'}`

```python
        # docstring inherited
        allfiles = await self.fs._find(self.path, detail=False, withdirs=False)
        for onefile in (a.removeprefix(f"{self.path}/") for a in allfiles):
```

#### 16. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L428) (Line 428)
- **Target Call:** `self.fs._ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.list_dir`
- **Arguments:** `prefix`
- **Keywords:** `{'detail': 'False'}`

```python
        try:
            allfiles = await self.fs._ls(prefix, detail=False)
        except FileNotFoundError:
```

#### 17. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L436) (Line 436)
- **Target Call:** `self.fs._find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs._info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecStore.getsize`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = _dereference_path(self.path, key)
        info = await self.fs._info(path)

```

### DVC ([iterative/dvc](https://github.com/iterative/dvc))
- **Usages Found:** `326` in `55` files.

#### 1. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L53) (Line 53)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `artifacts_show`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            root = _repo.fs.root_marker
            _dirname = _repo.fs.join(root, dirname) if dirname else root
            with Repo(_dirname, fs=_repo.fs, scm=_repo.scm) as r:
```

#### 2. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L56) (Line 56)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `artifacts_show`
- **Arguments:** `_repo.fs.root_marker, as_posix(path)`
- **Keywords:** `{}`

```python
                path = r.artifacts.get_path(name)
                path = _repo.fs.join(_repo.fs.root_marker, as_posix(path))
                parts = _repo.fs.relparts(path, _repo.root_dir)
```

#### 3. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L57) (Line 57)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `artifacts_show`
- **Arguments:** `path, _repo.root_dir`
- **Keywords:** `{}`

```python
                path = _repo.fs.join(_repo.fs.root_marker, as_posix(path))
                parts = _repo.fs.relparts(path, _repo.root_dir)
                return {"rev": rev, "path": os.path.join(*parts)}
```

#### 4. [dvc/api/data.py](https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L294) (Line 294)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_open`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                fs = DVCFileSystem(repo=_repo, subrepos=True)
                fs_path = fs.from_os_path(path)

```

#### 5. [dvc/api/data.py](https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L297) (Line 297)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode', 'encoding': 'encoding'}`

```python
            try:
                with fs.open(fs_path, mode=mode, encoding=encoding) as fobj:
                    yield fobj
```

#### 6. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L30) (Line 30)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_odb`
- **Arguments:** `fs_path, *prefix`
- **Keywords:** `{}`

```python
    if prefix:
        fs_path = fs.join(fs_path, *prefix)
    if hash_name:
```

#### 7. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L89) (Line 89)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CacheManager.fs_cache`
- **Arguments:** `self.local_cache_dir, self.FS_DIR`
- **Keywords:** `{}`

```python
            fs=self.local.fs,
            path=self.local.fs.join(self.local_cache_dir, self.FS_DIR),
        )
```

#### 8. [dvc/commands/dag.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dag.py#L89) (Line 89)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_targets`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        for out in outs_trie.itervalues(prefix=repo.fs.parts(path)):
            targets.extend(str(out))
```

#### 9. [dvc/commands/dataset.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dataset.py#L66) (Line 66)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CmdDatasetAdd.run`
- **Arguments:** `existing.manifest_path`
- **Keywords:** `{}`

```python
            if not self.args.force and existing:
                path = self.repo.fs.relpath(existing.manifest_path)
                raise DvcException(
```

#### 10. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L99) (Line 99)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.__init__`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
        if dvc_dir:
            self.dvc_dir = self.fs.abspath(dvc_dir)

```

#### 11. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L140) (Line 140)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.files`
- **Arguments:** `self.dvc_dir, self.CONFIG`
- **Keywords:** `{}`

```python
        if self.dvc_dir is not None:
            files["repo"] = self.fs.join(self.dvc_dir, self.CONFIG)

```

#### 12. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L211) (Line 211)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.load_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        with fs.open(path) as fobj:
            try:
```

#### 13. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L238) (Line 238)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config._save_config`
- **Arguments:** `os.path.dirname(filename)`
- **Keywords:** `{}`

```python

        fs.makedirs(os.path.dirname(filename))

```

#### 14. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L241) (Line 241)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config._save_config`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        config = ConfigObj(_pack_named(conf_dict))
        with fs.open(filename, "wb") as fobj:
            config.write(fobj)
```

#### 15. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L39) (Line 39)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Remote.odb`
- **Arguments:** `path, '.dvc', CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
        if self.worktree:
            path = self.fs.join(path, ".dvc", CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
        else:
```

#### 16. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L41) (Line 41)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Remote.odb`
- **Arguments:** `path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
        else:
            path = self.fs.join(path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
        return get_odb(self.fs, path, hash_name=DEFAULT_ALGORITHM, **self.config)
```

#### 17. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L214) (Line 214)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataCloud._push`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Pushing to {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 18. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L275) (Line 275)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataCloud._pull`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Fetching from {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 19. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L355) (Line 355)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataCloud.get_url_for`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = odb.oid_to_path(checksum)
        return odb.fs.unstrip_protocol(path)
```

#### 20. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L34) (Line 34)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dependency.workspace_status`
- **Arguments:** `self.fs_path, None`
- **Keywords:** `{}`

```python
            try:
                self.fs_path = self.fs.version_path(self.fs_path, None)
                if self.changed_meta():
```

#### 21. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L43) (Line 43)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dependency.update`
- **Arguments:** `self.fs_path, rev`
- **Keywords:** `{}`

```python
        if self.fs.version_aware:
            self.fs_path = self.fs.version_path(self.fs_path, rev)
            self.meta = self.get_meta()
```

#### 22. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L45) (Line 45)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dependency.update`
- **Arguments:** `self.fs_path, self.meta.version_id`
- **Keywords:** `{}`

```python
            self.meta = self.get_meta()
            self.fs_path = self.fs.version_path(self.fs_path, self.meta.version_id)

```

#### 23. [dvc/dependency/base.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/base.py#L53) (Line 53)
- **Target Call:** `self.fs.version_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dependency.save`
- **Arguments:** `self.fs_path, self.meta.version_id`
- **Keywords:** `{}`

```python
        if self.fs.version_aware:
            self.fs_path = self.fs.version_path(self.fs_path, self.meta.version_id)

```

#### 24. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L40) (Line 40)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RepoDependency.__init__`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python
        self.fs = self._make_fs()
        self.fs_path = as_posix(self.fs.normpath(self.def_path))

```

#### 25. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L106) (Line 106)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RepoDependency.download`
- **Arguments:** `src_path`
- **Keywords:** `{}`

```python
            try:
                info = maybe_info or self.fs.info(src_path)
                hash_info = info["dvc_info"]["entry"].hash_info
```

#### 26. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L108) (Line 108)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RepoDependency.download`
- **Arguments:** `dest_path`
- **Keywords:** `{}`

```python
                hash_info = info["dvc_info"]["entry"].hash_info
                dest_info = to.fs.info(dest_path)
            except (KeyError, AttributeError):
```

#### 27. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L108) (Line 108)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileMixin.exists`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        is_ignored = self.repo.dvcignore.is_ignored_file(self.path)
        return self.repo.fs.exists(self.path) and not is_ignored

```

#### 28. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L136) (Line 136)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileMixin._load`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        self._verify_filename()
        if not self.repo.fs.isfile(self.path):
            raise StageFileIsNotDvcFileError(self.path)
```

#### 29. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L333) (Line 333)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ProjectFile.resolver`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python

        wdir = self.repo.fs.parent(self.path)
        return DataResolver(self.repo, wdir, self.contents)
```

#### 30. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L56) (Line 56)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    with TqdmCallback(desc=f"Downloading {fs.name(fs_path)}", unit="files") as cb:
        if isinstance(fs, DVCFileSystem):
```

#### 31. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L62) (Line 62)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                    f"{fs.normpath(glob.escape(fs_path))}/**"
                    if fs.isdir(fs_path)
                    else glob.escape(fs_path)
```

#### 32. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L61) (Line 61)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `glob.escape(fs_path)`
- **Keywords:** `{}`

```python
                [
                    f"{fs.normpath(glob.escape(fs_path))}/**"
                    if fs.isdir(fs_path)
```

#### 33. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L67) (Line 67)
- **Target Call:** `fs._get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `fs_path, to`
- **Keywords:** `{'batch_size': 'jobs', 'callback': 'cb'}`

```python
            if not glob.has_magic(fs_path):
                return fs._get(fs_path, to, batch_size=jobs, callback=cb)

```

#### 34. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L71) (Line 71)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        # download atomic and avoids fsspec glob/regex path expansion.
        if fs.isdir(fs_path):
            from_infos = [
```

#### 35. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L73) (Line 73)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            from_infos = [
                path for path in fs.find(fs_path) if not path.endswith(fs.flavour.sep)
            ]
```

#### 36. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L79) (Line 79)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download`
- **Arguments:** `info, fs_path`
- **Keywords:** `{}`

```python
            to_infos = [
                localfs.join(to, *fs.relparts(info, fs_path)) for info in from_infos
            ]
```

#### 37. [dvc/fs/data.py](https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L31) (Line 31)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 38. [dvc/fs/data.py](https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L34) (Line 34)
- **Target Call:** `self.fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataFileSystem.isdvc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def isdvc(self, path, **kwargs):
        return self.fs.isdvc(path, **kwargs)

```

#### 39. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
        assert self.repo is not None
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

#### 40. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        assert self.repo is not None
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

#### 41. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
        return self.root_marker + self.sep.join(relparts)
```

#### 42. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
        return self.root_marker + self.sep.join(relparts)
```

#### 43. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L237) (Line 237)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._get_key`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        path = os.fspath(path)
        parts = self.repo.fs.relparts(path, self.repo.root_dir)
        if parts == (os.curdir,):
```

#### 45. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L268) (Line 268)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._from_key`
- **Arguments:** `self.repo.root_dir, *parts`
- **Keywords:** `{}`

```python
    def _from_key(self, parts: Key) -> str:
        return self.repo.fs.join(self.repo.root_dir, *parts)

```

#### 46. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L334) (Line 334)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `dir_path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python

        repo_path = self.repo.fs.join(dir_path, Repo.DVC_DIR)
        return self.repo.fs.isdir(repo_path)
```

#### 47. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L335) (Line 335)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = self.repo.fs.join(dir_path, Repo.DVC_DIR)
        return self.repo.fs.isdir(repo_path)

```

#### 48. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L362) (Line 362)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode'}`

```python
        try:
            return self.repo.fs.open(fs_path, mode=mode)
        except FileNotFoundError:
```

#### 49. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L401) (Line 401)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            try:
                fs_info = fs.info(fs_path)
                if fs_info["type"] == "file":
```

#### 50. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L408) (Line 408)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `info['name']`
- **Keywords:** `{}`

```python
                    ):
                        fs_infos[fs.name(info["name"])] = info
            except (FileNotFoundError, NotADirectoryError):
```

#### 51. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L465) (Line 465)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        try:
            fs_info = fs.info(fs_path)
            if check_ignored and repo.dvcignore.is_ignored(
```

#### 52. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L477) (Line 477)
- **Target Call:** `fs.parents` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if dvc_info and not fs_info:
            for parent in fs.parents(fs_path):
                try:
```

#### 53. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L479) (Line 479)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `parent`
- **Keywords:** `{}`

```python
                try:
                    if fs.info(parent)["type"] != "directory":
                        dvc_info = None
```

#### 54. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L591) (Line 591)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `src, dest`
- **Keywords:** `{'callback': 'child'}`

```python
            with callback.branched(src, dest) as child:
                fs.get_file(src, dest, callback=child, **kw)

```

#### 55. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L615) (Line 615)
- **Target Call:** `self.fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `fs_path, lpath`
- **Keywords:** `{}`

```python
        try:
            return self.repo.fs.get_file(fs_path, lpath, **kwargs)
        except FileNotFoundError:
```

#### 56. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L688) (Line 688)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 57. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L702) (Line 702)
- **Target Call:** `self.fs._get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DVCFileSystem.isdvc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def isdvc(self, path, **kwargs) -> bool:
        return self.fs.isdvc(path, **kwargs)

```

#### 59. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L753) (Line 753)
- **Target Call:** `self.fs.close` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DVCFileSystem.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if "fs" in self.__dict__:
            self.fs.close()
```

#### 60. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L48) (Line 48)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GitFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    def getcwd(self):
        return self.fs.getcwd()

```

#### 61. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L51) (Line 51)
- **Target Call:** `self.fs.chdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GitFileSystem.chdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def chdir(self, path):
        self.fs.chdir(path)

```

#### 62. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L58) (Line 58)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GitFileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'detail'}`

```python
    def ls(self, path, detail=True, **kwargs):
        return self.fs.ls(path, detail=detail, **kwargs) or []
```

#### 63. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L115) (Line 115)
- **Target Call:** `fs.isabs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def from_file(cls, path: str, fs: "FileSystem", name: str) -> "Self":
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
```

#### 64. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116) (Line 116)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `fs.dirname(path)`
- **Keywords:** `{}`

```python
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
```

#### 65. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116) (Line 116)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        assert fs.isabs(path)
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
```

#### 66. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L117) (Line 117)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        dirname = fs.normpath(fs.dirname(path))
        with fs.open(path, encoding="utf-8") as fobj:
            path_spec_lines = [
```

#### 67. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L300) (Line 300)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._get_key`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
    def _get_key(self, path: str) -> tuple[str, ...]:
        parts = self.fs.relparts(path, self.root_dir)
        if parts == (os.curdir,):
```

#### 68. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L310) (Line 310)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `dirname, DvcIgnore.DVCIGNORE_FILE`
- **Keywords:** `{}`

```python

        path = self.fs.join(dirname, DvcIgnore.DVCIGNORE_FILE)
        if not matches and self.fs.exists(path):
```

#### 69. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L311) (Line 311)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = self.fs.join(dirname, DvcIgnore.DVCIGNORE_FILE)
        if not matches and self.fs.exists(path):
            name = self.fs.relpath(path, self.root_dir)
```

#### 70. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L312) (Line 312)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
        if not matches and self.fs.exists(path):
            name = self.fs.relpath(path, self.root_dir)
            new_pattern = DvcIgnorePatterns.from_file(path, self.fs, name)
```

#### 71. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L340) (Line 340)
- **Target Call:** `self.fs.walk` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname`
- **Keywords:** `{}`

```python
                try:
                    _, dnames, _ = next(self.fs.walk(dirname))
                except StopIteration:
```

#### 72. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L345) (Line 345)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname, dname`
- **Keywords:** `{}`

```python
            for dname in dnames:
                self._update_sub_repo(self.fs.join(dirname, dname), ignore_trie)

```

#### 73. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L353) (Line 353)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python

        dvc_dir = self.fs.join(path, Repo.DVC_DIR)
        if not self.fs.exists(dvc_dir):
```

#### 74. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L354) (Line 354)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
        dvc_dir = self.fs.join(path, Repo.DVC_DIR)
        if not self.fs.exists(dvc_dir):
            return
```

#### 75. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L357) (Line 357)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        root, dname = self.fs.split(path)
        key = self._get_key(root)
```

#### 76. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L377) (Line 377)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.__call__`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
    ) -> tuple[list[str], list[str]]:
        abs_root = self.fs.abspath(root)
        ignore_pattern = self._get_trie_pattern(
```

#### 77. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L407) (Line 407)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python

        for entry in fs.ls(path, detail=True, **kwargs):
            name = fs.name(entry["name"])
```

#### 78. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L408) (Line 408)
- **Target Call:** `fs.name` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.ls`
- **Arguments:** `entry['name']`
- **Keywords:** `{}`

```python
        for entry in fs.ls(path, detail=True, **kwargs):
            name = fs.name(entry["name"])
            fs_dict[name] = entry
```

#### 79. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L433) (Line 433)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.protocol == Schemes.LOCAL:
            for root, dirs, files in fs.walk(path, **kwargs):
                if detail:
```

#### 80. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L451) (Line 451)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        else:
            yield from fs.walk(path, **kwargs)

```

#### 81. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L460) (Line 460)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.find`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        else:
            yield from fs.find(path)

```

#### 82. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L470) (Line 470)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._get_trie_pattern`
- **Arguments:** `dirname, self.root_dir`
- **Keywords:** `{}`

```python

        if not self.fs.isin_or_eq(dirname, self.root_dir):
            # outside of the repo
```

#### 83. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L481) (Line 481)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._get_trie_pattern`
- **Arguments:** `self.root_dir, *prefix_key`
- **Keywords:** `{}`

```python
        prefix_key = ignores_trie.longest_prefix(key).key or ()
        prefix = self.fs.join(self.root_dir, *prefix_key)

```

#### 84. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `self.fs.normpath(path)`
- **Keywords:** `{}`

```python
            return False
        dirname, basename = self.fs.split(self.fs.normpath(path))
        ignore_pattern = self._get_trie_pattern(dirname, None, ignore_subrepos)
```

#### 85. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return False
        dirname, basename = self.fs.split(self.fs.normpath(path))
        ignore_pattern = self._get_trie_pattern(dirname, None, ignore_subrepos)
```

#### 86. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L510) (Line 510)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.is_ignored_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # only used in LocalFileSystem
        path = self.fs.abspath(path)
        if path == self.root_dir:
```

#### 87. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L518) (Line 518)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.is_ignored_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # only used in LocalFileSystem
        path = self.fs.abspath(path)
        return self._is_ignored(path, False, ignore_subrepos=ignore_subrepos)
```

#### 88. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L522) (Line 522)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter._outside_repo`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
    def _outside_repo(self, path: str) -> bool:
        return not self.fs.isin_or_eq(path, self.root_dir)

```

#### 89. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L527) (Line 527)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        # https://github.com/treeverse/dvc/issues/5046
        full_target = self.fs.abspath(target)
        matched_patterns: list[PatternInfo] = []
```

#### 90. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Target Call:** `self.fs.split` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `self.fs.normpath(full_target)`
- **Keywords:** `{}`

```python
        if not self._outside_repo(full_target):
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
            pattern = self._get_trie_pattern(dirname)
```

#### 91. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
        if not self._outside_repo(full_target):
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
            pattern = self._get_trie_pattern(dirname)
```

#### 92. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L535) (Line 535)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
                ignore, matched_patterns = pattern.matches(
                    dirname, basename, self.fs.isdir(full_target), details=True
                )
```

#### 93. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L546) (Line 546)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return False
        if fs.isfile(path):
            return self.is_ignored_file(path, ignore_subrepos)
```

#### 94. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L548) (Line 548)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return self.is_ignored_file(path, ignore_subrepos)
        if fs.isdir(path):
            return self.is_ignored_dir(path, ignore_subrepos)
```

#### 95. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L367) (Line 367)
- **Target Call:** `self.fs.isabs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__init__`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python
            and self.fs.protocol == "local"
            and not self.fs.isabs(self.def_path)
        ):
```

#### 96. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L399) (Line 399)
- **Target Call:** `self.fs.coalesce_version` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.isabs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._parse_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            and self.stage.repo.fs == fs
            and not fs.isabs(fs_path)
        ):
```

#### 98. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L456) (Line 456)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._parse_path`
- **Arguments:** `self.stage.wdir, fs_path`
- **Keywords:** `{}`

```python
            # then we have #2059 bug and can't really handle that.
            fs_path = fs.join(self.stage.wdir, fs_path)

```

#### 99. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._parse_path`
- **Arguments:** `fs.normpath(fs_path)`
- **Keywords:** `{}`

```python

        return fs.abspath(fs.normpath(fs_path))

```

#### 100. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._parse_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

        return fs.abspath(fs.normpath(fs_path))

```

#### 101. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L474) (Line 474)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        if not self.fs.isin(self.fs_path, self.repo.root_dir):
            return self.fs_path
```

#### 102. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L477) (Line 477)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__str__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

        cur_dir = self.fs.getcwd()
        if self.fs.isin(cur_dir, self.repo.root_dir):
```

#### 103. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L478) (Line 478)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__str__`
- **Arguments:** `cur_dir, self.repo.root_dir`
- **Keywords:** `{}`

```python
        cur_dir = self.fs.getcwd()
        if self.fs.isin(cur_dir, self.repo.root_dir):
            return self.fs.relpath(self.fs_path, cur_dir)
```

#### 104. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L479) (Line 479)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, cur_dir`
- **Keywords:** `{}`

```python
        if self.fs.isin(cur_dir, self.repo.root_dir):
            return self.fs.relpath(self.fs_path, cur_dir)

```

#### 105. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L481) (Line 481)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        return self.fs.relpath(self.fs_path, self.repo.root_dir)

```

#### 106. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L498) (Line 498)
- **Target Call:** `self.fs.isabs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.is_in_repo`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python

        if self.fs.isabs(self.def_path):
            return False
```

#### 107. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L501) (Line 501)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.is_in_repo`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python

        return self.repo and self.fs.isin(self.fs_path, self.repo.root_dir)

```

#### 108. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L530) (Line 530)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.exists`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python

        return self.fs.exists(self.fs_path)

```

#### 110. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L592) (Line 592)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.index_key`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
            assert self.repo
            key = self.repo.fs.relparts(self.fs_path, self.repo.root_dir)
        else:
```

#### 111. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L596) (Line 596)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.index_key`
- **Arguments:** `no_drive`
- **Keywords:** `{}`

```python
            no_drive = self.fs.flavour.splitdrive(self.fs_path)[1]
            key = self.fs.parts(no_drive)[1:]
        return workspace, key
```

#### 112. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L653) (Line 653)
- **Target Call:** `self.fs.is_empty` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.is_empty`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
    def is_empty(self) -> bool:
        return self.fs.is_empty(self.fs_path)

```

#### 113. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L658) (Line 658)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.isdir`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
            return False
        return self.fs.isdir(self.fs_path)

```

#### 114. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L663) (Line 663)
- **Target Call:** `self.fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.isfile`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
            return False
        return self.fs.isfile(self.fs_path)

```

#### 115. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L787) (Line 787)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.commit`
- **Arguments:** `filter_info or self.fs_path`
- **Keywords:** `{}`

```python
                assert self.repo
                rel = self.fs.relpath(filter_info or self.fs_path)
                with CheckoutCallback(desc=f"Checking out {rel}", unit="files") as cb:
```

#### 116. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
    def _commit_granular_dir(self, filter_info, hardlink) -> Optional["HashFile"]:
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
        staging, _, obj = self._build(
```

#### 117. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
    def _commit_granular_dir(self, filter_info, hardlink) -> Optional["HashFile"]:
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
        staging, _, obj = self._build(
```

#### 118. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L844) (Line 844)
- **Target Call:** `self.fs.as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.dumpd`
- **Arguments:** `relpath(self.fs_path, self.stage.wdir)`
- **Keywords:** `{}`

```python
        if self.is_in_repo:
            path = self.fs.as_posix(relpath(self.fs_path, self.stage.wdir))
        else:
```

#### 119. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L990) (Line 990)
- **Target Call:** `self.fs.remove` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.remove`
- **Arguments:** `self.fs_path`
- **Keywords:** `{'recursive': 'True'}`

```python
        try:
            self.fs.remove(self.fs_path, recursive=True)
        except FileNotFoundError:
```

#### 120. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1002) (Line 1002)
- **Target Call:** `self.fs.move` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.move`
- **Arguments:** `self.fs_path, out.fs_path`
- **Keywords:** `{}`

```python
        if src_exists:
            self.fs.move(self.fs_path, out.fs_path)
        else:
```

#### 121. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1049) (Line 1049)
- **Target Call:** `self.fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.transfer`
- **Arguments:** `odb.path`
- **Keywords:** `{}`

```python
        with TqdmCallback(
            desc=f"Transferring to {odb.fs.unstrip_protocol(odb.path)}",
            unit="file",
```

#### 122. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
            assert obj
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
            return obj.filter(prefix)
```

#### 123. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
            assert obj
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
            return obj.filter(prefix)
```

#### 124. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.unstage`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python

        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 125. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.unstage`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python

        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 126. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.apply`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python
        append_only = True
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 127. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Output.apply`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python
        append_only = True
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))

```

#### 128. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L143) (Line 143)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataResolver.__init__`
- **Arguments:** `wdir`
- **Keywords:** `{}`

```python
        if os.path.isabs(wdir):
            wdir = fs.relpath(wdir)
            wdir = "" if wdir == os.curdir else wdir
```

#### 129. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataResolver.__init__`
- **Arguments:** `fs.join(self.wdir, 'dvc.yaml')`
- **Keywords:** `{}`

```python
        self.wdir = wdir
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))

```

#### 130. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DataResolver.__init__`
- **Arguments:** `self.wdir, 'dvc.yaml'`
- **Keywords:** `{}`

```python
        self.wdir = wdir
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))

```

#### 131. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L290) (Line 290)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `EntryDefinition._resolve_wdir`
- **Arguments:** `self.wdir, wdir`
- **Keywords:** `{}`

```python
            format_and_raise(exc, f"'{self.where}.{name}.wdir'", self.relpath)
        return self.resolver.fs.join(self.wdir, wdir)

```

#### 132. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L356) (Line 356)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if not fs.exists(path):
            raise ParamsLoadError(f"'{path}' does not exist")
```

#### 133. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L358) (Line 358)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            raise ParamsLoadError(f"'{path}' does not exist")
        if fs.isdir(path):
            raise ParamsLoadError(f"'{path}' is a directory")
```

#### 134. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.merge_from`
- **Arguments:** `fs.join(wdir, path)`
- **Keywords:** `{}`

```python
        path, _, keys_str = item.partition(":")
        path = fs.normpath(fs.join(wdir, path))

```

#### 135. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.merge_from`
- **Arguments:** `wdir, path`
- **Keywords:** `{}`

```python
        path, _, keys_str = item.partition(":")
        path = fs.normpath(fs.join(wdir, path))

```

#### 136. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L433) (Line 433)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.load_from_vars`
- **Arguments:** `wdir, default`
- **Keywords:** `{}`

```python
        if default:
            to_import = fs.join(wdir, default)
            if fs.exists(to_import):
```

#### 137. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L434) (Line 434)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Context.load_from_vars`
- **Arguments:** `to_import`
- **Keywords:** `{}`

```python
            to_import = fs.join(wdir, default)
            if fs.exists(to_import):
                self.merge_from(fs, default, wdir)
```

#### 138. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L116) (Line 116)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo._get_repo_dirs`
- **Arguments:** `root_dir, self.DVC_DIR`
- **Keywords:** `{}`

```python
            fs = fs or localfs
            dvc_dir = fs.join(root_dir, self.DVC_DIR)
        except NotDvcRepoError:
```

#### 139. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L203) (Line 203)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                assert self.tmp_dir
                self.fs.makedirs(self.tmp_dir, exist_ok=True)

```

#### 140. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L206) (Line 206)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir, 'lock'`
- **Keywords:** `{}`

```python
                self.lock = make_lock(
                    self.fs.join(self.tmp_dir, "lock"),
                    tmp_dir=self.tmp_dir,
```

#### 141. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L272) (Line 272)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.local_dvc_dir`
- **Arguments:** `self.root_dir, '/'`
- **Keywords:** `{}`

```python
            # subrepo
            relparts = self.fs.relparts(self.root_dir, "/")

```

#### 142. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L393) (Line 393)
- **Target Call:** `fs._get_key_from_relative` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            fs = self.dvcfs.fs
            key = fs._get_key_from_relative(fs_path)
            subrepo, _, key = fs._get_subrepo_info(key)
```

#### 143. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L394) (Line 394)
- **Target Call:** `fs._get_subrepo_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
            key = fs._get_key_from_relative(fs_path)
            subrepo, _, key = fs._get_subrepo_info(key)
            index = subrepo.index.data[workspace]
```

#### 144. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L398) (Line 398)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
            index = self.index.data[workspace]
            key = self.fs.relparts(path, self.root_dir)

```

#### 145. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L414) (Line 414)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_root`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
        root = root or os.curdir
        root_dir = fs.abspath(root)

```

#### 146. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L416) (Line 416)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python

        if not fs.isdir(root_dir):
            raise NotDvcRepoError(f"directory '{root}' does not exist")
```

#### 147. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L420) (Line 420)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
        while True:
            dvc_dir = fs.join(root_dir, cls.DVC_DIR)
            if fs.isdir(dvc_dir):
```

#### 148. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L421) (Line 421)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_root`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
            dvc_dir = fs.join(root_dir, cls.DVC_DIR)
            if fs.isdir(dvc_dir):
                return root_dir
```

#### 149. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L425) (Line 425)
- **Target Call:** `fs.parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
                break
            parent = fs.parent(root_dir)
            if parent == root_dir:
```

#### 150. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L443) (Line 443)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_dvc_dir`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
        root_dir = cls.find_root(root, fs=fs)
        return fs.join(root_dir, cls.DVC_DIR)

```

#### 151. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L554) (Line 554)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.find_outs_by_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        abs_path = self.fs.abspath(path)
        fs_path = abs_path
```

#### 152. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L565) (Line 565)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.func`
- **Arguments:** `out.fs_path, fs_path`
- **Keywords:** `{}`

```python
                return True
            return recursive and out.fs.isin(out.fs_path, fs_path)

```

#### 153. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L574) (Line 574)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Repo.is_dvc_internal`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def is_dvc_internal(self, path):
        path_parts = self.fs.normpath(path).split(self.fs.sep)
        return self.DVC_DIR in path_parts
```

#### 154. [dvc/repo/add.py](https://github.com/iterative/dvc/blob/main/dvc/repo/add.py#L181) (Line 181)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_add`
- **Arguments:** `source`
- **Keywords:** `{}`

```python
    out = stage.outs[0]
    path = out.fs.abspath(source) if source else None
    try:
```

#### 155. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L102) (Line 102)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.read`
- **Arguments:** `dvcfile, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for dvcfile, dvcfile_artifacts in self.repo.index._artifacts.items():
            dvcyaml = self.repo.fs.relpath(dvcfile, self.repo.root_dir)
            artifacts[dvcyaml] = {}
```

#### 156. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L180) (Line 180)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.get_path`
- **Arguments:** `scm_root, *dirparts, PROJECT_FILE`
- **Keywords:** `{}`

```python
        dirparts = posixpath.normpath(dirname).split(posixpath.sep) if dirname else ()
        abspath = fs.join(scm_root, *dirparts, PROJECT_FILE)
        rela = fs.relpath(abspath, self.repo.root_dir)
```

#### 157. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L181) (Line 181)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.get_path`
- **Arguments:** `abspath, self.repo.root_dir`
- **Keywords:** `{}`

```python
        abspath = fs.join(scm_root, *dirparts, PROJECT_FILE)
        rela = fs.relpath(abspath, self.repo.root_dir)
        try:
```

#### 158. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L210) (Line 210)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.download`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            root = self.repo.fs.root_marker
            _dirname = self.repo.fs.join(root, dirname) if dirname else root
            with Repo(_dirname, fs=self.repo.fs, scm=self.repo.scm) as r:
```

#### 159. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L213) (Line 213)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.download`
- **Arguments:** `root, as_posix(path)`
- **Keywords:** `{}`

```python
                path = r.artifacts.get_path(name)
                path = self.repo.fs.join(root, as_posix(path))
                path = self.repo.fs.relpath(path, self.repo.root_dir)
```

#### 160. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L214) (Line 214)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.download`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, as_posix(path))
                path = self.repo.fs.relpath(path, self.repo.root_dir)
                # when the `repo` is a subrepo, the path `/subrepo/myart.pkl` for dvcfs
```

#### 161. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L218) (Line 218)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.download`
- **Arguments:** `root, path`
- **Keywords:** `{}`

```python
                # i.e. relative to the root of the subrepo
                path = self.repo.fs.join(root, path)
                path = self.repo.fs.normpath(path)
```

#### 162. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L219) (Line 219)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Artifacts.download`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, path)
                path = self.repo.fs.normpath(path)

```

#### 163. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L64) (Line 64)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
    repo_root_parts: tuple[str, ...] = ()
    if self.fs.isin(self.root_dir, self.scm.root_dir):
        repo_root_parts = self.fs.relparts(self.root_dir, self.scm.root_dir)
```

#### 164. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L65) (Line 65)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.root_dir, self.scm.root_dir):
        repo_root_parts = self.fs.relparts(self.root_dir, self.scm.root_dir)

```

#### 165. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

#### 166. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

#### 167. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)

```

#### 168. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)

```

#### 169. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L129) (Line 129)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *repo_root_parts`
- **Keywords:** `{}`

```python
    fs = GitFileSystem(scm=repo.scm, rev=rev)
    root_dir = repo.fs.join("/", *repo_root_parts)
    if not fs.exists(root_dir):
```

#### 170. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L130) (Line 130)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
    root_dir = repo.fs.join("/", *repo_root_parts)
    if not fs.exists(root_dir):
        raise NotDvcRepoError(f"Commit '{rev[:7]}' does not contain a DVC repo")
```

#### 171. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L135) (Line 135)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir, repo.DVC_DIR`
- **Keywords:** `{}`

```python
    repo.root_dir = root_dir
    repo.dvc_dir = fs.join(root_dir, repo.DVC_DIR)
    repo._reset()
```

#### 172. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L139) (Line 139)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *cwd_parts`
- **Keywords:** `{}`

```python
    if cwd_parts:
        cwd = repo.fs.join("/", *cwd_parts)
        repo.fs.chdir(cwd)
```

#### 173. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L140) (Line 140)
- **Target Call:** `self.fs.chdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_switch_fs`
- **Arguments:** `cwd`
- **Keywords:** `{}`

```python
        cwd = repo.fs.join("/", *cwd_parts)
        repo.fs.chdir(cwd)

```

#### 174. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L152) (Line 152)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    repo_root_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.root_dir, repo.scm.root_dir):
        repo_root_parts = repo.fs.relparts(repo.root_dir, repo.scm.root_dir)
```

#### 175. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L153) (Line 153)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.root_dir, repo.scm.root_dir):
        repo_root_parts = repo.fs.relparts(repo.root_dir, repo.scm.root_dir)

```

#### 176. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

#### 177. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    cwd_parts: tuple[str, ...] = ()
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

#### 178. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)

```

#### 179. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)

```

#### 180. [dvc/repo/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/cache.py#L24) (Line 24)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `check_missing`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if not fs.exists(path):
            typ = "directory" if (entry.meta and entry.meta.isdir) else "file"
```

#### 181. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L98) (Line 98)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_check_can_delete`
- **Arguments:** `path, *(entry.key or ())`
- **Keywords:** `{}`

```python

        entry_paths.append(fs.join(path, *(entry.key or ())))

```

#### 182. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L174) (Line 174)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `checkout_onerror`
- **Arguments:** `dest_path, out_path`
- **Keywords:** `{}`

```python
        for out_path in out_paths:
            if self.fs.isin_or_eq(dest_path, out_path):
                failed.add(out_path)
```

#### 183. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L193) (Line 193)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `checkout`
- **Arguments:** `self.root_dir, *key`
- **Keywords:** `{}`

```python
    for key, (typ, _stats) in out_changes.items():
        out_path = self.fs.join(self.root_dir, *key)

```

#### 184. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L196) (Line 196)
- **Target Call:** `self.fs.remove` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `checkout`
- **Arguments:** `out_path`
- **Keywords:** `{'recursive': 'True'}`

```python
        if out_path in failed:
            self.fs.remove(out_path, recursive=True)
            continue
```

#### 185. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L34) (Line 34)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_paths`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
    fs = DVCFileSystem(repo=repo)
    fs_paths = [fs.from_os_path(target) for target in targets]

```

#### 186. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L38) (Line 38)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    for fs_path in fs_paths:
        if recursive and fs.isdir(fs_path):
            target_paths.extend(fs.find(fs_path))
```

#### 187. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L39) (Line 39)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if recursive and fs.isdir(fs_path):
            target_paths.extend(fs.find(fs_path))
        target_paths.append(fs_path)
```

#### 188. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L61) (Line 61)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    """Transform files rel. to Git root to DVC root, and drop outside files."""
    rel = repo.fs.relpath(repo.root_dir, repo.scm.root_dir).rstrip("/")

```

#### 190. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.fs.getcwd(), repo.root_dir`
- **Keywords:** `{}`

```python

    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
    if start in (os.curdir, ""):
```

#### 191. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Target Call:** `self.fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** ``
- **Keywords:** `{}`

```python

    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
    if start in (os.curdir, ""):
```

#### 192. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L385) (Line 385)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `file, start`
- **Keywords:** `{}`

```python
    # we need to convert repo relative paths to curdir relative.
    return [repo.fs.relpath(file, start) for file in files]

```

#### 193. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L513) (Line 513)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `status`
- **Arguments:** `os.fspath(t)`
- **Keywords:** `{}`

```python
    targets = targets or []
    filter_keys: list[DataIndexKey] = [repo.fs.relparts(os.fspath(t)) for t in targets]
    # try to remove duplicate and overlapping keys
```

#### 194. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L35) (Line 35)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

        if summarize or not fs.isdir(path):
            return [(path, fs.du(path, total=True))]
```

#### 195. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L36) (Line 36)
- **Target Call:** `fs.du` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{'total': 'True'}`

```python
        if summarize or not fs.isdir(path):
            return [(path, fs.du(path, total=True))]

```

#### 196. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Target Call:** `fs.du` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `du`
- **Arguments:** `entry_path`
- **Keywords:** `{'total': 'True'}`

```python
        ret = [
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
        ]
```

#### 197. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        ret = [
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
        ]
```

#### 198. [dvc/repo/experiments/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L53) (Line 53)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExpCache.get`
- **Arguments:** `obj.path, 'rb'`
- **Keywords:** `{}`

```python
        try:
            with obj.fs.open(obj.path, "rb") as fobj:
                data = fobj.read()
```

#### 199. [dvc/repo/experiments/executor/base.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/executor/base.py#L362) (Line 362)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseExecutor.pack_repro_args`
- **Arguments:** `dpath`
- **Keywords:** `{}`

```python
            open_func = fs.open
            fs.makedirs(dpath)
        else:
```

#### 200. [dvc/repo/experiments/utils.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/utils.py#L44) (Line 44)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_exp_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    path = os.path.join(repo.tmp_dir, EXEC_TMP_DIR)
    repo.fs.makedirs(path, exist_ok=True)

```

#### 201. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L169) (Line 169)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fetch`
- **Arguments:** `sorted((idx.data_tree.hash_info.value for idx in indexes.values()))`
- **Keywords:** `{}`

```python
        "fetch",
        tokenize(sorted(idx.data_tree.hash_info.value for idx in indexes.values())),
    )
```

#### 202. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224) (Line 224)
- **Target Call:** `fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_log_unversioned`
- **Arguments:** `fs.join(remote.path, *key)`
- **Keywords:** `{}`

```python
            if entry.meta and not entry.meta.isdir and entry.meta.version_id is None:
                unversioned.append(fs.unstrip_protocol(fs.join(remote.path, *key)))
            else:
```

#### 203. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224) (Line 224)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_log_unversioned`
- **Arguments:** `remote.path, *key`
- **Keywords:** `{}`

```python
            if entry.meta and not entry.meta.isdir and entry.meta.version_id is None:
                unversioned.append(fs.unstrip_protocol(fs.join(remote.path, *key)))
            else:
```

#### 204. [dvc/repo/get.py](https://github.com/iterative/dvc/blob/main/dvc/repo/get.py#L60) (Line 60)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs = DataFileSystem(index=repo.index.data["local"])
            fs_path = fs.from_os_path(path)
        else:
```

#### 205. [dvc/repo/get.py](https://github.com/iterative/dvc/blob/main/dvc/repo/get.py#L63) (Line 63)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs = repo.dvcfs
            fs_path = fs.from_os_path(path)
        download(fs, fs_path, os.path.abspath(out), jobs=jobs)
```

#### 206. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L146) (Line 146)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
                continue
            dep_key = dep.fs.parts(dep.fs_path)
            overlapping = [n.value for n in outs_trie.prefixes(dep_key)]
```

#### 207. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L176) (Line 176)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_outs_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
                continue
            dep_key = dep.fs.parts(dep.fs_path)
            overlapping = [n.value for n in outs_trie.prefixes(dep_key)]
```

#### 208. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L91) (Line 91)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `collect_files`
- **Arguments:** `root, file`
- **Keywords:** `{}`

```python
        for file in filter(dvcfile_filter, files):
            file_path = fs.join(root, file)
            try:
```

#### 209. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L203) (Line 203)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_storage_from_import`
- **Arguments:** `dep.meta.to_dict()`
- **Keywords:** `{}`

```python
        else:
            meta_token = tokenize(dep.meta.to_dict())

```

#### 210. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L210) (Line 210)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_storage_from_import`
- **Arguments:** `dep.fs_path, meta_token`
- **Keywords:** `{}`

```python
                    dep.fs.protocol,
                    tokenize(dep.fs_path, meta_token),
                ),
```

#### 212. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L513) (Line 513)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Index.metric_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for path in _collect_top_level_metrics(self.repo):
            key = self.repo.fs.relparts(path, self.repo.root_dir)
            by_workspace["repo"].add(key)
```

#### 213. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L527) (Line 527)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Index.param_keys`
- **Arguments:** `f'{self.repo.fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        default_file: str = ParamsDependency.DEFAULT_PARAMS_FILE
        if self.repo.fs.exists(f"{self.repo.fs.root_marker}{default_file}"):
            param_paths = chain(param_paths, [default_file])
```

#### 214. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L531) (Line 531)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Index.param_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        for path in param_paths:
            key = self.repo.fs.relparts(path, self.repo.root_dir)
            by_workspace["repo"].add(key)
```

#### 215. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L550) (Line 550)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Index.plot_keys`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        for path in self._plot_sources:
            key = self.repo.fs.parts(path)
            by_workspace["repo"].add(key)
```

#### 216. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L788) (Line 788)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            workspace, key = out.index_key
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

#### 217. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L789) (Line 789)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
            entry = self._index.data[workspace].get(key)
```

#### 218. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L805) (Line 805)
- **Target Call:** `self.fs.isin` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            workspace, key = out.index_key
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

#### 219. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L806) (Line 806)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
                key = key + out.fs.relparts(filter_info, out.fs_path)
            ret[workspace].add(key)
```

#### 220. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L856) (Line 856)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
    for key in index.data_keys.get(workspace, set()):
        out_path = fs.join(path, *key)

```

#### 221. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L861) (Line 861)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_data_index`
- **Arguments:** `out_path`
- **Keywords:** `{}`

```python

        if not fs.exists(out_path):
            continue
```

#### 222. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L901) (Line 901)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
    for key in parents:
        parent_path = fs.join(path, *key)
        if not fs.exists(parent_path):
```

#### 223. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L902) (Line 902)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_data_index`
- **Arguments:** `parent_path`
- **Keywords:** `{}`

```python
        parent_path = fs.join(path, *key)
        if not fs.exists(parent_path):
            continue
```

#### 224. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L84) (Line 84)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs: DVCFileSystem = repo.dvcfs
        fs_path = fs.from_os_path(path)
        return _ls(fs, fs_path, recursive, dvc_only, maxdepth)
```

#### 225. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L101) (Line 101)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls_tree`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs: DVCFileSystem = repo.dvcfs
        fs_path = fs.from_os_path(path)
        return _ls_tree(
```

#### 226. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L114) (Line 114)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
):
    fs_path = fs.info(path)["name"]

```

#### 227. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L120) (Line 120)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    maxdepth = maxdepth if recursive else None
    if maxdepth == 0 or fs.isfile(fs_path):
        infos[os.path.basename(path) or os.curdir] = fs.info(fs_path)
```

#### 228. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L121) (Line 121)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if maxdepth == 0 or fs.isfile(fs_path):
        infos[os.path.basename(path) or os.curdir] = fs.info(fs_path)
    else:
```

#### 229. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L123) (Line 123)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
        ):
            parts = fs.relparts(root, fs_path)
            if parts == (".",):
```

#### 231. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L151) (Line 151)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def _ls_tree(fs, path, maxdepth=None, _info=None, **fs_kwargs):
    info = _info or fs.info(path)
    if _info is None:
```

#### 232. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L168) (Line 168)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python
        try:
            infos = fs.ls(path, detail=True, **fs_kwargs)
        except FileNotFoundError:
```

#### 233. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L10) (Line 10)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls_url`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    try:
        info = fs.info(fs_path)
    except FileNotFoundError as exc:
```

#### 234. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L18) (Line 18)
- **Target Call:** `_LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls_url`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        # dvc's LocalFileSystem does not support maxdepth yet
        walk = _LocalFileSystem().walk
    else:
```

#### 235. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L24) (Line 24)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls_url`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
    for root, dirs, files in walk(fs_path, detail=True, maxdepth=maxdepth):
        parts = fs.relparts(root, fs_path)
        if parts == (".",):
```

#### 236. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L32) (Line 32)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ls_url`
- **Arguments:** `info['name'], fs_path`
- **Keywords:** `{}`

```python
            ls_info = {
                "path": fs.relpath(info["name"], fs_path),
                "isdir": info["type"] == "directory",
```

#### 237. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28) (Line 28)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
    for dvcfile, metrics in top_metrics.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in metrics:
```

#### 238. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28) (Line 28)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `dvcfile`
- **Keywords:** `{}`

```python
    for dvcfile, metrics in top_metrics.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in metrics:
```

#### 239. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L30) (Line 30)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
        for file in metrics:
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)
```

#### 240. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L31) (Line 31)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)

```

#### 241. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L104) (Line 104)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_metrics`
- **Arguments:** `metric`
- **Keywords:** `{}`

```python
    # convert to posixpath for DVCFileSystem
    paths = (fs.from_os_path(metric) for metric in metrics)
    # make paths absolute for DVCFileSystem
```

#### 242. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L123) (Line 123)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        try:
            if fs.isdir(path):
                yield from fs.find(path)
```

#### 243. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L124) (Line 124)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if fs.isdir(path):
                yield from fs.find(path)
                continue
```

#### 244. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L138) (Line 138)
- **Target Call:** `fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `to_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    relpath = fs.relpath
    cwd = fs.getcwd()

```

#### 245. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L165) (Line 165)
- **Target Call:** `fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_gather_metrics`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = fs_path.lstrip(fs.root_marker)
        repo_os_path = os.sep.join(fs.parts(repo_path))
        if not isinstance(result, Exception):
```

#### 246. [dvc/repo/open_repo.py](https://github.com/iterative/dvc/blob/main/dvc/repo/open_repo.py#L70) (Line 70)
- **Target Call:** `fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `make_repo`
- **Arguments:** `path, root_dir`
- **Keywords:** `{}`

```python
            fs = fs or localfs
            repo_path = os.path.join(url, *fs.relparts(path, root_dir))
            _config.update(_get_remote_config(repo_path))
```

#### 247. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24) (Line 24)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_params`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
    for dvcfile, params in top_params.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in params:
```

#### 248. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24) (Line 24)
- **Target Call:** `self.fs.parent` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_params`
- **Arguments:** `dvcfile`
- **Keywords:** `{}`

```python
    for dvcfile, params in top_params.items():
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
        for file in params:
```

#### 249. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L26) (Line 26)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_params`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
        for file in params:
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)
```

#### 250. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L27) (Line 27)
- **Target Call:** `self.fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_top_level_params`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
            yield repo.fs.normpath(path)

```

#### 251. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L68) (Line 68)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_params`
- **Arguments:** `f'{fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        params.extend({param: []} for param in _collect_top_level_params(repo))
        if default_file and fs.exists(f"{fs.root_marker}{default_file}"):
            params.append({default_file: []})
```

#### 252. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L77) (Line 77)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_params`
- **Arguments:** `param`
- **Keywords:** `{}`

```python
        # convert to posixpath for DVCFileSystem
        path = fs.from_os_path(param)
        # make paths absolute for DVCFileSystem
```

#### 253. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L96) (Line 96)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_vars`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
                # `file` is relative
                abspath = repo.fs.abspath(file)
                repo_path = repo.dvcfs.from_os_path(abspath)
```

#### 254. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L141) (Line 141)
- **Target Call:** `fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_gather_params`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_path = fs_path.lstrip(fs.root_marker)
        repo_os_path = os.sep.join(fs.parts(repo_path))
        if not isinstance(result, Exception):
```

#### 255. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L63) (Line 63)
- **Target Call:** `fs.find` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def _unpack_dir_files(fs, path, **kwargs):
    ret = list(fs.find(path))
    if not ret:
```

#### 256. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L66) (Line 66)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # This will raise FileNotFoundError if it is a broken symlink or TreeError
        next(iter(fs.ls(path)), None)
    return ret
```

#### 257. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_relpath`
- **Arguments:** `fs.join('/', fs.from_os_path(path)), fs.getcwd()`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 258. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_relpath`
- **Arguments:** `'/', fs.from_os_path(path)`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 259. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.from_os_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_relpath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 260. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Target Call:** `fs.getcwd` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    # ("../../../../../../dvc.yaml") - investigate
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())

```

#### 261. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L405) (Line 405)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_output_plots`
- **Arguments:** `wdir_relpath, plot.def_path`
- **Keywords:** `{}`

```python
                fs,
                _normpath(fs.join(wdir_relpath, plot.def_path)),
                props=plot_props | props,
```

#### 262. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L433) (Line 433)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_adjust_sources`
- **Arguments:** `config_dir, filepath`
- **Keywords:** `{}`

```python
        for filepath, val in old.items():
            new[_normpath(fs.join(config_dir, filepath))] = val
        new_plot_props[axis] = new
```

#### 263. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L447) (Line 447)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
    config_path = os.fspath(config_path)
    config_dir = fs.dirname(config_path)
    result: dict[str, dict] = {}
```

#### 264. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L451) (Line 451)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
    plot_ids_parents = [
        _normpath(fs.join(config_dir, plot_id)) for plot_id in definitions
    ]
```

#### 265. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L457) (Line 457)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
        if _id_is_path(plot_props):
            data_path = _normpath(fs.join(config_dir, plot_id))
            if _matches(targets, config_path, plot_id):
```

#### 266. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L480) (Line 480)
- **Target Call:** `fs.commonpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_closest_parent`
- **Arguments:** `[path, parent]`
- **Keywords:** `{}`

```python
    for parent in parents:
        common_path = fs.commonpath([path, parent])
        if len(common_path) > len(best_result):
```

#### 267. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L524) (Line 524)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_definitions`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
    for target in targets:
        if not result or fs.exists(target):
            unpacked = unpack_if_dir(fs, target, props=props, onerror=onerror)
```

#### 268. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L533) (Line 533)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `unpack_if_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    result: dict[str, dict] = defaultdict(dict)
    if fs.isdir(path):
        unpacked = _unpack_dir_files(fs, path, onerror=onerror)
```

#### 269. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L552) (Line 552)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'"}`

```python
    if extension in SUPPORTED_IMAGE_EXTENSIONS:
        with fs.open(path, mode="rb", **fs_kwargs) as fd:
            return fd.read()
```

#### 270. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L559) (Line 559)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf8'"}`

```python
    with reraise(UnicodeDecodeError, EncodingError(path, "utf8")):
        with fs.open(path, mode="r", encoding="utf8", **fs_kwargs) as fd:
            contents = fd.read()
```

#### 271. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_rebuild`
- **Arguments:** `fs.join(path, *key)`
- **Keywords:** `{}`

```python
            try:
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
            except FileNotFoundError:
```

#### 272. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_rebuild`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
            try:
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
            except FileNotFoundError:
```

#### 273. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L127) (Line 127)
- **Target Call:** `tokenize` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `push`
- **Arguments:** `sorted((idx.data_tree.hash_info.value for idx in indexes.values()))`
- **Keywords:** `{}`

```python
        "push",
        tokenize(sorted(idx.data_tree.hash_info.value for idx in indexes.values())),
    )
```

#### 274. [dvc/repo/remove.py](https://github.com/iterative/dvc/blob/main/dvc/repo/remove.py#L27) (Line 27)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `remove`
- **Arguments:** `target + DVC_FILE_SUFFIX`
- **Keywords:** `{}`

```python
        # give a more helpful error message.
        if self.fs.exists(target + DVC_FILE_SUFFIX):
            raise StageFileIsNotDvcFileError(target) from e
```

#### 275. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L63) (Line 63)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_maybe_collect_from_dvc_yaml`
- **Arguments:** `PROJECT_FILE`
- **Keywords:** `{}`

```python
    stages: StageList = []
    if loader.fs.exists(PROJECT_FILE):
        with suppress(StageNotFound):
```

#### 276. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L90) (Line 90)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_collect_specific_target`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        logger.debug(msg, target, PROJECT_FILE)
        if not (recursive and loader.fs.isdir(target)):
            stages = _maybe_collect_from_dvc_yaml(loader, target, with_deps)
```

#### 277. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L223) (Line 223)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StageLoad._get_filepath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if path:
            return self.repo.fs.abspath(path)

```

#### 278. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L349) (Line 349)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python

        if recursive and self.fs.isdir(target):
            from dvc.repo.graph import collect_inside_path
```

#### 279. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L352) (Line 352)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python

            path = self.fs.abspath(target)
            return collect_inside_path(path, graph or self.repo.index.graph)
```

#### 280. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L394) (Line 394)
- **Target Call:** `self.fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        if not stages:
            if not (recursive and self.fs.isdir(target)):
                try:
```

#### 281. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L397) (Line 397)
- **Target Call:** `self.fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
                    (out,) = self.repo.find_outs_by_path(target, strict=False)
                    return [StageInfo(out.stage, self.fs.abspath(target))]
                except OutputNotFoundError:
```

#### 282. [dvc/repo/trie.py](https://github.com/iterative/dvc/blob/main/dvc/repo/trie.py#L12) (Line 12)
- **Target Call:** `self.fs.parts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build_outs_trie`
- **Arguments:** `out.fs_path`
- **Keywords:** `{}`

```python
        for out in stage.outs:
            out_key = out.fs.parts(out.fs_path)

```

#### 283. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L131) (Line 131)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_merge_push_meta`
- **Arguments:** `repo.root_dir, *subkey`
- **Keywords:** `{}`

```python
                continue
            fs_path = repo.fs.join(repo.root_dir, *subkey)
            meta, hash_info = old_tree.get(repo.fs.relparts(fs_path, out.fs_path)) or (
```

#### 284. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L132) (Line 132)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_merge_push_meta`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
            fs_path = repo.fs.join(repo.root_dir, *subkey)
            meta, hash_info = old_tree.get(repo.fs.relparts(fs_path, out.fs_path)) or (
                None,
```

#### 285. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L331) (Line 331)
- **Target Call:** `self.fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_update_diff_index`
- **Arguments:** `repo.root_dir, *entry.key`
- **Keywords:** `{}`

```python
                if not entry.meta.isdir:
                    fs_path = repo.fs.join(repo.root_dir, *entry.key)
                    tree = out.obj
```

#### 286. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L335) (Line 335)
- **Target Call:** `self.fs.relparts` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_update_diff_index`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
                    _, entry.hash_info = tree.get(  # type: ignore[misc]
                        repo.fs.relparts(fs_path, out.fs_path)
                    )
```

#### 287. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L46) (Line 46)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_FILE`
- **Keywords:** `{}`

```python
def _edit_rwlock(lock_dir, fs, hardlink):
    path = fs.join(lock_dir, RWLOCK_FILE)

```

#### 288. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L49) (Line 49)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_LOCK`
- **Keywords:** `{}`

```python
    rwlock_guard = make_lock(
        fs.join(lock_dir, RWLOCK_LOCK),
        tmp_dir=lock_dir,
```

#### 289. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L55) (Line 55)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_edit_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        try:
            with fs.open(path, encoding="utf-8") as fobj:
                lock = SCHEMA(json.load(fobj))
```

#### 290. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L66) (Line 66)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_edit_rwlock`
- **Arguments:** `path, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        yield lock
        with fs.open(path, "w", encoding="utf-8") as fobj:
            json.dump(lock, fobj)
```

#### 291. [dvc/stage/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/stage/__init__.py#L640) (Line 640)
- **Target Call:** `self.fs.isin_or_eq` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Stage._func`
- **Arguments:** `fs_path, o.fs_path`
- **Keywords:** `{}`

```python
        def _func(o):
            return o.fs.isin_or_eq(fs_path, o.fs_path)

```

#### 292. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L185) (Line 185)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
def resolve_paths(fs, path, wdir=None):
    path = fs.abspath(path)
    wdir = wdir or os.curdir
```

#### 293. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.abspath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_paths`
- **Arguments:** `fs.join(fs.dirname(path), wdir)`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 294. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_paths`
- **Arguments:** `fs.dirname(path), wdir`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 295. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Target Call:** `fs.dirname` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    wdir = wdir or os.curdir
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
    return path, wdir
```

#### 296. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L72) (Line 72)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{'detail': 'False'}`

```python

        assert fs.ls("/", detail=False) == M.unordered(
            "/.gitignore", "/scripts", "/data"
```

#### 297. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L75) (Line 75)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts'`
- **Keywords:** `{'detail': 'False'}`

```python
        )
        assert fs.ls("scripts", detail=False) == ["scripts/script1"]
        assert fs.ls("data", detail=False) == M.unordered("data/foo", "data/bar")
```

#### 298. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L76) (Line 76)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data'`
- **Keywords:** `{'detail': 'False'}`

```python
        assert fs.ls("scripts", detail=False) == ["scripts/script1"]
        assert fs.ls("data", detail=False) == M.unordered("data/foo", "data/bar")

```

#### 299. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L85) (Line 85)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert sorted(fs.ls("/"), key=lambda i: i["name"]) == [
            M.dict(name="/.gitignore", type="file", isexec=False),
```

#### 300. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L92) (Line 92)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/not-existing-path'`
- **Keywords:** `{}`

```python
        with pytest.raises(FileNotFoundError):
            fs.info("/not-existing-path")

```

#### 301. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L94) (Line 94)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert fs.info("/") == M.dict(name="/", isexec=False, type="directory")
        assert fs.info("/data") == data_info
```

#### 302. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L95) (Line 95)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data'`
- **Keywords:** `{}`

```python
        assert fs.info("/") == M.dict(name="/", isexec=False, type="directory")
        assert fs.info("/data") == data_info
        assert fs.info("/scripts") == scripts_info
```

#### 303. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L96) (Line 96)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts'`
- **Keywords:** `{}`

```python
        assert fs.info("/data") == data_info
        assert fs.info("/scripts") == scripts_info
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
```

#### 304. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L97) (Line 97)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
        assert fs.info("/scripts") == scripts_info
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
        assert fs.info("/scripts/script1") == M.dict(
```

#### 305. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L98) (Line 98)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
        assert fs.info("/data/foo") == M.dict(name="/data/foo", type="file")
        assert fs.info("/scripts/script1") == M.dict(
            name="/scripts/script1", type="file"
```

#### 306. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L102) (Line 102)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python

        assert not fs.isdvc("/")
        assert fs.isdvc("/data")
```

#### 307. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L103) (Line 103)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data'`
- **Keywords:** `{}`

```python
        assert not fs.isdvc("/")
        assert fs.isdvc("/data")
        assert fs.isdvc("/data/foo")
```

#### 308. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L104) (Line 104)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
        assert fs.isdvc("/data")
        assert fs.isdvc("/data/foo")
        assert not fs.isdvc("/scripts")
```

#### 309. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L105) (Line 105)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts'`
- **Keywords:** `{}`

```python
        assert fs.isdvc("/data/foo")
        assert not fs.isdvc("/scripts")
        assert not fs.isdvc("/scripts/script1")
```

#### 310. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L106) (Line 106)
- **Target Call:** `fs.isdvc` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
        assert not fs.isdvc("/scripts")
        assert not fs.isdvc("/scripts/script1")

```

#### 311. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L109) (Line 109)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data'`
- **Keywords:** `{}`

```python
        with pytest.raises((IsADirectoryError, PermissionError)):
            fs.open("data")
        with pytest.raises((IsADirectoryError, PermissionError)):
```

#### 312. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L111) (Line 111)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts'`
- **Keywords:** `{}`

```python
        with pytest.raises((IsADirectoryError, PermissionError)):
            fs.open("scripts")
        with fs.open("/data/foo") as fobj:
```

#### 313. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L112) (Line 112)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/data/foo'`
- **Keywords:** `{}`

```python
            fs.open("scripts")
        with fs.open("/data/foo") as fobj:
            assert fobj.read() == b"foo"
```

#### 314. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L114) (Line 114)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/scripts/script1'`
- **Keywords:** `{}`

```python
            assert fobj.read() == b"foo"
        with fs.open("/scripts/script1") as fobj:
            assert fobj.read() == b"script1"
```

#### 315. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L118) (Line 118)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'data/foo', (tmp / 'foo').fs_path`
- **Keywords:** `{}`

```python
        tmp = make_tmp_dir("temp-download")
        fs.get_file("data/foo", (tmp / "foo").fs_path)
        assert (tmp / "foo").read_text() == "foo"
```

#### 316. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L121) (Line 121)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'scripts/script1', (tmp / 'script1').fs_path`
- **Keywords:** `{}`

```python

        fs.get_file("scripts/script1", (tmp / "script1").fs_path)
        assert (tmp / "script1").read_text() == "script1"
```

#### 317. [dvc/testing/api_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/api_tests.py#L124) (Line 124)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestAPI.test_filesystem`
- **Arguments:** `'/', (tmp / 'all').fs_path`
- **Keywords:** `{'recursive': 'True'}`

```python

        fs.get("/", (tmp / "all").fs_path, recursive=True)
        assert (tmp / "all").read_text() == {
```

#### 318. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L195) (Line 195)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `match_files`
- **Arguments:** `d['path']`
- **Keywords:** `{}`

```python
def match_files(fs, entries, expected):
    entries_content = {(fs.normpath(d["path"]), d["isdir"]) for d in entries}
    expected_content = {(fs.normpath(d["path"]), d["isdir"]) for d in expected}
```

#### 319. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L196) (Line 196)
- **Target Call:** `fs.normpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `match_files`
- **Arguments:** `d['path']`
- **Keywords:** `{}`

```python
    entries_content = {(fs.normpath(d["path"]), d["isdir"]) for d in entries}
    expected_content = {(fs.normpath(d["path"]), d["isdir"]) for d in expected}
    assert entries_content == expected_content
```

#### 320. [dvc/testing/workspace_tests.py](https://github.com/iterative/dvc/blob/main/dvc/testing/workspace_tests.py#L206) (Line 206)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestLsUrl.test_file`
- **Arguments:** `fs_path, fname`
- **Keywords:** `{}`

```python
        result = ls_url(str(cloud / fname), fs_config=cloud.config)
        match_files(fs, result, [{"path": fs.join(fs_path, fname), "isdir": False}])

```

#### 321. [dvc/utils/serialize/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/__init__.py#L23) (Line 23)
- **Target Call:** `fs.suffix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
def load_path(fs_path, fs, **kwargs):
    suffix = fs.suffix(fs_path).lower()
    loader = LOADERS[suffix]
```

#### 322. [dvc/utils/serialize/_common.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_common.py#L88) (Line 88)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_modify_data`
- **Arguments:** `os.fspath(path)`
- **Keywords:** `{}`

```python
):
    file_exists = fs.exists(os.fspath(path)) if fs else os.path.exists(path)
    data = _load_data(path, parser=parser, fs=fs) if file_exists else {}
```

#### 323. [dvc/utils/strictyaml.py](https://github.com/iterative/dvc/blob/main/dvc/utils/strictyaml.py#L47) (Line 47)
- **Target Call:** `fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `make_relpath`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if fs and not isinstance(fs, LocalFileSystem):
        rel = fs.relpath(fs_path).replace(fs.sep, sep)
    else:
```

#### 324. [dvc/utils/studio.py](https://github.com/iterative/dvc/blob/main/dvc/utils/studio.py#L126) (Line 126)
- **Target Call:** `self.fs.relpath` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_subrepo_relpath`
- **Arguments:** `repo.root_dir, scm_root_dir`
- **Keywords:** `{}`

```python

    relpath = as_posix(repo.fs.relpath(repo.root_dir, scm_root_dir))

```

#### 325. [tests/remotes/git_server.py](https://github.com/iterative/dvc/blob/main/tests/remotes/git_server.py#L34) (Line 34)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_check`
- **Arguments:** `'/'`
- **Keywords:** `{}`

```python
            fs = get_fs()
            fs.exists("/")
            fs.execute("git --version")
```

#### 326. [tests/remotes/git_server.py](https://github.com/iterative/dvc/blob/main/tests/remotes/git_server.py#L35) (Line 35)
- **Target Call:** `fs.execute` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_check`
- **Arguments:** `'git --version'`
- **Keywords:** `{}`

```python
            fs.exists("/")
            fs.execute("git --version")
        except asyncssh.Error:
```

### Kedro ([kedro-org/kedro](https://github.com/kedro-org/kedro))
- **Usages Found:** `4` in `1` files.

#### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L397) (Line 397)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'tar'", 'fo': 'conf_source'}`

```python
        if file_mimetype == "application/x-tar":
            return fsspec.filesystem(protocol="tar", fo=conf_source), "tar"
        elif file_mimetype in (
```

#### 2. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L403) (Line 403)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'zip'", 'fo': 'conf_source'}`

```python
        ):
            return fsspec.filesystem(protocol="zip", fo=conf_source), "zip"

```

#### 3. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L412) (Line 412)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': 'protocol'}`

```python
            # For HTTP and cloud storage protocols, create the appropriate filesystem
            return fsspec.filesystem(protocol=protocol), protocol
        else:
```

#### 4. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L415) (Line 415)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'file'", 'fo': 'conf_source'}`

```python
            # Default to local filesystem
            return fsspec.filesystem(protocol="file", fo=conf_source), "file"

```

### Hugging Face Datasets ([huggingface/datasets](https://github.com/huggingface/datasets))
- **Usages Found:** `88` in `17` files.

#### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1851) (Line 1851)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, _ = url_to_fs(dataset_path, **(storage_options or {}))

```

#### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1863) (Line 1863)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python

        fs.makedirs(dataset_path, exist_ok=True)

```

#### 3. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1931) (Line 1931)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, dataset_path = url_to_fs(dataset_path, **(storage_options or {}))

```

#### 6. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2029) (Line 2029)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python

        dataset_dict_is_file = fs.isfile(dataset_dict_json_path)
        dataset_info_is_file = fs.isfile(dataset_info_path)
```

#### 7. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2030) (Line 2030)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
        dataset_dict_is_file = fs.isfile(dataset_dict_json_path)
        dataset_info_is_file = fs.isfile(dataset_info_path)
        dataset_state_is_file = fs.isfile(dataset_state_json_path)
```

#### 8. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2031) (Line 2031)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
        dataset_info_is_file = fs.isfile(dataset_info_path)
        dataset_state_is_file = fs.isfile(dataset_state_json_path)
        if not dataset_info_is_file and not dataset_state_is_file:
```

#### 9. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2061) (Line 2061)
- **Target Call:** `fs.download` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `src_dataset_path, dest_dataset_path.as_posix()`
- **Keywords:** `{'recursive': 'True'}`

```python
            dest_dataset_path = Dataset._build_local_temp_path(src_dataset_path)
            fs.download(src_dataset_path, dest_dataset_path.as_posix(), recursive=True)
            dataset_state_json_path = posixpath.join(dest_dataset_path, config.DATASET_STATE_JSON_FILENAME)
```

#### 10. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6754) (Line 6754)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_push_to_repo`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
        hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
        dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 11. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6844) (Line 6844)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_push_to_bucket`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
    hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
    dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 12. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6911) (Line 6911)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    try:
        legacy_dataset_info: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8")).get(
            config_name, None
```

#### 13. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6920) (Line 6920)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.REPOCARD_FILENAME`
- **Keywords:** `{'newline': "''", 'encoding': "'utf-8'"}`

```python
    try:
        dataset_card = DatasetCard(fs.read_text(config.REPOCARD_FILENAME, newline="", encoding="utf-8"))
        dataset_card_data = dataset_card.data
```

#### 14. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6966) (Line 6966)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace('{split}', '*')`
- **Keywords:** `{}`

```python
    pattern = glob_pattern_to_regex(PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED)
    for file_path in fs.glob(PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace("{split}", "*")):
        split_pattern_fields = string_to_dict(file_path, pattern)
```

#### 15. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L7019) (Line 7019)
- **Target Call:** `fs.read_text` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    if legacy_dataset_info:
        legacy_dataset_infos: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8"))
        legacy_dataset_infos[config_name] = asdict(info_to_dump)
```

#### 16. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L521) (Line 521)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ArrowWriter.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if stream is None:
            fs, path = url_to_fs(path, **(storage_options or {}))
            self._fs: fsspec.AbstractFileSystem = fs
```

#### 17. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L422) (Line 422)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetBuilder.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self._output_dir = self._cache_dir
        self._fs: fsspec.AbstractFileSystem = fsspec.filesystem("file")

```

#### 18. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L789) (Line 789)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetBuilder.download_and_prepare`
- **Arguments:** `output_dir`
- **Keywords:** `{}`

```python
        # output_dir can be a remote bucket on GCS or S3
        fs, output_dir = url_to_fs(output_dir, **(storage_options or {}))
        self._fs = fs
```

#### 19. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L356) (Line 356)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_pattern`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    pattern, storage_options = _prepare_path_and_storage_options(pattern, download_config=download_config)
    fs, fs_pattern = url_to_fs(pattern, **storage_options)
    files_to_ignore = set(FILES_TO_IGNORE) - {xbasename(pattern)}
```

#### 20. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L372) (Line 372)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `resolve_pattern`
- **Arguments:** `fs_pattern`
- **Keywords:** `{'detail': 'True'}`

```python
    matched_paths = []
    for filepath, info in fs.glob(fs_pattern, detail=True, **glob_kwargs).items():
        if not (info["type"] == "file" or (info.get("islink") and os.path.isfile(os.path.realpath(filepath)))) or (
```

#### 21. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L509) (Line 509)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `data_file`
- **Keywords:** `{}`

```python
        data_file, storage_options = _prepare_path_and_storage_options(data_file, download_config=download_config)
        fs, fs_path = url_to_fs(data_file, **storage_options)
    if isinstance(fs, HfFileSystem):
```

#### 22. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L511) (Line 511)
- **Target Call:** `fs.resolve_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if isinstance(fs, HfFileSystem):
        resolved_path = fs.resolve_path(fs_path)
        if hasattr(resolved_path, "revision"):  # no revision for buckets
```

#### 23. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L514) (Line 514)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            return resolved_path.repo_id, resolved_path.revision
    info = fs.info(fs_path)
    # s3fs uses "ETag", gcsfs uses "etag", and for local we simply check mtime
```

#### 24. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1359) (Line 1359)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, _ = url_to_fs(dataset_dict_path, **(storage_options or {}))

```

#### 25. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1368) (Line 1368)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python

        fs.makedirs(dataset_dict_path, exist_ok=True)

```

#### 26. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1370) (Line 1370)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, dataset_dict_path = url_to_fs(dataset_dict_path, **(storage_options or {}))

```

#### 28. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1423) (Line 1423)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python
        dataset_info_path = posixpath.join(dataset_dict_path, config.DATASET_INFO_FILENAME)
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
```

#### 29. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
                raise FileNotFoundError(
```

#### 30. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
        if not fs.isfile(dataset_dict_json_path):
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
                raise FileNotFoundError(
```

#### 31. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1432) (Line 1432)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python

        with fs.open(dataset_dict_json_path, "r", encoding="utf-8") as f:
            splits = json.load(f)["splits"]
```

#### 32. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1437) (Line 1437)
- **Target Call:** `fs.unstrip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        for k in splits:
            dataset_dict_split_path = posixpath.join(fs.unstrip_protocol(dataset_dict_path), k)
            dataset_dict[k] = Dataset.load_from_disk(
```

#### 33. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2626) (Line 2626)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_push_to_repo`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
        hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
        dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 34. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2713) (Line 2713)
- **Target Call:** `DirFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_push_to_bucket`
- **Arguments:** ``
- **Keywords:** `{'fs': 'hffs', 'path': 'hf_path'}`

```python
    hffs = HfFileSystem(endpoint=config.HF_ENDPOINT, token=token)
    dirfs = DirFileSystem(fs=hffs, path=hf_path)

```

#### 35. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L196) (Line 196)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                path = url_or_path_join(self._base_path, path)
            fs, path = url_to_fs(path, **download_config.storage_options)
            size = 0
```

#### 36. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L199) (Line 199)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            try:
                size = fs.info(path).get("size", 0)
            except Exception:
```

#### 37. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L27) (Line 27)
- **Target Call:** `fsspec.register_implementation` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `global`
- **Arguments:** `fs_class.protocol, fs_class`
- **Keywords:** `{'clobber': 'True'}`

```python
        warnings.warn(f"A filesystem protocol was already set for {fs_class.protocol} and will be overwritten.")
    fsspec.register_implementation(fs_class.protocol, fs_class, clobber=True)
    for extension in fs_class.extensions:
```

#### 38. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L50) (Line 50)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rename`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
        # LocalFileSystem.mv does copy + rm, it is more efficient to simply move a local directory
        shutil.move(fs._strip_protocol(src), fs._strip_protocol(dst))
    else:
```

#### 39. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L50) (Line 50)
- **Target Call:** `fs._strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rename`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
        # LocalFileSystem.mv does copy + rm, it is more efficient to simply move a local directory
        shutil.move(fs._strip_protocol(src), fs._strip_protocol(dst))
    else:
```

#### 40. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L52) (Line 52)
- **Target Call:** `fs.mv` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rename`
- **Arguments:** `src, dst`
- **Keywords:** `{'recursive': 'True'}`

```python
    else:
        fs.mv(src, dst, recursive=True)
```

#### 41. [src/datasets/filesystems/compression.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/compression.py#L66) (Line 66)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseCompressedFileFileSystem._get_dirs`
- **Arguments:** `self.fo`
- **Keywords:** `{}`

```python
        if self.dir_cache is None:
            f = {**self._open_with_fsspec().fs.info(self.fo), "name": self.uncompressed_name}
            self.dir_cache = {f["name"]: f}
```

#### 42. [src/datasets/hub.py](https://github.com/huggingface/datasets/blob/main/src/datasets/hub.py#L44) (Line 44)
- **Target Call:** `fs.resolve_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `delete_from_hub`
- **Arguments:** `data_file`
- **Keywords:** `{}`

```python
    for data_file in chain(*builder.config.data_files.values()):
        data_file_resolved_path = fs.resolve_path(data_file)
        if data_file_resolved_path.repo_id == repo_id:
```

#### 43. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L208) (Line 208)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "wb") as f:
```

#### 44. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L209) (Line 209)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "wb") as f:
            self._dump_info(f, pretty_print=pretty_print)
```

#### 45. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L212) (Line 212)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
        if self.license:
            with fs.open(posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), "wb") as f:
                self._dump_license(f)
```

#### 46. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L273) (Line 273)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs: fsspec.AbstractFileSystem
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
        logger.debug(f"Loading Dataset info from {dataset_info_dir}")
```

#### 47. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L277) (Line 277)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            raise ValueError("Calling DatasetInfo.from_directory() with undefined dataset_info_dir.")
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "r", encoding="utf-8") as f:
            dataset_info_dict = json.load(f)
```

#### 48. [src/datasets/io/csv.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L94) (Line 94)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CsvDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
        if isinstance(self.path_or_buf, (str, bytes, os.PathLike)):
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
                written = self._write(file_obj=buffer, header=header, index=index, **self.to_csv_kwargs)
```

#### 49. [src/datasets/io/json.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L113) (Line 113)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ParquetDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
        if isinstance(self.path_or_buf, (str, bytes, os.PathLike)):
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
                written = self._write(
```

#### 51. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1768) (Line 1768)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    fs: fsspec.AbstractFileSystem
    fs, *_ = url_to_fs(dataset_path, **(storage_options or {}))
    if not fs.exists(dataset_path):
```

#### 52. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1769) (Line 1769)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    fs, *_ = url_to_fs(dataset_path, **(storage_options or {}))
    if not fs.exists(dataset_path):
        raise FileNotFoundError(f"Directory {dataset_path} not found")
```

#### 53. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1771) (Line 1771)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)`
- **Keywords:** `{}`

```python
        raise FileNotFoundError(f"Directory {dataset_path} not found")
    if fs.isfile(posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)) and fs.isfile(
        posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)
```

#### 54. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1771) (Line 1771)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)`
- **Keywords:** `{}`

```python
        return Dataset.load_from_disk(dataset_path, keep_in_memory=keep_in_memory, storage_options=storage_options)
    elif fs.isfile(posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)):
        return DatasetDict.load_from_disk(dataset_path, keep_in_memory=keep_in_memory, storage_options=storage_options)
```

#### 56. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L396) (Line 396)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FaissIndex.save`
- **Arguments:** `str(file), 'wb'`
- **Keywords:** `{}`

```python

        with fsspec.open(str(file), "wb", **(storage_options or {})) as f:
            faiss.write_index(index, faiss.BufferedIOWriter(faiss.PyCallbackIOWriter(f.write)))
```

#### 57. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L411) (Line 411)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FaissIndex.load`
- **Arguments:** `str(file), 'rb'`
- **Keywords:** `{}`

```python
        faiss_index = cls(device=device)
        with fsspec.open(str(file), "rb", **(storage_options or {})) as f:
            index = faiss.read_index(faiss.BufferedIOReader(faiss.PyCallbackIOReader(f.read)))
```

#### 58. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L166) (Line 166)
- **Target Call:** `can_be_local` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `cached_path`
- **Arguments:** `url_or_filename`
- **Keywords:** `{}`

```python
    # Convert fsspec URL in the format "file://local/path" to "local/path"
    if can_be_local(url_or_filename):
        url_or_filename = strip_protocol(url_or_filename)
```

#### 59. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L167) (Line 167)
- **Target Call:** `strip_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `cached_path`
- **Arguments:** `url_or_filename`
- **Keywords:** `{}`

```python
    if can_be_local(url_or_filename):
        url_or_filename = strip_protocol(url_or_filename)

```

#### 60. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L295) (Line 295)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fsspec_head`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    _raise_if_offline_mode_is_enabled(f"Tried to reach {url}")
    fs, path = url_to_fs(url, **(storage_options or {}))
    return fs.info(path)
```

#### 61. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L296) (Line 296)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fsspec_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    fs, path = url_to_fs(url, **(storage_options or {}))
    return fs.info(path)

```

#### 62. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L317) (Line 317)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fsspec_get`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    _raise_if_offline_mode_is_enabled(f"Tried to reach {url}")
    fs, path = url_to_fs(url, **(storage_options or {}))
    callback = TqdmCallback(
```

#### 63. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L330) (Line 330)
- **Target Call:** `fs.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fsspec_get`
- **Arguments:** `path, temp_file.name`
- **Keywords:** `{'callback': 'callback'}`

```python
    )
    fs.get_file(path, temp_file.name, callback=callback)

```

#### 64. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L559) (Line 559)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_extraction_protocol`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
    try:
        with fsspec.open(urlpath, **(storage_options or {})) as f:
            return _get_extraction_protocol_with_magic_number(f)
```

#### 65. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L645) (Line 645)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xexists`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        return fs.exists(main_hop)
```

#### 66. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L646) (Line 646)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xexists`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(urlpath, **storage_options)
        return fs.exists(main_hop)

```

#### 67. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L745) (Line 745)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xisfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = url_to_fs(path, **storage_options)
        return fs.isfile(main_hop)
```

#### 68. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L746) (Line 746)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xisfile`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(path, **storage_options)
        return fs.isfile(main_hop)

```

#### 69. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L765) (Line 765)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xgetsize`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
        try:
```

#### 70. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L767) (Line 767)
- **Target Call:** `fs.size` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xgetsize`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        try:
            size = fs.size(main_hop)
        except huggingface_hub.utils.EntryNotFoundError:
```

#### 71. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L793) (Line 793)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xisdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 72. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L797) (Line 797)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xisdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
            return True
        return fs.isdir(inner_path)

```

#### 73. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L913) (Line 913)
- **Target Call:** `fsspec.available_protocols` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_prepare_single_hop_path_and_storage_options`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            for option_name, option_value in download_config.storage_options.items()
            if option_name not in fsspec.available_protocols()
        }
```

#### 74. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L977) (Line 977)
- **Target Call:** `fsspec.get_fs_token_paths` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
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
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xopen`
- **Arguments:** `paths[0], mode`
- **Keywords:** `{}`

```python
            )
            file_obj = fs.open(paths[0], mode)
            if hasattr(fs, "of") and hasattr(fs.of, "__exit__"):
```

#### 76. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1030) (Line 1030)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xlistdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = path.split("::")
        fs, *_ = url_to_fs(path, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 77. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1032) (Line 1032)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[-1]
        if inner_path.strip("/") and not fs.isdir(inner_path):
            raise FileNotFoundError(f"Directory doesn't exist: {path}")
```

#### 78. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1034) (Line 1034)
- **Target Call:** `fs.listdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{'detail': 'False'}`

```python
            raise FileNotFoundError(f"Directory doesn't exist: {path}")
        paths = fs.listdir(inner_path, detail=False)
        return [os.path.basename(path.rstrip("/")) for path in paths]
```

#### 79. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1057) (Line 1057)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xglob`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        inner_path = main_hop.split("://")[1]
```

#### 80. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1059) (Line 1059)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xglob`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[1]
        globbed_paths = fs.glob(inner_path)
        protocol = fs.protocol if isinstance(fs.protocol, str) else fs.protocol[-1]
```

#### 81. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1083) (Line 1083)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xwalk`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        main_hop, *rest_hops = urlpath.split("::")
        fs, *_ = url_to_fs(urlpath, **storage_options)
        inner_path = main_hop.split("://")[-1]
```

#### 82. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1085) (Line 1085)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        inner_path = main_hop.split("://")[-1]
        if inner_path.strip("/") and not fs.isdir(inner_path):
            return []
```

#### 83. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1088) (Line 1088)
- **Target Call:** `fs.walk` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        protocol = fs.protocol if isinstance(fs.protocol, str) else fs.protocol[-1]
        for dirpath, dirnames, filenames in fs.walk(inner_path, **kwargs):
            yield "::".join([f"{protocol}://{dirpath}"] + rest_hops), dirnames, filenames
```

#### 84. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1161) (Line 1161)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(posix_path, pattern)`
- **Keywords:** `{}`

```python
                storage_options = None
            fs, *_ = url_to_fs(xjoin(posix_path, pattern), **(storage_options or {}))
            globbed_paths = fs.glob(xjoin(main_hop, pattern))
```

#### 85. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1162) (Line 1162)
- **Target Call:** `fs.glob` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(main_hop, pattern)`
- **Keywords:** `{}`

```python
            fs, *_ = url_to_fs(xjoin(posix_path, pattern), **(storage_options or {}))
            globbed_paths = fs.glob(xjoin(main_hop, pattern))
            for globbed_path in globbed_paths:
```

#### 86. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L15) (Line 15)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MockFileSystem.__init__`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
        super().__init__()
        self._fs = LocalFileSystem(*args, **kwargs)
        self.local_root_dir = Path(local_root_dir).resolve().as_posix() + "/"
```

#### 87. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L71) (Line 71)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MockFileSystem._strip_protocol`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def _strip_protocol(cls, path):
        path = stringify_path(path)
        if path.startswith("mock://"):
```

#### 88. [tests/fixtures/fsspec.py](https://github.com/huggingface/datasets/blob/main/tests/fixtures/fsspec.py#L87) (Line 87)
- **Target Call:** `stringify_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TmpDirFileSystem._strip_protocol`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def _strip_protocol(cls, path):
        path = stringify_path(path)
        if path.startswith("tmp://"):
```

### PyTorch ([pytorch/pytorch](https://github.com/pytorch/pytorch))
- **Usages Found:** `38` in `6` files.

#### 1. [torch/_dynamo/pgo.py](https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/pgo.py#L749) (Line 749)
- **Target Call:** `fs.render` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `render_code_state`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        + "\n".join(
            f"  {src}: {fs.render()}" for src, fs in v.automatic_dynamic.items()
        )
```

#### 2. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L47) (Line 47)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.create_stream`
- **Arguments:** `path, mode`
- **Keywords:** `{}`

```python
        # just manually delete the file if necessary on errors.
        with self.fs.open(path, mode) as stream:
            try:
```

#### 3. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L62) (Line 62)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.init_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def init_path(self, path: str | os.PathLike, **kwargs) -> str | os.PathLike:
        self.fs, _ = url_to_fs(path, **kwargs)
        return path
```

#### 4. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L66) (Line 66)
- **Target Call:** `self.fs.rename` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.rename`
- **Arguments:** `path, new_path`
- **Keywords:** `{}`

```python
    def rename(self, path: str | os.PathLike, new_path: str | os.PathLike) -> None:
        self.fs.rename(path, new_path)

```

#### 5. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L69) (Line 69)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.mkdir`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    def mkdir(self, path: str | os.PathLike) -> None:
        self.fs.makedirs(path, exist_ok=True)

```

#### 6. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L77) (Line 77)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.validate_checkpoint_id`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
        try:
            url_to_fs(checkpoint_id)
        except ValueError:
```

#### 7. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L84) (Line 84)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.exists`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def exists(self, path: str | os.PathLike) -> bool:
        return self.fs.exists(path)

```

#### 8. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L87) (Line 87)
- **Target Call:** `self.fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.rm_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def rm_file(self, path: str | os.PathLike) -> None:
        self.fs.rm(path)

```

#### 9. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L92) (Line 92)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'False'}`

```python
        # instead of the list[Dict] return type when detail=True
        return self.fs.ls(path, detail=False)

```

#### 10. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L147) (Line 147)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecWriter.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs = FileSystem()
        self.path = self.fs.init_path(path, **kwargs)

```

#### 11. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L158) (Line 158)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FsspecReader.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs = FileSystem()
        self.path = self.fs.init_path(path, **kwargs)

```

#### 12. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L621) (Line 621)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs = FileSystem()
        self.path = self.fs.init_path(path)
        self.single_file_per_rank = single_file_per_rank
```

#### 13. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L635) (Line 635)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.reset`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
        if checkpoint_id:
            self.path = self.fs.init_path(checkpoint_id)
        self.save_id = _generate_uuid()
```

#### 14. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L653) (Line 653)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter._metadata_exists`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python

        return self.fs.exists(metadata_path)

```

#### 15. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L656) (Line 656)
- **Target Call:** `self.fs.mkdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.prepare_local_plan`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
    def prepare_local_plan(self, plan: SavePlan) -> SavePlan:
        self.fs.mkdir(self.path)
        if self._metadata_exists():
```

#### 16. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L702) (Line 702)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.write_data`
- **Arguments:** `self.path, file_name`
- **Keywords:** `{}`

```python
                file_name = gen_file()
                path = self.fs.concat_path(self.path, file_name)
                file_queue.put((path, file_name, bucket))
```

#### 17. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L707) (Line 707)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.write_data`
- **Arguments:** `self.path, file_name`
- **Keywords:** `{}`

```python
                file_name = gen_file()
                path = self.fs.concat_path(self.path, file_name)
                file_queue.put((path, file_name, [item]))
```

#### 18. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L776) (Line 776)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `self.path, tmp_filename`
- **Keywords:** `{}`

```python
        )
        tmp_path = cast(Path, self.fs.concat_path(self.path, tmp_filename))
        with self.fs.create_stream(tmp_path, "wb") as metadata_file:
```

#### 19. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L777) (Line 777)
- **Target Call:** `self.fs.create_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `tmp_path, 'wb'`
- **Keywords:** `{}`

```python
        tmp_path = cast(Path, self.fs.concat_path(self.path, tmp_filename))
        with self.fs.create_stream(tmp_path, "wb") as metadata_file:
            pickle.dump(metadata, metadata_file)
```

#### 20. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L795) (Line 795)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python

        if self.fs.exists(metadata_path):
            self.fs.rm_file(metadata_path)
```

#### 21. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L796) (Line 796)
- **Target Call:** `self.fs.rm_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        if self.fs.exists(metadata_path):
            self.fs.rm_file(metadata_path)

```

#### 22. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L798) (Line 798)
- **Target Call:** `self.fs.rename` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `tmp_path, metadata_path`
- **Keywords:** `{}`

```python

        self.fs.rename(tmp_path, metadata_path)

```

#### 23. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L805) (Line 805)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileSystemWriter._get_metadata_path`
- **Arguments:** `self.path, filename`
- **Keywords:** `{}`

```python
        filename = f"{_metadata_fn}" if rank is None else f"__{rank}{_metadata_fn}"
        return cast(Path, self.fs.concat_path(self.path, filename))

```

#### 24. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L853) (Line 853)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs = FileSystem()
        self.path = self.fs.init_path(path)
        self.storage_data: dict[Any, Any] = {}
```

#### 25. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L866) (Line 866)
- **Target Call:** `self.fs.init_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader.reset`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
        if checkpoint_id:
            self.path = self.fs.init_path(checkpoint_id)
        self.load_id = _generate_uuid()
```

#### 26. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L878) (Line 878)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader.read_data`
- **Arguments:** `self.path, relative_path`
- **Keywords:** `{}`

```python
        for relative_path, reqs in per_file.items():
            new_path = self.fs.concat_path(self.path, relative_path)
            with self.fs.create_stream(new_path, "rb") as stream:
```

#### 27. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L879) (Line 879)
- **Target Call:** `self.fs.create_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader.read_data`
- **Arguments:** `new_path, 'rb'`
- **Keywords:** `{}`

```python
            new_path = self.fs.concat_path(self.path, relative_path)
            with self.fs.create_stream(new_path, "rb") as stream:
                # TODO sort by offset and cache the reading
```

#### 28. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L931) (Line 931)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader._get_metadata_path`
- **Arguments:** `self.path, filename`
- **Keywords:** `{}`

```python
        filename = f"{_metadata_fn}" if rank is None else f"__{rank}{_metadata_fn}"
        return cast(Path, self.fs.concat_path(self.path, filename))

```

#### 29. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L937) (Line 937)
- **Target Call:** `self.fs.create_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemReader.read_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        path = self._get_metadata_path(rank)
        with self.fs.create_stream(path, "rb") as metadata_file:
            metadata = pickle.load(metadata_file)
```

#### 30. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L92) (Line 92)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HuggingFaceStorageWriter.__init__`
- **Arguments:** `self.path, SHARDED_DIR_NAME`
- **Keywords:** `{}`

```python
            self.consolidated_output_path = str(self.path)
            self.path = self.fs.concat_path(self.path, SHARDED_DIR_NAME)
        self.thread_count_consolidation = thread_count_consolidation
```

#### 31. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L134) (Line 134)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HuggingFaceStorageWriter.write_data`
- **Arguments:** `self.path, file_name`
- **Keywords:** `{}`

```python
            file_queue.put(
                (self.fs.concat_path(self.path, file_name), file_name, write_items)
            )
```

#### 32. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L174) (Line 174)
- **Target Call:** `self.fs.concat_path` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HuggingFaceStorageWriter.finish`
- **Arguments:** `self.path, f'{_metadata_fn}'`
- **Keywords:** `{}`

```python

        metadata_path = self.fs.concat_path(self.path, f"{_metadata_fn}")
        with self.fs.create_stream(metadata_path, "w") as metadata_file:
```

#### 33. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L175) (Line 175)
- **Target Call:** `self.fs.create_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HuggingFaceStorageWriter.finish`
- **Arguments:** `metadata_path, 'w'`
- **Keywords:** `{}`

```python
        metadata_path = self.fs.concat_path(self.path, f"{_metadata_fn}")
        with self.fs.create_stream(metadata_path, "w") as metadata_file:
            json.dump(metadata_to_write, metadata_file, indent=2)
```

#### 34. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L321) (Line 321)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HuggingFaceStorageReader.read_metadata`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        safetensors_files = []
        for file in self.fs.ls(self.path):
            if file.endswith(SUFFIX):
```

#### 35. [torch/utils/tensorboard/_embedding.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/_embedding.py#L21) (Line 21)
- **Target Call:** `fs.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_gfile_join`
- **Arguments:** `a, b`
- **Keywords:** `{}`

```python
        fs = tf.io.gfile.get_filesystem(a)
        return fs.join(a, b)

```

#### 36. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L920) (Line 920)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
        fs = tf.io.gfile
        if fs.exists(save_path):
            if fs.isdir(save_path):
```

#### 37. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L921) (Line 921)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
        if fs.exists(save_path):
            if fs.isdir(save_path):
                print(
```

#### 38. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L930) (Line 930)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
        else:
            fs.makedirs(save_path)

```

### PyTorch Lightning ([Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning))
- **Usages Found:** `69` in `17` files.

#### 1. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L131) (Line 131)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_copy`
- **Arguments:** `str(to_path.parent)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
            if isinstance(fs, LocalFileSystem):
                fs.makedirs(str(to_path.parent), exist_ok=True)

```

#### 2. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L133) (Line 133)
- **Target Call:** `fs.put` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_copy`
- **Arguments:** `str(from_path), str(to_path)`
- **Keywords:** `{'recursive': 'False'}`

```python

            fs.put(str(from_path), str(to_path), recursive=False)
        except Exception as ex:
```

#### 3. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L153) (Line 153)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_copy_files`
- **Arguments:** `str(destination_path.parent)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        if isinstance(fs, LocalFileSystem):
            fs.makedirs(str(destination_path.parent), exist_ok=True)

```

#### 4. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L155) (Line 155)
- **Target Call:** `fs.put` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_copy_files`
- **Arguments:** `str(source_path), str(destination_path)`
- **Keywords:** `{}`

```python

        fs.put(str(source_path), str(destination_path))
```

#### 5. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L88) (Line 88)
- **Target Call:** `self.fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.root`
- **Arguments:** `root_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        if isinstance(self.fs, LocalFileSystem):
            self.fs.makedirs(root_path, exist_ok=True)
        return root_path
```

#### 6. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L151) (Line 151)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.list`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        for p in paths:
            if self.fs.exists(p):
                for f in self.fs.ls(p):
```

#### 7. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L152) (Line 152)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.list`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
            if self.fs.exists(p):
                for f in self.fs.ls(p):
                    files.append(str(pathlib.Path(*pathlib.Path(f).parts[prefix_len:])))
```

#### 8. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L183) (Line 183)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.get`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
                start_time = time()
                while not self.fs.exists(shared_path):
                    sleep(1)
```

#### 9. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L228) (Line 228)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.delete`
- **Arguments:** `str(shared_path)`
- **Keywords:** `{}`

```python
        )
        if self.fs.exists(str(shared_path)):
            self.fs.rm(str(shared_path))
```

#### 10. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L229) (Line 229)
- **Target Call:** `self.fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive.delete`
- **Arguments:** `str(shared_path)`
- **Keywords:** `{}`

```python
        if self.fs.exists(str(shared_path)):
            self.fs.rm(str(shared_path))
        else:
```

#### 11. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L264) (Line 264)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._collect_component_names`
- **Arguments:** `self.drive_root`
- **Keywords:** `{}`

```python
        sep = "/"
        if self.fs.exists(self.drive_root):
            # Invalidate cache before running ls in case new directories have been added
```

#### 12. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L267) (Line 267)
- **Target Call:** `self.fs.invalidate_cache` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._collect_component_names`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            # TODO: Re-evaluate this - may lead to performance issues
            self.fs.invalidate_cache()
            return [str(p.split(sep)[-1]) for p in self.fs.ls(self.drive_root)]
```

#### 13. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L268) (Line 268)
- **Target Call:** `self.fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._collect_component_names`
- **Arguments:** `self.drive_root`
- **Keywords:** `{}`

```python
            self.fs.invalidate_cache()
            return [str(p.split(sep)[-1]) for p in self.fs.ls(self.drive_root)]
        return []
```

#### 14. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L279) (Line 279)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._get`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
    def _get(self, fs, src: pathlib.Path, dst: pathlib.Path, overwrite: bool):
        if fs.isdir(src):
            if isinstance(fs, LocalFileSystem):
```

#### 15. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L282) (Line 282)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._get`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
                dst = dst.resolve()
                if fs.exists(dst):
                    if overwrite:
```

#### 16. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L284) (Line 284)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._get`
- **Arguments:** `str(dst)`
- **Keywords:** `{'recursive': 'True'}`

```python
                    if overwrite:
                        fs.rm(str(dst), recursive=True)
                    else:
```

#### 17. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L291) (Line 291)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._get`
- **Arguments:** `glob, str(dst.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
                glob = f"{str(src)}/**"
                fs.get(glob, str(dst.absolute()), recursive=False)
        else:
```

#### 18. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L293) (Line 293)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._get`
- **Arguments:** `str(src), str(dst.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
        else:
            fs.get(str(src), str(dst.absolute()), recursive=False)

```

#### 19. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L299) (Line 299)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._find_match`
- **Arguments:** `possible_path`
- **Keywords:** `{}`

```python
            possible_path = self._to_shared_path(path, component_name=component_name)
            if self.fs.exists(possible_path):
                matches.append(possible_path)
```

#### 20. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L322) (Line 322)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Drive._check_for_allow_duplicates`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        ]
        matches = [self.fs.exists(p) for p in possible_paths]

```

#### 21. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L14) (Line 14)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_files`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
    dst = dst.resolve()
    if fs.isdir(src):
        if isinstance(fs, LocalFileSystem):
```

#### 22. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L17) (Line 17)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_files`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
            dst = dst.resolve()
            if fs.exists(dst):
                if overwrite:
```

#### 23. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L19) (Line 19)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_files`
- **Arguments:** `str(dst)`
- **Keywords:** `{'recursive': 'True'}`

```python
                if overwrite:
                    fs.rm(str(dst), recursive=True)
                else:
```

#### 24. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L26) (Line 26)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_files`
- **Arguments:** `glob, str(dst)`
- **Keywords:** `{'recursive': 'False'}`

```python
            glob = f"{str(src)}/**"
            fs.get(glob, str(dst), recursive=False)
    else:
```

#### 25. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L28) (Line 28)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_files`
- **Arguments:** `str(src), str(dst)`
- **Keywords:** `{'recursive': 'False'}`

```python
    else:
        fs.get(str(src), str(dst), recursive=False)

```

#### 26. [src/lightning/app/storage/orchestrator.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L122) (Line 122)
- **Target Call:** `self.fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageOrchestrator.run_once`
- **Arguments:** `maybe_artifact_path`
- **Keywords:** `{}`

```python

                if self.fs.exists(maybe_artifact_path):
                    # First check if the shared filesystem has the requested file stored as an artifact
```

#### 27. [src/lightning/app/storage/orchestrator.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L134) (Line 134)
- **Target Call:** `self.fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageOrchestrator.run_once`
- **Arguments:** `maybe_artifact_path`
- **Keywords:** `{}`

```python
                            hash=request.hash,
                            size=self.fs.info(maybe_artifact_path)["size"],
                            destination=request.destination,
```

#### 28. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223) (Line 223)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        # 3. Wait until the file appears in shared storage
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
            sleep(REMOTE_STORAGE_WAIT)
```

#### 29. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223) (Line 223)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        # 3. Wait until the file appears in shared storage
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
            sleep(REMOTE_STORAGE_WAIT)
```

#### 30. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L231) (Line 231)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        # 4. Copy the file from the shared storage to the destination on the local filesystem
        if fs.isdir(response.path):
            if isinstance(fs, LocalFileSystem):
```

#### 31. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L237) (Line 237)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Path.get`
- **Arguments:** `glob, str(self.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
                _logger.debug(f"Attempting to copy {glob} -> {str(self.absolute())}")
                fs.get(glob, str(self.absolute()), recursive=False)
        else:
```

#### 32. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L240) (Line 240)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Path.get`
- **Arguments:** `str(response.path), str(self.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
            _logger.debug(f"Attempting to copy {str(response.path)} -> {str(self.absolute())}")
            fs.get(str(response.path), str(self.absolute()), recursive=False)

```

#### 33. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L434) (Line 434)
- **Target Call:** `LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def _filesystem() -> AbstractFileSystem:
    fs = LocalFileSystem()

```

#### 34. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L450) (Line 450)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_filesystem`
- **Arguments:** `_shared_storage_path()`
- **Keywords:** `{}`

```python

        if not fs.exists(_shared_storage_path()):
            raise RuntimeError(f"shared filesystem {_shared_storage_path()} does not exist")
```

#### 35. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182) (Line 182)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_BasePayload.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        # 3. Wait until the file appears in shared storage
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
            sleep(REMOTE_STORAGE_WAIT)
```

#### 36. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182) (Line 182)
- **Target Call:** `fs.info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_BasePayload.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        # 3. Wait until the file appears in shared storage
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
            sleep(REMOTE_STORAGE_WAIT)
```

#### 37. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L188) (Line 188)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_BasePayload.get`
- **Arguments:** `str(response.path), str(local_path)`
- **Keywords:** `{'recursive': 'False'}`

```python
        _logger.debug(f"Attempting to copy {str(response.path)} -> {str(local_path)}")
        fs.get(str(response.path), str(local_path), recursive=False)

```

#### 38. [src/lightning/app/utilities/commands/base.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/utilities/commands/base.py#L204) (Line 204)
- **Target Call:** `fs.put` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_upload`
- **Arguments:** `source_file, remote_url`
- **Keywords:** `{}`

```python
        remote_url = str(_shared_storage_path() / "artifacts" / filepath)
        fs.put(source_file, remote_url)
        return filepath
```

#### 39. [src/lightning/fabric/plugins/environments/lsf.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/environments/lsf.py#L170) (Line 170)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LSFEnvironment._read_hosts`
- **Arguments:** `rankfile, 'r'`
- **Keywords:** `{}`

```python
        fs = get_filesystem(rankfile)
        with fs.open(rankfile, "r") as f:
            ret = [line.strip() for line in f]
```

#### 40. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L57) (Line 57)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchCheckpointIO.save_checkpoint`
- **Arguments:** `os.path.dirname(path)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs = get_filesystem(path)
        fs.makedirs(os.path.dirname(path), exist_ok=True)
        _atomic_save(checkpoint, path)
```

#### 41. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L80) (Line 80)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchCheckpointIO.load_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs = get_filesystem(path)
        if not fs.exists(path):
            raise FileNotFoundError(f"Checkpoint file not found: {path}")
```

#### 42. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L94) (Line 94)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchCheckpointIO.remove_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs = get_filesystem(path)
        if fs.exists(path):
            fs.rm(path, recursive=True)
```

#### 43. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L95) (Line 95)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchCheckpointIO.remove_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
        if fs.exists(path):
            fs.rm(path, recursive=True)
            log.debug(f"Removed checkpoint: {path}")
```

#### 44. [src/lightning/fabric/plugins/io/xla.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/xla.py#L64) (Line 64)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `XLACheckpointIO.save_checkpoint`
- **Arguments:** `os.path.dirname(path)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs = get_filesystem(path)
        fs.makedirs(os.path.dirname(path), exist_ok=True)
        if RequirementCache("omegaconf"):
```

#### 45. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L56) (Line 56)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load`
- **Arguments:** `path_or_url, 'rb'`
- **Keywords:** `{}`

```python
    fs = get_filesystem(path_or_url)
    with fs.open(path_or_url, "rb") as f:
        return torch.load(f, map_location=map_location)  # type: ignore[arg-type]
```

#### 46. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L61) (Line 61)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_filesystem`
- **Arguments:** `str(path)`
- **Keywords:** `{}`

```python
def get_filesystem(path: _PATH, **kwargs: Any) -> AbstractFileSystem:
    fs, _ = url_to_fs(str(path), **kwargs)
    return fs
```

#### 47. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L79) (Line 79)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_atomic_save`
- **Arguments:** `filepath, 'wb'`
- **Keywords:** `{}`

```python
    torch.save(checkpoint, bytesbuffer)
    with fsspec.open(filepath, "wb") as f:
        f.write(bytesbuffer.getvalue())
```

#### 48. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L126) (Line 126)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if strict:
            return fs.isdir(path)

```

#### 49. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L130) (Line 130)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        # because the directory (and all non-existing parent directories) will be created on the fly.
        return not fs.isfile(path)

```

#### 50. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L132) (Line 132)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

    return fs.isdir(path)

```

#### 51. [src/lightning/pytorch/cli.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L258) (Line 258)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SaveConfigCallback.setup`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
                # check if the file exists on rank 0
                file_exists = fs.isfile(config_path) if trainer.is_global_zero else False
                # broadcast whether to fail to all ranks
```

#### 52. [src/lightning/pytorch/cli.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L273) (Line 273)
- **Target Call:** `fs.makedirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SaveConfigCallback.setup`
- **Arguments:** `log_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                # but it hasn't logged anything at this point
                fs.makedirs(log_dir, exist_ok=True)
                self.parser.save(
```

#### 53. [src/lightning/pytorch/core/module.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/module.py#L1480) (Line 1480)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LightningModule.to_torchscript`
- **Arguments:** `file_path, 'wb'`
- **Keywords:** `{}`

```python
            fs = get_filesystem(file_path)
            with fs.open(file_path, "wb") as f:
                torch.jit.save(torchscript_module, f)
```

#### 54. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L259) (Line 259)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_hparams_from_tags_csv`
- **Arguments:** `tags_csv`
- **Keywords:** `{}`

```python
    fs = get_filesystem(tags_csv)
    if not fs.exists(tags_csv):
        rank_zero_warn(f"Missing Tags: {tags_csv}.", category=RuntimeWarning)
```

#### 55. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L263) (Line 263)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_hparams_from_tags_csv`
- **Arguments:** `tags_csv, 'r'`
- **Keywords:** `{'newline': "''"}`

```python

    with fs.open(tags_csv, "r", newline="") as fp:
        csv_reader = csv.reader(fp, delimiter=",")
```

#### 56. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L276) (Line 276)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `save_hparams_to_tags_csv`
- **Arguments:** `tags_csv, 'w'`
- **Keywords:** `{'newline': "''"}`

```python

    with fs.open(tags_csv, "w", newline="") as fp:
        fieldnames = ["key", "value"]
```

#### 57. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L302) (Line 302)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_hparams_from_yaml`
- **Arguments:** `config_yaml`
- **Keywords:** `{}`

```python
    fs = get_filesystem(config_yaml)
    if not fs.exists(config_yaml):
        rank_zero_warn(f"Missing Tags: {config_yaml}.", category=RuntimeWarning)
```

#### 58. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L306) (Line 306)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_hparams_from_yaml`
- **Arguments:** `config_yaml, 'r'`
- **Keywords:** `{}`

```python

    with fs.open(config_yaml, "r") as fp:
        hparams = yaml.full_load(fp)
```

#### 59. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L346) (Line 346)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `save_hparams_to_yaml`
- **Arguments:** `config_yaml, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        hparams = apply_to_collection(hparams, DictConfig, OmegaConf.to_container, resolve=True)
        with fs.open(config_yaml, "w", encoding="utf-8") as fp:
            try:
```

#### 60. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L369) (Line 369)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `save_hparams_to_yaml`
- **Arguments:** `config_yaml, 'w'`
- **Keywords:** `{'newline': "''"}`

```python
    # saving the standard way
    with fs.open(config_yaml, "w", newline="") as fp:
        yaml.dump(hparams_allowed, fp)
```

#### 61. [src/lightning/pytorch/profilers/profiler.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L98) (Line 98)
- **Target Call:** `fs.mkdirs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Profiler._prepare_streams`
- **Arguments:** `self.dirpath`
- **Keywords:** `{'exist_ok': 'True'}`

```python
            fs = get_filesystem(filepath)
            fs.mkdirs(self.dirpath, exist_ok=True)
            file = fs.open(filepath, "a")
```

#### 62. [src/lightning/pytorch/profilers/profiler.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L99) (Line 99)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Profiler._prepare_streams`
- **Arguments:** `filepath, 'a'`
- **Keywords:** `{}`

```python
            fs.mkdirs(self.dirpath, exist_ok=True)
            file = fs.open(filepath, "a")
            self._output_file = file
```

#### 63. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L53) (Line 53)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector._hpc_resume_path`
- **Arguments:** `dir_path_hpc`
- **Keywords:** `{}`

```python
        dir_path_hpc = str(dir_path_hpc)
        fs, path = url_to_fs(dir_path_hpc)
        if not _is_dir(fs, path):
```

#### 64. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L183) (Line 183)
- **Target Call:** `fs.modified` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector._parse_ckpt_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            candidates_fs = {path: get_filesystem(path) for path in candidates if path}
            candidates_ts = {path: fs.modified(path) for path, fs in candidates_fs.items() if fs.exists(path)}
            if not candidates_ts:
```

#### 65. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L183) (Line 183)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector._parse_ckpt_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            candidates_fs = {path: get_filesystem(path) for path in candidates if path}
            candidates_ts = {path: fs.modified(path) for path, fs in candidates_fs.items() if fs.exists(path)}
            if not candidates_ts:
```

#### 66. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L519) (Line 519)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `str(dir_path)`
- **Keywords:** `{}`

```python
        # check directory existence
        fs, uri = url_to_fs(str(dir_path))
        if not fs.exists(dir_path):
```

#### 67. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L520) (Line 520)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `dir_path`
- **Keywords:** `{}`

```python
        fs, uri = url_to_fs(str(dir_path))
        if not fs.exists(dir_path):
            return None
```

#### 68. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L524) (Line 524)
- **Target Call:** `fs.listdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `uri`
- **Keywords:** `{}`

```python
        # check corresponding file existence
        files = [os.path.basename(f["name"]) for f in fs.listdir(uri)]
        files = [x for x in files if name_key in x]
```

#### 69. [tests/integrations_app/apps/idle_timeout/app.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/tests/integrations_app/apps/idle_timeout/app.py#L55) (Line 55)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RootFlow.run`
- **Arguments:** `destination_path`
- **Keywords:** `{}`

```python
            destination_path = _artifacts_path(self.work) / pathlib.Path(*self.work.path.resolve().parts[1:])
            assert fs.exists(destination_path)
            self.dest_work.run(self.work.path)
```

### TorchTitan ([pytorch/torchtitan](https://github.com/pytorch/torchtitan))
- **Usages Found:** `27` in `3` files.

#### 1. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L161) (Line 161)
- **Target Call:** `filesystem.rmtree` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `purge_thread`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            try:
                filesystem.rmtree(path)
            except Exception as e:
```

#### 2. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L403) (Line 403)
- **Target Call:** `filesystem.is_remote` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.__post_init__`
- **Arguments:** `self.initial_load_path`
- **Keywords:** `{}`

```python
                    self.initial_load_path.startswith("/")
                    or filesystem.is_remote(self.initial_load_path)
                ):
```

#### 3. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L424) (Line 424)
- **Target Call:** `filesystem.is_remote` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.__post_init__`
- **Arguments:** `self.folder`
- **Keywords:** `{}`

```python
            # reject the combination up front instead of failing deep in DCP.
            if self.last_save_in_hf and filesystem.is_remote(self.folder):
                raise ValueError(
```

#### 4. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L432) (Line 432)
- **Target Call:** `filesystem.is_remote` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Config.__post_init__`
- **Arguments:** `self.initial_load_path`
- **Keywords:** `{}`

```python
                and self.initial_load_path
                and filesystem.is_remote(self.initial_load_path)
            ):
```

#### 5. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L473) (Line 473)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.__init__`
- **Arguments:** `base_folder, config.folder`
- **Keywords:** `{}`

```python

        self.folder = filesystem.join(base_folder, config.folder)
        self.interval = config.interval
```

#### 6. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L826) (Line 826)
- **Target Call:** `filesystem.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.load`
- **Arguments:** `self.folder`
- **Keywords:** `{}`

```python

        has_checkpoint_folder = filesystem.exists(self.folder)
        load_step = -1
```

#### 7. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L852) (Line 852)
- **Target Call:** `filesystem.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.load`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
                checkpoint_id = self.initial_load_path
                if not filesystem.isdir(checkpoint_id):
                    raise ValueError(
```

#### 8. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L867) (Line 867)
- **Target Call:** `filesystem.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.load`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
                checkpoint_id = self.sd_adapter.hf_assets_path
                if not filesystem.isdir(checkpoint_id):
                    raise ValueError(
```

#### 9. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L892) (Line 892)
- **Target Call:** `filesystem.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.load`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python

            if not filesystem.isdir(checkpoint_id):
                raise FileNotFoundError(
```

#### 10. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L991) (Line 991)
- **Target Call:** `filesystem.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `folder`
- **Keywords:** `{}`

```python
        folder = folder or self.folder
        if not filesystem.isdir(folder):
            return -1
```

#### 11. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L997) (Line 997)
- **Target Call:** `filesystem.listdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `folder`
- **Keywords:** `{}`

```python

        for filename in filesystem.listdir(folder):
            match = re.search(pattern, filename)
```

#### 12. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1003) (Line 1003)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `folder, filename`
- **Keywords:** `{}`

```python
            # A checkpoint is valid only if it contains core metadata
            checkpoint_path = filesystem.join(folder, filename)
            is_dcp = filesystem.isfile(filesystem.join(checkpoint_path, ".metadata"))
```

#### 13. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1004) (Line 1004)
- **Target Call:** `filesystem.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `filesystem.join(checkpoint_path, '.metadata')`
- **Keywords:** `{}`

```python
            checkpoint_path = filesystem.join(folder, filename)
            is_dcp = filesystem.isfile(filesystem.join(checkpoint_path, ".metadata"))
            is_hf = filesystem.isfile(
```

#### 14. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1004) (Line 1004)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `checkpoint_path, '.metadata'`
- **Keywords:** `{}`

```python
            checkpoint_path = filesystem.join(folder, filename)
            is_dcp = filesystem.isfile(filesystem.join(checkpoint_path, ".metadata"))
            is_hf = filesystem.isfile(
```

#### 15. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1005) (Line 1005)
- **Target Call:** `filesystem.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `filesystem.join(checkpoint_path, 'model.safetensors.index.json')`
- **Keywords:** `{}`

```python
            is_dcp = filesystem.isfile(filesystem.join(checkpoint_path, ".metadata"))
            is_hf = filesystem.isfile(
                filesystem.join(checkpoint_path, "model.safetensors.index.json")
            )

```

#### 16. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1006) (Line 1006)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `checkpoint_path, 'model.safetensors.index.json'`
- **Keywords:** `{}`

```python
            is_hf = filesystem.isfile(
                filesystem.join(checkpoint_path, "model.safetensors.index.json")
            )
```

#### 17. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1018) (Line 1018)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._create_checkpoint_id`
- **Arguments:** `folder, f'step-{step}'`
- **Keywords:** `{}`

```python
        folder = folder or self.folder
        return filesystem.join(folder, f"step-{step}")

```

#### 18. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1144) (Line 1144)
- **Target Call:** `filesystem.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._should_purge`
- **Arguments:** `self.folder`
- **Keywords:** `{}`

```python
            and dist.get_rank() == 0
            and filesystem.isdir(self.folder)
        )
```

#### 19. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1152) (Line 1152)
- **Target Call:** `filesystem.listdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._purge_stale_checkpoints`
- **Arguments:** `self.folder`
- **Keywords:** `{}`

```python
            discovered_checkpoints = []
            for filename in filesystem.listdir(self.folder):
                match = re.search(r"step-(\d+)", filename)
```

#### 20. [torchtitan/components/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py#L1155) (Line 1155)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager._purge_stale_checkpoints`
- **Arguments:** `self.folder, filename`
- **Keywords:** `{}`

```python
                if match:
                    path = filesystem.join(self.folder, filename)
                    discovered_checkpoints.append((int(match.group(1)), path))
```

#### 21. [torchtitan/experiments/torchft/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/experiments/torchft/checkpoint.py#L197) (Line 197)
- **Target Call:** `filesystem.join` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TorchFTCheckpointManager._ft_folder`
- **Arguments:** `self.folder, f'ft-replicat-{self.ft_replica_id}'`
- **Keywords:** `{}`

```python
    def _ft_folder(self) -> str:
        return filesystem.join(self.folder, f"ft-replicat-{self.ft_replica_id}")

```

#### 22. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L40) (Line 40)
- **Target Call:** `url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve`
- **Arguments:** `path`
- **Keywords:** `{}`

```python

    return url_to_fs(path)

```

#### 23. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L46) (Line 46)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `exists`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        fs, p = _resolve(path)
        return fs.exists(p)
    return os.path.exists(path)
```

#### 24. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L53) (Line 53)
- **Target Call:** `fs.isdir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `isdir`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        fs, p = _resolve(path)
        return fs.isdir(p)
    return os.path.isdir(path)
```

#### 25. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L60) (Line 60)
- **Target Call:** `fs.isfile` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `isfile`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        fs, p = _resolve(path)
        return fs.isfile(p)
    return os.path.isfile(path)
```

#### 26. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L81) (Line 81)
- **Target Call:** `fs.ls` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `listdir`
- **Arguments:** `p`
- **Keywords:** `{'detail': 'False'}`

```python
            posixpath.basename(entry.rstrip("/"))
            for entry in fs.ls(p, detail=False)
            if entry.rstrip("/") != self_entry
```

#### 27. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L94) (Line 94)
- **Target Call:** `fs.rm` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rmtree`
- **Arguments:** `p`
- **Keywords:** `{'recursive': 'True'}`

```python
        try:
            fs.rm(p, recursive=True)
        except FileNotFoundError:
```

### Ray ([ray-project/ray](https://github.com/ray-project/ray))
- **Usages Found:** `123` in `34` files.

#### 1. [python/ray/_private/runtime_env/protocol.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L203) (Line 203)
- **Target Call:** `filesystem.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ProtocolsProvider.open_file`
- **Arguments:** `uri, mode`
- **Keywords:** `{}`

```python
            )
            return filesystem.open(uri, mode)

```

#### 2. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L87) (Line 87)
- **Target Call:** `self.fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        """
        return self._storage_filesystem or pyarrow.fs.LocalFileSystem()

```

#### 3. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L240) (Line 240)
- **Target Call:** `fs.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** `error_file_path`
- **Keywords:** `{}`

```python
        if _exists_at_fs_path(fs, error_file_path):
            with fs.open_input_stream(error_file_path) as f:
                error = ray.cloudpickle.load(f)
```

#### 4. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** `video_path`
- **Keywords:** `{}`

```python
                if video_path not in self._cache:
                    file_handle = fsspec.open(video_path, **opts).__enter__()
                    try:
```

#### 5. [python/ray/data/_internal/datasource/json_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/json_datasource.py#L253) (Line 253)
- **Target Call:** `filesystem.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PandasJSONDatasource._open_input_source`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            # We use a seekable file to estimate chunksize.
            return filesystem.open_input_file(path)

```

#### 6. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L165) (Line 165)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_build_schema`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    )
    with fs.open(path, "rb") as f:
        pq_schema = pq.read_schema(f)
```

#### 7. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L352) (Line 352)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `root_uri`
- **Keywords:** `{}`

```python
    video_storage_options = dict(storage_options)
    protocol, rest = split_protocol(root_uri)
    if protocol and rest and rest.startswith("anonymous@"):
```

#### 8. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L373) (Line 373)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python

            fs = ArrowFSWrapper(filesystem)
            # A pyarrow filesystem does not expose its credentials, so it can't
```

#### 9. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L386) (Line 386)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        # storage_options and default branches, which already strip the marker.
        _, fs_root = split_protocol(video_root_uri)
        fs_root = (fs_root or video_root_uri).rstrip("/")
```

#### 10. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L401) (Line 401)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
        resolved_paths, pa_fs = _resolve_paths_and_filesystem([root_uri])
        fs = ArrowFSWrapper(pa_fs)
        fs_root = resolved_paths[0].rstrip("/")
```

#### 11. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L417) (Line 417)
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta/info.json'`
- **Keywords:** `{}`

```python
    fs_root = fs_root.rstrip("/")
    if not fs.exists(f"{fs_root}/meta/info.json"):
        raise FileNotFoundError(
```

#### 12. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L431) (Line 431)
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta', os.path.join(local_root, 'meta')`
- **Keywords:** `{'recursive': 'True'}`

```python
    local_root = tempfile.mkdtemp(prefix="ray_data_lerobot_")
    fs.get(f"{fs_root}/meta", os.path.join(local_root, "meta"), recursive=True)
    meta = LeRobotDatasetMetadata(repo_id=root_uri, root=local_root)
```

#### 13. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L753) (Line 753)
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_lerobot_segment`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    for path in parquet_segs:
        with fs.open(path, "rb") as f:
            pq_tables.append(pq.read_table(f, filters=filters))
```

#### 14. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1229) (Line 1229)
- **Target Call:** `self.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_decode_image_frames`
- **Arguments:** `p, 'rb'`
- **Keywords:** `{}`

```python
                p = p if p.startswith(root.fs_root) else f"{root.fs_root}/{p}"
                with root.fs.open(p, "rb") as fh:
                    data = fh.read()
```

#### 15. [python/ray/data/_internal/datasource/parquet_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/parquet_datasource.py#L680) (Line 680)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ParquetDatasource.from_pyarrow_dataset`
- **Arguments:** `pq_paths`
- **Keywords:** `{}`

```python

            infos = filesystem.get_file_info(pq_paths)
            file_sizes = [info.size if info.size is not None else 0 for info in infos]
```

#### 16. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317) (Line 317)
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `'zip'`
- **Keywords:** `{'fo': 'self.paths[0]'}`

```python

            self._fs = fsspec.filesystem("zip", fo=self.paths[0])
            self._store_path = ""
```

#### 17. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L327) (Line 327)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
            resolved_paths, pa_fs = _resolve_paths_and_filesystem([self.paths[0]])
            self._fs = ArrowFSWrapper(pa_fs)
            self._store_path = resolved_paths[0].rstrip("/")
```

#### 18. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L337) (Line 337)
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python

                self._fs = ArrowFSWrapper(filesystem)
            else:
```

#### 19. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L353) (Line 353)
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `self.paths[0]`
- **Keywords:** `{}`

```python

                _, store_path = split_protocol(self.paths[0])
                self._store_path = store_path.rstrip("/")
```

#### 20. [python/ray/data/_internal/datasource_v2/listing/indexing_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource_v2/listing/indexing_utils.py#L44) (Line 44)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_expand_directory`
- **Arguments:** `selector`
- **Keywords:** `{}`

```python
    )
    children = filesystem.get_file_info(selector)

```

#### 21. [python/ray/data/_internal/datasource_v2/listing/indexing_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource_v2/listing/indexing_utils.py#L90) (Line 90)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_path_contents`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    try:
        file_info = filesystem.get_file_info(path)
    except OSError as e:
```

#### 22. [python/ray/data/_internal/datasource_v2/parquet_datasource_v2.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource_v2/parquet_datasource_v2.py#L241) (Line 241)
- **Target Call:** `filesystem.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ParquetDatasourceV2._read_schema`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                    return pq.read_schema(path)
                with filesystem.open_input_file(path) as handle:
                    return pq.read_schema(handle)
```

#### 23. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L281) (Line 281)
- **Target Call:** `filesystem.__reduce__` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_native_s3_obstore_kwargs`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        # from the underlying credentials kind, so this is the authoritative view.
        state = filesystem.__reduce__()[1][0]
    except Exception as e:
```

#### 24. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L360) (Line 360)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_extract_credentials_from_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, RetryingPyFileSystem):
        filesystem = filesystem.unwrap()

```

#### 25. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L473) (Line 473)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_obstore_filesystem_requires_threaded_download`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, RetryingPyFileSystem):
        filesystem = filesystem.unwrap()

```

#### 26. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L497) (Line 497)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_fsspec_s3_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, RetryingPyFileSystem):
        filesystem = filesystem.unwrap()
    if not isinstance(filesystem, pyarrow.fs.PyFileSystem):
```

#### 27. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L530) (Line 530)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_warn_fsspec_s3_credentials_unextractable`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    unwrapped = (
        filesystem.unwrap()
        if isinstance(filesystem, RetryingPyFileSystem)
```

#### 28. [python/ray/data/_internal/planner/_obstore_download.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/_obstore_download.py#L606) (Line 606)
- **Target Call:** `self.fs.resolve_s3_region` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_discover_aws_bucket_region`
- **Arguments:** `bucket`
- **Keywords:** `{}`

```python
    try:
        region = pyarrow.fs.resolve_s3_region(bucket)
    except Exception as e:
```

#### 29. [python/ray/data/_internal/planner/checkpoint/plan_read_op.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/checkpoint/plan_read_op.py#L56) (Line 56)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `create_checkpoint_filter_op`
- **Arguments:** `_unwrap_protocol(checkpoint_config.checkpoint_path)`
- **Keywords:** `{}`

```python
    # 2. no valid files under checkpoint_path (for example, it is an empty directory).
    info = checkpoint_config.filesystem.get_file_info(
        _unwrap_protocol(checkpoint_config.checkpoint_path)
    )
    if info.type == fs.FileType.NotFound:
```

#### 30. [python/ray/data/_internal/planner/download_partition_actor.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/planner/download_partition_actor.py#L62) (Line 62)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_PyArrowFileSizeProvider.get_file_size`
- **Arguments:** `uri_path`
- **Keywords:** `{}`

```python
            try:
                return fs.get_file_info(uri_path).size
            except Exception:
```

#### 31. [python/ray/data/checkpoint/checkpoint_filter.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_filter.py#L240) (Line 240)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CheckpointManager.load_checkpoint`
- **Arguments:** `FileSelector(self.checkpoint_path_unwrapped, recursive=self.checkpoint_path_partition_filter is not None, allow_not_found=True)`
- **Keywords:** `{}`

```python
        # the top level.
        entries = self.filesystem.get_file_info(
            FileSelector(
                self.checkpoint_path_unwrapped,
                recursive=self.checkpoint_path_partition_filter is not None,
                allow_not_found=True,
            )
        )
        if not any(f.type == FileType.File for f in entries):
```

#### 32. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L133) (Line 133)
- **Target Call:** `self.filesystem.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BatchBasedCheckpointWriter.__init__`
- **Arguments:** `self.checkpoint_path_unwrapped`
- **Keywords:** `{'recursive': 'True'}`

```python

        self.filesystem.create_dir(self.checkpoint_path_unwrapped, recursive=True)

```

#### 33. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L248) (Line 248)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BatchBasedCheckpointWriter._rename`
- **Arguments:** `pending.committed_path`
- **Keywords:** `{}`

```python
            # Check if already committed (idempotent)
            committed_info = self.filesystem.get_file_info(pending.committed_path)
            pending_info = self.filesystem.get_file_info(pending.pending_path)
```

#### 34. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L249) (Line 249)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BatchBasedCheckpointWriter._rename`
- **Arguments:** `pending.pending_path`
- **Keywords:** `{}`

```python
            committed_info = self.filesystem.get_file_info(pending.committed_path)
            pending_info = self.filesystem.get_file_info(pending.pending_path)

```

#### 35. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L257) (Line 257)
- **Target Call:** `self.filesystem.delete_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BatchBasedCheckpointWriter._rename`
- **Arguments:** `pending.pending_path`
- **Keywords:** `{}`

```python
                if pending_exists:
                    self.filesystem.delete_file(pending.pending_path)
                return
```

#### 36. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L267) (Line 267)
- **Target Call:** `self.filesystem.move` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BatchBasedCheckpointWriter._rename`
- **Arguments:** `pending.pending_path, pending.committed_path`
- **Keywords:** `{}`

```python
            # Normal case: move pending to committed
            self.filesystem.move(pending.pending_path, pending.committed_path)

```

#### 37. [python/ray/data/checkpoint/load_checkpoint_callback.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/load_checkpoint_callback.py#L34) (Line 34)
- **Target Call:** `filesystem.delete_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LoadCheckpointCallback._delete_checkpoint`
- **Arguments:** `checkpoint_path_unwrapped`
- **Keywords:** `{}`

```python
        filesystem = self._config.filesystem
        filesystem.delete_dir(checkpoint_path_unwrapped)

```

#### 38. [python/ray/data/datasource/file_based_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_based_datasource.py#L395) (Line 395)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileBasedDatasource._file_to_snappy_stream`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        stream = io.BytesIO()
        if isinstance(filesystem.unwrap(), HadoopFileSystem):
            snappy.hadoop_snappy.stream_decompress(src=file, dst=stream)
```

#### 39. [python/ray/data/datasource/file_based_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_based_datasource.py#L427) (Line 427)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileBasedDatasource._open_input_source`
- **Arguments:** `path`
- **Keywords:** `{'buffer_size': 'buffer_size'}`

```python
            open_args["compression"] = None
            file = filesystem.open_input_stream(
                path, buffer_size=buffer_size, **open_args
            )
            return self._file_to_snappy_stream(file, filesystem)
```

#### 40. [python/ray/data/datasource/file_based_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_based_datasource.py#L433) (Line 433)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileBasedDatasource._open_input_source`
- **Arguments:** `path`
- **Keywords:** `{'buffer_size': 'buffer_size'}`

```python
        open_args["compression"] = compression
        return filesystem.open_input_stream(path, buffer_size=buffer_size, **open_args)

```

#### 41. [python/ray/data/datasource/file_based_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_based_datasource.py#L529) (Line 529)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_wrap_s3_serialization_workaround`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, RetryingPyFileSystem):
        base_fs = filesystem.unwrap()

```

#### 42. [python/ray/data/datasource/file_based_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_based_datasource.py#L541) (Line 541)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_unwrap_s3_serialization_workaround`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, _S3FileSystemWrapper):
        filesystem = filesystem.unwrap()
    return filesystem
```

#### 43. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L90) (Line 90)
- **Target Call:** `self.filesystem.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink.open_output_stream`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    def open_output_stream(self, path: str) -> "pyarrow.NativeFile":
        return self.filesystem.open_output_stream(path, **self.open_stream_args)

```

#### 44. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L101) (Line 101)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink.on_write_start`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        dir_exists = (
            self.filesystem.get_file_info(self.path).type is not FileType.NotFound
        )
```

#### 45. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L115) (Line 115)
- **Target Call:** `self.filesystem.delete_dir_contents` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink.on_write_start`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
                logger.warning(f"[SaveMode={self.mode}] Replacing contents {self.path}")
                self.filesystem.delete_dir_contents(self.path)
        self.has_created_dir = self._create_dir(self.path)
```

#### 46. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L141) (Line 141)
- **Target Call:** `self.filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink._create_dir`
- **Arguments:** `dest`
- **Keywords:** `{}`

```python
        if self.try_create_dir and not skip_create_dir_for_s3:
            if self.filesystem.get_file_info(dest).type is FileType.NotFound:
                # Arrow's S3FileSystem doesn't allow creating buckets by default, so we
```

#### 47. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L145) (Line 145)
- **Target Call:** `self.filesystem.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink._create_dir`
- **Arguments:** `tmp`
- **Keywords:** `{'recursive': 'True'}`

```python
                tmp = add_creatable_buckets_param_if_s3_uri(dest)
                self.filesystem.create_dir(tmp, recursive=True)
                return True
```

#### 48. [python/ray/data/datasource/file_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_datasink.py#L173) (Line 173)
- **Target Call:** `self.filesystem.delete_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_FileDatasink.on_write_complete`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        if self.has_created_dir and write_result.num_rows == 0:
            self.filesystem.delete_dir(self.path)

```

#### 49. [python/ray/data/datasource/file_meta_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_meta_provider.py#L278) (Line 278)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_expand_paths`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(filesystem, RetryingPyFileSystem):
        is_local = isinstance(filesystem.unwrap(), LocalFileSystem)

```

#### 50. [python/ray/data/datasource/file_meta_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_meta_provider.py#L433) (Line 433)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_file_infos`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    try:
        file_info = filesystem.get_file_info(path)
    except OSError as e:
```

#### 51. [python/ray/data/datasource/file_meta_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/file_meta_provider.py#L477) (Line 477)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_expand_directory`
- **Arguments:** `selector`
- **Keywords:** `{}`

```python
    selector = FileSelector(path, recursive=True, allow_not_found=ignore_missing_path)
    files = filesystem.get_file_info(selector)
    base_path = selector.base_dir
```

#### 52. [python/ray/data/datasource/path_util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L39) (Line 39)
- **Target Call:** `HTTPFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_fsspec_http_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python

    return PyFileSystem(FSSpecHandler(HTTPFileSystem()))

```

#### 53. [python/ray/data/datasource/path_util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L198) (Line 198)
- **Target Call:** `filesystem.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_filesystem_compatible_with_scheme`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    unwrapped = (
        filesystem.unwrap()
        if isinstance(filesystem, RetryingPyFileSystem)
```

#### 54. [python/ray/data/datasource/path_util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L438) (Line 438)
- **Target Call:** `fs.unwrap` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_http_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if isinstance(fs, RetryingPyFileSystem):
        fs = fs.unwrap()

```

#### 55. [python/ray/data/tests/conftest.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/conftest.py#L177) (Line 177)
- **Target Call:** `self.fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_s3_fs`
- **Arguments:** ``
- **Keywords:** `{'region': "'us-west-2'", 'endpoint_override': 's3_server'}`

```python
    try:
        fs = pa.fs.S3FileSystem(
            region="us-west-2",
            endpoint_override=s3_server,
            **kwargs,
        )
        if s3_path.startswith("s3://"):
```

#### 56. [python/ray/data/tests/conftest.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/conftest.py#L188) (Line 188)
- **Target Call:** `fs.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_s3_fs`
- **Arguments:** `s3_path`
- **Keywords:** `{}`

```python
        s3_path = urllib.parse.quote(s3_path)
        fs.create_dir(s3_path)
        yield fs
```

#### 57. [python/ray/data/tests/conftest.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/conftest.py#L197) (Line 197)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_s3_fs`
- **Arguments:** `s3_path`
- **Keywords:** `{}`

```python
                try:
                    file_info = fs.get_file_info(s3_path)
                    if file_info.type != pa.fs.FileType.NotFound:
```

#### 58. [python/ray/data/tests/conftest.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/conftest.py#L199) (Line 199)
- **Target Call:** `fs.delete_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_s3_fs`
- **Arguments:** `s3_path`
- **Keywords:** `{}`

```python
                    if file_info.type != pa.fs.FileType.NotFound:
                        fs.delete_dir(s3_path)
                except (OSError, pa.lib.ArrowIOError):
```

#### 59. [python/ray/data/tests/conftest.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/conftest.py#L218) (Line 218)
- **Target Call:** `self.fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `local_fs`
- **Arguments:** ``
- **Keywords:** `{}`

```python
def local_fs():
    yield pa.fs.LocalFileSystem()

```

#### 60. [python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py#L194) (Line 194)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PyArrowFileSystem._filter_files`
- **Arguments:** `file_selector`
- **Keywords:** `{}`

```python
        file_selector = pa_fs.FileSelector(source_path, recursive=True)
        file_infos = fs.get_file_info(file_selector)

```

#### 61. [python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py#L237) (Line 237)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PyArrowFileSystem.get_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            # Check if file exists
            if not fs.get_file_info(path).type == pa_fs.FileType.File:
                logger.info(f"URI {object_uri} does not exist.")
```

#### 62. [python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py#L242) (Line 242)
- **Target Call:** `fs.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PyArrowFileSystem.get_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            # Read file
            with fs.open_input_file(path) as f:
                body = f.read()
```

#### 63. [python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_filesystem/pyarrow_filesystem.py#L269) (Line 269)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PyArrowFileSystem.list_subfolders`
- **Arguments:** `pa_fs.FileSelector(path, recursive=False)`
- **Keywords:** `{}`

```python
            # List directory contents
            file_infos = fs.get_file_info(pa_fs.FileSelector(path, recursive=False))

```

#### 64. [python/ray/train/_checkpoint.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_checkpoint.py#L157) (Line 157)
- **Target Call:** `self.filesystem.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpoint.get_metadata`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python

        with self.filesystem.open_input_file(metadata_path) as f:
            return json.loads(f.readall().decode("utf-8"))
```

#### 65. [python/ray/train/_checkpoint.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_checkpoint.py#L166) (Line 166)
- **Target Call:** `self.filesystem.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpoint.set_metadata`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        metadata_path = Path(self.path, _METADATA_FILE_NAME).as_posix()
        with self.filesystem.open_output_stream(metadata_path) as f:
            f.write(json.dumps(metadata).encode("utf-8"))
```

#### 66. [python/ray/train/_checkpoint.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_checkpoint.py#L188) (Line 188)
- **Target Call:** `self.fs.LocalFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpoint.from_directory`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        """
        return cls(path, filesystem=pyarrow.fs.LocalFileSystem())

```

#### 67. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L118) (Line 118)
- **Target Call:** `self.fs.copy_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_pyarrow_fs_copy_files`
- **Arguments:** `source, destination`
- **Keywords:** `{'source_filesystem': 'source_filesystem', 'destination_filesystem': 'destination_filesystem'}`

```python

    return pyarrow.fs.copy_files(
        source,
        destination,
        source_filesystem=source_filesystem,
        destination_filesystem=destination_filesystem,
        **kwargs,
    )

```

#### 68. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L135) (Line 135)
- **Target Call:** `fs.delete_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_delete_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if is_dir:
            fs.delete_dir(fs_path)
        else:
```

#### 69. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L137) (Line 137)
- **Target Call:** `fs.delete_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_delete_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        else:
            fs.delete_file(fs_path)
    except Exception:
```

#### 70. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L232) (Line 232)
- **Target Call:** `self.fs.FSSpecHandler` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_upload_to_uri_with_exclude_fsspec`
- **Arguments:** `local_fs`
- **Keywords:** `{}`

```python
    local_fs = _ExcludingLocalFilesystem(root_path=local_path, exclude=exclude)
    handler = pyarrow.fs.FSSpecHandler(local_fs)
    source_fs = pyarrow.fs.PyFileSystem(handler)
```

#### 71. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L233) (Line 233)
- **Target Call:** `self.fs.PyFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_upload_to_uri_with_exclude_fsspec`
- **Arguments:** `handler`
- **Keywords:** `{}`

```python
    handler = pyarrow.fs.FSSpecHandler(local_fs)
    source_fs = pyarrow.fs.PyFileSystem(handler)

```

#### 72. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L253) (Line 253)
- **Target Call:** `self.fs.FileSelector` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_list_at_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{'allow_not_found': 'True', 'recursive': 'False'}`

```python

    selector = pyarrow.fs.FileSelector(fs_path, allow_not_found=True, recursive=False)
    return [
```

#### 73. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L256) (Line 256)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_list_at_fs_path`
- **Arguments:** `selector`
- **Keywords:** `{}`

```python
        os.path.relpath(file_info.path.lstrip("/"), start=fs_path.lstrip("/"))
        for file_info in fs.get_file_info(selector)
        if file_filter(file_info)
```

#### 74. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L264) (Line 264)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_exists_at_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    valid = fs.get_file_info(fs_path)
    return valid.type != pyarrow.fs.FileType.NotFound
```

#### 75. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L282) (Line 282)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_directory`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    file_info = fs.get_file_info(fs_path)
    if file_info.type == pyarrow.fs.FileType.NotFound:
```

#### 76. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L299) (Line 299)
- **Target Call:** `fs.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_create_directory`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    try:
        fs.create_dir(fs_path)
    except Exception:
```

#### 77. [python/ray/train/base_trainer.py](https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L381) (Line 381)
- **Target Call:** `fs.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseTrainer.restore`
- **Arguments:** `trainer_pkl_path`
- **Keywords:** `{}`

```python
        trainer_pkl_path = Path(fs_path, _TRAINER_PKL).as_posix()
        with fs.open_input_file(trainer_pkl_path) as f:
            trainer_cls, param_dict = pickle.loads(f.readall())
```

#### 78. [python/ray/train/base_trainer.py](https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L776) (Line 776)
- **Target Call:** `fs.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseTrainer._save`
- **Arguments:** `experiment_path`
- **Keywords:** `{}`

```python

        fs.create_dir(experiment_path)
        with fs.open_output_stream(Path(experiment_path, _TRAINER_PKL).as_posix()) as f:
```

#### 79. [python/ray/train/base_trainer.py](https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L777) (Line 777)
- **Target Call:** `fs.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseTrainer._save`
- **Arguments:** `Path(experiment_path, _TRAINER_PKL).as_posix()`
- **Keywords:** `{}`

```python
        fs.create_dir(experiment_path)
        with fs.open_output_stream(Path(experiment_path, _TRAINER_PKL).as_posix()) as f:
            f.write(pickle.dumps(cls_and_param_dict))
```

#### 80. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L112) (Line 112)
- **Target Call:** `self.fs.copy_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_pyarrow_fs_copy_files`
- **Arguments:** `source, destination`
- **Keywords:** `{'source_filesystem': 'source_filesystem', 'destination_filesystem': 'destination_filesystem'}`

```python

    return pyarrow.fs.copy_files(
        source,
        destination,
        source_filesystem=source_filesystem,
        destination_filesystem=destination_filesystem,
        **kwargs,
    )

```

#### 81. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L130) (Line 130)
- **Target Call:** `fs.delete_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `delete_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if is_dir:
            fs.delete_dir(fs_path)
        else:
```

#### 82. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L132) (Line 132)
- **Target Call:** `fs.delete_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `delete_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        else:
            fs.delete_file(fs_path)
    except Exception:
```

#### 83. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L227) (Line 227)
- **Target Call:** `self.fs.FSSpecHandler` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_upload_to_uri_with_exclude_fsspec`
- **Arguments:** `local_fs`
- **Keywords:** `{}`

```python
    local_fs = _ExcludingLocalFilesystem(root_path=local_path, exclude=exclude)
    handler = pyarrow.fs.FSSpecHandler(local_fs)
    source_fs = pyarrow.fs.PyFileSystem(handler)
```

#### 84. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L228) (Line 228)
- **Target Call:** `self.fs.PyFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_upload_to_uri_with_exclude_fsspec`
- **Arguments:** `handler`
- **Keywords:** `{}`

```python
    handler = pyarrow.fs.FSSpecHandler(local_fs)
    source_fs = pyarrow.fs.PyFileSystem(handler)

```

#### 85. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L245) (Line 245)
- **Target Call:** `self.fs.FileSelector` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_list_at_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{'allow_not_found': 'True', 'recursive': 'False'}`

```python
    """
    selector = pyarrow.fs.FileSelector(fs_path, allow_not_found=True, recursive=False)
    return [
```

#### 86. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L248) (Line 248)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_list_at_fs_path`
- **Arguments:** `selector`
- **Keywords:** `{}`

```python
        os.path.relpath(file_info.path.lstrip("/"), start=fs_path.lstrip("/"))
        for file_info in fs.get_file_info(selector)
        if file_filter(file_info)
```

#### 87. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L256) (Line 256)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_exists_at_fs_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    valid = fs.get_file_info(fs_path)
    return valid.type != pyarrow.fs.FileType.NotFound
```

#### 88. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L274) (Line 274)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_directory`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python

    file_info = fs.get_file_info(fs_path)
    if file_info.type == pyarrow.fs.FileType.NotFound:
```

#### 89. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L291) (Line 291)
- **Target Call:** `fs.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_create_directory`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    try:
        fs.create_dir(fs_path)
    except Exception:
```

#### 90. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L773) (Line 773)
- **Target Call:** `fs.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.get_pickled_error`
- **Arguments:** `pickled_error_fs_path`
- **Keywords:** `{}`

```python
        if _exists_at_fs_path(fs=fs, fs_path=pickled_error_fs_path):
            with fs.open_input_stream(pickled_error_fs_path) as f:
                return cloudpickle.loads(f.readall())
```

#### 91. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L792) (Line 792)
- **Target Call:** `fs.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.get_error`
- **Arguments:** `txt_error_fs_path`
- **Keywords:** `{}`

```python
        if _exists_at_fs_path(fs=fs, fs_path=txt_error_fs_path):
            with fs.open_input_stream(txt_error_fs_path) as f:
                return f.readall().decode()
```

#### 92. [python/ray/tune/impl/tuner_internal.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L182) (Line 182)
- **Target Call:** `fs.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TunerInternal.__init__`
- **Arguments:** `storage.experiment_fs_path`
- **Keywords:** `{}`

```python
        fs = storage.storage_filesystem
        fs.create_dir(storage.experiment_fs_path)
        with fs.open_output_stream(
```

#### 93. [python/ray/tune/impl/tuner_internal.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L183) (Line 183)
- **Target Call:** `fs.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TunerInternal.__init__`
- **Arguments:** `Path(storage.experiment_fs_path, _TUNER_PKL).as_posix()`
- **Keywords:** `{}`

```python
        fs.create_dir(storage.experiment_fs_path)
        with fs.open_output_stream(
            Path(storage.experiment_fs_path, _TUNER_PKL).as_posix()
        ) as f:
            f.write(pickle.dumps(self.__getstate__()))
```

#### 94. [python/ray/tune/impl/tuner_internal.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L379) (Line 379)
- **Target Call:** `fs.open_input_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TunerInternal._restore_from_path_or_uri`
- **Arguments:** `Path(fs_path, _TUNER_PKL).as_posix()`
- **Keywords:** `{}`

```python
        fs, fs_path = get_fs_and_path(path_or_uri, storage_filesystem)
        with fs.open_input_file(Path(fs_path, _TUNER_PKL).as_posix()) as f:
            tuner_state = pickle.loads(f.readall())
```

#### 95. [python/ray/tune/logger/logger.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/logger.py#L125) (Line 125)
- **Target Call:** `self.fs.copy_files` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LoggerCallback._restore_from_remote`
- **Arguments:** `remote_file, local_file`
- **Keywords:** `{'source_filesystem': 'trial.storage.storage_filesystem'}`

```python
        try:
            pyarrow.fs.copy_files(
                remote_file,
                local_file,
                source_filesystem=trial.storage.storage_filesystem,
            )
            logger.debug(f"Copied {remote_file} to {local_file}")
```

#### 96. [release/nightly_tests/dataset/multi_node_train_benchmark.py](https://github.com/ray-project/ray/blob/master/release/nightly_tests/dataset/multi_node_train_benchmark.py#L667) (Line 667)
- **Target Call:** `fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_s3fs_with_boto_creds`
- **Arguments:** ``
- **Keywords:** `{'access_key': 'credentials.access_key', 'secret_key': 'credentials.secret_key', 'session_token': 'credentials.token', 'region': "'us-west-2'"}`

```python

    s3fs = fs.S3FileSystem(
        access_key=credentials.access_key,
        secret_key=credentials.secret_key,
        session_token=credentials.token,
        region="us-west-2",
    )
    return s3fs
```

#### 97. [release/nightly_tests/dataset/training_ingest_benchmark.py](https://github.com/ray-project/ray/blob/master/release/nightly_tests/dataset/training_ingest_benchmark.py#L480) (Line 480)
- **Target Call:** `fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `S3ReadImagesDataLoader._get_s3fs_with_boto_creds`
- **Arguments:** ``
- **Keywords:** `{'access_key': 'credentials.access_key', 'secret_key': 'credentials.secret_key', 'session_token': 'credentials.token', 'region': 'S3_IMAGE_AWS_REGION'}`

```python
        credentials = boto3.Session().get_credentials()
        s3fs = fs.S3FileSystem(
            access_key=credentials.access_key,
            secret_key=credentials.secret_key,
            session_token=credentials.token,
            region=S3_IMAGE_AWS_REGION,
        )
        return s3fs
```

#### 98. [release/train_tests/benchmark/image_classification/jpeg/factory.py](https://github.com/ray-project/ray/blob/master/release/train_tests/benchmark/image_classification/jpeg/factory.py#L63) (Line 63)
- **Target Call:** `self.fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ImageClassificationJpegRayDataLoaderFactory.get_s3fs_with_boto_creds`
- **Arguments:** ``
- **Keywords:** `{'access_key': 'credentials.access_key', 'secret_key': 'credentials.secret_key', 'session_token': 'credentials.token', 'region': 'AWS_REGION', 'connect_timeout': 'connection_timeout', 'request_timeout': 'request_timeout'}`

```python

        s3fs = pyarrow.fs.S3FileSystem(
            access_key=credentials.access_key,
            secret_key=credentials.secret_key,
            session_token=credentials.token,
            region=AWS_REGION,
            connect_timeout=connection_timeout,
            request_timeout=request_timeout,
        )
        return s3fs
```

#### 99. [rllib/offline/offline_data.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_data.py#L69) (Line 69)
- **Target Call:** `gcsfs.GCSFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineData.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

            self.filesystem_object = gcsfs.GCSFileSystem(**self.filesystem_kwargs)
        elif self.filesystem == "s3":
```

#### 100. [rllib/offline/offline_data.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_data.py#L71) (Line 71)
- **Target Call:** `self.fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineData.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        elif self.filesystem == "s3":
            self.filesystem_object = pyarrow.fs.S3FileSystem(**self.filesystem_kwargs)
        elif self.filesystem == "abs":
```

#### 101. [rllib/offline/offline_env_runner.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_env_runner.py#L86) (Line 86)
- **Target Call:** `gcsfs.GCSFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineSingleAgentEnvRunner.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

            self.filesystem_object = gcsfs.GCSFileSystem(**self.filesystem_kwargs)
        elif self.filesystem == "s3":
```

#### 102. [rllib/offline/offline_env_runner.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_env_runner.py#L90) (Line 90)
- **Target Call:** `fs.S3FileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineSingleAgentEnvRunner.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python

            self.filesystem_object = fs.S3FileSystem(**self.filesystem_kwargs)
        elif self.filesystem == "abs":
```

#### 103. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L167) (Line 167)
- **Target Call:** `filesystem.create_dir` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.save_to_path`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
        # Make sure, path exists.
        filesystem.create_dir(path, recursive=True)

```

#### 104. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L178) (Line 178)
- **Target Call:** `filesystem.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.save_to_path`
- **Arguments:** `(path / self.METADATA_FILE_NAME).as_posix()`
- **Keywords:** `{}`

```python
            )
        with filesystem.open_output_stream(
            (path / self.METADATA_FILE_NAME).as_posix()
        ) as f:
            f.write(json.dumps(metadata).encode("utf-8"))
```

#### 105. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L186) (Line 186)
- **Target Call:** `filesystem.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.save_to_path`
- **Arguments:** `(path / self.CLASS_AND_CTOR_ARGS_FILE_NAME).as_posix()`
- **Keywords:** `{}`

```python
        # non-serializable data.
        with filesystem.open_output_stream(
            (path / self.CLASS_AND_CTOR_ARGS_FILE_NAME).as_posix()
        ) as f:
            pickle.dump(
```

#### 106. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L321) (Line 321)
- **Target Call:** `filesystem.open_output_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.save_to_path`
- **Arguments:** `filename.as_posix()`
- **Keywords:** `{}`

```python
        )
        with filesystem.open_output_stream(filename.as_posix()) as f:
            if use_msgpack:
```

#### 107. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L405) (Line 405)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.restore_from_path`
- **Arguments:** `filename.with_suffix('.msgpack').as_posix()`
- **Keywords:** `{}`

```python
                msgpack = try_import_msgpack(error=True)
                with filesystem.open_input_stream(
                    filename.with_suffix(".msgpack").as_posix()
                ) as f:
                    state = msgpack.load(f, strict_map_key=False)
```

#### 108. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L410) (Line 410)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.restore_from_path`
- **Arguments:** `filename.with_suffix('.pkl').as_posix()`
- **Keywords:** `{}`

```python
            else:
                with filesystem.open_input_stream(
                    filename.with_suffix(".pkl").as_posix()
                ) as f:
                    state = pickle.load(f)
```

#### 109. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L463) (Line 463)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpointable.from_checkpoint`
- **Arguments:** `(path / cls.CLASS_AND_CTOR_ARGS_FILE_NAME).as_posix()`
- **Keywords:** `{}`

```python
        try:
            with filesystem.open_input_stream(
                (path / cls.CLASS_AND_CTOR_ARGS_FILE_NAME).as_posix()
            ) as f:
                ctor_info = pickle.load(f)
```

#### 110. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L713) (Line 713)
- **Target Call:** `fs.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_exists_at_fs_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    """Returns `True` if the path can be found in the filesystem."""
    valid = fs.get_file_info(path)
    return valid.type != pyarrow.fs.FileType.NotFound
```

#### 111. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L775) (Line 775)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `checkpoint.as_posix()`
- **Keywords:** `{}`

```python
    if _exists_at_fs_path(filesystem, checkpoint.as_posix()) and _is_dir(
        filesystem.get_file_info(checkpoint.as_posix())
    ):
```

#### 112. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L781) (Line 781)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `pyarrow.fs.FileSelector(checkpoint.as_posix(), recursive=False)`
- **Keywords:** `{}`

```python
        # (with a `checkpoint-\d+` file in it).
        file_info_list = filesystem.get_file_info(
            pyarrow.fs.FileSelector(checkpoint.as_posix(), recursive=False)
        )
        for file_info in file_info_list:
```

#### 113. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L782) (Line 782)
- **Target Call:** `self.fs.FileSelector` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `checkpoint.as_posix()`
- **Keywords:** `{'recursive': 'False'}`

```python
        file_info_list = filesystem.get_file_info(
            pyarrow.fs.FileSelector(checkpoint.as_posix(), recursive=False)
        )
```

#### 114. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L804) (Line 804)
- **Target Call:** `filesystem.open_input_stream` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `(checkpoint / 'rllib_checkpoint.json').as_posix()`
- **Keywords:** `{}`

```python
            # if (checkpoint / "rllib_checkpoint.json").is_file():
            with filesystem.open_input_stream(
                (checkpoint / "rllib_checkpoint.json").as_posix()
            ) as f:
                # with open(checkpoint / "rllib_checkpoint.json") as f:
```

#### 115. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L846) (Line 846)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `state_file.as_posix()`
- **Keywords:** `{}`

```python
                _exists_at_fs_path(filesystem, state_file.as_posix())
                and filesystem.get_file_info(state_file.as_posix()).is_file
            ):
```

#### 116. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L866) (Line 866)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `policies_dir.as_posix()`
- **Keywords:** `{}`

```python
        if _exists_at_fs_path(filesystem, policies_dir.as_posix()) and _is_dir(
            filesystem.get_file_info(policies_dir.as_posix())
        ):
```

#### 117. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L869) (Line 869)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `pyarrow.fs.FileSelector(policies_dir.as_posix(), recursive=False)`
- **Keywords:** `{}`

```python
            policy_ids = set()
            file_info_list = filesystem.get_file_info(
                pyarrow.fs.FileSelector(policies_dir.as_posix(), recursive=False)
            )
            for file_info in file_info_list:
```

#### 118. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L870) (Line 870)
- **Target Call:** `self.fs.FileSelector` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `policies_dir.as_posix()`
- **Keywords:** `{'recursive': 'False'}`

```python
            file_info_list = filesystem.get_file_info(
                pyarrow.fs.FileSelector(policies_dir.as_posix(), recursive=False)
            )
```

#### 119. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L884) (Line 884)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `modules_dir.as_posix()`
- **Keywords:** `{}`

```python
        if _exists_at_fs_path(filesystem, checkpoint.as_posix()) and _is_dir(
            filesystem.get_file_info(modules_dir.as_posix())
        ):
```

#### 120. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L887) (Line 887)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `pyarrow.fs.FileSelector(modules_dir.as_posix(), recursive=False)`
- **Keywords:** `{}`

```python
            module_ids = set()
            file_info_list = filesystem.get_file_info(
                pyarrow.fs.FileSelector(modules_dir.as_posix(), recursive=False)
            )
            for file_info in file_info_list:
```

#### 121. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L888) (Line 888)
- **Target Call:** `self.fs.FileSelector` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `modules_dir.as_posix()`
- **Keywords:** `{'recursive': 'False'}`

```python
            file_info_list = filesystem.get_file_info(
                pyarrow.fs.FileSelector(modules_dir.as_posix(), recursive=False)
            )
```

#### 122. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L894) (Line 894)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `module_dir.as_posix()`
- **Keywords:** `{}`

```python
                module_dir = modules_dir / file_info.base_name
                if _is_dir(filesystem.get_file_info(module_dir.as_posix())):
                    module_ids.add(file_info.base_name)
```

#### 123. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L902) (Line 902)
- **Target Call:** `filesystem.get_file_info` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_checkpoint_info`
- **Arguments:** `checkpoint.as_posix()`
- **Keywords:** `{}`

```python
        _exists_at_fs_path(filesystem, checkpoint.as_posix())
        and filesystem.get_file_info(checkpoint.as_posix()).is_file
    ):
```
