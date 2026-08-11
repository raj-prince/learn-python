# Python Data Science & AI Ecosystem: FSSPEC & Abstract Filesystem Method Usage Analysis

This directory contains automated GitHub AST crawler tools, an empirical analysis of **`fsspec`** (Filesystem Specification) and abstract filesystem API usage patterns across **12 well-established Python data science, machine learning, and MLOps open-source projects**, and a runnable end-to-end simulation script.

---

## 📑 Quick Reference & Artifact Links

* 🚀 **End-to-End Simulation Script:** [`projects/28_simulate_fsspec_methods.py`](file:///usr/local/google/home/princer/code/learn-python/projects/28_simulate_fsspec_methods.py) *(Simulates directory traversal, glob wildcards, recursive find/walk, path topologies, metadata, and stream operations together)*
* 📋 **Complete 4-Column Method Summary Table (All 183 Methods):** [`projects/all_methods_summary_table.md`](file:///usr/local/google/home/princer/code/learn-python/projects/all_methods_summary_table.md) *(Target Call, Occurrences, Major Repositories, and Primary Usage Pattern for every single call)*
* 📊 **Complete 183-Method Cross-Repository Grid:** [`projects/method_distribution_matrix.md`](file:///usr/local/google/home/princer/code/learn-python/projects/method_distribution_matrix.md) *(Exact occurrence count matrix across each of the 12 projects)*
* 🐍 **GitHub AST Crawler Script:** [`projects/26_fsspec_github_crawler.py`](file:///usr/local/google/home/princer/code/learn-python/projects/26_fsspec_github_crawler.py)
* 📄 **Master Markdown Crawl Report:** [`projects/combined_fsspec_report.md`](file:///usr/local/google/home/princer/code/learn-python/projects/combined_fsspec_report.md)
* 💾 **Master JSON Crawl Report:** [`projects/combined_fsspec_report.json`](file:///usr/local/google/home/princer/code/learn-python/projects/combined_fsspec_report.json)

---

## 📊 Crawl Dataset Overview

* **Target Repositories Analyzed:** `12` major production libraries
* **Total Python Files Scanned:** `9,645` files
* **Files with Validated Filesystem API Usages:** `167` files
* **Total AST-Verified Method Usages:** `867` calls
* **Local Test Suite Reference Crawl:** `19` usages across local lessons in `raj-prince/learn-python`

### Analyzed Repositories Summary
| Project | Repository | Files Scanned | Files w/ Usages | Total Usages Detected | Primary Architectural Focus |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Dask** | [`dask/dask`](https://github.com/dask/dask) | 201 | 20 | 91 | Distributed DataFrame/Array block & Parquet streaming |
| **Intake** | [`intake/intake`](https://github.com/intake/intake) | 71 | 18 | 97 | Data catalog plugin loading & high-level open helpers |
| **pandas** | [`pandas-dev/pandas`](https://github.com/pandas-dev/pandas) | 538 | 25 | 57 | Input/Output backend delegation (`read_csv`, `read_parquet`) |
| **xarray** | [`pydata/xarray`](https://github.com/pydata/xarray) | 162 | 3 | 5 | Multi-dimensional labeled array store integration |
| **zarr** | [`zarr-developers/zarr-python`](https://github.com/zarr-developers/zarr-python) | 238 | 2 | 4 | Chunked, compressed multi-dimensional array storage |
| **DVC** | [`iterative/dvc`](https://github.com/iterative/dvc) | 326 | 60 | 254 | Data version control, dependency tree walking & hash tracking |
| **Kedro** | [`kedro-org/kedro`](https://github.com/kedro-org/kedro) | 152 | 9 | 28 | MLOps data pipeline dataset abstraction |
| **Hugging Face Datasets** | [`huggingface/datasets`](https://github.com/huggingface/datasets) | 162 | 43 | 163 | Multi-protocol remote/local dataset shard resolution |
| **PyTorch** | [`pytorch/pytorch`](https://github.com/pytorch/pytorch) | 3,412 | 320 | 670 | Native core stream & abstract path helpers |
| **PyTorch Lightning** | [`Lightning-AI/pytorch-lightning`](https://github.com/Lightning-AI/pytorch-lightning) | 767 | 72 | 182 | Distributed model checkpoint loading, existence checks & weights transfer |
| **TorchTitan** | [`pytorch/torchtitan`](https://github.com/pytorch/torchtitan) | 330 | 17 | 39 | Large language model training distributed file system helpers |
| **Ray** | [`ray-project/ray`](https://github.com/ray-project/ray) | 3,287 | 257 | 507 | PyArrow / abstract object store filesystem introspection |

---

## 📋 Comprehensive Method Summary Table (Top 35 Methods)

Below is the summary table for all top methods formatted in the identical structured reference layout (**Target Call** | **Occurrences** | **Major Repositories** | **Primary Usage Pattern**). To inspect all **183 distinct methods** in this table format, view [`projects/all_methods_summary_table.md`](file:///usr/local/google/home/princer/code/learn-python/projects/all_methods_summary_table.md).

| Target Call | Occurrences | Major Repositories | Primary Usage Pattern |
| :--- | :---: | :--- | :--- |
| **`fsspec.open`** | **52** | `intake/intake`, `huggingface/datasets`, `pandas-dev/pandas` | High-level context-managed file stream open across local or cloud URI paths (`with fsspec.open(url, mode) as f:`) |
| **`fs.open`** | **46** | `dask/dask`, `iterative/dvc`, `Lightning-AI/pytorch-lightning` | Direct abstract filesystem stream open handle for reading/writing binary or text data |
| **`fs.exists`** | **30** | `Lightning-AI/pytorch-lightning`, `iterative/dvc`, `dask/dask` | Checking existence of a file or directory node on a local or remote filesystem |
| **`url_to_fs`** | **29** | `huggingface/datasets`, `Lightning-AI/pytorch-lightning`, `pytorch/pytorch` | Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple |
| **`fs.join`** | **26** | `iterative/dvc`, `pytorch/pytorch` | Cross-platform abstract POSIX path joining without OS path separator assumptions |
| **`self.fs.join`** | **25** | `iterative/dvc` | Instance method wrapper for building paths relative to abstract remote root directories |
| **`fs.info`** | **24** | `iterative/dvc`, `intake/intake`, `huggingface/datasets` | Retrieving node metadata dictionary including `size`, `type` (`file` vs `directory`), and timestamp |
| **`fs.isdir`** | **23** | `iterative/dvc`, `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Verifying whether a path points to an abstract directory container node |
| **`self.fs.relparts`** | **18** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`self.fs.relpath`** | **17** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`self.fs.exists`** | **17** | `iterative/dvc`, `Lightning-AI/pytorch-lightning`, `pytorch/pytorch` | Instance method existence check within encapsulated filesystem handler objects |
| **`fs.isfile`** | **16** | `huggingface/datasets`, `iterative/dvc`, `Lightning-AI/pytorch-lightning` | Verifying whether a target path resolves to a leaf file node (not a directory) |
| **`filesystem.get_file_info`** | **14** | `ray-project/ray` | Extracting structured Arrow / PyArrow file metadata info from underlying filesystem handle |
| **`open_files`** | **13** | `dask/dask`, `intake/intake` | Batch context manager opening multiple matching file stream handles simultaneously |
| **`fs.get_file_info`** | **12** | `ray-project/ray` | Retrieving individual file information metadata object from filesystem driver |
| **`stringify_path`** | **11** | `dask/dask`, `huggingface/datasets` | Coercing pathlib.Path or abstract path objects to normalized string path representation |
| **`fs.ls`** | **11** | `iterative/dvc`, `intake/intake`, `pytorch/torchtitan` | Listing direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`self.fs.abspath`** | **11** | `iterative/dvc` | Resolving abstract relative path to fully qualified URI path from working directory |
| **`self.fs.getcwd`** | **11** | `iterative/dvc` | Querying current working directory path of abstract filesystem instance |
| **`self.fs.isin`** | **11** | `iterative/dvc` | Verifying whether a child path is contained within a given parent tree root |
| **`fsspec.filesystem`** | **10** | `intake/intake`, `kedro-org/kedro`, `huggingface/datasets` | Instantiating filesystem driver class by protocol string (e.g. `fsspec.filesystem("s3")`) |
| **`self.fs.parts`** | **10** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`fs.makedirs`** | **10** | `Lightning-AI/pytorch-lightning`, `iterative/dvc`, `huggingface/datasets` | Recursively creating directory tree hierarchy (`exist_ok=True`) |
| **`fs.from_os_path`** | **9** | `iterative/dvc` | Converting native OS filesystem path to abstract protocol URI path representation |
| **`fs.get`** | **9** | `Lightning-AI/pytorch-lightning`, `iterative/dvc`, `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self.fs.concat_path`** | **9** | `pytorch/pytorch` | Joining base directory prefix with relative child object key or filename |
| **`filesystem.unwrap`** | **9** | `ray-project/ray` | Unwrapping abstract wrapper object to extract underlying native filesystem instance |
| **`get_fs_token_paths`** | **7** | `dask/dask` | Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization |
| **`fs.find`** | **7** | `iterative/dvc`, `dask/dask` | Recursively finding all file paths inside a directory subtree matching optional criteria |
| **`self.fs.normpath`** | **7** | `iterative/dvc` | Normalizing redundant dot/double-dot segments in remote object keys |
| **`fs.normpath`** | **7** | `iterative/dvc` | Static or method normalization of abstract filesystem paths |
| **`filesystem.join`** | **7** | `pytorch/torchtitan` | Joining path segments within PyArrow / custom filesystem interface wrappers |
| **`self.fs.ls`** | **6** | `pytorch/pytorch`, `Lightning-AI/pytorch-lightning`, `intake/intake` | Instance directory listing call yielding direct children inside filesystem context |
| **`self.fs.unstrip_protocol`** | **6** | `iterative/dvc`, `intake/intake` | Prepending protocol prefix back onto stripped relative key string |
| **`fs.glob`** | **6** | `huggingface/datasets`, `intake/intake`, `pydata/xarray` | Wildcard expression matching (`*`, `?`, `[...]`) across remote or local directory trees |

---

## 📈 Functional Categories Summary Table (All 867 Calls Across 8 Categories)

| Functional Category | Total Calls | % Share | Top Methods Used | Dominant Repositories | Primary Architectural Usage Pattern |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Path Arithmetic & Topologies** | **185** | `21.3%` | `fs.join` (26), `self.fs.join` (25), `self.fs.relparts` (18), `self.fs.relpath` (17) | `dvc` (176), `pytorch` (7), `intake` (2) | Calculating relative dependency paths, repository roots, and component trees |
| **Metadata & Existence Checks** | **181** | `20.9%` | `fs.exists` (30), `fs.info` (24), `fs.isdir` (23), `self.fs.exists` (17), `fs.isfile` (16) | `dvc` (63), `ray` (34), `pytorch-lightning` (30) | Validating local/remote path presence, directory checks, and header dictionary lookups |
| **Stream Reading & Writing** | **178** | `20.5%` | `fsspec.open` (52), `fs.open` (46), `open_files` (13), `fs.read_block` (2), `fs.cat` (2) | `intake` (56), `dask` (30), `ray` (27) | High-level context-managed and batch stream opening for Parquet/CSV/checkpoint files |
| **Protocol & Driver Resolution** | **154** | `17.8%` | `url_to_fs` (29), `stringify_path` (11), `fsspec.filesystem` (10), `fs.from_os_path` (9) | `datasets` (36), `ray` (36), `dask` (21) | Extracting abstract `(fs, path)` tuples from URI strings (`s3://...`, `gs://...`) |
| **Driver Instances & Subclass Wrappers** | **58** | `6.7%` | `ArrowFSWrapper` (5), `fs.isdvc` (5), `fs.create_dir` (5), `self.fs.FileSelector` (5) | `dvc` (20), `ray` (17), `dask` (8) | Wrapping PyArrow filesystems or implementing subclass-specific abstract protocol handlers |
| **File & Directory Creation / Cleanup** | **49** | `5.7%` | `fs.makedirs` (10), `fs.rm` (5), `fs.mkdirs` (5), `make_path_posix` (5), `fs.delete_dir` (3) | `pytorch-lightning` (11), `ray` (8), `pytorch` (7) | Creating output directory hierarchies and cleaning up checkpoint/scratch artifacts |
| **Directory Traversal & Wildcards** | **40** | `4.6%` | `fs.ls` (11), `fs.find` (7), `self.fs.ls` (6), `fs.glob` (6), `fs.walk` (4) | `dvc` (18), `datasets` (5), `intake` (4) | Wildcard shard matching (`*`) and recursive directory tree discovery (`find`/`walk`) |
| **Remote Transfer (Download / Upload)** | **22** | `2.5%` | `fs.get` (9), `fs.get_file` (4), `fs.put` (3), `self.fs.get_file` (2) | `pytorch-lightning` (10), `dvc` (8), `datasets` (2) | Staging bulk remote model checkpoints or dataset artifacts to local worker disks |

---

## 🔍 Directory Traversal, Wildcard & Path Expansion Methods (`glob`, `find`, `walk`)

Across the dataset, **21 method calls** specifically performed directory graph recursion, pattern matching, or deep traversal:

| Target Call | Occurrences | Major Repositories | Usage Pattern |
| :--- | :---: | :--- | :--- |
| **`fs.find`** | **7** | `dask`, `dvc` | Recursively finding all file paths inside a subtree |
| **`fs.glob`** | **6** | `huggingface/datasets`, `intake`, `xarray` | Wildcard expression expansion (`*`, `?`, `[...]`) |
| **`fs.walk`** | **4** | `dvc`, `huggingface/datasets` | Pythonic `os.walk` generator yielding `(root, dirs, files)` |
| **`self.fs._find`** | **3** | `zarr-python` | Asynchronous low-level recursive discovery of store chunks |
| **`self.fs.walk`** | **1** | `dvc` | Walking local/remote ignore-tree nodes |

### Real Production Traversal Examples from AST Crawler Analysis

* **Dask DataFrame Parquet Reader Recursive File Search ([`dask/dataframe/io/parquet/arrow.py`](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L961))**:
  ```python
  path for path in fs.find(paths) if path.endswith(parquet_file_extension)
  ```
* **Hugging Face Datasets Sharded File Pattern Matching ([`src/datasets/data_files.py`](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L372))**:
  ```python
  for filepath, info in fs.glob(fs_pattern, detail=True, **glob_kwargs).items():
      if info["type"] == "file":
          ...
  ```
* **Hugging Face Datasets Protocol Tree Traversal ([`src/datasets/utils/file_utils.py`](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1088))**:
  ```python
  for dirpath, dirnames, filenames in fs.walk(inner_path, **kwargs):
      yield "::".join([f"{protocol}://{dirpath}"] + rest_hops), dirnames, filenames
  ```

---

## 🧪 Simulation Together: Run all Traversal & Stream Calls Live!

You can run our end-to-end simulator [`projects/28_simulate_fsspec_methods.py`](file:///usr/local/google/home/princer/code/learn-python/projects/28_simulate_fsspec_methods.py) which builds an in-memory storage environment and executes:
1. **URI Parsing & Driver Instantiation:** `url_to_fs`, `fsspec.filesystem("memory")`, `_strip_protocol`
2. **Directory & File Hierarchy Creation:** `makedirs`, `mkdir`, `touch`, `write_text`
3. **Metadata & Node Inspection:** `exists`, `info`, `stat`, `isdir`, `isfile`, `size`, `du`
4. **Path Topology Arithmetic:** `_parent`, component splitting, relative topologies
5. **Wildcard & Deep Recursive Traversal:** `ls`, `glob("/**/*.parquet")`, `find("/checkpoints")`, `walk("/analytics")`
6. **Stream Reading & Batch Readers:** `open`, `head`, `tail`, `cat`, `fsspec.open_files`

### Execute Simulation
```bash
.venv/bin/python projects/28_simulate_fsspec_methods.py
```

---

## 🛠️ Reproducing the GitHub Crawl
To re-run the crawl across all target repositories:
```bash
python projects/26_fsspec_github_crawler.py --all \
  --output-csv projects/fsspec_crawl_results.csv \
  --output-json projects/combined_fsspec_report.json \
  --output-md projects/combined_fsspec_report.md
```
