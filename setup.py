#! /usr/bin/env python3
"""Installation script."""

from setuptools import setup

setup(
    name="html5ds",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    python_requires=">=3.8",
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info@homeinfo.de>",
    maintainer="Richard Neumann",
    maintainer_email="<r.neumann@homeinfo.de>",
    packages=["html5ds"],
    entry_points={
        "console_scripts": [
            "html5ds = html5ds.main:main",
            "cleanup-chromium-cache = html5ds.cleanup:cleanup_chromium_cache",
            "cleanup-chromium-crash-logs = "
            "html5ds.cleanup:cleanup_chromium_crash_logs",
            "cleanup-chromium-browser-metrics = "
            "html5ds.cleanup:cleanup_chromium_browser_metrics",
            "html5ds-restart = html5ds.restart:restart",
        ]
    },
    description="Browser wrapper for HTML5 digital signage applications.",
)
