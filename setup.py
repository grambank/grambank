from setuptools import setup


setup(
    name='cldfbench_grambank',
    py_modules=['cldfbench_grambank'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'grambank=cldfbench_grambank:Dataset',
        ]
    },
    install_requires=[
        'cldfbench>=1.4',
        'pygrambank',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
