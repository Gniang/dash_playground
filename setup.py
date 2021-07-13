# プロジェクトフォルダをルートディレクトリとして
# モジュールインポートのパス解決を行うための変種可能なパッケージ化定義
from setuptools import setup, find_packages

setup(name='my_app_package_resolver', version='0.0.1', packages=find_packages())