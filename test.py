import argparse
import logging
import os
from time import time
import fsspec

try:
    import googlecloudprofiler as profiler
except ImportError:
    try:
        from google.cloud import profiler
    except ImportError:
        profiler = None


logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read a file from GCS using fsspec")
    parser.add_argument("--url", default="gs://princer-bucket/1gfile.bin", help="GCS path in the form bucket/path/to/file or gs://bucket/path/to/file")
    parser.add_argument("--block-size", dest="block_size", type=int, default=5 * 1024 * 1024, help="Block size passed to fsspec")
    parser.add_argument("--cache-type", dest="cache_type", default=None, help="Cache type passed to fsspec")
    parser.add_argument("--io-size", dest="io_size", type=int, default=8 * 1024 * 1024, help="I/O size passed to fsspec")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--enable-prefetch", action="store_true", help="Enable gcsfs adaptive prefetching via environment")
    parser.add_argument("--cloud-profiler", action="store_true", help="Enable Google Cloud Profiler")
    parser.add_argument("--project-id", default="gcs-aiml-clients-testing-101", help="Google Cloud project ID for Cloud Profiler")
    parser.add_argument("--profiler-service", default="gcsfs-read-script", help="Service name for Cloud Profiler")
    parser.add_argument("--profiler-service-version", default="1.0.1", help="Service version for Cloud Profiler")
    parser.add_argument("--repeats", type=int, default=1, help="Number of times to repeat the read operation for benchmarking")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
        logging.getLogger("fsspec").setLevel(logging.DEBUG)
        logging.getLogger("gcsfs").setLevel(logging.DEBUG)
    else :
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.enable_prefetch:
        os.environ["USE_EXPERIMENTAL_ADAPTIVE_PREFETCHING"] = "true"
        logger.debug("Enabled adaptive prefetching via USE_EXPERIMENTAL_ADAPTIVE_PREFETCHING")

    if args.cloud_profiler:
        if profiler is None:
            raise RuntimeError("google-cloud-profiler is not installed. Install it to use --cloud-profiler")
        project_id = args.project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
        profiler.start(service=args.profiler_service, service_version=args.profiler_service_version, project_id=project_id)
        logger.info("Started Cloud Profiler for service=%s, project_id=%s", args.profiler_service, project_id)

    open_kwargs = {}
    # if args.block_size is not None:
        # open_kwargs["block_size"] = args.block_size
    if args.cache_type is not None:
        open_kwargs["cache_type"] = args.cache_type
    # else :
        # open_kwargs["cache_type"] = None  # Disable caching if not specified

    logger.debug("Opening %s with block_size=%s and cache_type=%s", args.url, args.block_size, args.cache_type)

    stime = time()
    total_bytes = 0
    with fsspec.open(args.url, "rb", **open_kwargs) as f:
        cache_obj = getattr(f, "cache", None)
        cache_name = getattr(cache_obj, "name", "unknown") if cache_obj else "none"
        logger.info("Effective cache in use: %s", cache_name)
        # for readline in f:
        #     total_bytes += len(readline)
        #     logger.debug("Read line of %d bytes", len(readline))
            
        while True:
            data = f.read(args.io_size)
            # data = f.read()
            if not data:
                break
            total_bytes += len(data)
            logger.debug("Read chunk of %d bytes", len(data))

    elapsed = time() - stime
    throughput = (total_bytes / 1024 / 1024) / elapsed if elapsed > 0 else 0
    logger.info("Read %d bytes from %s in %.2f seconds, throughput: %.2f MB/second", total_bytes, args.url, elapsed, throughput)

    if args.cloud_profiler and hasattr(profiler, "stop"):
        profiler.stop()
        logger.debug("Stopped Cloud Profiler")


if __name__ == "__main__":
    main()
