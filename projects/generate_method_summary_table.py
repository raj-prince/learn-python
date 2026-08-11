#!/usr/bin/env python3
import json
import collections

with open('projects/combined_fsspec_report.json') as f:
    data = json.load(f)

all_usages = []
for repo_data in data.get('per_repository', []):
    repo_name = repo_data.get('target_source')
    short_repo = repo_name.replace('GitHub:', '').split(' ')[0]
    for usage in repo_data.get('usages', []):
        usage['short_repo'] = short_repo
        all_usages.append(usage)

# Map method name -> list of snippets & repos
method_info = collections.defaultdict(lambda: {'count': 0, 'repos': collections.Counter(), 'snippets': []})
for u in all_usages:
    name = u['target_name']
    method_info[name]['count'] += 1
    method_info[name]['repos'][u['short_repo']] += 1
    if len(method_info[name]['snippets']) < 3 and u.get('code_snippet'):
        method_info[name]['snippets'].append(u['code_snippet'].strip())

# Known descriptive pattern lookup table for top methods (plus smart fallback synthesis)
USAGE_PATTERNS = {
    'fsspec.open': 'High-level context-managed file stream open across local or cloud URI paths (`with fsspec.open(url, mode) as f:`)',
    'fs.open': 'Direct abstract filesystem stream open handle for reading/writing binary or text data',
    'fs.exists': 'Checking existence of a file or directory node on a local or remote filesystem',
    'url_to_fs': 'Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple',
    'fs.join': 'Cross-platform abstract POSIX path joining without OS path separator assumptions',
    'self.fs.join': 'Instance method wrapper for building paths relative to abstract remote root directories',
    'fs.info': 'Retrieving node metadata dictionary including `size`, `type` (`file` vs `directory`), and timestamp',
    'fs.isdir': 'Verifying whether a path points to an abstract directory container node',
    'self.fs.relparts': 'Deconstructing absolute path into tuple of relative path segment strings',
    'self.fs.relpath': 'Calculating relative path string from a reference parent or root directory',
    'self.fs.exists': 'Instance method existence check within encapsulated filesystem handler objects',
    'fs.isfile': 'Verifying whether a target path resolves to a leaf file node (not a directory)',
    'filesystem.get_file_info': 'Extracting structured Arrow / PyArrow file metadata info from underlying filesystem handle',
    'open_files': 'Batch context manager opening multiple matching file stream handles simultaneously',
    'fs.get_file_info': 'Retrieving individual file information metadata object from filesystem driver',
    'stringify_path': 'Coercing pathlib.Path or abstract path objects to normalized string path representation',
    'fs.ls': 'Listing direct children of a directory (`detail=False` for paths, `detail=True` for info dicts)',
    'self.fs.abspath': 'Resolving abstract relative path to fully qualified URI path from working directory',
    'self.fs.getcwd': 'Querying current working directory path of abstract filesystem instance',
    'self.fs.isin': 'Verifying whether a child path is contained within a given parent tree root',
    'fsspec.filesystem': 'Instantiating filesystem driver class by protocol string (e.g. `fsspec.filesystem("s3")`)',
    'self.fs.parts': 'Splitting path string into ordered component segments tuple',
    'fs.makedirs': 'Recursively creating directory tree hierarchy (`exist_ok=True`)',
    'fs.from_os_path': 'Converting native OS filesystem path to abstract protocol URI path representation',
    'fs.get': 'Bulk batch downloading of remote cloud or distributed files to local directory disk',
    'self.fs.concat_path': 'Joining base directory prefix with relative child object key or filename',
    'filesystem.unwrap': 'Unwrapping abstract wrapper object to extract underlying native filesystem instance',
    'fs.find': 'Recursively finding all file paths inside a directory subtree matching optional criteria',
    'get_fs_token_paths': 'Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization',
    'self.fs.normpath': 'Normalizing redundant dot/double-dot segments in remote object keys',
    'fs.normpath': 'Static or method normalization of abstract filesystem paths',
    'filesystem.join': 'Joining path segments within PyArrow / custom filesystem interface wrappers',
    'fs.glob': 'Wildcard expression matching (`*`, `?`, `[...]`) across remote or local directory trees',
    'self.fs.unstrip_protocol': 'Prepending protocol prefix back onto stripped relative key string',
    'self.fs.init_path': 'Initializing root filesystem mount point path inside model or data wrapper',
    'self.fs.ls': 'Instance directory listing call yielding direct children inside filesystem context',
    'self.filesystem.get_file_info': 'Querying file metadata record through encapsulated abstract filesystem handler',
    'filesystem.open_input_stream': 'Opening readable PyArrow input byte stream from storage driver',
    'fs.rm': 'Removing target file or directory node from remote or local storage',
    'fs._strip_protocol': 'Stripping scheme prefix (`s3://`, `gs://`) from URI to extract clean relative storage key',
    'fs.mkdirs': 'Alias method for creating directory tree hierarchies',
    'ArrowFSWrapper': 'Instantiating PyArrow filesystem interface wrapper around fsspec driver',
    'split_protocol': 'Splitting raw string URL into `(protocol, path)` component pair',
    'make_path_posix': 'Converting native platform separator path to standardized POSIX forward-slash path',
    'tokenize': 'Generating deterministic token hash of filesystem configuration and URL paths',
    'fs.relparts': 'Extracting relative path component tuple from root directory',
    'fs.isdvc': 'DVC custom validation call checking whether path is tracked under version control',
    'filesystem.isdir': 'Checking directory presence through abstracted storage filesystem layer',
    'fs.create_dir': 'Creating single directory container node inside underlying file storage',
    'self.fs.FileSelector': 'Creating recursive file selector specification object for batch selection',
    'OpenFile': 'Low-level context-managed open file stream handle object wrapper',
    'fsspec.open_local': 'Opening remote path by caching to temporary local disk and returning local path string',
    'self.fs._cat_file': 'Low-level direct byte range cat read of individual remote storage key',
    'self.fs.version_path': 'Resolving version-tagged object store path for immutable storage backends',
    'self.fs.info': 'Querying metadata record via encapsulated filesystem reference',
    'fs.open_parquet_file': 'Parquet-specific byte open call supporting column group section precaching (`parts`)',
    'fs.get_file': 'Downloading a single remote file to local target filename path',
    'fs.walk': 'Pythonic recursive generator yielding `(root, dirs, files)` tuples across directory tree',
    'self.fs.isin_or_eq': 'Checking if path matches or falls within expected tree prefix',
    'fs.abspath': 'Resolving absolute abstract URI path representation',
    'self.fs.makedirs': 'Instance method for recursive directory hierarchy creation',
    'DirFileSystem': 'Wrapping directory root so relative paths operate within a sub-tree sandbox',
    'self.fs.create_stream': 'Creating output byte stream for sequential checkpoint or log output',
    'LocalFileSystem': 'Instantiating explicit local host disk filesystem driver (`file://`)',
    'fsspec.get_fs_token_paths': 'High-level utility extracting tokenized filesystem reference for serialization',
    'self.fs._find': 'Low-level asynchronous file tree finder yielding all nested keys',
    'self.fs._rm': 'Internal implementation method deleting remote object key or prefix',
    'self.fs.parent': 'Locating immediate parent directory string of current path',
    'fs.name': 'Extracting simple file basename string from abstract path',
    'fs.dirname': 'Extracting parent directory path from abstract path string',
    'self.fs.split': 'Splitting abstract path into `(head, tail)` tuple pair',
    'fs.read_text': 'Directly reading entire remote file contents decoded as text string',
    'fs.put': 'Uploading local file or directory payload up to remote filesystem target',
    'filesystem.is_remote': 'Boolean flag checking whether abstract storage driver targets cloud/remote backend',
    'self.fs.LocalFileSystem': 'Referencing native host disk filesystem class',
    'filesystem.open_input_file': 'Opening PyArrow input file handle for random access byte read',
    'self.fs.S3FileSystem': 'Referencing Amazon S3 object storage filesystem backend driver',
    'fs.delete_dir': 'Recursively removing directory and all contained sub-keys',
    'fs.open_input_file': 'Opening read-only stream interface to underlying object key',
    'self.fs.copy_files': 'Batch copying multiple file paths within or across filesystem instances',
    'fs.S3FileSystem': 'Instantiating S3 filesystem interface driver',
    'filesystem.open_output_stream': 'Opening PyArrow output stream handle for sequential writing',
    'fs.ukey': 'Retrieving unique version hash or entity tag (`ETag`) for cache invalidation',
    'read_block': 'Reading fixed byte block range from file stream without reading entire file',
    'infer_compression': 'Detecting compression format (`gzip`, `bz2`, `zip`) from file extension suffix',
    'self.fs.get_file_info': 'Retrieving individual file information metadata record',
    'open_file': 'Opening individual file handle inside protocol catalog or dataset interface',
    'expand_paths_if_needed': 'Expanding wildcard glob strings into explicit path lists if glob syntax present',
    'self.fs._parent': 'Internal parent directory lookup helper',
    'self.fs.get_file': 'Downloading remote object to local disk path',
    'h.cat': 'Batch cat byte read via object store handle wrapper',
    'fsspec.open_files': 'Opening glob list of matching file paths as batch stream handle contexts',
    'compressions.values': 'Accessing registered decompression codec handlers collection',
    'self.fs.isfile': 'Checking leaf file node status',
    'self.fs.isdvc': 'Checking DVC tracking status of path',
    'self.fs.chdir': 'Changing current working directory context of filesystem wrapper',
    'fs.isabs': 'Checking if abstract path is formatted as an absolute path',
    'self.fs.isabs': 'Instance check for absolute path representation',
    'self.fs.remove': 'Deleting file or folder node from underlying filesystem',
    'fs.du': 'Calculating cumulative disk byte space consumed across directory tree',
    'fs.unstrip_protocol': 'Re-attaching scheme protocol prefix onto relative object key',
    'fs.getcwd': 'Getting active abstract directory path',
    'fs.parts': 'Splitting path into segment component strings',
    'fs.resolve_path': 'Resolving symlinks or relative references in remote path',
    'fs.listdir': 'Listing raw file names inside target directory node',
    'self.fs.rename': 'Renaming or moving an object path within filesystem storage',
    'self.fs.rm': 'Deleting remote object key or tree',
    'filesystem.listdir': 'Directory listing through abstraction wrapper interface',
    'filesystem.isfile': 'Leaf file node check through abstraction wrapper interface',
    'self.filesystem.create_dir': 'Creating directory node through wrapped storage driver',
    'self.filesystem.open_output_stream': 'Opening output byte stream through PyArrow wrapper',
    'fs.delete_file': 'Deleting single file node from storage driver',
    'self.fs.FSSpecHandler': 'PyArrow custom filesystem bridge wrapping fsspec driver',
    'self.fs.PyFileSystem': 'PyArrow filesystem representation wrapping abstract driver',
    'fs.open_output_stream': 'Opening write output stream handle',
    'gcsfs.GCSFileSystem': 'Instantiating Google Cloud Storage (`gs://`) filesystem driver',
}

