from setuptools import setup


setup(
    name='cldfbench_grambank',
    py_modules=['cldfbench_grambank'],
    packages=['grambank_cldfbench_commands'],
    package_dir={'grambank_cldfbench_commands': 'grambank_cldfbench_commands'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'grambank=cldfbench_grambank:Dataset',
        ],
        'cldfbench.commands': [
            'gb=grambank_cldfbench_commands',
        ],
    },
    install_requires=[
        'cldfbench[glottolog]>=1.4',
        'pygrambank>=2.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
