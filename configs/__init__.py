import os.path
import random

from jinja2 import Environment, FileSystemLoader

from configs import path_define, ark_pixel_config
from configs.download_config import DownloadConfig
from configs.dump_config import DumpConfig
from configs.git_deploy_config import GitDeployConfig
from utils.unidata_util import UnidataDB

build_random_key = random.random()

download_configs = [
    DownloadConfig(
        name='ark-pixel-monospaced',
        font_name='方舟像素字体-等宽模式',
        repository_name=ark_pixel_config.repository_name,
        tag_name=ark_pixel_config.tag_name,
        asset_file_name='ark-pixel-font-12px-monospaced-otf-v{version}.zip',
        font_file_path=f'ark-pixel-12px-monospaced-{ark_pixel_config.language_specific}.otf',
        ofl_file_path='OFL.txt',
    ),
    DownloadConfig(
        name='ark-pixel-proportional',
        font_name='方舟像素字体-比例模式',
        repository_name=ark_pixel_config.repository_name,
        tag_name=ark_pixel_config.tag_name,
        asset_file_name='ark-pixel-font-12px-proportional-otf-v{version}.zip',
        font_file_path=f'ark-pixel-12px-proportional-{ark_pixel_config.language_specific}.otf',
        ofl_file_path='OFL.txt',
    ),
    DownloadConfig(
        name='cubic-11',
        font_name='俐方體11號',
        repository_name='ACh-K/Cubic-11',
        tag_name=None,
        asset_file_name='Cubic_11.zip',
        font_file_path=os.path.join('fonts', 'ttf', 'Cubic_11_{version}_R.ttf'),
        ofl_file_path='OFL.txt',
    ),
    DownloadConfig(
        name='galmuri',
        font_name='Galmuri',
        repository_name='quiple/galmuri',
        tag_name=None,
        asset_file_name='Galmuri-v{version}.zip',
        font_file_path=os.path.join('dist', 'Galmuri11.ttf'),
        ofl_file_path=os.path.join('dist', 'LICENSE.txt'),
    ),
]

dump_configs = [
    DumpConfig('ark-pixel-monospaced'),
    DumpConfig('ark-pixel-proportional'),
    DumpConfig('cubic-11', offset_xy=(-1, 1)),
    DumpConfig('galmuri', offset_xy=(0, 1)),
]

fallback_names = [
    'cubic-11',
    'galmuri',
]

width_modes = ['monospaced', 'proportional']

font_formats = ['otf', 'woff2', 'ttf']

unidata_db = UnidataDB(os.path.join(path_define.unidata_dir, 'Blocks.txt'))

template_env = Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(path_define.templates_dir),
)

git_deploy_configs = [GitDeployConfig(
    url='git@github.com:TakWolf/fusion-pixel-font.git',
    remote_name='github',
    branch_name='gh-pages',
)]