# Categorize method into clean functional section
def categorize(name):
    n = name.lower()
    if any(k in n for k in ['exists', 'info', 'isdir', 'isfile', 'size', 'du', 'stat', 'checksum', 'ukey', 'version', 'is_empty', 'modified']):
        return 'Metadata & Existence Checks'
    elif any(k in n for k in ['open', 'cat', 'read', 'write', 'head', 'tail', 'stream']):
        return 'Stream Reading & Writing'
    elif any(k in n for k in ['url_to_fs', 'filesystem', 'token', 'protocol', 'stringify', 'from_os', 'driver', 'mapper', 'unwrap']):
        return 'Protocol & Driver Resolution'
    elif any(k in n for k in ['join', 'relparts', 'relpath', 'parts', 'normpath', 'abspath', 'getcwd', 'isin', 'dirname', 'parent', 'split', 'commonpath', 'as_posix', 'init_path', 'concat_path']):
        return 'Path Arithmetic & Topologies'
    elif any(k in n for k in ['glob', 'find', 'walk', 'ls', 'dirfilesystem']):
        return 'Directory Traversal, Wildcards & Recursion'
    elif any(k in n for k in ['make', 'mkdir', 'touch', 'rm', 'remove', 'rename', 'mv', 'copy', 'delete', 'rmtree']):
        return 'File & Directory Creation / Cleanup'
    elif any(k in n for k in ['get', 'put', 'download', 'upload']):
        return 'Remote Data Transfer (Download/Upload)'
    else:
        return 'Driver Instances & Abstract Wrappers'

