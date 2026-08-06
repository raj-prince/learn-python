# GitHub Issues Performance & FSSPEC Crawl Report

- **Repositories Crawled:** `2`
- **Total Issues Scanned:** `297`
- **Matched Performance / FSSPEC Issues:** `229`

---

## 📊 Repository Issue Breakdown

| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |
| :--- | :--- | :--- | :--- |
| [fsspec/gcsfs](https://github.com/fsspec/gcsfs) | `97` | `76` | [#761](https://github.com/fsspec/gcsfs/issues/761) |
| [fsspec/filesystem_spec](https://github.com/fsspec/filesystem_spec) | `200` | `153` | [#1960](https://github.com/fsspec/filesystem_spec/issues/1960) |

---

## 🔍 Detailed Matched Issues

### [fsspec/gcsfs](https://github.com/fsspec/gcsfs) (76 issues)

#### 1. [[Feature Request] Decouple read cache size and write buffer size in AbstractBufferedFile](https://github.com/fsspec/gcsfs/issues/761) (#761)
- **URL:** https://github.com/fsspec/gcsfs/issues/761
- **Relevance Score:** `26` | **State:** `open` | **Author:** `suni72`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `block_size`, `cache`, `hang`, `io`, `performance`, `throughput`
- **Excerpt:** *"**The Problem** Currently, `AbstractBufferedFile` uses a single argument, `block_size`, to control both: 1. The size of the read cache (passed to cache initialization). 2. The write buffer size (triggering a flush/upload when the buffer exceeds this size). This coupling creates a limitation for down..."*

#### 2. [GCSFileSystem() hangs when called from multiple processes](https://github.com/fsspec/gcsfs/issues/379) (#379)
- **URL:** https://github.com/fsspec/gcsfs/issues/379
- **Relevance Score:** `23` | **State:** `open` | **Author:** `JackKelly`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `concurrent`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"**What happened**: In the last two versions of gcsfs (versions 2021.04.0 and 0.8.0), calling `gcsfs.GCSFileSystem()` from multiple processes hangs without any error messages if `gcsfs.GCSFileSystem()` has been called previously in the same Python interpreter session. This bug was not present in gcsf..."*

#### 3. [Empty HttpError is raised on _fetch_range randomly](https://github.com/fsspec/gcsfs/issues/323) (#323)
- **URL:** https://github.com/fsspec/gcsfs/issues/323
- **Relevance Score:** `21` | **State:** `open` | **Author:** `DPGrev`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

#### 4. [Max retries exceeded with url: /o/oauth2/token](https://github.com/fsspec/gcsfs/issues/91) (#91)
- **URL:** https://github.com/fsspec/gcsfs/issues/91
- **Relevance Score:** `21` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `block_size`, `cache`, `concurrent`, `io`, `timeout`
- **Excerpt:** *"I am trying to push a very large dataset to gcs via the xarray / zarr / gcsfs / dask stack. I have encountered a new error at the gcsfs level. Here's a summary of what I am doing ```python # manually created an xarray dataset called `ds` by concat-ing together many individual ones token = 'cache' fs..."*

#### 5. [ClientConnectorCertificateError on GET request to any blob](https://github.com/fsspec/gcsfs/issues/296) (#296)
- **URL:** https://github.com/fsspec/gcsfs/issues/296
- **Relevance Score:** `20` | **State:** `open` | **Author:** `v-hunt`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `io`, `stall`, `timeout`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

#### 6. [unexceptionally long timeout](https://github.com/fsspec/gcsfs/issues/633) (#633)
- **URL:** https://github.com/fsspec/gcsfs/issues/633
- **Relevance Score:** `19` | **State:** `open` | **Author:** `tcrasset`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`, `url_to_fs`
- **Perf Keywords:** `hang`, `io`, `timeout`
- **Excerpt:** *"In my app, I'd like to timeout after a certain amount of seconds if my bucket cannot be reached, and fall back on a local copy of my file. This is useful on deployments where egress to external sites is heavily firewalled. However, passing in all the timeout information I could find by looking at [t..."*

#### 7. [credentials error with distributed](https://github.com/fsspec/gcsfs/issues/90) (#90)
- **URL:** https://github.com/fsspec/gcsfs/issues/90
- **Relevance Score:** `18` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `concurrent`, `io`, `timeout`
- **Excerpt:** *"I am trying to use gcsfs via distributed in pangeo-data/pangeo#150. I have uncovered what seems like a serialization bug. This works from my notebook (the token appears to be cached): ```python fs = gcsfs.GCSFileSystem(project='pangeo-181919') fs.buckets ``` It returns the four buckets: `['pangeo', ..."*

#### 8. ['err': 'Please install gcsfs to access Google Storage'](https://github.com/fsspec/gcsfs/issues/439) (#439)
- **URL:** https://github.com/fsspec/gcsfs/issues/439
- **Relevance Score:** `17` | **State:** `open` | **Author:** `DanTaranis`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"when I : ``` from fsspec.registry import known_implementation print(known_implementations["gcs"]) ``` I get: ``` {'class': 'gcsfs.GCSFileSystem', 'err': 'Please install gcsfs to access Google Storage'} ``` However, I have already installed gcsfs and it's showing up in my pip freeze ``` import gcsfs ..."*

#### 9. [sys:1: RuntimeWarning: coroutine 'GCSFileSystem._info' was never awaited](https://github.com/fsspec/gcsfs/issues/285) (#285)
- **URL:** https://github.com/fsspec/gcsfs/issues/285
- **Relevance Score:** `17` | **State:** `open` | **Author:** `darkclouder`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"**What happened**: Exception: ``` Traceback (most recent call last): File "googleload.py", line 12, in <module> asyncio.get_event_loop().run_until_complete(main()) File "/path/to/python/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete return future.result() File "googleload.py"..."*

#### 10. [TypeError: __init__() got an unexpected keyword argument 'callback_timeout' ERROR   2022-07-04 13:39:43 +0200   master-replica-0        NoneType: None](https://github.com/fsspec/gcsfs/issues/482) (#482)
- **URL:** https://github.com/fsspec/gcsfs/issues/482
- **Relevance Score:** `16` | **State:** `open` | **Author:** `RobinGeibel`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`, `open_files`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"Hi, I am trying to train a PyTorch model on GCP and I am reading a csv file from a cloud storage bucket in the mean time. I get the same error when reading the file in two different ways: 1 - simply using pd.read_csv: code: `GCS_BUCKET = "led-test-run" GCS_BASE_ROOT = f"gs://{GCS_BUCKET}" TRAIN_DIR ..."*

#### 11. [glob performance regression](https://github.com/fsspec/gcsfs/issues/641) (#641)
- **URL:** https://github.com/fsspec/gcsfs/issues/641
- **Relevance Score:** `15` | **State:** `open` | **Author:** `mhfrantz`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `hang`, `io`, `performance`
- **Excerpt:** *"When using `GCSFileSystem.glob` with a pattern like `"bucket-name/prefix*suffix"`, version 2023.9.0 introduced a performance regression. Previously, this `glob` would be resolved with an efficient API call whose performance was proportional to the number of matching objects. Since 2023.9.0, the perf..."*

#### 12. [isdir/info method works incorrectly ](https://github.com/fsspec/gcsfs/issues/574) (#574)
- **URL:** https://github.com/fsspec/gcsfs/issues/574
- **Relevance Score:** `15` | **State:** `open` | **Author:** `TSienki`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `hang`, `hanging`, `io`
- **Excerpt:** *"Hello, I've found a strange behavior of the `isdir` method (digging deeper also with `info` method). It returns incorrect values. These values seem to be returned randomly. I use Python 3.10.12 and I've tested this behavior on `gscfs=2022.3.0`, and the latest version `gscfs=2023.6.0` I've prepared a..."*

#### 13. ["TypeError: from_buffer() cannot return the address of the raw string within a bytes or unicode object" when creating a GCSFileSystem object](https://github.com/fsspec/gcsfs/issues/365) (#365)
- **URL:** https://github.com/fsspec/gcsfs/issues/365
- **Relevance Score:** `15` | **State:** `open` | **Author:** `wpm`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `hang`, `io`, `stall`
- **Excerpt:** *"**What happened**: When I tried to load a `GCSFileSystem` object, I got the exception `TypeError: from_buffer() cannot return the address of the raw string within a bytes or unicode object`. **What you expected to happen**: I expect the `GCSFileSystem` object to instantiate and be usable. This has w..."*

#### 14. [Calling rm(path, recursive=true) on an empty bucket causes a FileNotFound error](https://github.com/fsspec/gcsfs/issues/324) (#324)
- **URL:** https://github.com/fsspec/gcsfs/issues/324
- **Relevance Score:** `15` | **State:** `open` | **Author:** `NickAJScott`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `hang`, `io`, `stall`
- **Excerpt:** *"**What happened**: Upgrading to version 0.7.1 from 0.6.2 i found behaviour had changed where calling remove on a bucket with recursive = true with the below parameters now throws a FileNotFoundError if the bucket is empty, if the bucket contains a file it successfully deletes it, however it also del..."*

#### 15. [Confusion over paths in put(recursive=True)](https://github.com/fsspec/gcsfs/issues/249) (#249)
- **URL:** https://github.com/fsspec/gcsfs/issues/249
- **Relevance Score:** `15` | **State:** `open` | **Author:** `max-sixty`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `hang`, `hanging`, `io`
- **Excerpt:** *"I'm facing some confusion over how paths are handled in `fs.put(recursive=True)`. In addition, the upload location seems different depending on whether the remote path exists. If I run this code from `~/workspace/project` ```python fs = gcsfs.GCSFileSystem() fs.put("./data/transformed/", "gs://proje..."*

#### 16. [Warnings on connection](https://github.com/fsspec/gcsfs/issues/104) (#104)
- **URL:** https://github.com/fsspec/gcsfs/issues/104
- **Relevance Score:** `15` | **State:** `open` | **Author:** `mrocklin`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `stall`, `timeout`
- **Excerpt:** *"I've just `pip install gcsfs` from what I believe to be a somewhat fresh environment. On trying to connect I get a number of warnings that I'm not able to easily understand. Things do seem to work afterwards though. ```python In [1]: import gcsfs In [2]: fs = gcsfs.GCSFileSystem() _call exception: H..."*

#### 17. [Uninformative error with invalid / not set credentials](https://github.com/fsspec/gcsfs/issues/82) (#82)
- **URL:** https://github.com/fsspec/gcsfs/issues/82
- **Relevance Score:** `15` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `stall`, `timeout`
- **Excerpt:** *"I am trying to use gcsfs to access gcs from the NASA pleaides supercomputer. I tried to initialize a gcsfs.mapping before having my credentials set up properly (although I thought my default credentials were valid.) I was able to get past this error by setting `GOOGLE_APPLICATION_CREDENTIALS` enviro..."*

#### 18. [`google.auth.exceptions.RefreshError` with excessive concurrent requests.](https://github.com/fsspec/gcsfs/issues/71) (#71)
- **URL:** https://github.com/fsspec/gcsfs/issues/71
- **Relevance Score:** `15` | **State:** `open` | **Author:** `asford`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `concurrent`, `io`
- **Excerpt:** *"`gcsfs` propagates an `google.auth.exceptions.RefreshError` when executing many concurrent requests from a single node using the `google_default` credentials class. This is likely due to repeated, excessive number of requests to the internal metadata service. This is a known bug of the external libr..."*

#### 19. [`_isdir()` does not put entry in the dircache](https://github.com/fsspec/gcsfs/issues/702) (#702)
- **URL:** https://github.com/fsspec/gcsfs/issues/702
- **Relevance Score:** `14` | **State:** `open` | **Author:** `aabmass`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Thanks for the awesome project! I'm running into an issue where gcsfs is making many unexpected `GET` requests when I try to upload to a directory within a GCS bucket using `put()`. I believe the issue can be reproduced by just calling `GcsFileSystem.put("somefile.txt", "gs://bucket/subdir/somefile...."*

#### 20. [Unable to use ls and open operations because of threading error](https://github.com/fsspec/gcsfs/issues/465) (#465)
- **URL:** https://github.com/fsspec/gcsfs/issues/465
- **Relevance Score:** `14` | **State:** `open` | **Author:** `SwarnaBharathiMantena`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"Hi, I tried the ls() and open() operations following the examples stated here: https://gcsfs.readthedocs.io/en/latest/ I get no result for both the calls. When I interrupt, I see the traceback as mentioned below. ``` import gcsfs import pandas as pd fs = gcsfs.GCSFileSystem(project='<my-bucket-name>..."*

#### 21. [rm fails on path with leading slash](https://github.com/fsspec/gcsfs/issues/300) (#300)
- **URL:** https://github.com/fsspec/gcsfs/issues/300
- **Relevance Score:** `14` | **State:** `open` | **Author:** `chiaral`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"**What happened**: I tried to remove an object from a Google Cloud Storage. The operation works if I have no leading slash, i.e. ``` pangeo-scratch/chiaral/test_path/foo ``` It fails with a leading slash ``` /pangeo-scratch/chiaral/test_path/foo ``` However, I can write / list / read the object with..."*

#### 22. [[Feature Request] Dynamically set VARIABLE_IO_THRESHOLD in Prefetcher](https://github.com/fsspec/gcsfs/issues/852) (#852)
- **URL:** https://github.com/fsspec/gcsfs/issues/852
- **Relevance Score:** `13` | **State:** `open` | **Author:** `googlyrahman`
- **Labels:** `enhancement`
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `hang`, `io`, `prefetch`
- **Excerpt:** *"See https://github.com/fsspec/gcsfs/pull/818/changes#r3235520806 for more details."*

#### 23. [refresh = True should be the default for GCSFS.ls](https://github.com/fsspec/gcsfs/issues/647) (#647)
- **URL:** https://github.com/fsspec/gcsfs/issues/647
- **Relevance Score:** `13` | **State:** `open` | **Author:** `rickmcgeer`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfs`
- **Perf Keywords:** `caching`, `hang`, `io`
- **Excerpt:** *"I was working with this system today, and noticed that ls wasn't returning all the files in a bucket. After I changed the call from: ``` gcs_file_system.ls(my_bucket) ``` To ``` gcs_file_system.ls(my_bucket, refresh=True) ``` I can appreciate the value of caching as an option, but returning an outda..."*

#### 24. [GCSFS reports directory as FileNotFoundError when it exists. Run 1 fails, run 2 succeeds. Caching?](https://github.com/fsspec/gcsfs/issues/632) (#632)
- **URL:** https://github.com/fsspec/gcsfs/issues/632
- **Relevance Score:** `12` | **State:** `open` | **Author:** `pascalwhoop`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `caching`, `io`
- **Excerpt:** *"Hi, We went down a rabbit hole trying to find this one. https://github.com/apache/arrow/issues/31339 Turns out Pandas can't read partitioned parquet files from a directory because of PyArrow using GCSFS. However in this repo there seems to be no mention of this. Are you aware of any situation where ..."*

#### 25. [Compute Engine Metadata server unavailable when VM instance preempties](https://github.com/fsspec/gcsfs/issues/476) (#476)
- **URL:** https://github.com/fsspec/gcsfs/issues/476
- **Relevance Score:** `12` | **State:** `open` | **Author:** `Trollgeir`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"I am using a shutdown script to save a file whenever [preemptible VM instances](https://cloud.google.com/compute/docs/instances/preemptible) shut down. I am authed to my project inside the VM through service accounts (`cloud`), as I have access by simply doing `fs = gcsfs.GCSFileSystem()` during run..."*

#### 26. [Missing zarr chunks written directly to bucket in parallel](https://github.com/fsspec/gcsfs/issues/327) (#327)
- **URL:** https://github.com/fsspec/gcsfs/issues/327
- **Relevance Score:** `12` | **State:** `open` | **Author:** `rafa-guedes`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"We have recently started writing large zarr archives directly to google buckets in parallel using fsspec/gcsfs and the new `regions` capability in latest xarray release. We have found some intermittent issues that appear to be related to gcsfs (they are not seen when writing locally to disk). The mo..."*

#### 27. [File paths with "#" characters cannot be opened.](https://github.com/fsspec/gcsfs/issues/270) (#270)
- **URL:** https://github.com/fsspec/gcsfs/issues/270
- **Relevance Score:** `12` | **State:** `open` | **Author:** `zafercavdar`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

#### 28. ["Forbidden" for writing, but not reading, when using `token='cache'` and `token='cloud'`](https://github.com/fsspec/gcsfs/issues/230) (#230)
- **URL:** https://github.com/fsspec/gcsfs/issues/230
- **Relevance Score:** `12` | **State:** `open` | **Author:** `arokem`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"We are using gcsfs inside a pangeo-powered cluster on GCP. One of our users has run into the following somewhat-mysterious behavior: initializing a `gcfs.GCSFileSystem` object with `token='cache'` and `token='cloud'` allows him to read items that are in a bucket on our project, but he hits a 403 and..."*

#### 29. [[Future Work] Promote DirectMemmoveBuffer into Standard Bucket Path](https://github.com/fsspec/gcsfs/issues/888) (#888)
- **URL:** https://github.com/fsspec/gcsfs/issues/888
- **Relevance Score:** `11` | **State:** `open` | **Author:** `googlyrahman`
- **Labels:** `enhancement`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `throughput`
- **Excerpt:** *"ZonalFile manages concurrency through an in-house buffer that preallocates space, allowing workers to write directly to memory. It uses the `ctypes.pythonAPI` library to execute GIL-free writes, which avoids unnecessary data copies and prevents the global interpreter lock from creating a bottleneck...."*

#### 30. [GCS High Performance Parallel Listing ](https://github.com/fsspec/gcsfs/issues/567) (#567)
- **URL:** https://github.com/fsspec/gcsfs/issues/567
- **Relevance Score:** `11` | **State:** `open` | **Author:** `hanseaston`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`, `performance`, `speed`
- **Excerpt:** *"Hello Martin, I am currently a Google SWE intern, and I am working as a part of the GCS team. We are thinking of optimizing the listing operation in GCSFS, and want to get your initial approval on this. In particular, we are thinking of utilizing **multiple processes** (using the `concurrency.future..."*

#### 31. [cat_file with start and end of gzipped file does not work.](https://github.com/fsspec/gcsfs/issues/512) (#512)
- **URL:** https://github.com/fsspec/gcsfs/issues/512
- **Relevance Score:** `11` | **State:** `open` | **Author:** `racinmat`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Reading gzipped file using transcoding works when you use the `fs.open`, but not when using `fs.cat_file`. Here is and example uploading 2 files, 1 plaintext, 1 gzipped, and both files are read using open, and then using cat_file: This part works: ```python fs = gcsfs.GCSFileSystem(project='a') a_fi..."*

#### 32. [Using browser authorization url but shows "401 Error: deleted_client"](https://github.com/fsspec/gcsfs/issues/511) (#511)
- **URL:** https://github.com/fsspec/gcsfs/issues/511
- **Relevance Score:** `11` | **State:** `open` | **Author:** `orcahmlee`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I tried to use browser authorization but kept getting the `401`. <img width="502" alt="Screenshot 2022-11-28 at 16 44 03" src="https://user-images.githubusercontent.com/26179752/204233071-3ab75113-2d8b-49ea-8aae-abb973ff4a94.png"> ```python from gcsfs import GCSFileSystem fs = GCSFileSystem(token="b..."*

#### 33. [Release 0.7.0 causes GCP Cloud Function to fail to deploy](https://github.com/fsspec/gcsfs/issues/278) (#278)
- **URL:** https://github.com/fsspec/gcsfs/issues/278
- **Relevance Score:** `11` | **State:** `open` | **Author:** `nmetts`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `hang`, `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

#### 34. [uploadType change between 0.2.3 and 0.3.0](https://github.com/fsspec/gcsfs/issues/172) (#172)
- **URL:** https://github.com/fsspec/gcsfs/issues/172
- **Relevance Score:** `11` | **State:** `open` | **Author:** `gogasca`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `hang`, `io`, `stall`
- **Excerpt:** *"I'm trying to write remotely a file in my bucket storage. In 0.2.3 I see GCSFS sending: https://www.googleapis.com:443 "POST /upload/storage/v1/b/dpe-sandbox/o?uploadType=multipart HTTP/1.1" 429 463 In 0.3.0: https://www.googleapis.com:443 "POST /upload/storage/v1/b/dpe-sandbox/o?uploadType=resumabl..."*

#### 35. [gcsfuse entrypoint conflicts with Google Cloud Platform's fuse solution](https://github.com/fsspec/gcsfs/issues/135) (#135)
- **URL:** https://github.com/fsspec/gcsfs/issues/135
- **Relevance Score:** `11` | **State:** `open` | **Author:** `AneeshSachdeva`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `hang`, `io`, `stall`
- **Excerpt:** *"I use gcsfs to easily load and dump data distributively with Dask. Recently I needed to install Google Cloud's official fuse tool, called [gcsfuse](https://github.com/GoogleCloudPlatform/gcsfuse), and I ran into a conflict between Google Cloud's "gcsfuse" cli and this repo's "gcsfuse" cli. I had to ..."*

#### 36. [GCSMap: error first time command is run but not the second](https://github.com/fsspec/gcsfs/issues/117) (#117)
- **URL:** https://github.com/fsspec/gcsfs/issues/117
- **Relevance Score:** `11` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"I'm trying to access data from a public GCS bucket using gcsfs.GCSMap. The first time I run this code ```python import gcsfs gcmap = gcsfs.GCSMap('pangeo-data/pyqg/barotropic/beta_00.zarr') ``` it fails with this error: ``` _call exception: ('invalid_grant: Bad Request', '{\n "error": "invalid_grant..."*

#### 37. [FileNotFoundError on file.read](https://github.com/fsspec/gcsfs/issues/184) (#184)
- **URL:** https://github.com/fsspec/gcsfs/issues/184
- **Relevance Score:** `10` | **State:** `open` | **Author:** `zafercavdar`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"I have uploaded a file to GCS and was able to read it without problem. After that I deleted the file and uploaded it again with a same name. When I called file.read function again, I receive FileNotFoundError coming from fetch range though the file exists. Full traceback: ``` byte_str = csv_file.rea..."*

#### 38. [Streamed writes above 5MB may cause writes to be rejected due to lack of alignment](https://github.com/fsspec/gcsfs/issues/886) (#886)
- **URL:** https://github.com/fsspec/gcsfs/issues/886
- **Relevance Score:** `9` | **State:** `open` | **Author:** `datumest`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"In [ads_oneshop](https://github.com/google/ads_oneshop/blob/328955b48cfdacbda62d070666d4f33258fdcbae/acit/gaql.py#L183), we stream JSON objects directly into a gcsfs file via etils, delegating flush logic to gcsfs. Recently, one of the users of that project identified a case where a streamed write w..."*

#### 39. [Support for IAM-based signing for GCS Bucket blobs](https://github.com/fsspec/gcsfs/issues/653) (#653)
- **URL:** https://github.com/fsspec/gcsfs/issues/653
- **Relevance Score:** `9` | **State:** `open` | **Author:** `benglewis`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Current state: Currently, `gcsfs` does not natively support generating signed URLs using IAM-based credentials provided by GCP Workload Identity or other non-private key credentials. This is a limitation when running on environments such as Google Kubernetes Engine (GKE) with Workload Identity, ..."*

#### 40. [Missing 'name' attribute in 'GCSFile' object when accessing PDF files](https://github.com/fsspec/gcsfs/issues/617) (#617)
- **URL:** https://github.com/fsspec/gcsfs/issues/617
- **Relevance Score:** `9` | **State:** `open` | **Author:** `bhavan-kaya`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"**Description:** In the context of using `gcsfs` with `llama-index` for reading files from a GCP bucket, an error occurs for PDF files indicating that the `'GCSFile' object has no attribute 'name'`. This issue does not occur when accessing DOCX files. It suggests that there may be an inconsistency o..."*

#### 41. [put() has inconsistent results if you run from Python Console vs in a file.](https://github.com/fsspec/gcsfs/issues/517) (#517)
- **URL:** https://github.com/fsspec/gcsfs/issues/517
- **Relevance Score:** `9` | **State:** `open` | **Author:** `AkshitaB`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"On version `gcsfs==2022.11.0` Consider the following code snippet: ``` import gcsfs source = 'abc' # this is a folder - abc/file.txt, abc/subfolder/file.txt target = 'my_bucket/folder' fs = gcsfs.GCSFileSystem(consistency="md5") fs.touch(target + "/.placeholder", truncate=True) # to create a folder ..."*

#### 42. [Why doesn't gcsfs allow projects different from the default project in google_default?](https://github.com/fsspec/gcsfs/issues/483) (#483)
- **URL:** https://github.com/fsspec/gcsfs/issues/483
- **Relevance Score:** `9` | **State:** `open` | **Author:** `yokomotod`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"With account which has `$ gcloud config get-value project # => project-a`, ```python fs = gcsfs.GCSFileSystem(project='project-b') ``` raise validation error: ``` ValueError: User-provided project 'project-b' does not match the google default project 'project-a'. Either 1. Accept the google-default ..."*

#### 43. [Requester Pays blocks typical auth mechanism](https://github.com/fsspec/gcsfs/issues/470) (#470)
- **URL:** https://github.com/fsspec/gcsfs/issues/470
- **Relevance Score:** `9` | **State:** `open` | **Author:** `nbren12`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I'm not if sure if this is a "bug" or intentional, but I've had some difficulty when using requester pays mode. Typical google auth doesn't require a default project to be configured in order to access some files, but gcsfs+requester_pays does. See this code: ``` Python 3.8.10 (default, Mar 15 2022,..."*

#### 44. [google.cloud.storage allows access but gcsfs does not](https://github.com/fsspec/gcsfs/issues/395) (#395)
- **URL:** https://github.com/fsspec/gcsfs/issues/395
- **Relevance Score:** `9` | **State:** `open` | **Author:** `awa5114`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I would like to connect to a bucket on google cloud storage using `gcsfs`. So far I have only been using the native `google.cloud` module but it turns out I actually need file like objects for a certain application so had to switch over. My `GOOGLE_APPLICATION_CREDENTIALS` environment variable point..."*

#### 45. [Should the default consistency for GCSFile be md5?](https://github.com/fsspec/gcsfs/issues/361) (#361)
- **URL:** https://github.com/fsspec/gcsfs/issues/361
- **Relevance Score:** `9` | **State:** `open` | **Author:** `isidentical`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Composite objects in GCSFs doesn't have a md5 hash, so it kinda feels weird that the default consistency is md5 (also it never gets used since most of the operations around it is done by `_open` which passes the consistency as either None or the instance's consistency [defaults to also None]). Maybe..."*

#### 46. [GCSFileSystem constructor with token=None does not try to get credentials from metadata service](https://github.com/fsspec/gcsfs/issues/264) (#264)
- **URL:** https://github.com/fsspec/gcsfs/issues/264
- **Relevance Score:** `9` | **State:** `open` | **Author:** `dynamix`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Tried connect methods according to the documentation: https://github.com/dask/gcsfs/blob/2021a89471990c58f3acaf84bd4e277c0d6c2e4d/gcsfs/core.py#L143-L146 However the methods are: https://github.com/dask/gcsfs/blob/2021a89471990c58f3acaf84bd4e277c0d6c2e4d/gcsfs/core.py#L408 The google compute metadat..."*

#### 47. [read() returns incomplete file? (not clear on documentation)](https://github.com/fsspec/gcsfs/issues/233) (#233)
- **URL:** https://github.com/fsspec/gcsfs/issues/233
- **Relevance Score:** `9` | **State:** `open` | **Author:** `fernandobrito`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hello, This is my first time using the library, so please apologize me if I'm missing something obvious. I'm trying to read a `.csv.gz` file (quite small, less than 100kb) following the documentation (https://gcsfs.readthedocs.io/en/latest/#examples), by doing: ``` fs = gcsfs.GCSFileSystem(project=p..."*

#### 48. [service account permissions error](https://github.com/fsspec/gcsfs/issues/89) (#89)
- **URL:** https://github.com/fsspec/gcsfs/issues/89
- **Relevance Score:** `9` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I am trying to use gcsfs with a GCS service account .json token. I created a token at https://console.cloud.google.com/iam-admin/serviceaccounts/ and assigned it the role of "Storage Admin". This should have permissions to do anything to my GCS resources. I downloaded the .json token. I use this wit..."*

#### 49. [We are having multiple Task failures for Cloud run, the error message in Cloud Run says "md5 checksum error"](https://github.com/fsspec/gcsfs/issues/661) (#661)
- **URL:** https://github.com/fsspec/gcsfs/issues/661
- **Relevance Score:** `8` | **State:** `open` | **Author:** `Gowtham589`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"We are getting the md5 checksum error again across multiple pipelines. this error is causing failures for our data pipelines. Earlier, we received this error and Google provided the following findings: "GCS doesn't store MD5 checksums for composite objects. A composite object isn't a single entity; ..."*

#### 50. [Cannot connect to host when running in dataproc](https://github.com/fsspec/gcsfs/issues/444) (#444)
- **URL:** https://github.com/fsspec/gcsfs/issues/444
- **Relevance Score:** `8` | **State:** `open` | **Author:** `pepperbc`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"When running in dataproc, I get the following error: `aiohttp.client_exceptions.ClientConnectorError: Cannot connect to host storage.googleapis.com:443 ssl:default [Network is unreachable] ` I have tried using both None, "cloud", and "google_default" for token. (I believe "cloud" is the correct opti..."*

#### 51. [touch(truncate=True) is a bad default](https://github.com/fsspec/gcsfs/issues/364) (#364)
- **URL:** https://github.com/fsspec/gcsfs/issues/364
- **Relevance Score:** `8` | **State:** `open` | **Author:** `rabernat`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"**What happened**: I wanted to update the timestamp on 2000 objects, comprising of 5 TB of data on Google Cloud. So I ran ```python for obj in obj_list: fs.touch(obj) ``` **What you expected to happen**: Consistent with my experience with the unix `touch` command, I assumed the default behavior woul..."*

#### 52. [Failed to Establish New Connection Error on GKE ](https://github.com/fsspec/gcsfs/issues/241) (#241)
- **URL:** https://github.com/fsspec/gcsfs/issues/241
- **Relevance Score:** `8` | **State:** `open` | **Author:** `bgoodman44`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"I'm using gcfs version 0.6.0, and everything was working fine yesterday (so it might be a GKE issue). I'm on a GKE cluster, so my login credentials are already available, and I'm not explicitly providing a token. I've tried the "browser" method as well, with the same result. Because everything was w..."*

#### 53. [write/flush asynchronous](https://github.com/fsspec/gcsfs/issues/188) (#188)
- **URL:** https://github.com/fsspec/gcsfs/issues/188
- **Relevance Score:** `8` | **State:** `open` | **Author:** `yan-hic`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`, `speed`
- **Excerpt:** *"More question first: is flushing to gcs asynchronous ? i.e. I like this not to be a blocking operation so that the buffer (and new one ?) gets filled in while the previous block is being written to backend. If it is a blocking op, request is to not make it ;-) or provide an option to enable/disable...."*

#### 54. [Authenticating via Interoperable storage access keys](https://github.com/fsspec/gcsfs/issues/154) (#154)
- **URL:** https://github.com/fsspec/gcsfs/issues/154
- **Relevance Score:** `8` | **State:** `open` | **Author:** `mzjp2`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `caching`, `io`
- **Excerpt:** *"Hi, I'm working on a project that implements connections to S3 via the super simple ``aws_access_key_id``, ``aws_secret_access_key`` variables and I'd like to extend the functionality to include GCS access too. GCS has similar functionality via their interoperability API but I can't seem to figure o..."*

#### 55. [Can't open gcsfuse-mounted HDF5 file with h5py](https://github.com/fsspec/gcsfs/issues/107) (#107)
- **URL:** https://github.com/fsspec/gcsfs/issues/107
- **Relevance Score:** `8` | **State:** `open` | **Author:** `ryan-williams`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `block_size`, `io`
- **Excerpt:** *"First I ran: ``` gcsfuse <bucket> /tmp/<bucket> ``` Then, attempting to open an HDF5 file with [h5py](http://www.h5py.org/): ``` >>> from h5py import * >>> input = '/tmp/<bucket>/file' >>> f = File(input, 'r') Traceback (most recent call last): File "<stdin>", line 1, in <module> File "…/venv/lib/py..."*

#### 56. [too many deps for microbenchmarks](https://github.com/fsspec/gcsfs/issues/743) (#743)
- **URL:** https://github.com/fsspec/gcsfs/issues/743
- **Relevance Score:** `7` | **State:** `open` | **Author:** `martindurant`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `benchmark`
- **Excerpt:** *"The gcsfs test suite is now now importable without extra libraries like psutil, numpy, prettytable and others - even if we don't intend to actually run the benchmarks. fsspec runs the gcsfs test suite as part of its CI, and although I have started to add some deps, I would much rather remove their n..."*

#### 57. [Pin generation on open for version aware file system](https://github.com/fsspec/gcsfs/issues/601) (#601)
- **URL:** https://github.com/fsspec/gcsfs/issues/601
- **Relevance Score:** `7` | **State:** `open` | **Author:** `emfdavid`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"[Here is an example](https://gist.github.com/emfdavid/c4f4e0573444944b3161430d24998c07) of the current behavior of version_aware file systems and open files in GCSFS. I would have expected a version_aware file system to pin the generation of an object while the file is open so that the reads are con..."*

#### 58. [_connect_cloud regression in 2022.7.1 - Invalid gcloud credentials](https://github.com/fsspec/gcsfs/issues/486) (#486)
- **URL:** https://github.com/fsspec/gcsfs/issues/486
- **Relevance Score:** `7` | **State:** `open` | **Author:** `baxen`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Our workflows using gcsfs==2022.7.1 are seeing a new error connecting from google cloud environments ``` File "/usr/local/lib/python3.8/site-packages/gcsfs/core.py", line 280, in __init__ self.credentials = GoogleCredentials(project, access, token) File "/usr/local/lib/python3.8/site-packages/gcsfs/..."*

#### 59. [`flush` doesn't create or upload the file until the file is closed](https://github.com/fsspec/gcsfs/issues/484) (#484)
- **URL:** https://github.com/fsspec/gcsfs/issues/484
- **Relevance Score:** `7` | **State:** `open` | **Author:** `VOvchinnikov`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"`fsspec` version `2022.5.0` `gcsfs` version `2022.5.0` Code to reproduce: ``` import fsspec fileobj = fsspec.open('gs://<insert-your-bucket-here>/test-write-flush', 'w', auto_mkdirs=True) f = fileobj.fs.open(fileobj.path, mode=fileobj.mode) f.write('w' * (2**20)) # is guaranteed to be larger than mi..."*

#### 60. [Unexpected ParseError](https://github.com/fsspec/gcsfs/issues/318) (#318)
- **URL:** https://github.com/fsspec/gcsfs/issues/318
- **Relevance Score:** `7` | **State:** `open` | **Author:** `eric-czech`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I saw this when running a long job that writes Zarr archives on GS: ``` Traceback (most recent call last): File "scripts/gwas.py", line 420, in <module> fire.Fire() File "/home/eczech/repos/ukb-gwas-pipeline-nealelab/.snakemake/conda/b5bd29d8/lib/python3.8/site-packages/fire/core.py", line 138, in F..."*

#### 61. [GCS session does not support requests transport adapters](https://github.com/fsspec/gcsfs/issues/253) (#253)
- **URL:** https://github.com/fsspec/gcsfs/issues/253
- **Relevance Score:** `7` | **State:** `open` | **Author:** `matthewtberry`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"I would like to use a custom [requests transport adapter](https://requests.readthedocs.io/en/master/user/advanced/#transport-adapters) on the session with GCS. The session object is managed by `GCSFileSystem` class so a caller has no control over it."*

#### 62. [Resolved to no files error. using dd.read_csv and a globstring](https://github.com/fsspec/gcsfs/issues/205) (#205)
- **URL:** https://github.com/fsspec/gcsfs/issues/205
- **Relevance Score:** `7` | **State:** `open` | **Author:** `PoradaKev`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi! dask 2.8.0, gcsfs 0.4.0 I have the following error when trying to use a glob string in a file path: ``` --------------------------------------------------------------------------- OSError Traceback (most recent call last) <ipython-input-14-559125deb7ec> in <module> 5 ) and clusterid !=32003 6 ''..."*

#### 63. [Getting 'GS' key error when reading a csv from GCS using gcsfc](https://github.com/fsspec/gcsfs/issues/162) (#162)
- **URL:** https://github.com/fsspec/gcsfs/issues/162
- **Relevance Score:** `7` | **State:** `open` | **Author:** `ohashmi1`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi I upgraded gcsfs and now I get the following error: My code is pretty simple: ``` data = dd.read_csv(file_path, parse_dates=[date_column])\ .compute() return data``` It used to work but all of a sudden it stopped working. file_path = gs://mybuck/res.csv ```File "main.py", line 51, in run data = l..."*

#### 64. [The _cat_file doesn't respect the header passed via user.](https://github.com/fsspec/gcsfs/issues/889) (#889)
- **URL:** https://github.com/fsspec/gcsfs/issues/889
- **Relevance Score:** `5` | **State:** `open` | **Author:** `googlyrahman`
- **Labels:** `bug`, `enhancement`
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The `_cat_file` function currently ignores headers provided by the user. While this might be intended behavior since we have not supported them historically, I believe now is a good time to add support for this use case, given that `_get_file` will soon depend on it."*

#### 65. [RuntimeError - Please reduce your request rate](https://github.com/fsspec/gcsfs/issues/650) (#650)
- **URL:** https://github.com/fsspec/gcsfs/issues/650
- **Relevance Score:** `5` | **State:** `open` | **Author:** `norlandrhagen`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi there 👋 Deep within pangeo-forge-recipes we're seeing this error crop up when writing to a gcs bucket. It seem to happen on multiple gcsfs version (2024.10.0, 2024.09.0, etc..) ```RuntimeError: gcsfs.retry.HttpError: The object <path>/chirps-global-daily.zarr/time/0 exceeded the rate limit for ob..."*

#### 66. [Is there an async version of touch?](https://github.com/fsspec/gcsfs/issues/634) (#634)
- **URL:** https://github.com/fsspec/gcsfs/issues/634
- **Relevance Score:** `5` | **State:** `open` | **Author:** `vedantroy`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Exactly as the question sounds. Is there an async version of touch?"*

#### 67. [Question: aiohttp vs. gRPC API](https://github.com/fsspec/gcsfs/issues/625) (#625)
- **URL:** https://github.com/fsspec/gcsfs/issues/625
- **Relevance Score:** `5` | **State:** `open` | **Author:** `keunhong`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hello! I was curious if there was a reason gcsfs uses `aiohttp` with the JSON API to query GCS rather than using the Google Python client which calls the gRPC API. AFAIK the gRPC API is a lot more efficient."*

#### 68. [Is there already a way to list metadata attributes?](https://github.com/fsspec/gcsfs/issues/545) (#545)
- **URL:** https://github.com/fsspec/gcsfs/issues/545
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Tunneller`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I see:: ``` async def _getxattr(self, path, attr): """Get user-defined metadata attribute""" meta = (await self._info(path)).get("metadata", {}) return meta[attr] getxattr = sync_wrapper(_getxattr) ``` Could we have as well something like: ``` async def _listxattr(self, path, attr): """List all user..."*

#### 69. [ gcsfs put copies files out of order](https://github.com/fsspec/gcsfs/issues/468) (#468)
- **URL:** https://github.com/fsspec/gcsfs/issues/468
- **Relevance Score:** `5` | **State:** `open` | **Author:** `mlahir1`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"i am trying to copy multiple files using gcsfs put API. The syntax provided to copy multiple files goes like this. lpath1 is supposed to put the data into rapth1 and respectively for other files. gcs.put([lpath1, lpath2, lpath3, lapth4], [rpath1, rpath2, rpath3, rpath4]) Issue: The copy happens out ..."*

#### 70. [gcsfs doesn't properly handle gzipped files, ignoring content-encoding](https://github.com/fsspec/gcsfs/issues/461) (#461)
- **URL:** https://github.com/fsspec/gcsfs/issues/461
- **Relevance Score:** `5` | **State:** `open` | **Author:** `jimmywan`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have a file "foo.txt.gz" that has been uploaded with the following metadata: > Content-Type: text/plain > Content-Encoding: gzip I'm trying to copy its contents to a new file in cloud storage that is uncompressed to workaround a bug where my tooling (gcloud) can't properly handle gzip input. If I ..."*

#### 71. [Generation ID ignored when reading from gcs](https://github.com/fsspec/gcsfs/issues/446) (#446)
- **URL:** https://github.com/fsspec/gcsfs/issues/446
- **Relevance Score:** `5` | **State:** `open` | **Author:** `xquek-fn`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, I am having an issue reading specific generation/versions of files from gcs. For instance, in a bucket with versioning enabled: ``` # old gs://mock-bucket/something.csv#123456789 # new gs://mock-bucket/something.csv#999999999 ``` when trying to read `gs://mock-bucket/something.csv#123456789`, it..."*

#### 72. [Set content encoding (i.e. gzip) when writing file](https://github.com/fsspec/gcsfs/issues/306) (#306)
- **URL:** https://github.com/fsspec/gcsfs/issues/306
- **Relevance Score:** `5` | **State:** `open` | **Author:** `isaacbrodsky`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"When writing files, it's helpful to be able to specify the Content-Encoding in addition to the Content-Type. I didn't see a way I could pass that option through. Otherwise, another call to `setxattrs` is needed. Current: ``` path = 'gs://some_bucket/some_blob.gz' with fs.open(path, mode='wb', conten..."*

#### 73. [Exceptions don't have a common superclass](https://github.com/fsspec/gcsfs/issues/236) (#236)
- **URL:** https://github.com/fsspec/gcsfs/issues/236
- **Relevance Score:** `5` | **State:** `open` | **Author:** `helgridly`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have code that uses gcsfs peppered in with other work. I'd like to catch gcsfs-related errors and treat them separately, but [validate_response](https://github.com/dask/gcsfs/blob/d7b832e13de6b5b0df00eeb7454c6547bf30d7b9/gcsfs/core.py#L151) uses many different exception types from multiple librari..."*

#### 74. [glob without star (*) returns wrong value](https://github.com/fsspec/gcsfs/issues/235) (#235)
- **URL:** https://github.com/fsspec/gcsfs/issues/235
- **Relevance Score:** `5` | **State:** `open` | **Author:** `wookayin`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"``` >>> gcsfs.__version__ '0.2.3' ``` The `glob()` function without star (*) returns wrong value. This is an inconsistent behavior different than `glob.glob` or `tensorflow.io.gfile.glob`. ```python >>> fs.glob('gs://mybucket/folder/*.csv') ['mybucket/folder/a.csv'] # why without gs:// ??? >>> fs.gl..."*

#### 75. [FileNotFoundError when using pandas df.to_excel](https://github.com/fsspec/gcsfs/issues/201) (#201)
- **URL:** https://github.com/fsspec/gcsfs/issues/201
- **Relevance Score:** `5` | **State:** `open` | **Author:** `mosqueteiro`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Similar to #184 When trying to write an excel file with pandas to a cloud bucket I get these errors: ```python df.to_excel('gs://bucket_name/path/to/data/test_excel.xlsx') ... FileNotFoundError: [Errno 2] No such file or directory: 'gs://bucket_name/path/to/data/test_excel.xlsx' ... FileCreateError:..."*

#### 76. [Unsuccessful recovery from ConnectionError ](https://github.com/fsspec/gcsfs/issues/61) (#61)
- **URL:** https://github.com/fsspec/gcsfs/issues/61
- **Relevance Score:** `5` | **State:** `open` | **Author:** `jhamman`
- **Labels:** None
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I'm trying to push a large-ish dataset to GCS via xarray/dask/zarr/gcsfs. Things are generally working during the setup and for the first part of the upload. However, after a bit, I'm getting a `ConnectionError` that is not recoverable. I'm pushing from a server at the University of Washington to bu..."*

### [fsspec/filesystem_spec](https://github.com/fsspec/filesystem_spec) (153 issues)

#### 77. [Block Cache requests the data twice for reads greater than 160MB](https://github.com/fsspec/filesystem_spec/issues/1960) (#1960)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1960
- **Relevance Score:** `27` | **State:** `open` | **Author:** `googlyrahman`
- **Labels:** None
- **FS Keywords:** `blockcache`, `cache_type`, `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`
- **Perf Keywords:** `block_size`, `cache`, `caching`, `io`, `oom`
- **Excerpt:** *"The code for block cache is located [here](https://github.com/fsspec/filesystem_spec/blob/master/fsspec/caching.py#L331) The relevant code pulled from the above file ``` def _fetch(self, start: int | None, end: int | None) -> bytes: .... # these are cached, so safe to do multiple calls for the same ..."*

#### 78. [2024.10.0: pytest fails in fsspec/implementations/tests/test_ftp.py units](https://github.com/fsspec/filesystem_spec/issues/1730) (#1730)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1730
- **Relevance Score:** `23` | **State:** `open` | **Author:** `kloczek`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `pyarrow.fs`, `s3fs`
- **Perf Keywords:** `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"I'm packaging your module as an rpm package so I'm using the typical PEP517 based build, install and test cycle used on building packages from non-root account. - `python3 -sBm build -w --no-isolation` - because I'm calling `build` with `--no-isolation` I'm using during all processes only locally in..."*

#### 79. [BytesCache use of .fetcher might lead to a stall if original coroutine stalls?](https://github.com/fsspec/filesystem_spec/issues/1666) (#1666)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1666
- **Relevance Score:** `23` | **State:** `open` | **Author:** `yarikoptic`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `block_size`, `cache`, `caching`, `hang`, `io`, `stall`, `timeout`
- **Excerpt:** *"We have an issue - https://github.com/dandi/dandi-cli/issues/1450 that one of our tests once in a while hangs (well, times out at 300 sec), but typically succeeds ok. <details><summary>the "fuller" traceback is </summary> ``` dandi/pynwb_utils.py:206: in _get_pynwb_metadata with open_readable(path) ..."*

#### 80. [2023.12.0: pytest fails in units which are using `libarchive` module](https://github.com/fsspec/filesystem_spec/issues/1470) (#1470)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1470
- **Relevance Score:** `23` | **State:** `open` | **Author:** `kloczek`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `pyarrow.fs`, `s3fs`
- **Perf Keywords:** `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"I'm packaging your module as an rpm package so I'm using the typical PEP517 based build, install and test cycle used on building packages from non-root account. - `python3 -sBm build -w --no-isolation` - because I'm calling `build` with `--no-isolation` I'm using during all processes only locally in..."*

#### 81. [Unexpected Local Data Transfer During xarray Preprocessing on Dask Cluster](https://github.com/fsspec/filesystem_spec/issues/1890) (#1890)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1890
- **Relevance Score:** `21` | **State:** `open` | **Author:** `lbesnard`
- **Labels:** None
- **FS Keywords:** `cache_type`, `filesystem`, `fsspec`, `readahead`, `s3filesystem`, `s3fs`
- **Perf Keywords:** `cache`, `io`, `speed`
- **Excerpt:** *"## TL;DR When running a script on a remote Dask cluster (e.g., via Coiled), memory on the local machine (which starts the cluster) is unexpectedly used. This happens I think after opening NetCDF files from S3 via ```s3fs``` with ```xarray.open_mfdataset``` and applying a preprocess function — even t..."*

#### 82. [How to properly close (SSH) file systems?](https://github.com/fsspec/filesystem_spec/issues/1682) (#1682)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1682
- **Relevance Score:** `19` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `timeout`
- **Excerpt:** *"I did open an SSH file system and used it successfully: ```python3 o = fsspec.open("ssh://user@127.0.0.1") o.fs.listdir("/") ``` Then, I lost the SSH connection because I lost WLAN connectivity because I entered suspend mode on my notebook. After that, I got this error on `o.fs.listdir`: ```python3 ..."*

#### 83. [Using blockcache with local breaks, because the `LocalFileOpener.closed` property doesn't have a setter](https://github.com/fsspec/filesystem_spec/issues/1456) (#1456)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1456
- **Relevance Score:** `19` | **State:** `open` | **Author:** `tonnydourado`
- **Labels:** None
- **FS Keywords:** `abfs`, `abstractfilesystem`, `blockcache`, `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `caching`, `io`
- **Excerpt:** *"Trying to use the `blockcache` filesystem with a `local` filesystem as a target raises an error if you try to close a file manually. Here's a reproduction: ```python from tempfile import TemporaryDirectory from fsspec import AbstractFileSystem, filesystem local: AbstractFileSystem = filesystem("loca..."*

#### 84. [FTPFileSystem open file cannot read from filezilla server](https://github.com/fsspec/filesystem_spec/issues/1417) (#1417)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1417
- **Relevance Score:** `19` | **State:** `open` | **Author:** `zzl221000`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `timeout`
- **Excerpt:** *"The ABOR command is sent when the ftp file download is finished, the server no longer responds and raises the TimeoutError code: ```python def test1(): fs: FTPFileSystem = fsspec.filesystem('ftp', asynchronous=True, host='127.0.0.1', port=21, username='admin', password='admin', timeout=10) with fs.o..."*

#### 85. [Proposal to change implementation of globbing for possible performance increase ](https://github.com/fsspec/filesystem_spec/issues/1355) (#1355)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1355
- **Relevance Score:** `19` | **State:** `open` | **Author:** `tfelbr`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`
- **Perf Keywords:** `hang`, `io`, `performance`, `slow`, `speed`
- **Excerpt:** *"Hello, I am using the build-in SFTP implementation to access an SFTP server. Unfortunately, this server is pretty slow, so I used globbing with the hope it will speed up things. The files on this server are ordered in different subdirectories. Only files in all subdirs that start with an "A" are rel..."*

#### 86. ['pyarrow._hdfs.HadoopFileSystem' object has no attribute 'host'](https://github.com/fsspec/filesystem_spec/issues/1870) (#1870)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1870
- **Relevance Score:** `16` | **State:** `open` | **Author:** `marberi`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"I tried connecting to a HDFS storage, through the default configuation (core-site.xml). Connecting, plus writing and reading a dataframe worked find (not shown). However, when attempting to run the code: """ import dask.array as da N = 10_000 rng = da.random.default_rng() x = rng.random((N, N), chun..."*

#### 87. [GCSFilesystem creation is surprisingly slow](https://github.com/fsspec/filesystem_spec/issues/1768) (#1768)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1768
- **Relevance Score:** `16` | **State:** `open` | **Author:** `d-v-b`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`, `url_to_fs`
- **Perf Keywords:** `io`, `slow`
- **Excerpt:** *"this snippet takes ~24s to run on my laptop in Germany: ```python # /// script # requires-python = ">=3.11" # dependencies = [ # "fsspec", # "gcsfs", # ] # /// from fsspec import url_to_fs from time import time url = 'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3' if __name__ ..."*

#### 88. [Passing callbacks to get_file calls used by CacheFileSystems](https://github.com/fsspec/filesystem_spec/issues/1623) (#1623)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1623
- **Relevance Score:** `16` | **State:** `open` | **Author:** `NickGeneva`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `block_size`, `cache`, `caching`, `io`
- **Excerpt:** *"Hi Fsspec experts, I'm presently using Fsspec with one of the built in caching file systems, `WholeFileCacheFileSystem`, and enjoy using the callback feature that is present in functions like `.get()` to communicate to users the download progress of getting files from remote file stores. I am dealin..."*

#### 89. [GenericFileSystem Buffered Copy](https://github.com/fsspec/filesystem_spec/issues/1578) (#1578)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1578
- **Relevance Score:** `16` | **State:** `open` | **Author:** `ryaminal`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfilesystem`, `gcsfs`, `url_to_fs`
- **Perf Keywords:** `io`, `performance`
- **Excerpt:** *"Hi all. Love fsspec. I'm trying to use GenericFileSystem like this: ```python import fsspec import fsspec.generic fs = fsspec.url_to_fs("sftp://username@host")[0] fsspec.generic.rsync( "sftp:///stuff", # only the path necessary here. the username and host and stuff is discarded. just the protocol an..."*

#### 90. [Adaptive Prefetcher on top of different cache-types](https://github.com/fsspec/filesystem_spec/issues/2090) (#2090)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/2090
- **Relevance Score:** `15` | **State:** `open` | **Author:** `raj-prince`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`
- **Perf Keywords:** `cache`, `hang`, `prefetch`
- **Excerpt:** *"Hi @martindurant, Creating this issues to take an alignment before making any changes to move [prefetcher](https://github.com/fsspec/gcsfs/blob/main/gcsfs/prefetcher.py) logic (from gcsfs) to filesystem_spec repo: 1. Do you want to keep prefetcher as a new cache-type or want to keep over the existin..."*

#### 91. [HTTPFileSystem isdir downloads the whole file](https://github.com/fsspec/filesystem_spec/issues/1707) (#1707)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1707
- **Relevance Score:** `15` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`, `speed`
- **Excerpt:** *"I need to implement the FUSE getattr (stat) callback. I.e., I need to get at least the file type and size, and possibly name for a given path. I am failing to do this with the HTTP filesystem implementation because: - `info(path)` always returns the file information for the HTML file, i.e., the file..."*

#### 92. [HTTPFileSystem breaks when range requests are not supported](https://github.com/fsspec/filesystem_spec/issues/1626) (#1626)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1626
- **Relevance Score:** `15` | **State:** `open` | **Author:** `dholth`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `url_to_fs`
- **Perf Keywords:** `cache`, `io`, `range request`
- **Excerpt:** *"``` from fsspec.core import url_to_fs ufs, url = url_to_fs("https://example.org/") f = ufs.open("https://example.org/no-range-requests/data.txt") f.seek(8192) f.read(1) ``` Will raise `# ValueError: The HTTP server doesn't appear to support range requests.` I was having trouble with cache options, b..."*

#### 93. [Custom Caching Filesystem does not work with a url string](https://github.com/fsspec/filesystem_spec/issues/1609) (#1609)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1609
- **Relevance Score:** `15` | **State:** `open` | **Author:** `mpiannucci`
- **Labels:** None
- **FS Keywords:** `blockcache`, `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `caching`, `io`
- **Excerpt:** *"I am creating a custom [redis caching filesystem](https://github.com/mpiannucci/redis-fsspec-cache) and I found that opening a file with a custom string does not work because of this hardcoded sequence https://github.com/fsspec/filesystem_spec/blob/0bb3f26c412d7ad9b2d52a5c32265014709d1c1f/fsspec/cor..."*

#### 94. [Getting a generator or iterator instead of lists of OpenFile objects or addresses.](https://github.com/fsspec/filesystem_spec/issues/1882) (#1882)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1882
- **Relevance Score:** `13` | **State:** `open` | **Author:** `MalteEbner`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `gcsfs`, `open_files`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Functions like `fsspec.open_files` or `FileSystem.ls` return list-like objects when run on directories or with glob patterns. This has two main drawbacks: - The functions only return once the entire directory has been listed. When listing cloud buckets with millions of entries, this can take many mi..."*

#### 95. [inconsistent path parsing from url_to_fs](https://github.com/fsspec/filesystem_spec/issues/1722) (#1722)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1722
- **Relevance Score:** `13` | **State:** `open` | **Author:** `jhamman`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3filesystem`, `s3fs`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"`fsspec.url_to_fs` seems to be inconsistently parsing the path from urls. ```python import fsspec print(fsspec.url_to_fs("s3://icechunk-test/ryan")) print(fsspec.url_to_fs("http://earthmover.io/joe")) (<s3fs.core.S3FileSystem object at 0x1334187a0>, 'icechunk-test/ryan') (<fsspec.implementations.htt..."*

#### 96. [Incosistency with async mode when using wrapper filesystems (e.g. dir and cache)](https://github.com/fsspec/filesystem_spec/issues/1709) (#1709)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1709
- **Relevance Score:** `13` | **State:** `open` | **Author:** `orenl`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `caching`, `io`
- **Excerpt:** *"The documentation says: > The class attribute `async_impl` can be used to test whether an implementation is async of not. DirFileSystem inherits from AsyncFileSystem, so it sets `async_impl = True`. As a wrapper filesystem it requires to match the sync/async operation mode to that of the underlying ..."*

#### 97. [Context not preserved when open file with compression, leading exception to be ignored](https://github.com/fsspec/filesystem_spec/issues/1672) (#1672)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1672
- **Relevance Score:** `13` | **State:** `open` | **Author:** `heiseish`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `block_size`, `cache`, `io`
- **Excerpt:** *"## Context - When providing the `compression` parameter to `fsspec.open`, the underlying Filesystem object is not properly cleaned up (even with context). - This causes any errors related to the Filesystem object cleanup to be suppressed and show up during garbage collection instead. ## Details ### ..."*

#### 98. [Pickle writing fails with `simplecache::` using xrootd paths (maybe with other remote paths as well).](https://github.com/fsspec/filesystem_spec/issues/1671) (#1671)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1671
- **Relevance Score:** `13` | **State:** `open` | **Author:** `ikrommyd`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`, `timeout`
- **Excerpt:** *"Something like this to reproduce: ```python import pickle import fsspec with fsspec.open("simplecache::root://cmseos.fnal.gov//store/user/ikrommyd/dummy/dummy.pkl", "wb") as f: d = {"1": 1, "2": 2} pickle.dump(d, f) ``` fails with: ``` ----------------------------------------------------------------..."*

#### 99. [Transaction doesn't work well with compression](https://github.com/fsspec/filesystem_spec/issues/1584) (#1584)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1584
- **Relevance Score:** `13` | **State:** `open` | **Author:** `roosephu`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `hanging`, `io`
- **Excerpt:** *"Here is the code to reproduce (fsspec version 2024.3.1): ```python import fsspec fs = fsspec.filesystem('local') with fs.transaction: with fs.open('/tmp/a.txt.gz', 'wt', compression='infer') as f: f.write('Hello, world!\n') ``` Here is the error: ``` Traceback (most recent call last): File "/tmp/a.p..."*

#### 100. [HTTPFilesystem has a race condition on data size between the open and read calls, if content changes at server between the 2 calls](https://github.com/fsspec/filesystem_spec/issues/1541) (#1541)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1541
- **Relevance Score:** `13` | **State:** `open` | **Author:** `masariello`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `hanging`, `io`
- **Excerpt:** *"The following script reproduces the issues The script spins up an http server that makes the json content 1 chat longer every 1s. Then the client bit hits the url with a 1s `sleep` between the `open` and `read` calls. The json parsing immediately fails because the terminating `{` gets chopped. For g..."*

#### 101. [HTTPFileSystem prints tracebacks if skip_instance_cache=True if called more than once](https://github.com/fsspec/filesystem_spec/issues/1506) (#1506)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1506
- **Relevance Score:** `13` | **State:** `open` | **Author:** `f4hy`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`, `timeout`
- **Excerpt:** *"I have been debugging an issue for a while and finally have a small reproducible snip. Using `fsspec==2023.12.2` ```python import fsspec some_public_url = "http://replace.me.with.a.public.url" def read_my_data(url: str) -> None: for i in range(10): fs = fsspec.filesystem("http", skip_instance_cache=..."*

#### 102. [Reading data from `raw.githubusercontent.com` hangs](https://github.com/fsspec/filesystem_spec/issues/1471) (#1471)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1471
- **Relevance Score:** `13` | **State:** `open` | **Author:** `nenb`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`, `timeout`
- **Excerpt:** *"## What When using the GitHub `fsspec` implementation, an attempt to `open(...)` data at `raw.githubusercontent.com` hangs indefinitely on my local machine. ## Why My DNS server returns both IPv4 and IPv6 addresses for `raw.githubusercontent.com`: ```bash > nslookup raw.githubusercontent.com <IP_OF_..."*

#### 103. [concurrent.futures.ProcessPoolExecutor fails for HTTPFileSystem](https://github.com/fsspec/filesystem_spec/issues/1298) (#1298)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1298
- **Relevance Score:** `13` | **State:** `open` | **Author:** `bendichter`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `concurrent`, `io`, `stall`
- **Excerpt:** *"@CodyCBakerPhD and I have been exploring different ways of parallelizing with http fsspec. We have found that you can use multiple processes in joblib (1), and parallelizing over threads using `concurrent.futures.ThreadPoolExecutor` works (2), but `concurrent.futures.ProcessPoolExecutor` stalls. ## ..."*

#### 104. [Intermittent deadlock when reading file with gcsfs](https://github.com/fsspec/filesystem_spec/issues/1136) (#1136)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1136
- **Relevance Score:** `13` | **State:** `open` | **Author:** `bnaul`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `hang`, `io`, `timeout`
- **Excerpt:** *"Not sure whether to post here or under gcsfs but seemed potentially related to #565: when reading a bunch of Parquet files with Dask (`distributed` scheduler), we occasionally (say one in ten thousand, or maybe one hundred thousand?) get a worker that deadlocks at the following: ``` ... File "/usr/l..."*

#### 105. [`async_wrapper` protocol yields `ModuleNotFoundError`](https://github.com/fsspec/filesystem_spec/issues/1822) (#1822)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1822
- **Relevance Score:** `12` | **State:** `open` | **Author:** `nils3er`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `url_to_fs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Trying to use the `async_wrapper` with `url_to_fs` to build an asynchronouos filesystem like: ```python fsspec.url_to_fs("async_wrapper://simplecache://https://www.foo.de") ``` It gives me a `ModuleNotFoundError`: ``` Traceback (most recent call last): File "/home/nils/projects/filesystem_spec/fsspe..."*

#### 106. [Seeking on Async FS is bugged / not-working](https://github.com/fsspec/filesystem_spec/issues/1772) (#1772)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1772
- **Relevance Score:** `12` | **State:** `open` | **Author:** `bluecoconut`
- **Labels:** None
- **FS Keywords:** `cache_type`, `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Here's a minimal example: ```python import fsspec import asyncio async def async_version(): print("Async Version") fs = fsspec.filesystem("http", asynchronous=True) session = await fs.set_session() file = await fs.open_async("https://example.com/") print("Starting Tell", file.tell(), "seeking to 20"..."*

#### 107. [DirFileSystem.ls(path, detail=True) hits AssertionError with S3FileSystem](https://github.com/fsspec/filesystem_spec/issues/1638) (#1638)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1638
- **Relevance Score:** `12` | **State:** `open` | **Author:** `metadaddy`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3filesystem`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"This is a similar issue to #924. **Code** ```python fs = DirFileSystem(f'/{bucket_name}', S3FileSystem()) files = fs.ls('/') ``` **Error** ```text Traceback (most recent call last): File "/Users/ppatterson/src/b2_zip_files/app.py", line 40, in <module> files = fs.ls('/') ^^^^^^^^^^ File "/Users/ppat..."*

#### 108. [DirFileSystem not forwarding 'local_file'](https://github.com/fsspec/filesystem_spec/issues/1110) (#1110)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1110
- **Relevance Score:** `12` | **State:** `open` | **Author:** `jdonnerstag`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `mmap`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"My use case: I'm using the following snippet to create a virtual filesystem, and create an OpenFile handle. Important to me is that I have a common base class/interface (OpenFile) to pass on to my "business logic" because I've extended it already with types. `fs.open()` is returning different things..."*

#### 109. [Some implementations don't have same function signatures as base class](https://github.com/fsspec/filesystem_spec/issues/1100) (#1100)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1100
- **Relevance Score:** `12` | **State:** `open` | **Author:** `leoleoasd`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"Hi, I noticed some implementations change the default value of some parameters, for example: `AbstractFilesystem` have `detail=True` in `ls`, however `LocalFileSystem` have `detail=False`. (https://github.com/fsspec/filesystem_spec/blob/master/fsspec/spec.py#L301, https://github.com/fsspec/filesyste..."*

#### 110. [LocalFileSystem does not work with CachingFileSystem](https://github.com/fsspec/filesystem_spec/issues/1618) (#1618)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1618
- **Relevance Score:** `11` | **State:** `open` | **Author:** `Alessi42`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `cache`, `caching`, `io`
- **Excerpt:** *"I am attempting to use the block wise cache to read from networked drive however I am finding that the cache does not store any blocks. I believe this is due to the fact that LocalFileOpener does not inherit from AbstractBufferedFile but io.IOBase I have experimented by modifying LocalFileOpener to ..."*

#### 111. [ArrowFSWrapper should not use "/" root_marker for all filesystems](https://github.com/fsspec/filesystem_spec/issues/1464) (#1464)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1464
- **Relevance Score:** `11` | **State:** `open` | **Author:** `b-phi`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `pyarrow.fs`, `s3filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"For the arrow S3FileSystem for example, using `root_market = "/"` throws an error when trying to upload a local file. Love the arrow integration, please let me know if I'm misusing something here. ```python from pyarrow.fs import S3FileSystem from fsspec.implementations.arrow import ArrowFSWrapper f..."*

#### 112. [Recover full name for `OpenFile` objects](https://github.com/fsspec/filesystem_spec/issues/1459) (#1459)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1459
- **Relevance Score:** `11` | **State:** `open` | **Author:** `lobis`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `open_files`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Currently `fsspec.core.OpenFile` objects have a property called `full_name` which I think should return the full file name i.e. the protocol + local path. I think it would be nice that user should be able to pass this property to `fsspec.core.url_to_fs` and produce the same filesystem and local path..."*

#### 113. [AbstractFileSystem is not abstract](https://github.com/fsspec/filesystem_spec/issues/1446) (#1446)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1446
- **Relevance Score:** `11` | **State:** `open` | **Author:** `TomNicholas`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`, `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"I'm trying to learn more about how fsspec works (so I can better understand the IO part of the Pangeo stack), but I'm confused by the structure of `fsspec/filesystem_spec`. Despite the name, it seems `AbstractFileSystem` is not an abstract base class (nor is `AbstractBufferedFile`) - I'm able to imp..."*

#### 114. [S3 URL containing versionId is misinterpreted as glob pattern](https://github.com/fsspec/filesystem_spec/issues/1439) (#1439)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1439
- **Relevance Score:** `11` | **State:** `open` | **Author:** `mdwint`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3filesystem`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I am trying to load a specific version of an S3 object into a Dask dataframe as follows: ```python >>> import dask.dataframe as dd >>> dd.read_parquet("s3://example-bucket/dataset/part.0.parquet?versionId=se654wJoRQcirhKoHRkN4hsFmhNwMg27") ``` This example returns an empty DataFrame, even though the..."*

#### 115. [Glue 1.0 pythonshell job with Python 3.6 with awswrangler is failing with - "ModuleNotFoundError: No module named 'importlib.metadata'"](https://github.com/fsspec/filesystem_spec/issues/1207) (#1207)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1207
- **Relevance Score:** `11` | **State:** `open` | **Author:** `rsingh-821`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"awswrnagler installed latest version for fsspec - ![image](https://user-images.githubusercontent.com/102376854/223785273-8b4a6222-70aa-461d-b0ed-3a4a45b6ff06.png) error - ![image](https://user-images.githubusercontent.com/102376854/223785186-ceef5532-d8f1-4eaa-a480-9140b1788c98.png)"*

#### 116. [Use mv_file instead of copy + rm to implement mv](https://github.com/fsspec/filesystem_spec/issues/2017) (#2017)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/2017
- **Relevance Score:** `10` | **State:** `open` | **Author:** `Yonghui-Lee`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `io`, `performance`
- **Excerpt:** *"As discussed in https://github.com/fsspec/gcsfs/pull/800#discussion_r3041091240, we can consider using mv_file to implement mv method. We might see performance gains if some fsspec implementations include atomic mv_file like we see in case of GCSFS."*

#### 117. [Using smb safely in multiuser environments](https://github.com/fsspec/filesystem_spec/issues/2006) (#2006)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/2006
- **Relevance Score:** `10` | **State:** `open` | **Author:** `bernt-matthias`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"I was considering to [implement access to smb for the Galaxy project](https://github.com/galaxyproject/galaxy/pull/22274) where we use fsspec a lot. Galaxy is a multi user environment where we would safely store the information needed to access a smb share (server, port, username, password, path ......"*

#### 118. [Change the default value for replication factor in HadoopFileSystem](https://github.com/fsspec/filesystem_spec/issues/1868) (#1868)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1868
- **Relevance Score:** `10` | **State:** `open` | **Author:** `kopczynski-9livesdata`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"Hey there! The current implementation of `HadoopFileSystem` assumes replication 3 by default. The code I'm referring to is here: https://github.com/fsspec/filesystem_spec/blob/8463a6a587f722f279e987b3e8508f2c9bba50d2/fsspec/implementations/arrow.py#L257 It would be better, IMO, to just use this para..."*

#### 119. [[feature request] More global porcelain methods like `fsspec.listdir(...)` for basic usecases](https://github.com/fsspec/filesystem_spec/issues/1860) (#1860)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1860
- **Relevance Score:** `10` | **State:** `open` | **Author:** `vadimkantorov`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Currently the user must instantiate a filesystem object manually (and thus know the filesystem name) to do analogue of `os.listdir(...)`. It would be nice to have more methods like existing `fsspec.open(...)` mimicking Python's core `open(...)`. E.g. methods with similar invokation API as `os.listdi..."*

#### 120. [Docs updates aren't being built automatically](https://github.com/fsspec/filesystem_spec/issues/1846) (#1846)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1846
- **Relevance Score:** `10` | **State:** `open` | **Author:** `danyeaw`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"I noticed that documentation updates aren't being built automatically, for example the updates to the changelog are in the repo here: https://github.com/fsspec/filesystem_spec/blob/master/docs/source/changelog.rst but not in the latest RTD build here: https://filesystem-spec.readthedocs.io/en/latest..."*

#### 121. [Protocol of URI without authority not correctly idenfied](https://github.com/fsspec/filesystem_spec/issues/1811) (#1811)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1811
- **Relevance Score:** `10` | **State:** `open` | **Author:** `observingClouds`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"I am currently developing a fsspec driver for a filesystem protocol that does not need/have an authority, such that: ``` URI = protocol ":" path ``` is a valid URI. However, fsspec's `split_protocol` function seems to assume that an authority is always given, i.e.: ``` URI = protocol ":" "//" author..."*

#### 122. [Listing Index in Tarfiles](https://github.com/fsspec/filesystem_spec/issues/1808) (#1808)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1808
- **Relevance Score:** `10` | **State:** `open` | **Author:** `pgierz`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Hi there, I'm trying to write some examples for our users using `fsspec` so they can incorporate it into their own scripts. Only some of our users are proficient in Python, so these examples need to be super verbose and simple. Our use case is climate model simulation and archiving on a tape system...."*

#### 123. [`LocalFileSystem.ls()` with `details=False` slow](https://github.com/fsspec/filesystem_spec/issues/1788) (#1788)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1788
- **Relevance Score:** `10` | **State:** `open` | **Author:** `FrankEssenberger`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`, `slow`
- **Excerpt:** *"Hi fsspec developers, I realized when using a later version of fsspec than the ones from 2023 that the `.ls()` was super slow. The reason came in in this issue PR: #1479 where always the `info` is taken for all files ![Image](https://github.com/user-attachments/assets/dd721727-e71d-468a-aa6d-de4efb8..."*

#### 124. [fsspec URIs with '+' instead of '::'](https://github.com/fsspec/filesystem_spec/issues/1752) (#1752)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1752
- **Relevance Score:** `10` | **State:** `open` | **Author:** `hhoeflin`
- **Labels:** None
- **FS Keywords:** `fsspec`, `s3fs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Hi, I wanted to ask about the fsspec convention of using '::' to chain URL handling protocols (e.g. simplecache with s3fs). Using '::' means the resulting string is not a URI (e.g. 'simplecache::s3fs://bucket_name/myfile') as the 'simplecache::s3fs' violates https://datatracker.ietf.org/doc/html/rfc..."*

#### 125. [Keyboard interrupt does not work properly with ipython and TqdmCallback](https://github.com/fsspec/filesystem_spec/issues/1667) (#1667)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1667
- **Relevance Score:** `10` | **State:** `open` | **Author:** `malmans2`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"Hi there, It looks like keyboard interrupt in ipython does not work properly when downloading files using TqdmCallback. I noticed it while downloading a ~1GB file: ```python URL = ... import fsspec fs = fsspec.filesystem("http", asynchronous=False) fs.get_file(URL, "test-file", callback=fsspec.callb..."*

#### 126. [fsspec.fuse ready_file does not work](https://github.com/fsspec/filesystem_spec/issues/1587) (#1587)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1587
- **Relevance Score:** `10` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Create test file: ```bash echo bar > foo tar -cf foo{.tar,} ``` Mount: ```python3 from fsspec.implementations.tar import TarFileSystem as tafs fs = tafs("foo.tar") import fsspec.fuse fsspec.fuse.run(fs, "./", "mounted", ready_file=True) ``` Calling `stat` and `cat` on `mounted/.fuse_ready` will resu..."*

#### 127. [indicate read-only / immutable filesystems](https://github.com/fsspec/filesystem_spec/issues/1511) (#1511)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1511
- **Relevance Score:** `10` | **State:** `open` | **Author:** `efiop`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"These are some early thoughts, but I just wanted to share in case anyone else will find this useful or will have any thoughts/comments. Some fsspec filesystems might raise `EROFS` error if you try to actively write something to them, but it would be nice to indicate that for the whole filesystem wit..."*

#### 128. [HTTP implementaion not comaptible with Azure BlobStorage](https://github.com/fsspec/filesystem_spec/issues/1390) (#1390)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1390
- **Relevance Score:** `10` | **State:** `open` | **Author:** `honkomonk`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"What I wanted to do: Read and write to an Azure BlobStorage via pre-signed URLs using the fsspec http implementation. How I tried to do it: As fsspec does not support write mode for http directly, I used it im combination with a local file cache, as suggested in #1325 and it nearly worked. For testi..."*

#### 129. [AbstractFileSystem.exists() catches every exception](https://github.com/fsspec/filesystem_spec/issues/1379) (#1379)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1379
- **Relevance Score:** `10` | **State:** `open` | **Author:** `tfelbr`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"Hello, I would like to kindly request a change in the implementation of `AbstractFileSystem.exists()`, as it currently catches every exception that might get thrown without any notice. An in my opinion better approach would be something like this: ```py def exists(self, path, **kwargs): try: self.in..."*

#### 130. [Inconsistencies: `ls` may have `detail=True` or `detail=False`](https://github.com/fsspec/filesystem_spec/issues/1205) (#1205)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1205
- **Relevance Score:** `10` | **State:** `open` | **Author:** `lhoestq`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"I saw the `AbstractArchiveFileSystem` switched to `detail=True` in https://github.com/fsspec/filesystem_spec/commit/0f3ecd8e629043646ab19b1a2b00d895f0553a81. There are some inconstencies with other filesystems which have `detail=False` (e.g. the local filesystem). with `fsspec==2023.3.0` Currently: ..."*

#### 131. [Copying files between filesystems via GenericFileSystem broken for filesystems requiring init parameters](https://github.com/fsspec/filesystem_spec/issues/1167) (#1167)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1167
- **Relevance Score:** `10` | **State:** `open` | **Author:** `Metamess`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"In our project, we use the GenericFileSystem's [`_cp_file`](https://github.com/fsspec/filesystem_spec/blob/012816bb142de1e507423b81dc3b2c925d4424c3/fsspec/generic.py#L254) function to (asynchronously) copy files from a remote SSH filesystem to our local filesystem (as suggested in [this comment](htt..."*

#### 132. [Unable to use "simplecache" to write NETCDF to Open Storage Network S3 storage](https://github.com/fsspec/filesystem_spec/issues/1131) (#1131)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1131
- **Relevance Score:** `10` | **State:** `open` | **Author:** `alaws-USGS`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"Hello, I'm running into a bug where I am unable to write NETCDF files to permissioned storage on Open Storage Network without having to explicitly create a local copy and then use `put`. The code is being run in parallel using Dask and Xarray on a kubernetes cluster. I've used the code snippet below..."*

#### 133. [Feature Request: single environment variable config for protocol](https://github.com/fsspec/filesystem_spec/issues/1130) (#1130)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1130
- **Relevance Score:** `10` | **State:** `open` | **Author:** `mauvilsa`
- **Labels:** None
- **FS Keywords:** `fsspec`, `s3fs`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"Currently it is possible to provide overrides with environment variables of the style `FSSPEC_{protocol}_{kwargname}=value`. However, this is limited since it is not possible to provide a dict value. One example where this is needed is s3 with a custom `endpoint_url`, see https://github.com/fsspec/s..."*

#### 134. [ssh filesystem and put_file are incompatible](https://github.com/fsspec/filesystem_spec/issues/1071) (#1071)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1071
- **Relevance Score:** `10` | **State:** `open` | **Author:** `ghislainp`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"Using a ssh filesystem and put_files gives an error ```python import fsspec import sshfs fs = fsspec.filesystem("ssh", host='xx.xx.xx.xx', username='eouser') fs.put_file(lpath="t", rpath="/home/me/t") ``` I receive an exception: ``` File "/home/me/miniconda3/envs/olci/lib/python3.9/site-packages/fss..."*

#### 135. [Copying between different filesystems with unrepresentable directory structure](https://github.com/fsspec/filesystem_spec/issues/1968) (#1968)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1968
- **Relevance Score:** `9` | **State:** `open` | **Author:** `ap--`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi @martindurant, In universal-pathlib a user reported an incomplete copy operation when copying between s3 and local. Turns out they are basically trying to copy the following structure to a local filesystem, which can't be represented. ``` s3://bucket/key # data stored in object under 'key' s3://b..."*

#### 136. [`AbstractFileSystem.rm()` doc ambiguous - files, directories, both?](https://github.com/fsspec/filesystem_spec/issues/1914) (#1914)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1914
- **Relevance Score:** `9` | **State:** `open` | **Author:** `keen85`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, I noticed that [`AbstractFileSystem.rm()` docs is a little bit imprecise here:](https://filesystem-spec.readthedocs.io/en/latest/api.html#fsspec.spec.AbstractFileSystem.rm) <img width="679" height="343" alt="Image" src="https://github.com/user-attachments/assets/06b0d8b7-6734-4e21-b9de-ddc63bc5f..."*

#### 137. [create multiple separate memory filesystems](https://github.com/fsspec/filesystem_spec/issues/1904) (#1904)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1904
- **Relevance Score:** `9` | **State:** `open` | **Author:** `milahu`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"[fsspec/implementations/memory.py](https://github.com/fsspec/filesystem_spec/blob/c46db870f828f7f1318ed7a3dc26ecc8b48b3880/fsspec/implementations/memory.py#L17) ```py class MemoryFileSystem(AbstractFileSystem): """A filesystem based on a dict of BytesIO objects This is a global filesystem so instanc..."*

#### 138. [Outfile is overridden by lpath unless lpath is not file-like, and it is always closed](https://github.com/fsspec/filesystem_spec/issues/1841) (#1841)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1841
- **Relevance Score:** `9` | **State:** `open` | **Author:** `chrisdonlan`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"## What was promised: I could call `AbstractFileSystem.get_file(..., outfile=<some-file-handler>)`, and it would override `lpath` or serve in place of `lpath`. ## What I found: I could only call `AbstractFileSystem.get_file(..., lpath=some/real/dir, outfile=fh, ...)` to get the desired functionality..."*

#### 139. [Why is `urlpath` passed as a list to `open_files` if it can be already a list?](https://github.com/fsspec/filesystem_spec/issues/1773) (#1773)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1773
- **Relevance Score:** `9` | **State:** `open` | **Author:** `wachsylon`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `open_files`
- **Perf Keywords:** `io`
- **Excerpt:** *"The `fsspec.open` command allows `urlpath` to be a list. But [a few lines later](https://github.com/fsspec/filesystem_spec/blob/30af5e1d1f201d8681faf0ca163c4c9509de69a3/fsspec/core.py#L492), urlpath is passed as a list. If it is already a list, it becomes a list of lists. I ran into problems with th..."*

#### 140. [Inconsistent behaviour of `get_file` using compression with different filesystems](https://github.com/fsspec/filesystem_spec/issues/1758) (#1758)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1758
- **Relevance Score:** `9` | **State:** `open` | **Author:** `mraspaud`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have problems getting consistent behaviours when using `get_file` for different filesystems when using the `compression` parameter. My understanding from the AbstractFilesystem implementation of that method is that kwargs should be used by the `open` method, but for some filesystems it fails silen..."*

#### 141. [error using fsspec and flask-socketio](https://github.com/fsspec/filesystem_spec/issues/1701) (#1701)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1701
- **Relevance Score:** `9` | **State:** `open` | **Author:** `rob-ashdown-monolith`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I am trying to incorporate calls to fsppec-based packages (adlfs, s3fs) into a (sync) flask view. Flask is running using flask-socketio, which is in turn using gevent. Whenever I try and call a filesystem method (e.g. `ls`), it raise the following error ```NotImplementedError: Calling sync() from wi..."*

#### 142. [fs.cat_files signature consistency](https://github.com/fsspec/filesystem_spec/issues/1600) (#1600)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1600
- **Relevance Score:** `9` | **State:** `open` | **Author:** `nsmith-`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"In debugging https://github.com/scikit-hep/uproot5/pull/1198 I found I was assuming all implementations `fs.cat_files` had the same signature. In fact they do not, ``` >>> help(fsspec.filesystem("s3").cat_file) Help on function _cat_file in module s3fs.core: _cat_file(path, version_id=None, start=No..."*

#### 143. [FSSpec's get_mapper and other functions can produce nameless files for S3 Filesystems](https://github.com/fsspec/filesystem_spec/issues/1554) (#1554)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1554
- **Relevance Score:** `9` | **State:** `open` | **Author:** `jaedoucette`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Observed Behavior: When `fsspec`'s S3FS's `get_mapper` function is called on an empty directory-like path in an S3 filesystem, it can produce a dictionary-like object that is non-empty, and includes the key `''` (i.e. the empty string), and can produce files that are in fact empty directories in..."*

#### 144. [Cannot use chained Zip-URL with ReferenceFileSystem](https://github.com/fsspec/filesystem_spec/issues/1455) (#1455)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1455
- **Relevance Score:** `9` | **State:** `open` | **Author:** `forman`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Note, this issue could also be caused by `xarray`. I have [kerchunked](https://fsspec.github.io/kerchunk/reference.html#kerchunk.hdf.SingleHdf5ToZarr) a large number of NetCDF4 files (located in S3) and put the reference JSONs into a single Zip archive. If I open a NetCDF as Zarr with xarray using a..."*

#### 145. [LocalFileSystem glob removes trailing slash](https://github.com/fsspec/filesystem_spec/issues/1322) (#1322)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1322
- **Relevance Score:** `9` | **State:** `open` | **Author:** `jlanglois-jam`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"According to the [documentation of AbstractFileSystem](https://github.com/fsspec/filesystem_spec/blob/master/fsspec/spec.py#L541:L542), `glob` should act as `ls` when the path ends with `/`. But when using the `LocalFileSystem` method, [the trailing slash is removed](https://github.com/fsspec/filesy..."*

#### 146. [IndexError: list index out of range when 400 HTTP errors](https://github.com/fsspec/filesystem_spec/issues/1265) (#1265)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1265
- **Relevance Score:** `9` | **State:** `open` | **Author:** `albertvillanova`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `open_files`
- **Perf Keywords:** `io`
- **Excerpt:** *"If we get a 400 HTTP error while trying to open a URL with: ```python fsspec.open(url) ``` this is not caught and instead an `IndexError` is raised: ``` IndexError: list index out of range ``` See for example: ``` File "/src/services/worker/.venv/lib/python3.9/site-packages/fsspec/core.py", line 419..."*

#### 147. [Can't access data from S3 Buckets](https://github.com/fsspec/filesystem_spec/issues/1195) (#1195)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1195
- **Relevance Score:** `9` | **State:** `open` | **Author:** `omertechverx`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"``` import fsspec s3_fs = fsspec.filesystem("s3", key="xxxxxx', secret="xxxxxxxxx", client_kwargs={ "region_name": 'xxxxxxx', }) s3_fs.ls('s3://') ``` It lists all the buckets but when i use `s3_fs.ls('s3://Bucket_name') ` It returns empty Same bucket can be accessed with boto3 and all the contents ..."*

#### 148. [ArrowFSWrapper._strip_protocol differs from pure fsspec implementation](https://github.com/fsspec/filesystem_spec/issues/1137) (#1137)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1137
- **Relevance Score:** `9` | **State:** `open` | **Author:** `rjzamora`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `pyarrow.fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Not sure if this is a "bug", but I ran into this discrepancy in https://github.com/dask/dask/pull/9699 for a local Windows filesystem, and needed to add an explicit workaround. Therefore, I'd like to establish what the "correct" behavior should be. **Reproducer:** ```python from fsspec.implementatio..."*

#### 149. [open_local not returning the file handle](https://github.com/fsspec/filesystem_spec/issues/1109) (#1109)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1109
- **Relevance Score:** `9` | **State:** `open` | **Author:** `jdonnerstag`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`, `open_files`
- **Perf Keywords:** `io`
- **Excerpt:** *"The [doc](https://filesystem-spec.readthedocs.io/en/latest/api.html#fsspec.open_local) for open_local says "Open file(s) which can be resolved to local". But looking at the [source-code](https://filesystem-spec.readthedocs.io/en/latest/_modules/fsspec/core.html#open_local) then it returns a local fi..."*

#### 150. [Fusepy, old libs](https://github.com/fsspec/filesystem_spec/issues/1759) (#1759)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1759
- **Relevance Score:** `8` | **State:** `open` | **Author:** `eamanu`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"Hi dear maintainer, Thanks for the work! This maybe is not a real bug/issue, but I put it on the table. In [#1085592](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1085592) was requested to remove python3-fusepy from Recommends, because fuse 2.x is obsolete. There's a PR in [fusepy](https://gith..."*

#### 151. [fsspec.asyn.sync shoud check the liveness of IO thread to avoid deadlocks](https://github.com/fsspec/filesystem_spec/issues/1723) (#1723)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1723
- **Relevance Score:** `8` | **State:** `open` | **Author:** `sugibuchi`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `timeout`
- **Excerpt:** *"`fsspec.asyn` creates and runs an event loop used by async file system implementations as the default event loop. However, this module does not explicitly close the event loop. As a result, when a Python interpreter enters the shutdown sequence, we experience a specific period during which the event..."*

#### 152. [fsspec.fuse -f is inverted and hangs when specified](https://github.com/fsspec/filesystem_spec/issues/1586) (#1586)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1586
- **Relevance Score:** `8` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"```bash echo bar > foo tar -cf foo{.tar,} python3 -m fsspec.fuse --version # 2024.3.1 python3 -m fsspec.fuse --help # -f, --foreground Running in foreground or not (Default: False) python3 -m fsspec.fuse local foo.tar mounted # Runs in the foreground contrary to the help message python3 -m fsspec.fu..."*

#### 153. [Add `get_protocols`, `strip_protocols`, and `is_fully_qualified` APIs](https://github.com/fsspec/filesystem_spec/issues/1461) (#1461)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1461
- **Relevance Score:** `8` | **State:** `open` | **Author:** `nicholasjng`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"I have a use case for the following APIs, and wanted to get opinions on whether they are feasible as additions: Firstly, ```py def get_protocols(url: str) -> tuple[str, ...]: """Returns all protocols found on a URL.""" -> get_protocols("my-bucket/a.txt") = () -> get_protocols("s3://my-bucket/a.txt")..."*

#### 154. [lost "seekable" parameter while load a zip file on HDFS](https://github.com/fsspec/filesystem_spec/issues/1189) (#1189)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1189
- **Relevance Score:** `8` | **State:** `open` | **Author:** `neiblegy`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"I'm using fsspec to load a zip file which store in HDFS, but encounter a problem ``` python3.9/fsspec/implementations/zip.py", line 54, in __init__ self.zip = zipfile.ZipFile(self.fo, mode=mode) File "python3.9/zipfile.py", line 1257, in __init__ self._RealGetContents() File "python3.9/zipfile.py", ..."*

#### 155. [Class-scoped fixture as instance method pytest deprecations](https://github.com/fsspec/filesystem_spec/issues/2059) (#2059)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/2059
- **Relevance Score:** `7` | **State:** `open` | **Author:** `smorken`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"some of the usages of test fixtures will be deprecated as of pytest version 9.1 and will break as of pytest version 10.0 for example: https://github.com/fsspec/filesystem_spec/blob/65d58d4346c235747b9c2166aa60c25a3031a590/fsspec/tests/abstract/__init__.py#L21 pytest deprecations: https://docs.pytest..."*

#### 156. [Rerecord cassettes/test_dbfs](https://github.com/fsspec/filesystem_spec/issues/1949) (#1949)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1949
- **Relevance Score:** `7` | **State:** `open` | **Author:** `hugovk`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi @mkoistinen, it looks like you were the last to rerecord the cassettes in https://github.com/fsspec/filesystem_spec/pull/1873. Please could you do it again? Re: https://github.com/fsspec/filesystem_spec/pull/1946#discussion_r2523676160 where the tests were previously being skipped for 3.10+, but ..."*

#### 157. [`HTTPFileSystem` reads an incorrect amount of data](https://github.com/fsspec/filesystem_spec/issues/1895) (#1895)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1895
- **Relevance Score:** `7` | **State:** `open` | **Author:** `bveeramani`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Here's a minimal-ish repro: ```python from fsspec.implementations.http import HTTPFileSystem remote_path = "https://huggingface.co/api/datasets/abisee/cnn_dailymail/parquet/3.0.0/train/0.parquet" expected_data_size = 256540614 filesystem = HTTPFileSystem() with filesystem.open(remote_path) as file: ..."*

#### 158. [Wrong behaviour of fs.get in "Directory to existing directory" case](https://github.com/fsspec/filesystem_spec/issues/1851) (#1851)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1851
- **Relevance Score:** `7` | **State:** `open` | **Author:** `nsundalov`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"**Problem**: fs.get copies source dir inside target dir but expected to copy content of source dir into target dir. [case 1e of the doc](https://filesystem-spec.readthedocs.io/en/latest/copying.html#copying-files-and-directories) Script to reproduce error: ```python import os from fsspec import file..."*

#### 159. [copy directory contains symbolic to subdir to directory twice bigger](https://github.com/fsspec/filesystem_spec/issues/1843) (#1843)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1843
- **Relevance Score:** `7` | **State:** `open` | **Author:** `pyfreyr`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"src dir: ``` data/2025-05-16 ├── sparse_embeddings -> model/sparse_embeddings └── model/sparse_embeddings/ ``` when use local fs to copy, the `sparse_embeddings` symbolic link will copy `model/sparse_embeddings` data duplicated. As a result, the `data/2025-05-16` directory will be twice bigger than ..."*

#### 160. [DirFileSystem does not propagate transaction context to underlying filesystem](https://github.com/fsspec/filesystem_spec/issues/1823) (#1823)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1823
- **Relevance Score:** `7` | **State:** `open` | **Author:** `patrickwolf`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"When wrapping a transactional file:// backend in DirFileSystem (e.g. filesystem("dir", …, fs=filesystem("file"))), entering with fs.transaction: on the dir:// wrapper sets only the wrapper’s _intrans flag. Because DirFileSystem never delegates its transaction context down to the wrapped LocalFileSys..."*

#### 161. [Positional Arguments Error](https://github.com/fsspec/filesystem_spec/issues/1819) (#1819)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1819
- **Relevance Score:** `7` | **State:** `open` | **Author:** `ruoyeruolan`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"- MacOS - python=3.12.4 - fsspec=2025.3.2 - torch-geometric=2.6.1 ```python dataset = TUDataset(root=root, name='ENZYMES') ``` Traceback (most recent call last): File "<stdin>", line 1, in <module> File "/Users/wakala/venvs/versions/3.12.4/torch/lib/python3.12/site-packages/torch_geometric/datasets/..."*

#### 162. [`fsspec/spec.py#L568` causes `AttributeError`](https://github.com/fsspec/filesystem_spec/issues/1813) (#1813)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1813
- **Relevance Score:** `7` | **State:** `open` | **Author:** `adi-dhulipala`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"## Bug stacktrace: Im on a macOS system. Here's a partial stacktrace screenshot of the error I ran into <img width="956" alt="Image" src="https://github.com/user-attachments/assets/82b7357c-1811-440f-9bd8-1e9243b44292" /> Everything else in stack trace is custom library code and truncated for brevit..."*

#### 163. [Don't type `protocol` as `ClassVar`](https://github.com/fsspec/filesystem_spec/issues/1800) (#1800)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1800
- **Relevance Score:** `7` | **State:** `open` | **Author:** `kylebarron`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Protocol is defined as a `ClassVar`: https://github.com/fsspec/filesystem_spec/blob/ffdfed146f070cd05bce78767fc9873d165c59fd/fsspec/spec.py#L109 This means that pylance gives me an error when I try to set it in a constructor: <img width="792" alt="Image" src="https://github.com/user-attachments/asse..."*

#### 164. [Use of '::' in file's name](https://github.com/fsspec/filesystem_spec/issues/1782) (#1782)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1782
- **Relevance Score:** `7` | **State:** `open` | **Author:** `maxgalli`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I am investigating [this issue](https://github.com/scikit-hep/uproot5/issues/1251) in uproot, where we try to open a file that contains ```::``` in the name of the file. As you can see, the expected behavior would be to correctly create the file indicated in the string, but it doesn't seem to be the..."*

#### 165. [Test failures with Zarr 3](https://github.com/fsspec/filesystem_spec/issues/1777) (#1777)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1777
- **Relevance Score:** `7` | **State:** `open` | **Author:** `QuLogic`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I've run a [test build with Zarr 3](https://copr.fedorainfracloud.org/coprs/qulogic/zarr3/build/8547554/) This update has caused some tests to fail due to some issue in `LazyReferenceMapper`: ```pytb ____________________ ERROR at setup of test_append_parquet _____________________ m = <fsspec.impleme..."*

#### 166. [Calling HTTPFileSystem.get on large files looks problematic](https://github.com/fsspec/filesystem_spec/issues/1766) (#1766)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1766
- **Relevance Score:** `7` | **State:** `open` | **Author:** `Koncopd`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The problem is that when `HTTPFileSystem.get is called`, it checks if it is a directory [here](https://github.com/fsspec/filesystem_spec/blob/90c7cd9e6c939fc37341fd793831a399753ebfd9/fsspec/asyn.py#L639), but to check that this is a directory, it downloads the whole body of the file [here](https://g..."*

#### 167. [Inconsistencies regarding quoting / escaping in URLs / paths](https://github.com/fsspec/filesystem_spec/issues/1713) (#1713)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1713
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I think that the interface regarding path inputs should be more consistent(ly defined). - While some file systems do accept simple paths such as `/` or `/folder`, others do not, e.g., for HTTPFileSystem, I have to specify the whole URL including the port again and again for each access, e.g., `resul..."*

#### 168. [Fails when`ArrowFile` is used](https://github.com/fsspec/filesystem_spec/issues/1711) (#1711)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1711
- **Relevance Score:** `7` | **State:** `open` | **Author:** `zsaladin`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"1. Variable [size](https://github.com/fsspec/filesystem_spec/blob/f2c7717bf87d3ad999afc2022660501cd19ab44b/fsspec/spec.py#L902) is set 2. But the `size` is [bound method](https://github.com/fsspec/filesystem_spec/blob/f2c7717bf87d3ad999afc2022660501cd19ab44b/fsspec/implementations/arrow.py#L223) whe..."*

#### 169. [File object opened via SSH is inconsistent with the file object API. Seek and write return nothing](https://github.com/fsspec/filesystem_spec/issues/1695) (#1695)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1695
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"This is kind of a duplicate of the [paramiko issue](https://github.com/paramiko/paramiko/issues/2452). But, I think it could also be fixed in fsspec. I'm not sure whether fsspec does define a standard for the file object. If not, maybe it should? I find it highly unexpected that for the file object:..."*

#### 170. [API for conditional / exclusive write](https://github.com/fsspec/filesystem_spec/issues/1693) (#1693)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1693
- **Relevance Score:** `7` | **State:** `open` | **Author:** `TomAugspurger`
- **Labels:** None
- **FS Keywords:** `gcsfs`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"Over in https://github.com/zarr-developers/zarr-python/pull/2262, we'd like to write a file but only if it doesn't already exist. On a local file system, this would be `open(path, mode="xb")`, which will fail with a `FileExistsError` if the file already exists. Now that S3 supports [conditional writ..."*

#### 171. [Return of info (FileInfo) is unspecified, need consistent way to detect get link information](https://github.com/fsspec/filesystem_spec/issues/1680) (#1680)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1680
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The [API specification](https://filesystem-spec.readthedocs.io/en/latest/_modules/fsspec/archive.html#AbstractArchiveFileSystem.ls) for `listdir` and by inference also `info` reads: > The specific keys, or perhaps a FileInfo class, or similar, is TBD, but must be consistent across implementations. M..."*

#### 172. [info returns something different than ls](https://github.com/fsspec/filesystem_spec/issues/1679) (#1679)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1679
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The [API specifications](https://filesystem-spec.readthedocs.io/en/latest/api.html#fsspec.archive.AbstractArchiveFileSystem) states: > Returns a single dictionary, with exactly the same information as ls would with detail=True. But, this does not hold true for this code: ```python3 import pprint o =..."*

#### 173. [[bug?] onerror vs on_error](https://github.com/fsspec/filesystem_spec/issues/1675) (#1675)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1675
- **Relevance Score:** `7` | **State:** `open` | **Author:** `AlbertDeFusco`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Question: should this call be `on_error="raise"`? `copy` is defined with `on_error` kwarg. https://github.com/fsspec/filesystem_spec/blob/76ca4a68885d572880ac6800f079738df562f02c/fsspec/spec.py#L1186-L1188"*

#### 174. [the glob() method does not follow symlinks](https://github.com/fsspec/filesystem_spec/issues/1674) (#1674)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1674
- **Relevance Score:** `7` | **State:** `open` | **Author:** `danol-px`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"This results in different behaviour vs other glob methods in e.g. glob or pathlib: ``` from fsspec.implementations.local import LocalFileSystem import glob fs = LocalFileSystem() fs.mkdir('original/target_dir') fs.mkdir('new') fs.touch('original/target_dir/example_file.txt') fs.symlink('original/tar..."*

#### 175. [Failed to read folder](https://github.com/fsspec/filesystem_spec/issues/1665) (#1665)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1665
- **Relevance Score:** `7` | **State:** `open` | **Author:** `FergusChen`
- **Labels:** None
- **FS Keywords:** `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I noticed a difference in fsspec's handling of folders containing parquet files: Call method:` pd.read_parquet ("s3://xxx/test_dir/")` Normally, if there is a parquet file under the test_dir, this method can read the contents of the parquet file normally. The problem is: If test_dir is a folder auto..."*

#### 176. [What filesystem to use with parquet files](https://github.com/fsspec/filesystem_spec/issues/1648) (#1648)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1648
- **Relevance Score:** `7` | **State:** `open` | **Author:** `kthyng`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"This might be a naive question but I have spent a bit of time trying to figure it out and haven't made much progress. I'm trying to do this workflow for a parquet file: ``` import fsspec fs = fsspec.filesystem().open(path_to_file) ``` This sort of workflow without specifying a protocol finds that th..."*

#### 177. [fsspec.fuse with zstd file crashes when trying to read from a file](https://github.com/fsspec/filesystem_spec/issues/1590) (#1590)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1590
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have a script called `fsspec`: ```python3 #!/usr/bin/env python3 import sys if '-f' in sys.argv: del sys.argv[sys.argv.index("-f")] from fsspec.implementations.tar import TarFileSystem as tafs fs = tafs(sys.argv[1]) print(f"Mount {sys.argv[1]} at {sys.argv[2]}") import fsspec.fuse fsspec.fuse.run(..."*

#### 178. [TarFileSystem cannot open files with .zstd extension](https://github.com/fsspec/filesystem_spec/issues/1589) (#1589)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1589
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have a script called `fsspec`: ```bash #!/usr/bin/env python3 import sys if '-f' in sys.argv: del sys.argv[sys.argv.index("-f")] from fsspec.implementations.tar import TarFileSystem as tafs fs = tafs(sys.argv[1]) print(f"Mount {sys.argv[1]} at {sys.argv[2]}") import fsspec.fuse fsspec.fuse.run(fs,..."*

#### 179. [Path expansion is inconsistent in helper utilities](https://github.com/fsspec/filesystem_spec/issues/1579) (#1579)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1579
- **Relevance Score:** `7` | **State:** `open` | **Author:** `Skylion007`
- **Labels:** None
- **FS Keywords:** `fsspec`, `open_files`
- **Perf Keywords:** `io`
- **Excerpt:** *"Path expansion is inconsistent when sequences are passed in to helper utilities such as `fsspec.mv`, `fsspec.copy` etc... `fsspec.open_files()` will call expand_if_needed depending on the args, but `fsspec.mv` and `fsspec.copy` will not. We should be consistently expanding file paths. Addditionally ..."*

#### 180. [Missing kwargs in ZipFileSystem leading to `botocore.exceptions.NoCredentialsError: Unable to locate credentials`](https://github.com/fsspec/filesystem_spec/issues/1573) (#1573)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1573
- **Relevance Score:** `7` | **State:** `open` | **Author:** `eschalkargans`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hello, ## Summary I initially created an issue on the xarray repository: https://github.com/pydata/xarray/issues/8944 ; I place it here for reference as it provides more context. The part concerning `fsspec` is the following: when trying to access a Zip file on a s3 bucket requiring authentication, ..."*

#### 181. [SMB: errors ignored when connecting](https://github.com/fsspec/filesystem_spec/issues/1571) (#1571)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1571
- **Relevance Score:** `7` | **State:** `open` | **Author:** `frafra`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The system tries to connect 5 times in a row, ignoring all errors. Since the for loop has no `else` branch, the function does not raise any error when all tentative failed. https://github.com/fsspec/filesystem_spec/blob/05e7d80ab2affaa01505ff2602b0097c38ad7688/fsspec/implementations/smb.py#L123-L136"*

#### 182. [Sanitize some common TAR path occurrences such as leading dots ./](https://github.com/fsspec/filesystem_spec/issues/1568) (#1568)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1568
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi there, we already wrote a bit back and forth in the issue in the smart_open repository. I wanted to give fsspec.fuse a quick try using the tar/libarchive backend. Unluckily, my very first test failed. I created the test tar with: ```bash echo foo > large tar -cf ./large{.tar,} tar tvlf large.tar ..."*

#### 183. [use pyarrow in LazyReferenceMapper.write?](https://github.com/fsspec/filesystem_spec/issues/1563) (#1563)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1563
- **Relevance Score:** `7` | **State:** `open` | **Author:** `raybellwaves`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Currently the `LazyReferenceMapper.write` uses fastparquet to write the parquet file (https://github.com/fsspec/filesystem_spec/blob/master/fsspec/implementations/reference.py#L467) I came across this as I didn't have fastparquet in my env. It would be nice to have a fallback to using pyarrow or eve..."*

#### 184. [Support stateful transactions by allowing to pass keyword arguments](https://github.com/fsspec/filesystem_spec/issues/1517) (#1517)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1517
- **Relevance Score:** `7` | **State:** `open` | **Author:** `nicholasjng`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"A file system's corresponding transaction class has been a class attribute since https://github.com/fsspec/filesystem_spec/pull/1424. However, the `fsspec.transaction.Transaction` interface is currently stateless. For someone trying to roll a transaction class that takes some state in the constructo..."*

#### 185. [http get() call creates malformed dest path](https://github.com/fsspec/filesystem_spec/issues/1505) (#1505)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1505
- **Relevance Score:** `7` | **State:** `open` | **Author:** `cgrass`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"See original discussion [here](https://github.com/fsspec/filesystem_spec/discussions/1490) and a linked bug [here](https://github.com/fsspec/filesystem_spec/issues/1504) ### Issue Creating an http file system and using an `rpath` with query params results in a malformed destination path. ### Steps t..."*

#### 186. ["File name too long" with HTTP presigned requests](https://github.com/fsspec/filesystem_spec/issues/1504) (#1504)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1504
- **Relevance Score:** `7` | **State:** `open` | **Author:** `cgrass`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Discussed in https://github.com/fsspec/filesystem_spec/discussions/1490 <div type='discussions-op-text'> <sup>Originally posted by **cgrass** January 4, 2024</sup> Hello, I'm new to python and fsspec, so hopefully there is an obvious answer to my question. Thanks for the help! ### Issue I need t..."*

#### 187. [429 Client Error: Too Many Requests for url azuredatabricks.net/api/2.0/dbfs/mkdirs](https://github.com/fsspec/filesystem_spec/issues/1488) (#1488)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1488
- **Relevance Score:** `7` | **State:** `open` | **Author:** `a24lorie`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I'm using the "fsspec.implementations.dbfs import DatabricksFileSystem" with pyarrow to write a parquet dataset on the DatabricksFilesystem DBFS, but when using the DatabricksFilesystem implementation with the write_to_dataset method from pyarrow I'm getting the following error: 429 Client Error: To..."*

#### 188. [UnsupportedOperation error with ZipFileSystem using append mode](https://github.com/fsspec/filesystem_spec/issues/1449) (#1449)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1449
- **Relevance Score:** `7` | **State:** `open` | **Author:** `forman`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"`fsspec.implementations.zip.ZipFileSystem` seems to have an issue with append mode 'a'. I assume, opening in mode 'a' allows for adding new Zip-entries to an existing Zip archive. At least this is what I need. While opening in append mode first seems to work - I can write to the archive - it will fa..."*

#### 189. [Error when processing file mode string](https://github.com/fsspec/filesystem_spec/issues/1425) (#1425)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1425
- **Relevance Score:** `7` | **State:** `open` | **Author:** `lobis`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"In the `memory` filesystem there is an error if you try to open it with `r+b` mode saying this mode is not supported. However this mode is apparently supported (https://github.com/fsspec/filesystem_spec/blob/master/fsspec/implementations/memory.py#L178). What I think is happening is that the `mode=r..."*

#### 190. [Ability to check if a filesystem implements an interface](https://github.com/fsspec/filesystem_spec/issues/1411) (#1411)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1411
- **Relevance Score:** `7` | **State:** `open` | **Author:** `lobis`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Apologies if this is currently possible, I couldn't find a clean way to achieve this. I think it would be useful to have a way to check if a given filesystem implements a given interface (e.g. is `cat_file` implemented for the `ssh` protocol?). Currently, when calling an interface that is not implem..."*

#### 191. [url_to_fs for a zip file system on a s3 bucket stopped working after upgrade.](https://github.com/fsspec/filesystem_spec/issues/1384) (#1384)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1384
- **Relevance Score:** `7` | **State:** `open` | **Author:** `louis-van-der-stam`
- **Labels:** None
- **FS Keywords:** `fsspec`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"fsspec.mapping.url_to_fs("zip::s://some-bucket/some-file.zip", mode="w") stopped working somewhere between 2023.5.0 and 2023.9.2. It seems to have something to do with removing the "mode" argument as one of the first things in the function. Is this intended or an unexpected side effect?"*

#### 192. [Unable to truncate file when using local storage](https://github.com/fsspec/filesystem_spec/issues/1338) (#1338)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1338
- **Relevance Score:** `7` | **State:** `open` | **Author:** `etiennelndr`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Description When trying to truncate a file while using local storage, an error is raised even if the provided `mode` is correct. This may be due to the missing implementation of `truncate` in [LocalFileOpener](https://github.com/fsspec/filesystem_spec/blob/1f12ee61e001e17c81af2a882a89d2eb7f44c88..."*

#### 193. [make `fsspec.asyn._get_batch_size()` public](https://github.com/fsspec/filesystem_spec/issues/1327) (#1327)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1327
- **Relevance Score:** `7` | **State:** `open` | **Author:** `pmrowla`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Being able to get the configured or system default batch size from fsspec is useful when using filesystems that support an additional level of concurrency (beyond the existing fs methods that support file batching like `get()`/`put()`). See: [adlfs](https://github.com/fsspec/adlfs/pull/420), which s..."*

#### 194. [Open the http file system in the wb mode](https://github.com/fsspec/filesystem_spec/issues/1325) (#1325)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1325
- **Relevance Score:** `7` | **State:** `open` | **Author:** `pingsutw`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"We can only use rb mode in the HTTP file system for now. It will be great if we can support wb mode. https://github.com/fsspec/filesystem_spec/blob/61cdf52cd0aaf524945ffb83502be39fccaee363/fsspec/implementations/http.py#L350-L351"*

#### 195. [Feature request:  classmethod returning possible keys of the details=True dictionary for each filesystem.](https://github.com/fsspec/filesystem_spec/issues/1301) (#1301)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1301
- **Relevance Score:** `7` | **State:** `open` | **Author:** `phil65`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have written a Qt ItemModel for fsspec, what is tricky though is that there is no way to know which keys the "details" dictionary can contain for each filesystem (I would like to show a dedicated column for each details key, depending on filesystem) It would be nice to have some classmethod for ea..."*

#### 196. [Inconsistent use of protocol specific options](https://github.com/fsspec/filesystem_spec/issues/1192) (#1192)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1192
- **Relevance Score:** `7` | **State:** `open` | **Author:** `agrinh`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Setting protocol specific options has been a convenient method for overriding the default options for each protocol. E.g., the Azure blob storage implementation behaves peculiarly and requires setting `anon=False` to use the credentials in the environment (https://github.com/fsspec/adlfs/issues/348)..."*

#### 197. [Register custom compression types via entrypoint mechanism](https://github.com/fsspec/filesystem_spec/issues/1187) (#1187)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1187
- **Relevance Score:** `7` | **State:** `open` | **Author:** `cjackal`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"While new `fsspec`-compatible filesystem can easily be registered via `fsspec.specs` entry points, there is no counterpart for compression types. As we already have the `fsspec.compression.register_compression` public API for custom compression types, it wouldn't be too much burden (and give better ..."*

#### 198. [Add function to return fully qualified urls for fsspec](https://github.com/fsspec/filesystem_spec/issues/1169) (#1169)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1169
- **Relevance Score:** `7` | **State:** `open` | **Author:** `JoostvDoorn`
- **Labels:** None
- **FS Keywords:** `fsspec`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"In some cases, it's necessary to use fsspec to list a directory and then reconstruct the results to a fully qualified path, especially when passing the URL to another service like a microservice. Currently, there is no generic way to handle this use case as the URL schema differs between Azure, Goog..."*

#### 199. [Handling of URL quoting (for `file://` URLs)](https://github.com/fsspec/filesystem_spec/issues/1168) (#1168)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1168
- **Relevance Score:** `7` | **State:** `open` | **Author:** `mih`
- **Labels:** None
- **FS Keywords:** `fsspec`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have a local file at `/tmp/URL--https&c%%zenodo.org%record%68331` that I am trying to access via FSSPEC. This fails due to a missing unquoting step, as far as I can tell. Here is a small demo to show the essence of the issue: ```py >>> from pathlib import Path >>> from fsspec.core import url_to_fs..."*

#### 200. [Dealing with an FTP server that doesn't support offsets](https://github.com/fsspec/filesystem_spec/issues/1116) (#1116)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1116
- **Relevance Score:** `7` | **State:** `open` | **Author:** `jobevers`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Running code like: ``` with fsspec.open(an_ftp_url) as fin: while True: buf = fin.read(16*1024) if not buf: break ``` raises a `error_temp: 426 Connection closed; transfer aborted.` here: https://github.com/fsspec/filesystem_spec/blob/62bb12e681b9e3dbd25df3991fd71552ea7654ee/fsspec/implementations/f..."*

#### 201. [Is there a way to map to pyarrow.hdfs.connect?](https://github.com/fsspec/filesystem_spec/issues/1113) (#1113)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1113
- **Relevance Score:** `7` | **State:** `open` | **Author:** `Jeffwan`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Let's say we have a file system called `bfs://` which is an equivalent implementation of HDFS. We can support pyarrow operation like following way. ``` import pyarrow as pa from pyarrow import fs bfs = pa.hdfs.connect('bfs://service-endpoint') # ---> work # bfs, _ = fs.FileSystem.from_uri('bfs://ser..."*

#### 202. [Link to Zenodo to gain DOI and improve citeability of this project](https://github.com/fsspec/filesystem_spec/issues/2018) (#2018)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/2018
- **Relevance Score:** `5` | **State:** `open` | **Author:** `yarikoptic`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Ideally -- accompany with CITATION.cff file with desired list/classification of authors/contributors."*

#### 203. [Equivalent to pyfilesystem2's MountFS?](https://github.com/fsspec/filesystem_spec/issues/1994) (#1994)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1994
- **Relevance Score:** `5` | **State:** `open` | **Author:** `dAnjou`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, just wanted to make sure I'm not completely missing something before I have a go at this myself. Is there an equivalent to https://pyfilesystem2.readthedocs.io/en/latest/reference/mountfs.html? Thanks 🙏"*

#### 204. [TypeError: ClientSession._request() got an unexpected keyword argument 's3'](https://github.com/fsspec/filesystem_spec/issues/1925) (#1925)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1925
- **Relevance Score:** `5` | **State:** `open` | **Author:** `codingl2k1`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I have a list of URLs that are mixed with different schemes, some in the format s3:// and others in https://. I want to use one global storage option to read them all. However, the HTTP backend is attempting to use the S3 storage option. Different protocol backends should only use their correspondin..."*

#### 205. [Support argument discovery](https://github.com/fsspec/filesystem_spec/issues/1913) (#1913)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1913
- **Relevance Score:** `5` | **State:** `open` | **Author:** `paulmillar`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"This is a somewhat speculative feature request. My exploration of fsspec suggests that there's currently no standard, machine-actionable mechanism through which a backend implementation can describe the arguments (args, kwargs) that it understands. The use-case I'm considering is for implementation-..."*

#### 206. [memory ls/walk/find algorithms](https://github.com/fsspec/filesystem_spec/issues/1906) (#1906)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1906
- **Relevance Score:** `5` | **State:** `open` | **Author:** `smorken`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I was wondering if anyone had considered using a tree-based structure rather than flat structure for the in-memory implementation. For my current experimentation, use case I'm ending up with A LOT of calls to `ls` via `walk` and `find` calls, and that calls `startswith` very many times when many pat..."*

#### 207. [when use QINIU as cloud storage service , the delete function will report an error](https://github.com/fsspec/filesystem_spec/issues/1867) (#1867)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1867
- **Relevance Score:** `5` | **State:** `open` | **Author:** `guolijing`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Missing required header for this request: Content-MD5"*

#### 208. [Documentation for using Compress/Decompress?](https://github.com/fsspec/filesystem_spec/issues/1775) (#1775)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1775
- **Relevance Score:** `5` | **State:** `open` | **Author:** `gaby`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I noticed that fsspec has `fsspec.compression` but it's not documented anywhere how to use it. Even a simple example would help on how to create a fs using `fsspec` and write files compressed to it. The other thing I read is that `fsspec` doesn't have compression dependencies, if I want to use `zstd..."*

#### 209. [Incomplete HTTP reads](https://github.com/fsspec/filesystem_spec/issues/1748) (#1748)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1748
- **Relevance Score:** `5` | **State:** `open` | **Author:** `amotl`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi there, thanks a stack for conceiving and maintaining fsspec. We are successfully using it in a few projects and never observed any kinds of issues so far. 💯 Right now, we may have discovered an edge case that leads to truncated HTTP response bodies. A simple reproducer is attached below. This rep..."*

#### 210. [run coros utility func](https://github.com/fsspec/filesystem_spec/issues/1740) (#1740)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1740
- **Relevance Score:** `5` | **State:** `open` | **Author:** `wild-endeavor`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi Team. I'd like to use the run_coros_in_chunks function. I understand there's some callback functionality in there, but can we make it a public function (just no `_`)? Maybe the public function always just hardcodes the noop callback? Thank you."*

#### 211. [Copy file to and from local](https://github.com/fsspec/filesystem_spec/issues/1694) (#1694)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1694
- **Relevance Score:** `5` | **State:** `open` | **Author:** `peterdudfield`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Ive perhaps missed something, and if so please do tell me, p.s this is a great package, and I really like using it. Im trying copy a file from 1. remote to local or 2. local to remote It seems like I have to use two different methods 1 ``` fs = fsspec.open(file2).fs fs.put(file1, file2) ``` and ``` ..."*

#### 212. [Instance of 'OpenFiles' has no 'path' member (no-member)](https://github.com/fsspec/filesystem_spec/issues/1678) (#1678)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1678
- **Relevance Score:** `5` | **State:** `open` | **Author:** `mxmlnkn`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, I'm trying to use fsspec, but I cannot convince pylint of the correctness of my program: ```python3 import fsspec file = fsspec.open("foo") print(file.path) ``` Calling `pylint test.py` yields: ``` test.py:1:0: C0114: Missing module docstring (missing-module-docstring) test.py:4:6: E1101: Instan..."*

#### 213. [zip tests error in Debian build](https://github.com/fsspec/filesystem_spec/issues/1677) (#1677)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1677
- **Relevance Score:** `5` | **State:** `open` | **Author:** `eamanu`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi!, I'm building the latest version `2024.9.0`, but I have two tests that are failing but I cannot figure out the issue. The tests are: ``` FAILED fsspec/implementations/tests/test_zip.py::test_find_returns_expected_result_detail_true - AssertionError: assert {'CRC': 39643...nt': b'', ...} == {'CRC..."*

#### 214. [github file 404 when folder has escaped symbols](https://github.com/fsspec/filesystem_spec/issues/1669) (#1669)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1669
- **Relevance Score:** `5` | **State:** `open` | **Author:** `DaveBoy`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"A 404 error may occur when a github folder has escaped symbols, because the actual raw address is not the folder name, but partially escaped. Example below: **url:** https ://github.com/msojocs/fiddler-everywhere-enhance/raw/master/server/file/api.getfiddler.com/c/NUNHMjIyNkpNMDg4ZjMzMjZlLTk0OWQtNDg..."*

#### 215. [Walk filesystem breaks if filesystem doesn't provide unique file names](https://github.com/fsspec/filesystem_spec/issues/1647) (#1647)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1647
- **Relevance Score:** `5` | **State:** `open` | **Author:** `jcampbell05`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"If the filesystem provides files with same name at different directory then it breaks for example with HTTPFilesystem if the response is as follows: ``` "/folder1/file" "/folder2/file" ``` Then it will only return the first file because the current implementation appears to assign them to the same k..."*

#### 216. [Add more logging of exceptions in backends](https://github.com/fsspec/filesystem_spec/issues/1642) (#1642)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1642
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Skylion007`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"A lot of backends can throw exceptions that are swallowed by fsspec, we should at least log these errors in debug or info level using the builtin loggers with exc_info=True to improve the debugging experience of the library."*

#### 217. [Suggestion: continue download](https://github.com/fsspec/filesystem_spec/issues/1617) (#1617)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1617
- **Relevance Score:** `5` | **State:** `open` | **Author:** `martindurant`
- **Labels:** None
- **FS Keywords:** `repo:fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"When downloading large files, it can commonly happen that the transfer aborts part way. Rather than having to restart the process, it would be nice to be able to read only the remaining bytes on a subsequent attempts. `cat_file()` already allows for providing a start byte (and end byte), but `get_fi..."*

#### 218. [Adding typing.override to various classes in fsspec](https://github.com/fsspec/filesystem_spec/issues/1588) (#1588)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1588
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Skylion007`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"This static typing utility could help catch potential bugs such as #1585"*

#### 219. [Feature request: Add FTP_TLS](https://github.com/fsspec/filesystem_spec/issues/1580) (#1580)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1580
- **Relevance Score:** `5` | **State:** `open` | **Author:** `bartvaneswhiffle`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, I'd like to use FTP with SSL/TLS in fsspec, to be specific: [this implementation](https://docs.python.org/3/library/ftplib.html#ftp-tls-objects). I've made a PR for it, will post the link soon. Regards, Bart"*

#### 220. [`LocalFileSystem` clobbers file permissions after cp_file](https://github.com/fsspec/filesystem_spec/issues/1524) (#1524)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1524
- **Relevance Score:** `5` | **State:** `open` | **Author:** `russell-horvath`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, I am trying to copy a local file with the following permissions: ``` -rwxrwxr-x 1 rhorvath rhorvath 7994 ``` after copying the file it becomes: ``` -rw-rw-r-- 1 rhorvath rhorvath 7994 ``` I have narrowed the reason for this down to the cp_file function in `LocalFileSystem` where `shutil.copyfile..."*

#### 221. [Expected behavior for "directory to new directory" depends on trailing slash](https://github.com/fsspec/filesystem_spec/issues/1500) (#1500)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1500
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Github-dm-CDE`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"In [Copying files and directories](https://filesystem-spec.readthedocs.io/en/latest/copying.html#single-source-to-single-target), 1f case "directory to new directory", it is stated that the trailing slashes in both `source` and `target` are optional. However, if `source/subdir` and `target/newdir/` ..."*

#### 222. [DirFileSystem breaks open_async for any underling filesystem](https://github.com/fsspec/filesystem_spec/issues/1414) (#1414)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1414
- **Relevance Score:** `5` | **State:** `open` | **Author:** `vovochka404`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"DirFileSystem can wrap any async filesystem. But cause `open_async` method is not redirected to wrapped fs, it will always raise `NotImplementedError`. As mentioned in #1411, cause all unimplemented methods in base abstract classes got no `abstractmethod` decorator, it's hard to see that u've missed..."*

#### 223. [Canonical form of memory urlpaths](https://github.com/fsspec/filesystem_spec/issues/1407) (#1407)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1407
- **Relevance Score:** `5` | **State:** `open` | **Author:** `ap--`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi @martindurant, I'm currently fixing `memory` URI handling in universal_pathlib for python versions up to 3.11 and was wondering which URI would be considered the canonical form of a memory urlpath: ``` memory://path/to/file.txt memory:///path/to/file.txt ``` universal_pathlib will support both as..."*

#### 224. [Using callbacks to filter files?](https://github.com/fsspec/filesystem_spec/issues/1368) (#1368)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1368
- **Relevance Score:** `5` | **State:** `open` | **Author:** `hhuuggoo`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Just a question - I would like to use the recursive mechanisms in fsspec to copy directories, but I also want to exclude some paths (for example `.git` directories). It does seem like the callback mechanism would be perfect for this, by implementing `wrap`. I haven't seen any examples of doing so, s..."*

#### 225. [FileNotFound for s3 file with / in the key](https://github.com/fsspec/filesystem_spec/issues/1310) (#1310)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1310
- **Relevance Score:** `5` | **State:** `open` | **Author:** `nick-amplify`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hello! I am trying to read a csv stored in a remote s3 bucket with a / in the name, like this: `'s3://mybucket/path/7/update//nicktorba.part_00000'` When i run this code, I get FileNotFound error: (as far as I can tell, when I run a pandas `read_csv`, this is the code used to read the file) ```pytho..."*

#### 226. [Release process](https://github.com/fsspec/filesystem_spec/issues/1200) (#1200)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1200
- **Relevance Score:** `5` | **State:** `open` | **Author:** `f4hy`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I was expecting there to be a February release but looks like there wasn't one. I am curious about the release cadence of fsspec, I don't see a document in the repo outlining the release process. There are number of fixes that have been merged but yet to be released that I am waiting on. It would be..."*

#### 227. [ Cached filesystem not concurrency-safe](https://github.com/fsspec/filesystem_spec/issues/1126) (#1126)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1126
- **Relevance Score:** `5` | **State:** `open` | **Author:** `yarikoptic`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `cache`
- **Excerpt:** *"This is #1107 reincarnated -- please see it for more details: #1111 provided remedy to only one aspect."*

#### 228. [logo (with a name) for fsspec?](https://github.com/fsspec/filesystem_spec/issues/1105) (#1105)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1105
- **Relevance Score:** `5` | **State:** `open` | **Author:** `yarikoptic`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"I thought to promote fsspec on a poster, but wasn't sure what is the logo? ![image](https://user-images.githubusercontent.com/39889/200669246-c0d412db-1784-4770-8205-f48c1b2bd540.png) used for organization? Would be nice if there was a rendering with project name (fsspec? FSSPEC?) included in the lo..."*

#### 229. [Integration with pyodide-http](https://github.com/fsspec/filesystem_spec/issues/1069) (#1069)
- **URL:** https://github.com/fsspec/filesystem_spec/issues/1069
- **Relevance Score:** `5` | **State:** `open` | **Author:** `martindurant`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"https://github.com/koenvo/pyodide-http provides patches to requests and urllib, to enable python stack HTTP calls in the browser. Since several fsspec backends (http, s3, gcs. azure) depend on HTTP, this raises the possibility of fsspec and pydata IO in the browser. Principle problem: - fsspec's bac..."*
