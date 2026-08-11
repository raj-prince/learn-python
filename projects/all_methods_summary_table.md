# Complete 4-Column Summary Table of All 183 FSSPEC Methods

This reference summary table documents **every single distinct method call** identified by our GitHub AST crawler across 12 major Python data science and AI codebases, matching the summary format (`Target Call` | `Occurrences` | `Major Repositories` | `Usage Pattern`).

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
| **`self.fs.isdir`** | **6** | `iterative/dvc` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`self.fs.init_path`** | **6** | `pytorch/pytorch` | Initializing root filesystem mount point path inside model or data wrapper |
| **`self.filesystem.get_file_info`** | **6** | `ray-project/ray` | Querying file metadata record through encapsulated abstract filesystem handler |
| **`filesystem.open_input_stream`** | **6** | `ray-project/ray` | Opening readable PyArrow input byte stream from storage driver |
| **`fs.rm`** | **5** | `Lightning-AI/pytorch-lightning`, `dask/dask`, `pytorch/torchtitan` | Removing target file or directory node from remote or local storage |
| **`fs._strip_protocol`** | **5** | `dask/dask`, `huggingface/datasets`, `pydata/xarray` | Stripping scheme prefix (`s3://`, `gs://`) from URI to extract clean relative storage key |
| **`fs.mkdirs`** | **5** | `dask/dask`, `Lightning-AI/pytorch-lightning` | Alias method for creating directory tree hierarchies |
| **`ArrowFSWrapper`** | **5** | `ray-project/ray`, `dask/dask` | Instantiating PyArrow filesystem interface wrapper around fsspec driver |
| **`split_protocol`** | **5** | `ray-project/ray`, `intake/intake` | Splitting raw string URL into `(protocol, path)` component pair |
| **`make_path_posix`** | **5** | `intake/intake` | Converting native platform separator path to standardized POSIX forward-slash path |
| **`tokenize`** | **5** | `iterative/dvc` | Generating deterministic token hash of filesystem configuration and URL paths |
| **`fs.relpath`** | **5** | `iterative/dvc` | Path Arithmetic & Topologies API method detected across repository storage interactions |
| **`fs.isdvc`** | **5** | `iterative/dvc` | DVC custom validation call checking whether path is tracked under version control |
| **`filesystem.isdir`** | **5** | `pytorch/torchtitan` | Checking directory presence through abstracted storage filesystem layer |
| **`fs.create_dir`** | **5** | `ray-project/ray` | Creating single directory container node inside underlying file storage |
| **`self.fs.FileSelector`** | **5** | `ray-project/ray` | Creating recursive file selector specification object for batch selection |
| **`OpenFile`** | **4** | `dask/dask` | Low-level context-managed open file stream handle object wrapper |
| **`fsspec.open_local`** | **4** | `intake/intake` | Opening remote path by caching to temporary local disk and returning local path string |
| **`self.fs._cat_file`** | **4** | `zarr-developers/zarr-python` | Low-level direct byte range cat read of individual remote storage key |
| **`self.fs.version_path`** | **4** | `iterative/dvc` | Resolving version-tagged object store path for immutable storage backends |
| **`self.fs.info`** | **4** | `iterative/dvc`, `huggingface/datasets`, `Lightning-AI/pytorch-lightning` | Querying metadata record via encapsulated filesystem reference |
| **`fs.relparts`** | **4** | `iterative/dvc` | Extracting relative path component tuple from root directory |
| **`self.fs.open`** | **4** | `iterative/dvc`, `pytorch/pytorch`, `ray-project/ray` | Stream Reading & Writing API method detected across repository storage interactions |
| **`fs.get_file`** | **4** | `iterative/dvc`, `huggingface/datasets` | Downloading a single remote file to local target filename path |
| **`fs.walk`** | **4** | `iterative/dvc`, `huggingface/datasets` | Pythonic recursive generator yielding `(root, dirs, files)` tuples across directory tree |
| **`self.fs.isin_or_eq`** | **4** | `iterative/dvc` | Checking if path matches or falls within expected tree prefix |
| **`fs.abspath`** | **4** | `iterative/dvc` | Resolving absolute abstract URI path representation |
| **`self.fs.makedirs`** | **4** | `iterative/dvc`, `pytorch/pytorch`, `Lightning-AI/pytorch-lightning` | Instance method for recursive directory hierarchy creation |
| **`DirFileSystem`** | **4** | `huggingface/datasets` | Wrapping directory root so relative paths operate within a sub-tree sandbox |
| **`self.fs.create_stream`** | **4** | `pytorch/pytorch` | Creating output byte stream for sequential checkpoint or log output |
| **`LocalFileSystem`** | **3** | `dask/dask`, `huggingface/datasets`, `Lightning-AI/pytorch-lightning` | Instantiating explicit local host disk filesystem driver (`file://`) |
| **`fsspec.get_fs_token_paths`** | **3** | `intake/intake`, `pydata/xarray`, `huggingface/datasets` | High-level utility extracting tokenized filesystem reference for serialization |
| **`self.fs._find`** | **3** | `zarr-developers/zarr-python` | Low-level asynchronous file tree finder yielding all nested keys |
| **`self.fs._rm`** | **3** | `zarr-developers/zarr-python` | Internal implementation method deleting remote object key or prefix |
| **`self.fs.parent`** | **3** | `iterative/dvc` | Locating immediate parent directory string of current path |
| **`fs.name`** | **3** | `iterative/dvc` | Extracting simple file basename string from abstract path |
| **`fs.dirname`** | **3** | `iterative/dvc` | Extracting parent directory path from abstract path string |
| **`self.fs.split`** | **3** | `iterative/dvc` | Splitting abstract path into `(head, tail)` tuple pair |
| **`fs.read_text`** | **3** | `huggingface/datasets` | Directly reading entire remote file contents decoded as text string |
| **`fs.put`** | **3** | `Lightning-AI/pytorch-lightning` | Uploading local file or directory payload up to remote filesystem target |
| **`filesystem.is_remote`** | **3** | `pytorch/torchtitan` | Boolean flag checking whether abstract storage driver targets cloud/remote backend |
| **`self.fs.LocalFileSystem`** | **3** | `ray-project/ray` | Referencing native host disk filesystem class |
| **`fs.open_input_stream`** | **3** | `ray-project/ray` | Stream Reading & Writing API method detected across repository storage interactions |
| **`self.fs.S3FileSystem`** | **3** | `ray-project/ray` | Referencing Amazon S3 object storage filesystem backend driver |
| **`fs.delete_dir`** | **3** | `ray-project/ray` | Recursively removing directory and all contained sub-keys |
| **`fs.open_input_file`** | **3** | `ray-project/ray` | Opening read-only stream interface to underlying object key |
| **`self.fs.copy_files`** | **3** | `ray-project/ray` | Batch copying multiple file paths within or across filesystem instances |
| **`fs.S3FileSystem`** | **3** | `ray-project/ray` | Instantiating S3 filesystem interface driver |
| **`filesystem.open_output_stream`** | **3** | `ray-project/ray` | Opening PyArrow output stream handle for sequential writing |
| **`fs.ukey`** | **2** | `dask/dask` | Retrieving unique version hash or entity tag (`ETag`) for cache invalidation |
| **`read_block`** | **2** | `dask/dask` | Reading fixed byte block range from file stream without reading entire file |
| **`infer_compression`** | **2** | `dask/dask` | Detecting compression format (`gzip`, `bz2`, `zip`) from file extension suffix |
| **`self.fs.get_file_info`** | **2** | `dask/dask` | Retrieving individual file information metadata record |
| **`open_file`** | **2** | `dask/dask` | Opening individual file handle inside protocol catalog or dataset interface |
| **`expand_paths_if_needed`** | **2** | `dask/dask` | Expanding wildcard glob strings into explicit path lists if glob syntax present |
| **`self.fs._parent`** | **2** | `intake/intake` | Internal parent directory lookup helper |
| **`self.fs.get_file`** | **2** | `intake/intake`, `iterative/dvc` | Downloading remote object to local disk path |
| **`h.cat`** | **2** | `intake/intake` | Batch cat byte read via object store handle wrapper |
| **`fsspec.open_files`** | **2** | `intake/intake` | Opening glob list of matching file paths as batch stream handle contexts |
| **`compressions.values`** | **2** | `intake/intake` | Accessing registered decompression codec handlers collection |
| **`self.fs.isfile`** | **2** | `iterative/dvc` | Checking leaf file node status |
| **`self.fs.isdvc`** | **2** | `iterative/dvc` | Checking DVC tracking status of path |
| **`self.fs.chdir`** | **2** | `iterative/dvc` | Changing current working directory context of filesystem wrapper |
| **`fs.isabs`** | **2** | `iterative/dvc` | Checking if abstract path is formatted as an absolute path |
| **`self.fs.isabs`** | **2** | `iterative/dvc` | Instance check for absolute path representation |
| **`self.fs.remove`** | **2** | `iterative/dvc` | Deleting file or folder node from underlying filesystem |
| **`fs.du`** | **2** | `iterative/dvc` | Calculating cumulative disk byte space consumed across directory tree |
| **`fs.unstrip_protocol`** | **2** | `iterative/dvc`, `huggingface/datasets` | Re-attaching scheme protocol prefix onto relative object key |
| **`fs.getcwd`** | **2** | `iterative/dvc` | Getting active abstract directory path |
| **`fs.parts`** | **2** | `iterative/dvc` | Splitting path into segment component strings |
| **`fs.resolve_path`** | **2** | `huggingface/datasets` | Resolving symlinks or relative references in remote path |
| **`fs.listdir`** | **2** | `huggingface/datasets`, `Lightning-AI/pytorch-lightning` | Listing raw file names inside target directory node |
| **`self.fs.rename`** | **2** | `pytorch/pytorch` | Renaming or moving an object path within filesystem storage |
| **`self.fs.rm`** | **2** | `pytorch/pytorch`, `Lightning-AI/pytorch-lightning` | Deleting remote object key or tree |
| **`filesystem.listdir`** | **2** | `pytorch/torchtitan` | Directory listing through abstraction wrapper interface |
| **`filesystem.isfile`** | **2** | `pytorch/torchtitan` | Leaf file node check through abstraction wrapper interface |
| **`filesystem.open_input_file`** | **2** | `ray-project/ray` | Opening PyArrow input file handle for random access byte read |
| **`self.filesystem.create_dir`** | **2** | `ray-project/ray` | Creating directory node through wrapped storage driver |
| **`self.filesystem.open_output_stream`** | **2** | `ray-project/ray` | Opening output byte stream through PyArrow wrapper |
| **`fs.delete_file`** | **2** | `ray-project/ray` | Deleting single file node from storage driver |
| **`self.fs.FSSpecHandler`** | **2** | `ray-project/ray` | PyArrow custom filesystem bridge wrapping fsspec driver |
| **`self.fs.PyFileSystem`** | **2** | `ray-project/ray` | PyArrow filesystem representation wrapping abstract driver |
| **`fs.open_output_stream`** | **2** | `ray-project/ray` | Opening write output stream handle |
| **`gcsfs.GCSFileSystem`** | **2** | `ray-project/ray` | Instantiating Google Cloud Storage (`gs://`) filesystem driver |
| **`fs_tokenize`** | **1** | `dask/dask` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`filesystem.lower`** | **1** | `dask/dask` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.equals`** | **1** | `dask/dask` | Directory Traversal, Wildcards & Recursion API method detected across repository storage interactions |
| **`fs.expand_path`** | **1** | `dask/dask` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.invalidate_cache`** | **1** | `dask/dask` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.checksum`** | **1** | `dask/dask` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`build_name_function`** | **1** | `dask/dask` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fsspec_parquet.open_parquet_file`** | **1** | `dask/dask` | Stream Reading & Writing API method detected across repository storage interactions |
| **`get_filesystem_class`** | **1** | `intake/intake` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.filesystem.open`** | **1** | `intake/intake` | Stream Reading & Writing API method detected across repository storage interactions |
| **`get_mapper`** | **1** | `intake/intake` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.cat_file`** | **1** | `intake/intake` | Stream Reading & Writing API method detected across repository storage interactions |
| **`fs._check_file`** | **1** | `intake/intake` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs._mapper`** | **1** | `intake/intake` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.get_mapper`** | **1** | `pydata/xarray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.to_json`** | **1** | `zarr-developers/zarr-python` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`AsyncFileSystemWrapper`** | **1** | `zarr-developers/zarr-python` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.fs._pipe_file`** | **1** | `zarr-developers/zarr-python` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`self.fs._exists`** | **1** | `zarr-developers/zarr-python` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`self.fs._cat_ranges`** | **1** | `zarr-developers/zarr-python` | Stream Reading & Writing API method detected across repository storage interactions |
| **`self.fs._ls`** | **1** | `zarr-developers/zarr-python` | Directory Traversal, Wildcards & Recursion API method detected across repository storage interactions |
| **`self.fs._info`** | **1** | `zarr-developers/zarr-python` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`fs._get`** | **1** | `iterative/dvc` | Remote Data Transfer (Download/Upload) API method detected across repository storage interactions |
| **`fs.parents`** | **1** | `iterative/dvc` | Path Arithmetic & Topologies API method detected across repository storage interactions |
| **`self.fs._get`** | **1** | `iterative/dvc` | Remote Data Transfer (Download/Upload) API method detected across repository storage interactions |
| **`self.fs.close`** | **1** | `iterative/dvc` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`self.fs.walk`** | **1** | `iterative/dvc` | Directory Traversal, Wildcards & Recursion API method detected across repository storage interactions |
| **`self.fs.coalesce_version`** | **1** | `iterative/dvc` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`self.fs.is_empty`** | **1** | `iterative/dvc` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`self.fs.as_posix`** | **1** | `iterative/dvc` | Path Arithmetic & Topologies API method detected across repository storage interactions |
| **`self.fs.move`** | **1** | `iterative/dvc` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs._get_key_from_relative`** | **1** | `iterative/dvc` | Remote Data Transfer (Download/Upload) API method detected across repository storage interactions |
| **`fs._get_subrepo_info`** | **1** | `iterative/dvc` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`fs.parent`** | **1** | `iterative/dvc` | Path Arithmetic & Topologies API method detected across repository storage interactions |
| **`_LocalFileSystem`** | **1** | `iterative/dvc` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.commonpath`** | **1** | `iterative/dvc` | Path Arithmetic & Topologies API method detected across repository storage interactions |
| **`fs.suffix`** | **1** | `iterative/dvc` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.execute`** | **1** | `iterative/dvc` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.download`** | **1** | `huggingface/datasets` | Remote Data Transfer (Download/Upload) API method detected across repository storage interactions |
| **`fsspec.register_implementation`** | **1** | `huggingface/datasets` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.mv`** | **1** | `huggingface/datasets` | File & Directory Creation / Cleanup API method detected across repository storage interactions |
| **`can_be_local`** | **1** | `huggingface/datasets` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`strip_protocol`** | **1** | `huggingface/datasets` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.size`** | **1** | `huggingface/datasets` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`fsspec.available_protocols`** | **1** | `huggingface/datasets` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.render`** | **1** | `pytorch/pytorch` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`self.fs.mkdir`** | **1** | `pytorch/pytorch` | File & Directory Creation / Cleanup API method detected across repository storage interactions |
| **`self.fs.rm_file`** | **1** | `pytorch/pytorch` | File & Directory Creation / Cleanup API method detected across repository storage interactions |
| **`self.fs.invalidate_cache`** | **1** | `Lightning-AI/pytorch-lightning` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`fs.modified`** | **1** | `Lightning-AI/pytorch-lightning` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`filesystem.rmtree`** | **1** | `pytorch/torchtitan` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`filesystem.exists`** | **1** | `pytorch/torchtitan` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`filesystem.open`** | **1** | `ray-project/ray` | Stream Reading & Writing API method detected across repository storage interactions |
| **`filesystem.__reduce__`** | **1** | `ray-project/ray` | Metadata & Existence Checks API method detected across repository storage interactions |
| **`self.fs.resolve_s3_region`** | **1** | `ray-project/ray` | Driver Instances & Abstract Wrappers API method detected across repository storage interactions |
| **`self.filesystem.delete_file`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.filesystem.move`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`filesystem.delete_dir`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.filesystem.delete_dir_contents`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.filesystem.delete_dir`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`HTTPFileSystem`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`fs.unwrap`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
| **`self.filesystem.open_input_file`** | **1** | `ray-project/ray` | Stream Reading & Writing API method detected across repository storage interactions |
| **`filesystem.create_dir`** | **1** | `ray-project/ray` | Protocol & Driver Resolution API method detected across repository storage interactions |