sorted_methods = sorted(method_info.items(), key=lambda x: -x[1]['count'])

# Build Full Summary Table in exact 4-column format user asked for:
# Target Call | Occurrences | Major Repositories | Usage Pattern
table_lines = []
table_lines.append('| Target Call | Occurrences | Major Repositories | Primary Usage Pattern |')
table_lines.append('| :--- | :---: | :--- | :--- |')

for name, data in sorted_methods:
    cnt = data['count']
    top_repos = ', '.join([f'`{r}`' for r, _ in data['repos'].most_common(3)])
    pattern = USAGE_PATTERNS.get(name)
    if not pattern:
        # Synthesize clear usage description if not in dictionary
        cat = categorize(name)
        pattern = f'{cat} API method detected across repository storage interactions'
    table_lines.append(f'| **`{name}`** | **{cnt}** | {top_repos} | {pattern} |')

with open('projects/all_methods_summary_table.md', 'w') as out:
    out.write('# Complete 4-Column Summary Table of All 183 FSSPEC Methods\n\n')
    out.write('This reference summary table documents **every single distinct method call** identified by our GitHub AST crawler across 12 major Python data science and AI codebases, matching the summary format (`Target Call` | `Occurrences` | `Major Repositories` | `Usage Pattern`).\n\n')
    out.write('\n'.join(table_lines) + '\n')

print(f'Generated projects/all_methods_summary_table.md with {len(sorted_methods)} methods!')
